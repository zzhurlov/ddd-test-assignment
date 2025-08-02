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
        reg_exp = re.fullmatch(r"\+7\d{10}", self.value)
        if not bool(reg_exp):
            return InvalidPhoneNumberException(self.value)

    def as_generic_type(self):
        return str(self.value)
