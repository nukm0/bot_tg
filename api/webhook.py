import json
import os
from http.server import BaseHTTPRequestHandler
import requests

# Токен бота
BOT_TOKEN = "8892504157:AAGrYBCYPOEr8hDzFNd9gWsjCgJa0LLB1po"

def send_message(chat_id, text):
    """Отправляет сообщение пользователю"""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": text
    }
    try:
        requests.post(url, json=data, timeout=5)
    except Exception as e:
        print(f"Ошибка: {e}")

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        """Telegram отправляет сюда все сообщения"""
        length = int(self.headers.get('Content-Length', 0))
        data = self.rfile.read(length)
        update = json.loads(data)
        
        # Проверяем, есть ли сообщение
        if 'message' in update:
            msg = update['message']
            chat_id = msg['chat']['id']
            
            # Проверяем текст сообщения
            if 'text' in msg:
                text = msg['text']
                
                # Если команда /start
                if text == '/start':
                    send_message(chat_id, "Привет!")
        
        # Отвечаем Telegram, что всё обработано
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({"ok": True}).encode())
    
    def do_GET(self):
        """Проверка работоспособности"""
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Bot is running")
