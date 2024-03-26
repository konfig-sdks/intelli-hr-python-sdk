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

from intelli_hr_python_sdk.type.job_requirement_groups_patch_request_library_item_ids import JobRequirementGroupsPatchRequestLibraryItemIds

class RequiredJobRequirementGroupsPatchRequest(TypedDict):
    # The issue date of the [Job Requirement Group](https://developers.intellihr.io/docs/v1/)
    name: str

    libraryItemIds: JobRequirementGroupsPatchRequestLibraryItemIds

class OptionalJobRequirementGroupsPatchRequest(TypedDict, total=False):
    pass

class JobRequirementGroupsPatchRequest(RequiredJobRequirementGroupsPatchRequest, OptionalJobRequirementGroupsPatchRequest):
    pass
