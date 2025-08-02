from dataclasses import dataclass

from app.domain.exceptions.base import ApplicationException


@dataclass
class OrganizationTitleTooLongException(ApplicationException):
    title: str

    @property
    def message(self):
        return f'Слишком длинное название организации "{self.title[:255]}..."'


@dataclass
class InvalidPhoneNumberException(ApplicationException):
    phone_number: str

    @property
    def message(self):
        return f'Невалидный номер телефона "{self.phone_number}"'
