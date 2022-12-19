
## Задача

Создать backend часть, состоящую из нескольких сервисов:
1. Сервер очередей rabbitmq
2. http api.
http API с единственным методом /queue_reverse_text
В качестве параметра должен быть произвольный текст.
Обработка заключается в том, что запрос попадает в персистентную очередь rabbitmq.
Реализовать можно на любом python http asyncio фреймворке (например aiohttp, fastapi).
3. background worker
Читает очередь заданий в rabbitmq, выполняет их обработку переворачивая текст и сохраняет результат.
Реализовать на python
4. web socket api
web socket api c эндпоинтом /listen_results
Клиент по этому эндпоинту может подключиться и пассивно получать результаты обработки задач по мере их получения.
Реализовать можно на любом python websocket asyncio фреймворке.

Сервисы релизовать как docker контейнеры.

Как предпологается проверять:
1. Разворачиваем сервисы локально на машине.
2. Скриптом подключаемся к эндпоинту /listen_results websocket api (например, скриптом listen_results.py)
3. С помощью другого небольшого скрипта создаем запросы на /queue_reverse_text (например, скрипт queue_reverse_text.py)
4. Смотрим, что в командной  строке listen_results.py, появляются результаты по мере того, как мы используем queue_reverse_text.py

Например:
1. ввели в командной строке: queue_reverse_text.py 123
2. в командной строке listen_results.py появилось: input: 123, output: 321



### Запуск сервисов

```bash
docker-compose up --build
```

### Запуск скрипта на обработку

```bash
pip install -r requirements.txt
```
```bash
python3 queue_reverse_text/queue_reverse_text.py
```

### Запуск скрипта на прослушивание результата

```bash
pip install -r requirements.txt
```
```bash
python3 listen_results/listen_results.py
```
