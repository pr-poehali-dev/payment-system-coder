
import aiohttp
import json
from abc import ABC, abstractmethod
from typing import Dict, Optional
import os

class PaymentGateway(ABC):
    """Базовый класс для платёжных шлюзов"""
    
    @abstractmethod
    async def create_payment(self, amount: float, currency: str, **kwargs) -> Dict:
        pass
    
    @abstractmethod
    async def capture_payment(self, payment_id: str) -> Dict:
        pass
    
    @abstractmethod
    async def refund_payment(self, payment_id: str, amount: float = None) -> Dict:
        pass

class StripeGateway(PaymentGateway):
    """Интеграция со Stripe"""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.stripe.com/v1"
    
    async def create_payment(self, amount: float, currency: str = "rub", **kwargs) -> Dict:
        """Создание платежа в Stripe"""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        
        data = {
            "amount": int(amount * 100),  # Копейки
            "currency": currency.lower(),
            "automatic_payment_methods[enabled]": "true"
        }
        
        if "customer_id" in kwargs:
            data["customer"] = kwargs["customer_id"]
        
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{self.base_url}/payment_intents",
                headers=headers,
                data=data
            ) as response:
                return await response.json()
    
    async def capture_payment(self, payment_id: str) -> Dict:
        """Подтверждение платежа"""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{self.base_url}/payment_intents/{payment_id}/confirm",
                headers=headers
            ) as response:
                return await response.json()
    
    async def refund_payment(self, payment_id: str, amount: float = None) -> Dict:
        """Возврат платежа"""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        
        data = {"payment_intent": payment_id}
        if amount:
            data["amount"] = int(amount * 100)
        
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{self.base_url}/refunds",
                headers=headers,
                data=data
            ) as response:
                return await response.json()

class YandexKassaGateway(PaymentGateway):
    """Интеграция с Яндекс.Кассой"""
    
    def __init__(self, shop_id: str, secret_key: str):
        self.shop_id = shop_id
        self.secret_key = secret_key
        self.base_url = "https://api.yookassa.ru/v3"
    
    async def create_payment(self, amount: float, currency: str = "RUB", **kwargs) -> Dict:
        """Создание платежа в Яндекс.Кассе"""
        headers = {
            "Authorization": f"Basic {self._get_auth_header()}",
            "Content-Type": "application/json",
            "Idempotence-Key": kwargs.get("idempotence_key", str(uuid.uuid4()))
        }
        
        data = {
            "amount": {
                "value": f"{amount:.2f}",
                "currency": currency
            },
            "confirmation": {
                "type": "redirect",
                "return_url": kwargs.get("return_url", "https://example.com/success")
            },
            "capture": True
        }
        
        if "description" in kwargs:
            data["description"] = kwargs["description"]
        
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{self.base_url}/payments",
                headers=headers,
                json=data
            ) as response:
                return await response.json()
    
    def _get_auth_header(self) -> str:
        import base64
        credentials = f"{self.shop_id}:{self.secret_key}"
        return base64.b64encode(credentials.encode()).decode()
    
    async def capture_payment(self, payment_id: str) -> Dict:
        """Подтверждение платежа (автоматически при создании)"""
        headers = {
            "Authorization": f"Basic {self._get_auth_header()}",
            "Content-Type": "application/json"
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{self.base_url}/payments/{payment_id}",
                headers=headers
            ) as response:
                return await response.json()
    
    async def refund_payment(self, payment_id: str, amount: float = None) -> Dict:
        """Возврат платежа"""
        headers = {
            "Authorization": f"Basic {self._get_auth_header()}",
            "Content-Type": "application/json",
            "Idempotence-Key": str(uuid.uuid4())
        }
        
        data = {"payment_id": payment_id}
        if amount:
            data["amount"] = {
                "value": f"{amount:.2f}",
                "currency": "RUB"
            }
        
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{self.base_url}/refunds",
                headers=headers,
                json=data
            ) as response:
                return await response.json()
