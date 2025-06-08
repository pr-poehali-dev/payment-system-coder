
from datetime import datetime
from typing import Optional, List
import sqlite3
import json

class DatabaseManager:
    """Менеджер базы данных для платежей"""
    
    def __init__(self, db_path: str = "payments.db"):
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """Создание таблиц"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Таблица платежей
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS payments (
                    id TEXT PRIMARY KEY,
                    amount REAL NOT NULL,
                    currency TEXT NOT NULL DEFAULT 'RUB',
                    status TEXT NOT NULL,
                    method TEXT NOT NULL,
                    customer_id TEXT,
                    gateway TEXT,
                    gateway_payment_id TEXT,
                    metadata TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    processed_at TIMESTAMP
                )
            ''')
            
            # Таблица возвратов
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS refunds (
                    id TEXT PRIMARY KEY,
                    payment_id TEXT NOT NULL,
                    amount REAL NOT NULL,
                    reason TEXT,
                    status TEXT NOT NULL DEFAULT 'pending',
                    gateway_refund_id TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (payment_id) REFERENCES payments (id)
                )
            ''')
            
            # Таблица клиентов
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS customers (
                    id TEXT PRIMARY KEY,
                    email TEXT UNIQUE,
                    name TEXT,
                    phone TEXT,
                    metadata TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Таблица webhook событий
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS webhook_events (
                    id TEXT PRIMARY KEY,
                    event_type TEXT NOT NULL,
                    payment_id TEXT,
                    data TEXT NOT NULL,
                    processed BOOLEAN DEFAULT FALSE,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            conn.commit()
    
    def create_payment(self, payment_data: dict) -> str:
        """Создание записи о платеже"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO payments 
                (id, amount, currency, status, method, customer_id, gateway, metadata)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                payment_data['id'],
                payment_data['amount'],
                payment_data.get('currency', 'RUB'),
                payment_data['status'],
                payment_data['method'],
                payment_data.get('customer_id'),
                payment_data.get('gateway'),
                json.dumps(payment_data.get('metadata', {}))
            ))
            
            conn.commit()
            return payment_data['id']
    
    def update_payment(self, payment_id: str, updates: dict):
        """Обновление платежа"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            set_clause = ', '.join([f"{key} = ?" for key in updates.keys()])
            values = list(updates.values()) + [payment_id]
            
            cursor.execute(f'''
                UPDATE payments 
                SET {set_clause}, updated_at = CURRENT_TIMESTAMP
                WHERE id = ?
            ''', values)
            
            conn.commit()
    
    def get_payment(self, payment_id: str) -> Optional[dict]:
        """Получение платежа по ID"""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            cursor.execute('SELECT * FROM payments WHERE id = ?', (payment_id,))
            row = cursor.fetchone()
            
            if row:
                payment = dict(row)
                payment['metadata'] = json.loads(payment['metadata'] or '{}')
                return payment
            return None
    
    def get_payments_by_customer(self, customer_id: str) -> List[dict]:
        """Получение всех платежей клиента"""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT * FROM payments 
                WHERE customer_id = ? 
                ORDER BY created_at DESC
            ''', (customer_id,))
            
            payments = []
            for row in cursor.fetchall():
                payment = dict(row)
                payment['metadata'] = json.loads(payment['metadata'] or '{}')
                payments.append(payment)
            
            return payments
    
    def create_refund(self, refund_data: dict) -> str:
        """Создание возврата"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO refunds (id, payment_id, amount, reason, status)
                VALUES (?, ?, ?, ?, ?)
            ''', (
                refund_data['id'],
                refund_data['payment_id'],
                refund_data['amount'],
                refund_data.get('reason'),
                refund_data.get('status', 'pending')
            ))
            
            conn.commit()
            return refund_data['id']
    
    def create_customer(self, customer_data: dict) -> str:
        """Создание клиента"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO customers (id, email, name, phone, metadata)
                VALUES (?, ?, ?, ?, ?)
            ''', (
                customer_data['id'],
                customer_data.get('email'),
                customer_data.get('name'),
                customer_data.get('phone'),
                json.dumps(customer_data.get('metadata', {}))
            ))
            
            conn.commit()
            return customer_data['id']
