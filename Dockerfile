# Используем многоступенчатую сборку
FROM python:3.12-slim as builder

WORKDIR /root/src/app

# Копируем только файл с зависимостями
COPY requirements.txt .

# Устанавливаем зависимости в виртуальное окружение
RUN python -m venv /venv \
    && /venv/bin/pip install --no-cache-dir -r requirements.txt

# Финальный этап сборки
FROM python:3.12-slim

# Создаем пользователя для запуска приложения
RUN useradd -m myuser
USER myuser

WORKDIR /home/myuser/src/app

# Копируем виртуальное окружение из предыдущего этапа
COPY --from=builder /venv /venv

# Копируем исходный код приложения
COPY . .

# Указываем путь к исполняемым файлам в виртуальном окружении
ENV PATH="/venv/bin:$PATH"

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
