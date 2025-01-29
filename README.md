# KYC Service

A service for client verification and order processing with Binance integration. Includes a survey system for preliminary client assessment and integration with an external KYC provider.

## Features

- Binance API Integration
- Client Assessment Survey System
- External KYC Provider Integration
- FastAPI REST API
- Asynchronous Request Processing

## Description

The service provides APIs for:
- Verifying order existence in Binance
- Client verification through KYC provider
- Managing client surveys
- Storing and processing client data

### Core Capabilities:

1. **Order Verification**
   - Validate order existence in Binance
   - Extract client data from orders
   - Automatic registration of new clients

2. **Client Verification**
   - KYC provider integration
   - Survey system for preliminary assessment
   - Verification status tracking

## Tech Stack

- **Backend**: Python 3.11, FastAPI
- **Database**: PostgreSQL, SQLAlchemy, Alembic
- **Containerization**: Docker, Docker Compose
- **CI/CD**: GitLab CI
- **Testing**: pytest
- **Linting**: flake8, black, isort

## Installation

### Requirements

- Python 3.11+
- PostgreSQL
- Docker and Docker Compose (optional)

### Local Installation

1. Clone the repository:
```bash
git clone https://gitlab.com/aheads-group/fast-api.git
cd fast-api
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
# or
.\venv\Scripts\activate   # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
```bash
cp .env.example .env
# Edit .env file with appropriate values
```

### Docker Installation

1. Build and run containers:
```bash
docker-compose up -d
```

## Configuration

Main settings in `.env`:

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

### Public Endpoints

#### Check Order
```http
GET /api/v1/public/check-order/{order_id}
```
Verifies order existence and client verification requirements

#### Get Survey
```http
GET /api/v1/public/survey
```
Returns active survey for client

#### Submit Survey
```http
POST /api/v1/public/survey/submit
```
Accepts survey responses and initiates KYC verification

### Webhook Endpoints

#### KYC Webhook
```http
POST /api/v1/webhooks/kyc-webhook
```
Processes verification results from KYC provider

## Development

### Running Tests
```bash
# Run all tests with coverage report
pytest --cov=app

# Run specific test
pytest tests/api/test_public.py -v
```

### Code Linting
```bash
# Style check
flake8 app

# Formatting
black app

# Import sorting
isort app
```

### Database Migrations
```bash
# Create new migration
alembic revision --autogenerate -m "Description"

# Apply migrations
alembic upgrade head
```

## CI/CD

The project uses GitLab CI/CD with the following stages:
- Code linting
- Running tests
- Docker image building
- Deployment (manual trigger)

## Project Structure

```
app/
├── alembic/                    # DB migrations
├── api/                        # API endpoints
│   └── v1/
│       ├── endpoints/         
│       │   ├── public.py      # Public endpoints
│       │   └── webhooks.py    # Webhooks
├── core/                      # Application core
│   ├── config.py             # Configuration
│   └── logger.py             # Logging settings
├── db/                       # Database
│   ├── base.py              # Base DB classes
│   └── session.py           # Session management
├── models/                   # SQLAlchemy models
│   ├── client.py            # Client model
│   ├── profile.py           # Profile model
│   ├── survey.py            # Survey models
│   └── verification.py      # Verification model
├── schemas/                  # Pydantic schemas
├── services/                 # Business logic
└── tests/                   # Tests
```

## Monitoring and Logging

### Logging
- All HTTP requests are logged with execution time
- Errors are automatically written to log files
- Log rotation configured through RotatingFileHandler

### Metrics
- Endpoint response time
- Verification status
- Successful/failed request count

### Alerts
- Critical error notifications
- Service status monitoring via /health endpoint

## Support and Development

### Bug Reporting
1. Check existing issues in GitLab
2. Create new issue with problem description:
   - Steps to reproduce
   - Expected behavior
   - Actual behavior
   - Logs and screenshots (if available)

### Contributing
1. Fork the repository
2. Make changes in a separate branch
3. Ensure all tests pass
4. Create Merge Request
