# 🚦 Signal Equipment Backend API

> **A modern, high-performance FastAPI backend that simulates signal equipment management with comprehensive CI/CD automation.**

This is a FastAPI backend that mimics signal equipment. It provides APIs to manage signals and their aspects (PERMISSIVE, RESTRICTIVE, OVERRIDE).

## ✨ Key Features

- 🚦 **Signal Management** - Create, read signals with comprehensive validation
- 🔄 **Aspect Control** - Create, read, and update aspects with state management
- 📊 **State Monitoring** - Get real-time aspect states and configurations
- 📋 **Signal Analytics** - Get all aspects of a signal with detailed information
- 🧠 **Smart Logic** - Business logic for mutual exclusivity between PERMISSIVE and RESTRICTIVE aspects
- 🐳 **Containerized** - Full Docker support with PostgreSQL database integration
- **🚀 Advanced CI/CD** - Complete GitHub Actions pipeline with automated workflows
- **🔧 Quality Assurance** - Automated testing and comprehensive code quality checks
- **🎨 Code Standards** - Automatic code formatting with Black and linting with Flake8
- **✅ Test Coverage** - Comprehensive unit tests with 89% coverage reporting
- **🐳 Container Registry** - Automated Docker image building and registry pushing
- **🔒 Security First** - Multi-layer security scanning with Trivy and Bandit tools
- **📈 Performance** - Optimized database queries and efficient API responses

## 🛠️ Technology Stack

| Component | Technology | Version |
|-----------|------------|---------|
| **Backend Framework** | FastAPI | 0.104+ |
| **Database** | PostgreSQL | 15+ |
| **ORM** | SQLAlchemy | 2.0+ |
| **Container** | Docker | Latest |
| **Testing** | Pytest | Latest |
| **Code Quality** | Black, Flake8 | Latest |

## 📋 System Requirements

- **Python**: 3.11+ (recommended 3.11.5+)
- **Docker**: Latest version with Docker Compose
- **PostgreSQL**: 15+ (when running locally without Docker)
- **Memory**: Minimum 2GB RAM for optimal performance
- **Storage**: 1GB free space for dependencies and database

## 🚀 Quick Start with Docker

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd signal-equipment-backend
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

## 🔧 Development Setup

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

3. **Activate the virtual environment**
   - **Windows**: `.venv\Scripts\activate`
   - **Linux/Mac**: `source .venv/bin/activate`

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

6. **Run the development server**
   ```bash
   python run.py
   ```

### Environment Configuration

The application supports flexible configuration through environment variables:

```bash
# Database Configuration
DATABASE_URL=postgresql://postgres:root123@db:5432/signal_equipment

# API Configuration  
API_HOST=0.0.0.0
API_PORT=8000
API_RELOAD=true

# Environment Settings
ENVIRONMENT=development
DEBUG=true

# Logging Configuration
LOG_LEVEL=INFO
LOG_FORMAT=detailed

# CORS Settings
CORS_ORIGINS=*
CORS_METHODS=*
CORS_HEADERS=*
```

## 🧪 Testing & Quality Assurance

### Running Tests Locally
```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=app --cov-report=html

# Run specific test file
pytest tests/test_api.py -v
```

### Code Quality Checks
```bash
# Format code with Black
black app/ tests/

# Lint with Flake8
flake8 app/ tests/

# Type checking (if mypy is configured)
mypy app/
```

## 🚀 CI/CD Pipeline

Our comprehensive CI/CD pipeline includes:

### 🔄 Continuous Integration
- **Automated Testing** - Full test suite execution on every push
- **Code Quality** - Black formatting and Flake8 linting checks
- **Security Scanning** - Vulnerability detection with Bandit and Trivy
- **Coverage Reporting** - Detailed test coverage analysis (89%+)

### 🚢 Continuous Deployment
- **Docker Building** - Automated container image creation
- **Registry Push** - Secure image publishing to container registry
- **Staging Deployment** - Automatic deployment to staging environment
- **Health Checks** - Post-deployment verification and monitoring

### 📊 Pipeline Triggers
- **Push to main** - Full pipeline execution with deployment
- **Pull Requests** - Testing and quality checks only
- **Manual Triggers** - On-demand pipeline execution

## 📚 API Documentation

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

## 🐳 Docker Configuration

### Production Deployment
```bash
# Build production image
docker build -t signal-equipment-api .

# Run with production settings
docker run -p 8000:8000 \
  -e DATABASE_URL=postgresql://user:pass@host:5432/db \
  signal-equipment-api
```

### Development with Docker Compose
```yaml
# docker-compose.override.yml for development
version: '3.8'
services:
  backend:
    volumes:
      - ./app:/app/app:ro
    environment:
      - DEBUG=true
      - API_RELOAD=true
```

## 🔒 Security Features

- **Input Validation** - Comprehensive request validation with Pydantic
- **SQL Injection Protection** - SQLAlchemy ORM with parameterized queries
- **CORS Configuration** - Configurable cross-origin resource sharing
- **Environment Isolation** - Secure environment variable management
- **Container Security** - Multi-stage Docker builds with minimal attack surface

## 📈 Performance Optimization

- **Database Indexing** - Optimized database queries with proper indexing
- **Connection Pooling** - Efficient database connection management
- **Async Operations** - FastAPI's async capabilities for high concurrency
- **Response Caching** - Strategic caching for frequently accessed data
- **Resource Monitoring** - Built-in health checks and monitoring endpoints

## 🤝 Contributing

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Make your changes** with proper testing
4. **Run quality checks** (`black app/ && flake8 app/`)
5. **Commit your changes** (`git commit -m 'Add amazing feature'`)
6. **Push to the branch** (`git push origin feature/amazing-feature`)
7. **Open a Pull Request** with detailed description

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support & Troubleshooting

### Common Issues

**Database Connection Issues**
```bash
# Check PostgreSQL status
docker-compose ps
docker-compose logs db
```

**Port Already in Use**
```bash
# Find and kill process using port 8000
netstat -ano | findstr :8000
taskkill /PID <process_id> /F
```

**Environment Variables Not Loading**
```bash
# Verify .env file exists and is properly formatted
cat .env
python -c "from dotenv import load_dotenv; load_dotenv(); import os; print(os.getenv('DATABASE_URL'))"
```

### Getting Help

- 📧 **Email**: support@signal-equipment-api.com
- 🐛 **Issues**: [GitHub Issues](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME/issues)
- 📖 **Documentation**: [Wiki](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME/wiki)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME/discussions)

---

**Made with ❤️ by the Signal Equipment Team** | **Last Updated**: December 2024