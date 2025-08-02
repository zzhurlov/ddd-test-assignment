from dataclasses import dataclass

from app.domain.exceptions.activities import ActivityTitleTooLongException
from app.domain.values.base import BaseValueObject
from app.settings.constants import MAX_TITLE_LENGTH


@dataclass(frozen=True)
class ActivityTitle(BaseValueObject):
    value: str

    def validate(self):
        if len(self.value) > MAX_TITLE_LENGTH:
            raise ActivityTitleTooLongException(self.value)

    def as_generic_type(self):
        return str(self.value)
