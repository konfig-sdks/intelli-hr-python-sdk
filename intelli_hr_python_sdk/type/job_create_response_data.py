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

from intelli_hr_python_sdk.type.custom_fields_response import CustomFieldsResponse
from intelli_hr_python_sdk.type.job_create_response_data_business_entity import JobCreateResponseDataBusinessEntity
from intelli_hr_python_sdk.type.job_create_response_data_business_unit import JobCreateResponseDataBusinessUnit
from intelli_hr_python_sdk.type.job_create_response_data_comments import JobCreateResponseDataComments
from intelli_hr_python_sdk.type.job_create_response_data_establishment import JobCreateResponseDataEstablishment
from intelli_hr_python_sdk.type.job_create_response_data_location import JobCreateResponseDataLocation
from intelli_hr_python_sdk.type.job_create_response_data_pay_grade import JobCreateResponseDataPayGrade
from intelli_hr_python_sdk.type.job_create_response_data_person import JobCreateResponseDataPerson
from intelli_hr_python_sdk.type.job_create_response_data_position_title import JobCreateResponseDataPositionTitle
from intelli_hr_python_sdk.type.job_create_response_data_recruitment import JobCreateResponseDataRecruitment
from intelli_hr_python_sdk.type.job_create_response_data_remuneration_schedule import JobCreateResponseDataRemunerationSchedule

class RequiredJobCreateResponseData(TypedDict):
    pass

class OptionalJobCreateResponseData(TypedDict, total=False):
    # The identifier string for the [Job](https://developers.intellihr.io/docs/v1/).
    id: str

    person: JobCreateResponseDataPerson

    recruitment: JobCreateResponseDataRecruitment

    # If this job has active extended leave, this will be populated, otherwise it will be null
    extendedLeave: typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]], none_type]

    location: JobCreateResponseDataLocation

    payGrade: JobCreateResponseDataPayGrade

    businessUnit: JobCreateResponseDataBusinessUnit

    businessEntity: JobCreateResponseDataBusinessEntity

    establishment: JobCreateResponseDataEstablishment

    # The [Job](https://developers.intellihr.io/docs/v1/) information for the supervisor of this [Job](https://developers.intellihr.io/docs/v1/) or null if they have no supervisor.
    supervisorJob: typing.Union[none_type, typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]

    # The [Person](https://developers.intellihr.io/docs/v1/) information for the supervisor of this job or null if they have no supervisor.
    supervisorPerson: typing.Union[none_type, typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]

    # An instance of the [Employment Condition](https://developers.intellihr.io/docs/v1/) that is attached to the job, contains the dates it is effective for.
    employmentCondition: typing.Union[none_type, typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]

    remunerationSchedule: JobCreateResponseDataRemunerationSchedule

    # The name of this [Job](https://developers.intellihr.io/docs/v1/).
    name: str

    positionTitle: JobCreateResponseDataPositionTitle

    # The full time equivalent of this [Job](https://developers.intellihr.io/docs/v1/). Indicating the workload of an employee that can be comparable across different contexts. This is null for people without an FTE.
    fte: typing.Union[none_type, typing.Union[int, float]]

    comments: JobCreateResponseDataComments

    # The latest comment that annotates the reason for a [Job's](https://developers.intellihr.io/docs/v1/) change. It will return the latest comment based on the asAt value or null if none exist.
    lastestJobChangeComment: typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]], none_type]

    # The [Work Class](https://developers.intellihr.io/docs/v1/) of this [Job](https://developers.intellihr.io/docs/v1/). This is extra details about the [Work Type](https://developers.intellihr.io/docs/v1/).
    workClass: str

    # This is the [Work Classification](https://developers.intellihr.io/docs/v1/) for this [Job](https://developers.intellihr.io/docs/v1/), it is used to differentiate between full-time and part time employees vs unpaid volunteers. Enum: `Permanent`, `Fixed Contract`, `Unpaid`, `Temporary/Casual`, `Independent Contract`.
    workType: str

    # Whether this job is the primary job on the [Person](https://developers.intellihr.io/docs/v1/). Only one job on a [Person](https://developers.intellihr.io/docs/v1/) can be primary at a time.
    isPrimaryJob: bool

    # The current status of this job within this organisation. Enum: `Past Job`, `Future Job`, `Ending Job`, `Current Job`.
    jobStatus: str

    # The [User](https://developers.intellihr.io/docs/v1/) who created this job. May be null for old [Jobs](https://developers.intellihr.io/docs/v1/). This field will remain null for API created jobs.
    createdBy: typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]], none_type]

    # The last [User](https://developers.intellihr.io/docs/v1/) who updated this job. May be null for old [Jobs](https://developers.intellihr.io/docs/v1/). This field will remain null if the last update was performed by the API.
    updatedBy: typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]], none_type]

    # The start date of the current position the person is in. The gap between the `companyStartDate` and `positionStartDate` will be filled with \"Previous position title\" historical records, to correctly depict the person as having no information recorded for old job positions. This date will follow the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6).   YYYY-MM-DD date formatting is also supported, although by using this format the date will be stored as the start of day in UTC time, not the requesting tenants timezone.
    positionStartDate: str

    # The date this [Job](https://developers.intellihr.io/docs/v1/) started or will start within the organisation. This date will follow the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6).
    companyStartDate: str

    # The <b>exclusive</b> date this [Job](https://developers.intellihr.io/docs/v1/) ended or will end within the organisation. For example, if the person's last working date is on 2025-04-23, the `companyEndDate` should be set as 2025-04-24 to reflect the exclusive date. This date will follow the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6).
    companyEndDate: typing.Union[str, none_type]

    # Whether the end date has been finalised within the intelliHR application.
    isEndDateConfirmed: bool

    # The type of turnover this end of job is classified as.
    turnoverType: typing.Union[str, none_type]

    # The name of the turnover reason.
    turnoverReason: typing.Union[str, none_type]

    # The custom field values for this Job
    customFields: CustomFieldsResponse

    # When this record was created. This date will follow the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6).
    createdAt: str

class JobCreateResponseData(RequiredJobCreateResponseData, OptionalJobCreateResponseData):
    pass
