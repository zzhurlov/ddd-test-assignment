from dataclasses import dataclass

from app.domain.exceptions.base import ApplicationException
from app.settings.constants import MAX_TITLE_LENGTH


@dataclass
class ActivityTitleTooLongException(ApplicationException):
    title: str

    @property
    def message(self):
        return f'Слишком длинное название деятельности "{self.title[:MAX_TITLE_LENGTH]}..."'
