
from fastapi import FastAPI, HTTPException, Depends, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional, Dict, List
import uuid
from datetime import datetime

from payment_processor import PaymentProcessor, PaymentMethod, PaymentStatus
from database_models import DatabaseManager
from payment_gateways import StripeGateway, YandexKassaGateway

app = FastAPI(title="Payment API", version="1.0.0")

# CORS для работы с React фронтендом
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Инициализация сервисов
payment_processor = PaymentProcessor()
db_manager = DatabaseManager()

# Pydantic модели для API
class PaymentCreateRequest(BaseModel):
    amount: float = Field(..., gt=0, description="Сумма платежа")
    currency: str = Field(default="RUB", description="Валюта")
    method: PaymentMethod = Field(default=PaymentMethod.CARD)
    customer_id: Optional[str] = None
    description: Optional[str] = None
    return_url: Optional[str] = None

class PaymentResponse(BaseModel):
    id: str
    amount: float
    currency: str
    status: str
    method: str
    payment_url: Optional[str] = None
    created_at: str

class RefundRequest(BaseModel):
    amount: Optional[float] = None
    reason: Optional[str] = None

@app.post("/api/payments", response_model=PaymentResponse)
async def create_payment(request: PaymentCreateRequest):
    """Создание нового платежа"""
    try:
        payment = await payment_processor.create_payment(
            amount=request.amount,
            currency=request.currency,
            method=request.method,
            customer_id=request.customer_id
        )
        
        # Сохранение в базу данных
        db_manager.create_payment(payment)
        
        return PaymentResponse(**payment)
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/api/payments/{payment_id}", response_model=PaymentResponse)
async def get_payment(payment_id: str):
    """Получение информации о платеже"""
    payment = db_manager.get_payment(payment_id)
    
    if not payment:
        raise HTTPException(status_code=404, detail="Платёж не найден")
    
    return PaymentResponse(**payment)

@app.post("/api/payments/{payment_id}/process")
async def process_payment(payment_id: str, card_data: Optional[Dict] = None):
    """Обработка платежа"""
    try:
        payment = await payment_processor.process_payment(payment_id, card_data)
        
        # Обновление в базе данных
        db_manager.update_payment(payment_id, {
            'status': payment['status'],
            'processed_at': payment.get('processed_at')
        })
        
        return {"status": "success", "payment": payment}
    
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/payments/{payment_id}/refund")
async def refund_payment(payment_id: str, request: RefundRequest):
    """Возврат платежа"""
    try:
        refund = await payment_processor.refund_payment(
            payment_id, 
            request.amount
        )
        
        # Сохранение возврата в базу данных
        refund['reason'] = request.reason
        db_manager.create_refund(refund)
        
        # Обновление статуса платежа
        db_manager.update_payment(payment_id, {
            'status': PaymentStatus.REFUNDED.value
        })
        
        return {"status": "success", "refund": refund}
    
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/api/customers/{customer_id}/payments")
async def get_customer_payments(customer_id: str):
    """Получение всех платежей клиента"""
    payments = db_manager.get_payments_by_customer(customer_id)
    return {"payments": payments}

@app.post("/api/webhooks/stripe")
async def stripe_webhook(background_tasks: BackgroundTasks):
    """Webhook для Stripe"""
    # Здесь обработка webhook от Stripe
    background_tasks.add_task(process_stripe_webhook)
    return {"status": "received"}

@app.post("/api/webhooks/yandex")
async def yandex_webhook(background_tasks: BackgroundTasks):
    """Webhook для Яндекс.Кассы"""
    # Здесь обработка webhook от Яндекс.Кассы
    background_tasks.add_task(process_yandex_webhook)
    return {"status": "received"}

async def process_stripe_webhook():
    """Фоновая обработка webhook от Stripe"""
    # Логика обработки событий от Stripe
    pass

async def process_yandex_webhook():
    """Фоновая обработка webhook от Яндекс.Кассы"""
    # Логика обработки событий от Яндекс.Кассы
    pass

@app.get("/health")
async def health_check():
    """Проверка состояния API"""
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
