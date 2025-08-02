import pytest

from app.domain.entities.activities import Activity
from app.domain.entities.buildings import Building
from app.domain.entities.organizations import Organization
from app.domain.exceptions.organizations import (
    InvalidPhoneNumberException,
    OrganizationTitleTooLongException,
)
from app.domain.values.activities import ActivityTitle
from app.domain.values.buildings import Address, GeoPoint
from app.domain.values.organizations import OrganizationTitle, PhoneNumber


def test_create_organization_title_success():
    assert OrganizationTitle(value="title")


def test_create_organization_title_too_long():
    with pytest.raises(OrganizationTitleTooLongException):
        OrganizationTitle(value="title" * 200)


def test_create_phone_number_success():
    assert PhoneNumber(value="+79528122211")


@pytest.mark.parametrize(
    "value", ["+7", "8 904", "", "dfsdgdgsdfg", ".g.h.;'g'f]&#&$#$*@*#"]
)
def test_create_invalid_phone_number(value):
    with pytest.raises(InvalidPhoneNumberException):
        PhoneNumber(value=value)


def test_create_organization_success():
    title = OrganizationTitle(value="title")
    phone = PhoneNumber(value="+7 904 765 11 11")

    address = Address(value="address")
    location = GeoPoint(value=(1.254, 8.340))
    building = Building(address=address, location=location)

    activity_title = ActivityTitle(value="Food")
    activity = Activity(title=activity_title)

    org = Organization(
        title=title, phone_numbers=[phone], building=building, activity=activity
    )

    assert org.title == title
    assert org.phone_numbers == [phone]
    assert org.building == building
    assert org.activity == activity
