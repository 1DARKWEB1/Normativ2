# 📊 Telegram Bot + Django Admin + PostgreSQL

Этот проект объединяет **Telegram-бота на Aiogram** и **административную панель Django**, работающих с одной и той же базой данных **PostgreSQL**.  

Бот сохраняет и показывает пользователей через **Django ORM (с использованием sync_to_async)**, а админка позволяет управлять данными через удобный интерфейс.

---

## 🚀 Возможности
### 🤖 Telegram-бот
- `/start` — регистрация пользователя в базе.  
- `/info` — просмотр своей информации.  
- `/users` — список всех пользователей.  
- Работа с базой через **Django ORM**, а не прямые SQL-запросы.  

### 🛠 Django Admin
- Просмотр и управление пользователями бота.  
- Поиск и фильтрация по `username` и `full_name`.  
- Возможность редактировать данные напрямую в админке.  

### 🗄 Общая база
- Единая база данных **PostgreSQL** для Django и Telegram-бота.  
- Удобное разделение: пользователи видят только бота, админ — всю базу через интерфейс.  

---

## 📂 Структура проекта
Normativ1/
- │── manage.py
- │── Normativ1/  # Telegram-бот
- │ └── settings.py # Настройки Django
- │── core/
- │ ├── models.py # Модель BotUser
- │ └── admin.py # Подключение модели в админку

---

## ⚙ Установка и запуск

### 1. Клонирование репозитория
- bash
- git clone https://github.com/username/telegram-django-bot.git
- cd telegram-django-bot
### 2. Установка зависимостей
- pip install -r requirements.txt
- python manage.py runserver
- Админка будет доступна по адресу: http://127.0.0.1:8000/admin/

3. Запуск Telegram-бота
- В файле normativ2.py вставьте ваш токен бота:
- TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
- Запуск:

---

## 💻 Пример работы бота
/start

Копировать код
👋 Привет! Ты зарегистрирован в базе ✅
/info

- 📝 Твои данные:
- ID: 12345678
- Имя: Jasurjon
- Username: @jasur
- Дата регистрации: 2025-10-01

<img width="914" height="215" alt="botn1" src="https://github.com/user-attachments/assets/14e4ef71-aa6b-42ce-a975-e5a27f4d29e8" />

---

/users

👥 Пользователи:
- @alex (Alex Ivanov)
- @jasur (Jasurjon)
- 🛠 Технологии
- Python 3.10+

<img width="924" height="322" alt="botn2" src="https://github.com/user-attachments/assets/c3f6e027-861c-4447-8168-73e3b676ba83" />

### Таблитца бд

<img width="627" height="313" alt="image" src="https://github.com/user-attachments/assets/ecf48a33-fef9-4f51-a623-b078596265fc" />

### Админка Джанго

<img width="1470" height="706" alt="image" src="https://github.com/user-attachments/assets/c3d9f4b9-614f-4133-8eb7-f90869dfbea7" />

---

## ORM через sync_to_async

<img width="1117" height="866" alt="image" src="https://github.com/user-attachments/assets/07ffd064-ca41-417a-ac32-7248f8674513" />




Aiogram — Telegram Bot Framework

Django — админка и ORM

PostgreSQL — база данных

asgiref.sync.sync_to_async — асинхронная работа с ORM
