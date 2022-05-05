from typing import List
from datetime import datetime

from sqlalchemy import select, insert, delete, exc
from sqlalchemy.future import Engine

from src.database import tables
from src.questions.models import QuestionResponseV1, QuestionAddResponseV1

from fastapi import HTTPException


class QuestionService:
    def __init__(self, engine: Engine) -> None:
        self._engine = engine

    def get_all_questions(self) -> List[QuestionResponseV1]:
        query = select(tables.questions)
        with self._engine.connect() as connection:
            questions_data = connection.execute(query)
        questions = []
        for question_data in questions_data:
            question_data = QuestionResponseV1(
                id=question_data['id'],
                external_id=question_data['external_id'],
                question=question_data['question'],
                answer=question_data['answer'],
                created_at_jservice=question_data['created_at_jservice'],
                created_at_db=question_data['created_at_db'],
                category_id=question_data['category_id']
            )
            questions.append(question_data)
        return questions

    def get_question_by_id(self, id: int) -> QuestionResponseV1:
        query = select(tables.questions).where(tables.questions.c.id == id)
        with self._engine.connect() as connection:
            question_data = connection.execute(query).first()
            if not question_data:
                raise HTTPException(
                    status_code=404,
                    detail="Question not found"
                )
        question = QuestionResponseV1(
            id=question_data['id'],
            external_id=question_data['external_id'],
            question=question_data['question'],
            answer=question_data['answer'],
            created_at_jservice=question_data['created_at_jservice'],
            created_at_db=question_data['created_at_db'],
            category_id=question_data['category_id']
        )
        return question

    def add_question(self, question: QuestionAddResponseV1) -> None:
        query = insert(tables.questions).values(
            external_id=None,
            question=question.question,
            answer=question.answer,
            created_at_jservice=None,
            created_at_db=datetime.now(),
            category_id=question.category_id
        )
        with self._engine.connect() as connection:
            try:
                connection.execute(query)
                connection.commit()
            except exc.IntegrityError:
                raise HTTPException(
                    status_code=409,
                    detail="An attempt was made to create an object that already exists"
                )
    def delete_question_by_id(self, id: int) -> None:
        query = delete(tables.questions).where(tables.questions.c.id == id)
        with self._engine.connect() as connection:
            connection.execute(query)
            connection.commit()
