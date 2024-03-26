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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from intelli_hr_python_sdk.pydantic.job_end_patch_response_data import JobEndPatchResponseData
from intelli_hr_python_sdk.pydantic.job_end_patch_response_meta import JobEndPatchResponseMeta

class JobEndPatchResponse(BaseModel):
    meta: typing.Optional[JobEndPatchResponseMeta] = Field(None, alias='meta')

    data: typing.Optional[JobEndPatchResponseData] = Field(None, alias='data')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
