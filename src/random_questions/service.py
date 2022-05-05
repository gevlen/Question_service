from datetime import datetime

import requests
import sqlalchemy.exc

from fastapi.encoders import jsonable_encoder

from sqlalchemy import select, insert, desc
from sqlalchemy.future import Engine

from src.database import tables
from src.random_questions.models import CountAddResponseV2
from src.questions.models import QuestionResponseV1


class RandomQuestionService:
    def __init__(self, engine: Engine) -> None:
        self._engine = engine

    def add_random_number_of_questions(self, count: CountAddResponseV2) -> QuestionResponseV1:
        json_compatible_item_data = jsonable_encoder(count)
        count = json_compatible_item_data['questions_num']
        with self._engine.connect() as connection:
            query = select(tables.questions).order_by(desc(tables.questions.c.created_at_db)).limit(1)
            question_data = connection.execute(query).first()
            if question_data:
                answer = QuestionResponseV1(
                    id=question_data['id'],
                    external_id=question_data['external_id'],
                    question=question_data['question'],
                    answer=question_data['answer'],
                    created_at_jservice=question_data['created_at_jservice'],
                    created_at_db=question_data['created_at_db'],
                    category_id=question_data['category_id']
                )
            else:
                answer = []
            while count > 0:
                questions_data = requests.get(f'https://jservice.io/api/random?count={count}').json()
                for question_data in questions_data:
                    query = insert(tables.questions).values(
                        external_id=question_data['id'],
                        question=question_data['question'],
                        answer=question_data['answer'],
                        created_at_jservice=question_data['created_at'],
                        created_at_db=datetime.now(),
                        category_id=question_data['category_id']
                    )
                    try:
                        connection.execute(query)
                        connection.commit()
                        count -= 1
                    except sqlalchemy.exc.IntegrityError:
                        continue
        return answer
