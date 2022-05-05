from typing import List

from src.questions.models import QuestionResponseV1, QuestionAddResponseV1
from src.random_questions.models import CountAddResponseV2


class QuestionServiceProtocol:
    def get_all_questions(self) -> List[QuestionResponseV1]:
        raise NotImplementedError

    def get_question_by_id(self, id: int) -> QuestionResponseV1:
        raise NotImplementedError

    def add_question(self, question: QuestionAddResponseV1) -> None:
        raise NotImplementedError

    def delete_question_by_id(self, id: int) -> None:
        raise NotImplementedError


class RandomQuestionServiceProtocol:
    def add_random_number_of_questions(self, count: CountAddResponseV2) -> List[QuestionResponseV1]:
        raise NotImplementedError
