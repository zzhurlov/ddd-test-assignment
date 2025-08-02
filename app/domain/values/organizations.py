from dataclasses import dataclass

from app.domain.exceptions.organizations import (
    InvalidPhoneNumberException,
    OrganizationTitleTooLongException,
)
from app.domain.values.base import BaseValueObject

import re

from app.settings.constants import MAX_TITLE_LENGTH, PHONE_REGEX


@dataclass(frozen=True)
class OrganizationTitle(BaseValueObject):
    value: str

    def validate(self):
        if len(self.value) > MAX_TITLE_LENGTH:
            raise OrganizationTitleTooLongException(self.value)

    def as_generic_type(self):
        return str(self.value)


@dataclass(frozen=True)
class PhoneNumber(BaseValueObject):
    value: str

    def validate(self):
        if not bool(PHONE_REGEX.match(self.value)):
            raise InvalidPhoneNumberException(self.value)

    def as_generic_type(self):
        return str(self.value)
