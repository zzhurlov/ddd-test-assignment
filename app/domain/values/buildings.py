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
    latitude: float
    longitude: float

    def validate(self):
        if not (-90 <= self.latitude <= 90):
            raise GeoPointException(self.latitude, self.longitude)
        if not (-180 <= self.longitude <= 180):
            raise GeoPointException(self.latitude, self.longitude)
