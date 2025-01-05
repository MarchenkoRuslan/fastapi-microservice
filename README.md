# KYC Service

Сервис для верификации клиентов и обработки заказов с интеграцией Binance. Включает в себя систему опросов для предварительной оценки клиентов и интеграцию с внешним KYC-провайдером.

## Особенности

- Интеграция с Binance API
- Система опросов для оценки клиентов
- Внешний KYC-провайдер для верификации
- REST API на FastAPI
- Асинхронная обработка запросов

## Описание

Сервис предоставляет API для:
- Проверки существования ордеров в Binance
- Верификации клиентов через KYC провайдера
- Управления анкетированием клиентов
- Хранения и обработки данных клиентов

### Основные возможности:

1. **Проверка ордеров**
   - Валидация существования ордера в Binance
   - Извлечение данных о клиенте из ордера
   - Автоматическая регистрация новых клиентов

2. **Верификация клиентов**
   - Интеграция с KYC провайдером
   - Система опросников для предварительной оценки
   - Отслеживание статуса верификации

## Технический стек

- **Backend**: Python 3.11, FastAPI
- **Database**: PostgreSQL, SQLAlchemy, Alembic
- **Контейнеризация**: Docker, Docker Compose
- **CI/CD**: GitLab CI
- **Тестирование**: pytest
- **Линтинг**: flake8, black, isort

## Установка

### Требования

- Python 3.11+
- PostgreSQL
- Docker и Docker Compose (опционально)

### Локальная установка

1. Клонируйте репозиторий:
```bash
git clone https://gitlab.com/aheads-group/fast-api.git
cd fast-api
```

2. Создайте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
# или
.\venv\Scripts\activate   # Windows
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Настройте переменные окружения:
```bash
cp .env.example .env
# Отредактируйте .env файл, установив необходимые значения
```

### Docker установка

1. Соберите и запустите контейнеры:
```bash
docker-compose up -d
```

## Конфигурация

Основные настройки в `.env`:

```ini
# PostgreSQL
POSTGRES_SERVER=localhost
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_password
POSTGRES_DB=kyc_service

# API Keys
BINANCE_API_KEY=your_binance_api_key
BINANCE_API_SECRET=your_binance_api_secret
KYC_PROVIDER_API_KEY=your_kyc_provider_api_key
KYC_PROVIDER_API_URL=https://api.kyc-provider.com

# Security
JWT_SECRET_KEY=your_secret_key
JWT_ALGORITHM=HS256
```

## API Endpoints

### Публичные эндпоинты

#### Проверка ордера
```http
GET /api/v1/public/check-order/{order_id}
```
Проверяет существование ордера и необходимость верификации клиента

#### Получение опросника
```http
GET /api/v1/public/survey
```
Возвращает активный опросник для клиента

#### Отправка ответов на опросник
```http
POST /api/v1/public/survey/submit
```
Принимает ответы на опросник и инициирует KYC верификацию

### Webhook эндпоинты

#### KYC вебхук
```http
POST /api/v1/webhooks/kyc-webhook
```
Обрабатывает результаты верификации от KYC провайдера

## Разработка

### Запуск тестов
```bash
# Запуск всех тестов с отчетом о покрытии
pytest --cov=app

# Запуск конкретного теста
pytest tests/api/test_public.py -v
```

### Линтинг кода
```bash
# Проверка стиля
flake8 app

# Форматирование
black app

# Сортировка импортов
isort app
```

### Миграции базы данных
```bash
# Создание новой миграции
alembic revision --autogenerate -m "Description"

# Применение миграций
alembic upgrade head
```

## CI/CD

Проект использует GitLab CI/CD со следующими этапами:
- Линтинг кода
- Запуск тестов
- Сборка Docker образа
- Деплой (ручной запуск)

## Структура проекта

```
app/
├── alembic/                    # Миграции БД
├── api/                        # API endpoints
│   └── v1/
│       ├── endpoints/         
│       │   ├── public.py      # Публичные эндпоинты
│       │   └── webhooks.py    # Вебхуки
├── core/                      # Ядро приложения
│   ├── config.py             # Конфигурация
│   └── logger.py             # Настройки логирования
├── db/                       # Работа с БД
│   ├── base.py              # Базовые классы БД
│   └── session.py           # Управление сессиями
├── models/                   # SQLAlchemy модели
│   ├── client.py            # Модель клиента
│   ├── profile.py           # Модель профиля
│   ├── survey.py            # Модели опросников
│   └── verification.py      # Модель верификации
├── schemas/                  # Pydantic схемы
├── services/                 # Бизнес-логика
└── tests/                   # Тесты
```

## Мониторинг и логирование

### Логирование
- Все HTTP запросы логируются с временем выполнения
- Ошибки автоматически записываются в лог-файлы
- Ротация логов настроена через RotatingFileHandler

### Метрики
- Время ответа эндпоинтов
- Статус верификаций
- Количество успешных/неуспешных запросов

### Алерты
- Оповещение при критических ошибках
- Мониторинг статуса сервиса через /health эндпоинт

## Поддержка и развитие

### Сообщение об ошибках
1. Проверьте существующие issues в GitLab
2. Создайте новый issue с описанием проблемы:
   - Шаги для воспроизведения
   - Ожидаемое поведение
   - Фактическое поведение
   - Логи и скриншоты (если есть)

### Внесение изменений
1. Создайте fork репозитория
2. Внесите изменения в отдельной ветке
3. Убедитесь, что все тесты проходят
4. Создайте Merge Request

## Лицензия

[MIT License](LICENSE)

## Авторы

- Команда Aheads Group
- Поддержка: support@aheads-group.com
