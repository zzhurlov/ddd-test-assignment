from dataclasses import dataclass

from app.domain.exceptions.base import ApplicationException


@dataclass
class TitleTooLongException(ApplicationException):
    title: str

    @property
    def message(self):
        return f'Слишком длинный текст названия "{self.title[:255]}..."'


@dataclass
class InvalidPhoneNumberException(ApplicationException):
    phone_number: str

    @property
    def message(self):
        return f'Невалидный номер телефона "{self.phone_number}"'
