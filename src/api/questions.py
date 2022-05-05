from typing import List

from fastapi import APIRouter, Depends, Path, status

from src.questions.models import QuestionResponseV1, QuestionAddResponseV1
from src.api.protocols import QuestionServiceProtocol

router = APIRouter(
    tags=['Questions']
)


@router.get(
    path='/v1/questions',
    response_model=List[QuestionResponseV1],
    summary='Список всех вопросов',
    description='Возвращает список всех вопросов.'
)
def get_all_questions(
        question_service: QuestionServiceProtocol = Depends()
):
    return question_service.get_all_questions()


@router.get(
    path='/v1/questions/{id}',
    response_model=QuestionResponseV1,
    summary='Информация о вопросе',
    description='Возвращает информацию о вопросе.'
)
def get_question(
        id: int = Path(..., ge=1),
        question_service: QuestionServiceProtocol = Depends()
):
    return question_service.get_question_by_id(id)


@router.put(
    path='/v1/questions',
    status_code=status.HTTP_201_CREATED,
    summary='Добавить вопрос',
    description='Добавляет вопрос и ответ в базу данных.'
)
def add_question(
        question_data: QuestionAddResponseV1,
        question_service: QuestionServiceProtocol = Depends()
):
    question_service.add_question(question_data)


@router.delete(
    path='/v1/questions/{id}',
    summary='Удалить вопрос',
    description='Удаляет вопрос.'
)
def delete_question(
        id: int = Path(..., ge=1),
        question_service: QuestionServiceProtocol = Depends()
):
    question_service.delete_question_by_id(id)
