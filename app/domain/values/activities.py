from dataclasses import dataclass

from app.domain.exceptions.activities import ActivityTitleTooLongException
from app.domain.values.base import BaseValueObject


@dataclass(frozen=True)
class ActivityTitle(BaseValueObject):
    value: str

    def validate(self):
        # TODO: dont hardcode
        if len(self.value) > 255:
            raise ActivityTitleTooLongException(self.value)

    def as_generic_type(self):
        return str(self.value)
