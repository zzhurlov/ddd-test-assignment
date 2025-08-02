import pytest

from app.domain.entities.buildings import Building
from app.domain.exceptions.buildings import InvalidAddressException, GeoPointException
from app.domain.values.buildings import Address, GeoPoint


def test_create_address_success():
    address = Address(value="address")

    assert address


def test_create_invalid_address():
    with pytest.raises(InvalidAddressException):
        Address(value="address" * 100)


def test_create_geopoint_success():
    geopoint = GeoPoint(value=(1.254, 8.340))

    assert geopoint


def test_create_invalid_location():
    with pytest.raises(GeoPointException):
        GeoPoint(value="address" * 100)


def test_create_building_success():
    address = Address(value="address")
    location = GeoPoint(value=(1.254, 8.340))

    building = Building(address=address, location=location)

    assert building.address == address
    assert building.location == location
