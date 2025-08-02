from dataclasses import dataclass

from app.domain.exceptions.buildings import GeoPointException, InvalidAddressException
from app.domain.values.base import BaseValueObject


@dataclass(frozen=True)
class Address(BaseValueObject):
    value: str

    def validate(self):
        # TODO: hardcode
        if len(self.value) > 255:
            raise InvalidAddressException(self.value)

    def as_generic_type(self):
        return str(self.value)


@dataclass(frozen=True, slots=True)
class GeoPoint(BaseValueObject):
    value: tuple

    def validate(self):
        latitude = self.value[0]
        longitude = self.value[1]

        if not (-90 <= latitude <= 90):
            raise GeoPointException(latitude, longitude)
        if not (-180 <= longitude <= 180):
            raise GeoPointException(latitude, longitude)

    def as_generic_type(self):
        return tuple(self.value)
