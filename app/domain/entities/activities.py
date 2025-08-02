from dataclasses import dataclass

from app.domain.entities.base import BaseEntity
from app.domain.values.activities import ActivityTitle


@dataclass
class Activity(BaseEntity):
    title: ActivityTitle
