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


class RequiredRecruitmentSourcesData(TypedDict):
    pass

class OptionalRecruitmentSourcesData(TypedDict, total=False):
    # The identifier string for the [Recruitment Source](https://developers.intellihr.io/docs/v1/).
    id: str

    # The name given to this recruitment source.
    name: str

    # The identifier string for the parent [Recruitment Source](https://developers.intellihr.io/docs/v1/), or null if there is no parent (this is a top level recruitment source).
    parentId: typing.Union[str, none_type]

    # Specifies whether users can select this [Recruitment Source](https://developers.intellihr.io/docs/v1/) in dropdowns.
    isEnabled: bool

class RecruitmentSourcesData(RequiredRecruitmentSourcesData, OptionalRecruitmentSourcesData):
    pass
