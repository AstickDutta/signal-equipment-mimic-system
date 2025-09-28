#  Signal Equipment Backend API

> **A modern, high-performance FastAPI backend that simulates signal equipment management with comprehensive CI/CD automation.**

This is a FastAPI backend that mimics signal equipment. It provides APIs to manage signals and their aspects (PERMISSIVE, RESTRICTIVE, OVERRIDE).

## Key Features

- **Signal Management** - Create, read signals with comprehensive validation
- **Aspect Control** - Create, read, and update aspects with state management
- **State Monitoring** - Get real-time aspect states and configurations
- **Signal Analytics** - Get all aspects of a signal with detailed information
- **Smart Logic** - Business logic for mutual exclusivity between PERMISSIVE and 
RESTRICTIVE aspects

- **Containerized** - Full Docker support with PostgreSQL database integration
- ** Advanced CI/CD** - Complete GitHub Actions pipeline with automated workflows
- ** Quality Assurance** - Automated testing and comprehensive code quality checks
- ** Code Standards** - Automatic code formatting with Black and linting with Flake8
- ** Test Coverage** - Comprehensive unit tests with 89% coverage reporting
- ** Container Registry** - Automated Docker image building and registry pushing
- ** Security First** - Multi-layer security scanning with Trivy and Bandit tools
- ** Performance** - Optimized database queries and efficient API responses

## Technology Stack

| Component | Technology | Version |
|-----------|------------|---------|
| **Backend Framework** | FastAPI | 0.104+ |
| **Database** | PostgreSQL | 15+ |
| **ORM** | SQLAlchemy | 2.0+ |
| **Container** | Docker | Latest |
| **Testing** | Pytest | Latest |
| **Code Quality** | Black, Flake8 | Latest |

## System Requirements

- **Python**: 3.11+ (recommended 3.11.5+)
- **Docker**: Latest version with Docker Compose
- **PostgreSQL**: 15+ (when running locally without Docker)

## Quick Start with Docker

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   ```

2. **Launch with Docker Compose**
   ```bash
   docker-compose up -d
   ```

3. **Verify deployment**
   ```bash
   curl http://localhost:8000/health
   ```

The API will be available at **http://localhost:8000** with interactive documentation at **http://localhost:8000/docs**

## Development Setup

### Local Development Environment

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd signal-equipment-backend
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv .venv
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   .env
   # Edit .env with your configuration
   ```

5. **Run the development server**
   ```bash
   python run.py
   ```

### Environment Configuration

The application supports flexible configuration through environment variables:

```bash
DATABASE_URL=postgresql://postgres:password@db:5432/signal_equipment

API_HOST=0.0.0.0
API_PORT=8000
API_RELOAD=true

ENVIRONMENT=development
DEBUG=true

LOG_LEVEL=INFO
LOG_FORMAT=detailed

CORS_ORIGINS=*
CORS_METHODS=*
CORS_HEADERS=*
```

## Testing & Quality Assurance

### Running Tests Locally
```bash
pytest

pytest --cov=app --cov-report=html

pytest tests/test_api.py -v
```

### Code Quality Checks
```bash
black app/ tests/

flake8 app/ tests/

mypy app/
```

## CI/CD Pipeline

My comprehensive CI/CD pipeline includes:

### Continuous Integration
- **Automated Testing** - Full test suite execution on every push
- **Code Quality** - Black formatting and Flake8 linting checks
- **Security Scanning** - Vulnerability detection with Bandit and Trivy
- **Coverage Reporting** - Detailed test coverage analysis (89%+)

### Continuous Deployment
- **Docker Building** - Automated container image creation
- **Registry Push** - Secure image publishing to container registry
- **Staging Deployment** - Automatic deployment to staging environment
- **Health Checks** - Post-deployment verification and monitoring

### Pipeline Triggers
- **Push to main** - Full pipeline execution with deployment
- **Pull Requests** - Testing and quality checks only
- **Manual Triggers** - On-demand pipeline execution

## API Documentation

### Interactive Documentation
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Core Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | API welcome message and status |
| `GET` | `/health` | Health check endpoint |
| `POST` | `/signals/` | Create a new signal |
| `GET` | `/signals/` | Get all signals |
| `GET` | `/signals/{signal_id}` | Get specific signal |
| `POST` | `/signals/{signal_id}/aspects/` | Create aspect for signal |
| `GET` | `/signals/{signal_id}/aspects/` | Get all aspects of signal |
| `GET` | `/aspects/` | Get all aspects |

## Docker Configuration

### Production Deployment
```bash
docker build -t signal-equipment-api .

docker run -p 8000:8000 \
  -e DATABASE_URL=postgresql://user:pass@host:5432/db \
  signal-equipment-api
```

### Development with Docker Compose
```yaml
version: '3.8'
services:
  backend:
    volumes:
      - ./app:/app/app:ro
    environment:
      - DEBUG=true
      - API_RELOAD=true
```

## Security Features

- **Input Validation** - Comprehensive request validation with Pydantic
- **SQL Injection Protection** - SQLAlchemy ORM with parameterized queries
- **CORS Configuration** - Configurable cross-origin resource sharing
- **Environment Isolation** - Secure environment variable management
- **Container Security** - Multi-stage Docker builds with minimal attack surface

## Performance Optimization

- **Database Indexing** - Optimized database queries with proper indexing
- **Connection Pooling** - Efficient database connection management
- **Async Operations** - FastAPI's async capabilities for high concurrency
- **Response Caching** - Strategic caching for frequently accessed data
- **Resource Monitoring** - Built-in health checks and monitoring endpoints


### Support & Troubleshooting

### Common Issues

**Database Connection Issues**
```bash
# Check PostgreSQL status
docker-compose ps
docker-compose logs db
```

**Port Already in Use**
```bash

netstat -ano | findstr :8000
taskkill /PID <process_id> /F
```

**Environment Variables Not Loading**
```bash

cat .env
python -c "from dotenv import load_dotenv; load_dotenv(); import os; print(os.getenv('DATABASE_URL'))"
```