
import asyncio
import logging
from datetime import datetime, timedelta
from typing import Dict, Optional, List
from enum import Enum
import uuid
import hashlib
import hmac

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PaymentStatus(Enum):
    PENDING = "pending"
    SUCCESS = "success"
    FAILED = "failed"
    CANCELLED = "cancelled"
    REFUNDED = "refunded"

class PaymentMethod(Enum):
    CARD = "card"
    BANK_TRANSFER = "bank_transfer"
    DIGITAL_WALLET = "digital_wallet"
    CRYPTO = "crypto"

class PaymentProcessor:
    def __init__(self):
        self.transactions = {}
        self.webhooks = []
    
    async def create_payment(self, amount: float, currency: str = "RUB", 
                           method: PaymentMethod = PaymentMethod.CARD,
                           customer_id: str = None) -> Dict:
        """Создание нового платежа"""
        payment_id = str(uuid.uuid4())
        
        payment = {
            "id": payment_id,
            "amount": amount,
            "currency": currency,
            "method": method.value,
            "status": PaymentStatus.PENDING.value,
            "customer_id": customer_id,
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "payment_url": f"https://pay.example.com/{payment_id}"
        }
        
        self.transactions[payment_id] = payment
        logger.info(f"Создан платёж {payment_id} на сумму {amount} {currency}")
        
        return payment
    
    async def process_payment(self, payment_id: str, card_data: Dict = None) -> Dict:
        """Обработка платежа"""
        if payment_id not in self.transactions:
            raise ValueError("Платёж не найден")
        
        payment = self.transactions[payment_id]
        
        try:
            # Симуляция обработки платежа
            await asyncio.sleep(1)  # Имитация задержки
            
            # Проверка валидности карты (упрощённая)
            if card_data and self._validate_card(card_data):
                payment["status"] = PaymentStatus.SUCCESS.value
                payment["processed_at"] = datetime.now().isoformat()
                logger.info(f"Платёж {payment_id} успешно обработан")
            else:
                payment["status"] = PaymentStatus.FAILED.value
                payment["error"] = "Неверные данные карты"
                logger.error(f"Платёж {payment_id} отклонён")
                
        except Exception as e:
            payment["status"] = PaymentStatus.FAILED.value
            payment["error"] = str(e)
            logger.error(f"Ошибка обработки платежа {payment_id}: {e}")
        
        payment["updated_at"] = datetime.now().isoformat()
        return payment
    
    def _validate_card(self, card_data: Dict) -> bool:
        """Валидация данных карты"""
        required_fields = ["number", "exp_month", "exp_year", "cvc"]
        return all(field in card_data for field in required_fields)
    
    async def refund_payment(self, payment_id: str, amount: float = None) -> Dict:
        """Возврат платежа"""
        if payment_id not in self.transactions:
            raise ValueError("Платёж не найден")
        
        payment = self.transactions[payment_id]
        
        if payment["status"] != PaymentStatus.SUCCESS.value:
            raise ValueError("Можно вернуть только успешный платёж")
        
        refund_amount = amount or payment["amount"]
        
        refund = {
            "id": str(uuid.uuid4()),
            "payment_id": payment_id,
            "amount": refund_amount,
            "status": PaymentStatus.REFUNDED.value,
            "created_at": datetime.now().isoformat()
        }
        
        payment["status"] = PaymentStatus.REFUNDED.value
        payment["refund"] = refund
        
        logger.info(f"Возврат {refund_amount} по платежу {payment_id}")
        return refund
    
    def get_payment(self, payment_id: str) -> Optional[Dict]:
        """Получение информации о платеже"""
        return self.transactions.get(payment_id)
    
    def get_payments_by_customer(self, customer_id: str) -> List[Dict]:
        """Получение всех платежей клиента"""
        return [p for p in self.transactions.values() 
                if p.get("customer_id") == customer_id]
