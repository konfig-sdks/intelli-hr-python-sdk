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

from intelli_hr_python_sdk.type.workflows_patch_response_data import WorkflowsPatchResponseData
from intelli_hr_python_sdk.type.workflows_patch_response_meta import WorkflowsPatchResponseMeta

class RequiredWorkflowsPatchResponse(TypedDict):
    pass

class OptionalWorkflowsPatchResponse(TypedDict, total=False):
    data: WorkflowsPatchResponseData

    meta: WorkflowsPatchResponseMeta

class WorkflowsPatchResponse(RequiredWorkflowsPatchResponse, OptionalWorkflowsPatchResponse):
    pass
