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

from intelli_hr_python_sdk.type.employment_conditions_list_meta_pagination import EmploymentConditionsListMetaPagination

class RequiredEmploymentConditionsListMeta(TypedDict):
    pass

class OptionalEmploymentConditionsListMeta(TypedDict, total=False):
    pagination: EmploymentConditionsListMetaPagination

    # The identifier string for the api request.
    requestId: str

class EmploymentConditionsListMeta(RequiredEmploymentConditionsListMeta, OptionalEmploymentConditionsListMeta):
    pass
