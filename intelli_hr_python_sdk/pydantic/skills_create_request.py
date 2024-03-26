# coding: utf-8

"""
    intelliHR Public API

    You can find developer's guide and more documentation on [https://developers.intellihr.io](https://developers.intellihr.io)

    The version of the OpenAPI document: V1
    Contact: support@intellihr.co
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel, ConfigDict


class SkillsCreateRequest(BaseModel):
    # A description of the [Skill](https://developers.intellihr.io/docs/v1/).
    description: str = Field(alias='description')

    # User friendly name given to this [Skill](https://developers.intellihr.io/docs/v1/).
    name: str = Field(alias='name')

    # Whether this [Skill](https://developers.intellihr.io/docs/v1/) is business critical.
    is_business_critical: bool = Field(alias='isBusinessCritical')

    # The identifier string for the [Skill Discipline](https://developers.intellihr.io/docs/v1/) to which this [Skill](https://developers.intellihr.io/docs/v1/) belongs.
    skill_discipline_id: str = Field(alias='skillDisciplineId')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
