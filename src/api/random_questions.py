from fastapi import APIRouter, Depends, status

from src.random_questions.models import CountAddResponseV2
from src.api.protocols import RandomQuestionServiceProtocol

router = APIRouter(
    tags=['RandomQuestions']
)


@router.post(
    path='/v1/random_questions',
    status_code=status.HTTP_201_CREATED,
    summary='Добавить вопросы',
    description='Добавляет заданное количество рандомных вопросов и ответов в базу данных.',
)
def add_question(
        question_data: CountAddResponseV2,
        question_service: RandomQuestionServiceProtocol = Depends()
):
    return question_service.add_random_number_of_questions(question_data)
