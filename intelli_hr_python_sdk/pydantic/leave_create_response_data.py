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

from intelli_hr_python_sdk.pydantic.leave_create_response_data_job import LeaveCreateResponseDataJob
from intelli_hr_python_sdk.pydantic.leave_create_response_data_leave_type import LeaveCreateResponseDataLeaveType
from intelli_hr_python_sdk.pydantic.leave_create_response_data_person import LeaveCreateResponseDataPerson

class LeaveCreateResponseData(BaseModel):
    # The identifier string for the [Extended Leave](https://developers.intellihr.io/docs/v1/).
    id: typing.Optional[str] = Field(None, alias='id')

    # The date this [Extended Leave](https://developers.intellihr.io/docs/v1/) started or will start. This date will follow the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6).
    start_date: typing.Optional[str] = Field(None, alias='startDate')

    # The date this [Extended Leave](https://developers.intellihr.io/docs/v1/) started or will start. This date will follow the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6).
    end_date: typing.Optional[str] = Field(None, alias='endDate')

    # Whether the end date has been finalised for this [Extended Leave](https://developers.intellihr.io/docs/v1/).
    is_end_date_confirmed: typing.Optional[bool] = Field(None, alias='isEndDateConfirmed')

    leave_type: typing.Optional[LeaveCreateResponseDataLeaveType] = Field(None, alias='leaveType')

    job: typing.Optional[LeaveCreateResponseDataJob] = Field(None, alias='job')

    person: typing.Optional[LeaveCreateResponseDataPerson] = Field(None, alias='person')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
