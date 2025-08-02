import pytest
from app.domain.entities.activities import Activity
from app.domain.exceptions.activities import ActivityTitleTooLongException
from app.domain.values.activities import ActivityTitle


def test_create_activity_title_success():
    assert ActivityTitle(value="Food")


def test_create_activity_success():
    activity_title = ActivityTitle(value="Food")
    activity = Activity(title=activity_title)

    assert activity.title == activity_title


def test_create_activity_title_too_long():
    with pytest.raises(ActivityTitleTooLongException):
        ActivityTitle(value="title" * 200)
