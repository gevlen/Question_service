import sqlalchemy as sa
from fastapi import FastAPI

from src.api import questions, random_questions, protocols
from src.database import DatabaseSettings, create_database_url
from src.questions.service import QuestionService
from src.random_questions.service import RandomQuestionService


def get_application() -> FastAPI:
    application = FastAPI(
        title='Questions from service.io',
        description='Сервис сбора вопросов с service.io.',
        version='1.0.0'
    )

    application.include_router(questions.router)
    application.include_router(random_questions.router)

    db_settings = DatabaseSettings()
    engine = sa.create_engine(
        create_database_url(db_settings),
        future=True
    )
    question_service = QuestionService(engine)
    application.dependency_overrides[protocols.QuestionServiceProtocol] = lambda: question_service

    random_question_service = RandomQuestionService(engine)
    application.dependency_overrides[protocols.RandomQuestionServiceProtocol] = lambda: random_question_service

    return application


app = get_application()
