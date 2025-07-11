# Используем официальный Python-образ
FROM python:3.11

# Устанавливаем Poetry
RUN pip install poetry

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем pyproject.toml и poetry.lock
COPY pyproject.toml poetry.lock* /app/

# Устанавливаем зависимости через Poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root

# Копируем весь проект
COPY . /app/

# Открываем порт (если нужно)
EXPOSE 8000

# Команда по умолчанию
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]