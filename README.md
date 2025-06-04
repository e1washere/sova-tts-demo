# 🎤 SOVA TTS Demo

## 📋 О проекте
Демонстрация системы синтеза русской речи SOVA TTS. Проект включает в себя:
- ✅ Рабочий API сервер для синтеза речи
- ✅ Веб-интерфейс для демонстрации
- ✅ Два голоса: Natasha (женский) и Ruslan (мужской)
- ✅ Полную документацию на русском языке

## 🚀 Быстрый старт

### 1. Установка зависимостей
```bash
pip3 install flask flask-cors pyyaml requests
```

### 2. Запуск демо
```bash
python3 demo_app.py
```

### 3. Открыть веб-интерфейс
- Перейдите по адресу: http://localhost:8899/demo_interface.html

### 4. Запустить тесты
```bash
python3 test_demo.py
```

## 🎯 Возможности

### Синтез речи
- Поддержка русского языка
- Два голоса: Natasha и Ruslan
- Настройка параметров:
  - Скорость речи (0.5 - 2.0)
  - Высота тона (0.5 - 2.0)
  - Громкость (-10 - +10 dB)

### API Endpoints
```bash
# Синтез речи
curl -X POST http://localhost:8899/synthesize/ \
  -H "Content-Type: application/json" \
  -d '{"text": "Привет мир!", "voice": "Natasha"}'

# Статус системы
curl http://localhost:8899/status

# Список голосов
curl http://localhost:8899/voices
```

### Пользовательские словари
```bash
# Добавить новое слово
curl -X POST http://localhost:8899/update_user_dict/ \
  -H "Content-Type: application/json" \
  -d '{
    "voice": "Natasha",
    "user_dict": {
      "TTS": "тэ тэ эс",
      "SOVA": "сова"
    }
  }'
```

## 📚 Документация
- [Полная презентация](SOVA_TTS_Demo_Presentation.md)
- [Инструкции по развертыванию](SHARING_INSTRUCTIONS.md)

## 🛠️ Технические детали
- **Модель**: Tacotron 2 + WaveGlow
- **API**: REST JSON
- **Язык**: Python
- **Интерфейс**: HTTP JSON API
- **Деплой**: Docker + Python

## 📞 Поддержка
Если у вас возникли вопросы по развертыванию или использованию демо, создайте Issue в этом репозитории.

---
