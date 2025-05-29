.PHONY: dev lint format migrate upgrade

# Запуск FastAPI сервера
back-dev:
	poetry run uvicorn wishwise_pr.main:app --reload

front-install:
	pnpm install

front-dev:
	pnpm run dev

# Применить все миграции
upgrade:
	poetry run alembic upgrade head

# Создать новую миграцию
migrate:
	poetry run alembic revision --autogenerate -m "update"

# Форматирование кода
format:
	poetry run black .
	poetry run ruff --fix .

# Проверка стиля
lint:
	poetry run ruff .
