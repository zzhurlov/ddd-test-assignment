from dataclasses import dataclass

from app.domain.exceptions.base import ApplicationException
from app.settings.constants import MAX_TITLE_LENGTH


@dataclass
class InvalidAddressException(ApplicationException):
    address: str

    @property
    def message(self):
        return f'Невалидный адрес здания "{self.address[:MAX_TITLE_LENGTH]}"'


@dataclass
class GeoPointException(ApplicationException):
    latitude: float | None
    longitude: float | None

    @property
    def message(self):
        return f'Невалидные геоданные "{self.latitude}, {self.longitude}"'
