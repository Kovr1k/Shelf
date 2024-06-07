FROM python:3.12-slim as builder

WORKDIR /root/src/app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Build your code here (e.g., compilation)

FROM python:3.12-slim

WORKDIR /root/src/app

COPY --from=builder /root/src/app/ .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
