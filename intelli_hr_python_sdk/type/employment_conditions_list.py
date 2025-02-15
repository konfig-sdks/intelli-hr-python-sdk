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

from intelli_hr_python_sdk.type.employment_conditions_list_data import EmploymentConditionsListData
from intelli_hr_python_sdk.type.employment_conditions_list_links import EmploymentConditionsListLinks
from intelli_hr_python_sdk.type.employment_conditions_list_meta import EmploymentConditionsListMeta

class RequiredEmploymentConditionsList(TypedDict):
    pass

class OptionalEmploymentConditionsList(TypedDict, total=False):
    data: EmploymentConditionsListData

    meta: EmploymentConditionsListMeta

    links: EmploymentConditionsListLinks

class EmploymentConditionsList(RequiredEmploymentConditionsList, OptionalEmploymentConditionsList):
    pass
