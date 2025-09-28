.PHONY: help build run test format lint clean docker-build docker-run docker-stop

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-15s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install: ## Install dependencies
	pip install -r requirements.txt

format: ## Format code with black
	black .

format-check: ## Check code formatting
	black --check --diff .

lint: ## Run linting
	flake8 app tests

test: ## Run tests
	pytest tests/ -v

test-cov: ## Run tests with coverage
	coverage run -m pytest tests/
	coverage report --show-missing
	coverage html

clean: ## Clean up cache files
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf .pytest_cache
	rm -rf .coverage
	rm -rf htmlcov

docker-build: ## Build Docker image
	docker build -t signal-equipment-api .

docker-run: ## Run with Docker Compose
	docker-compose up -d

docker-stop: ## Stop Docker Compose
	docker-compose down

docker-logs: ## View Docker logs
	docker-compose logs -f

dev: ## Run development server
	uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

migrate: ## Run database migrations (placeholder for future use)
	@echo "Database migrations would go here"

setup: install ## Setup development environment
	@echo "Development environment setup complete"