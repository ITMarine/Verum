FROM python:alpine

WORKDIR /app

RUN pip install fastapi uvicorn[standart] websockets

EXPOSE 8001

COPY . .

CMD ["uvicorn", "web_socket_api:app", "--host", "0.0.0.0", "--port", "8001"]