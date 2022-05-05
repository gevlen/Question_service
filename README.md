# Question_service

## Описание

1. Реализация задания основана на FastAPI, SqlAlchemy, PostgreSQL.
2. Описание ручек в Swagger по адресу '/docs'. 
3. Все секреты хранятся в .env файле
4. Запустить приложение можно двумя способами:
   - Запустить в контейнере с помощью docker-compose командой ```$ docker-compose up -d``` из корня проекта
   - Запуск в интерпретаторе питона:
     - Установить все зависимости ```$ pip install -r requirements.txt``` из корня проекта
     - Запустить PostgreSQL (например, через ```$ docker-compose up -d``` из папки postgres-data)
     - Произвести миграции с помощью alembic командой ```$ alembic upgrade head``` из корня проекта
     - Запустить проект в интерпретаторе питона: ```$ uvicorn src.api.main:app --host 0.0.0.0 --port 5000 --workers 4 ``` 

## Пример запроса к POST API сервиса

### Request

```curl
curl -X 'POST' \
  'http://0.0.0.0:5000/v1/random_questions' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "questions_num": 2
}'
```

### Response



Response body
```json
{
  "id": 4,
  "external_id": 94152,
  "question": "A \"Jack Bauer\" is a doc who is still up & working after this many hours",
  "answer": "24",
  "created_at_jservice": "2014-02-14T01:59:46.490000",
  "created_at_db": "2022-05-05T13:49:09.694923",
  "category_id": 12506
}
```

Response headers
```
  content-length: 245  
  content-type: application/json  
  date: Thu,05 May 2022 10:49:39 GMT  
  server: uvicorn 
```
