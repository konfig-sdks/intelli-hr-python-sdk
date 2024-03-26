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

from intelli_hr_python_sdk.type.workflows_patch_response_data_form_instance_schedule import WorkflowsPatchResponseDataFormInstanceSchedule
from intelli_hr_python_sdk.type.workflows_patch_response_data_workflow import WorkflowsPatchResponseDataWorkflow

class RequiredWorkflowsPatchResponseData(TypedDict):
    pass

class OptionalWorkflowsPatchResponseData(TypedDict, total=False):
    workflow: WorkflowsPatchResponseDataWorkflow

    formInstanceSchedule: WorkflowsPatchResponseDataFormInstanceSchedule

class WorkflowsPatchResponseData(RequiredWorkflowsPatchResponseData, OptionalWorkflowsPatchResponseData):
    pass
