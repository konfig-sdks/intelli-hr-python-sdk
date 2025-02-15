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

from intelli_hr_python_sdk.type.jobs_data import JobsData
from intelli_hr_python_sdk.type.jobs_meta import JobsMeta

class RequiredJobs(TypedDict):
    pass

class OptionalJobs(TypedDict, total=False):
    meta: JobsMeta

    data: JobsData

class Jobs(RequiredJobs, OptionalJobs):
    pass
