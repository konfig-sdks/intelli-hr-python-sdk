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

from intelli_hr_python_sdk.type.jobs_list_data import JobsListData
from intelli_hr_python_sdk.type.jobs_list_links import JobsListLinks
from intelli_hr_python_sdk.type.jobs_list_meta import JobsListMeta

class RequiredJobsList(TypedDict):
    pass

class OptionalJobsList(TypedDict, total=False):
    data: JobsListData

    meta: JobsListMeta

    links: JobsListLinks

class JobsList(RequiredJobsList, OptionalJobsList):
    pass
