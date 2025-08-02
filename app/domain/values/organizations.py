from dataclasses import dataclass

from app.domain.exceptions.organizations import (
    InvalidPhoneNumberException,
    OrganizationTitleTooLongException,
)
from app.domain.values.base import BaseValueObject

import re


@dataclass(frozen=True)
class OrganizationTitle(BaseValueObject):
    value: str

    def validate(self):
        # TODO: dont hardcode
        if len(self.value) > 255:
            raise OrganizationTitleTooLongException(self.value)

    def as_generic_type(self):
        return str(self.value)


@dataclass(frozen=True)
class PhoneNumber(BaseValueObject):
    value: str

    def validate(self):
        # TODO: в конфиг вынеси
        PHONE_REGEX = re.compile(r"^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$")
        if not bool(PHONE_REGEX.match(self.value)):
            raise InvalidPhoneNumberException(self.value)

    def as_generic_type(self):
        return str(self.value)
