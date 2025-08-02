from dataclasses import dataclass

from app.domain.exceptions.base import ApplicationException
from app.settings.constants import MAX_TITLE_LENGTH


@dataclass
class OrganizationTitleTooLongException(ApplicationException):
    title: str

    @property
    def message(self):
        return (
            f'Слишком длинное название организации "{self.title[:MAX_TITLE_LENGTH]}..."'
        )


@dataclass
class InvalidPhoneNumberException(ApplicationException):
    phone_number: str

    @property
    def message(self):
        return f'Невалидный номер телефона "{self.phone_number}"'
