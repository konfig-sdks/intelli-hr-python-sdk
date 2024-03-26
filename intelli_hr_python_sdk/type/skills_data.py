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

from intelli_hr_python_sdk.type.skills_data_skill_discipline import SkillsDataSkillDiscipline

class RequiredSkillsData(TypedDict):
    pass

class OptionalSkillsData(TypedDict, total=False):
    # A description of the [Skill](https://developers.intellihr.io/docs/v1/).
    description: str

    # The identifier string for the [Skill](https://developers.intellihr.io/docs/v1/).
    id: str

    # User friendly name given to this [Skill](https://developers.intellihr.io/docs/v1/).
    name: str

    # Whether this [Skill](https://developers.intellihr.io/docs/v1/) is business critical.
    isBusinessCritical: bool

    skillDiscipline: SkillsDataSkillDiscipline

class SkillsData(RequiredSkillsData, OptionalSkillsData):
    pass
