from dataclasses import dataclass

from app.domain.exceptions.base import ApplicationException


@dataclass
class ActivityTitleTooLongException(ApplicationException):
    title: str

    @property
    def message(self):
        return f'Слишком длинное название деятельности "{self.title[:255]}..."'
