from dataclasses import dataclass

from app.domain.exceptions.base import ApplicationException


@dataclass
class InvalidAddressException(ApplicationException):
    address: str

    @property
    def message(self):
        return f'Невалидный адрес здания "{self.address[:255]}"'


@dataclass
class GeoPointException(ApplicationException):
    latitude: float
    longitude: float

    @property
    def message(self):
        return f'Невалидные геоданные "{self.latitude}, {self.longitude}"'
