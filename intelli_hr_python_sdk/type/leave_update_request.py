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

from intelli_hr_python_sdk.type.leave_update_request_leave_type import LeaveUpdateRequestLeaveType

class RequiredLeaveUpdateRequest(TypedDict):
    # The identifier string for the [Job](https://developers.intellihr.io/docs/v1/) that this extended leave belongs to.
    jobId: str

    # The date this [Extended Leave](https://developers.intellihr.io/docs/v1/) is expected to end. Leave is created without a finalised return date. In order to create more than one Extended Leave on a Job, the end date must be finalised on the most recent created Extended Leave. This date will follow the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6).   YYYY-MM-DD date formatting is also supported, although by using this format the date will be stored as the start of day in UTC time, not the requesting tenants timezone.
    endDate: str

class OptionalLeaveUpdateRequest(TypedDict, total=False):
    # Whether or not to finalise the end date for the [Extended Leave](https://developers.intellihr.io/docs/v1/). This boolean will change the input variables required if you are finalising an Extended Leave or just updating it. Finalising the end date prevents any further changes to this Extended Leave.
    shouldNotFinaliseEndDate: bool

    # The date this [Extended Leave](https://developers.intellihr.io/docs/v1/) started or will start. This field is only required if not finalising the Extended Leave end date, and will not be used if shouldNotFinaliseEndDate is not set or is set to false. This date will follow the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6).   YYYY-MM-DD date formatting is also supported, although by using this format the date will be stored as the start of day in UTC time, not the requesting tenants timezone.
    startDate: str

    leaveType: LeaveUpdateRequestLeaveType

    # The full time equivalent for this [Job](https://developers.intellihr.io/docs/v1/) upon returning from Extended Leave. This field is only required when finalising the Extended Leave end date, and will not be used if shouldNotFinaliseEndDate is set to true.
    fte: str

class LeaveUpdateRequest(RequiredLeaveUpdateRequest, OptionalLeaveUpdateRequest):
    pass
