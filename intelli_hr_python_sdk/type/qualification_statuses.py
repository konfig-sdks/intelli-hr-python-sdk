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

from intelli_hr_python_sdk.type.qualification_statuses_data import QualificationStatusesData
from intelli_hr_python_sdk.type.qualification_statuses_meta import QualificationStatusesMeta

class RequiredQualificationStatuses(TypedDict):
    pass

class OptionalQualificationStatuses(TypedDict, total=False):
    data: QualificationStatusesData

    meta: QualificationStatusesMeta

class QualificationStatuses(RequiredQualificationStatuses, OptionalQualificationStatuses):
    pass
