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

from intelli_hr_python_sdk.pydantic.custom_fields_response import CustomFieldsResponse
from intelli_hr_python_sdk.pydantic.jobs_data_business_entity import JobsDataBusinessEntity
from intelli_hr_python_sdk.pydantic.jobs_data_business_unit import JobsDataBusinessUnit
from intelli_hr_python_sdk.pydantic.jobs_data_comments import JobsDataComments
from intelli_hr_python_sdk.pydantic.jobs_data_establishment import JobsDataEstablishment
from intelli_hr_python_sdk.pydantic.jobs_data_location import JobsDataLocation
from intelli_hr_python_sdk.pydantic.jobs_data_pay_grade import JobsDataPayGrade
from intelli_hr_python_sdk.pydantic.jobs_data_person import JobsDataPerson
from intelli_hr_python_sdk.pydantic.jobs_data_position_title import JobsDataPositionTitle
from intelli_hr_python_sdk.pydantic.jobs_data_recruitment import JobsDataRecruitment
from intelli_hr_python_sdk.pydantic.jobs_data_remuneration_schedule import JobsDataRemunerationSchedule

class JobsData(BaseModel):
    # The identifier string for the [Job](https://developers.intellihr.io/docs/v1/).
    id: typing.Optional[str] = Field(None, alias='id')

    person: typing.Optional[JobsDataPerson] = Field(None, alias='person')

    recruitment: typing.Optional[JobsDataRecruitment] = Field(None, alias='recruitment')

    # If this job has active extended leave, this will be populated, otherwise it will be null
    extended_leave: typing.Optional[typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]], none_type]] = Field(None, alias='extendedLeave')

    location: typing.Optional[JobsDataLocation] = Field(None, alias='location')

    pay_grade: typing.Optional[JobsDataPayGrade] = Field(None, alias='payGrade')

    business_unit: typing.Optional[JobsDataBusinessUnit] = Field(None, alias='businessUnit')

    business_entity: typing.Optional[JobsDataBusinessEntity] = Field(None, alias='businessEntity')

    establishment: typing.Optional[JobsDataEstablishment] = Field(None, alias='establishment')

    # The [Job](https://developers.intellihr.io/docs/v1/) information for the supervisor of this [Job](https://developers.intellihr.io/docs/v1/) or null if they have no supervisor.
    supervisor_job: typing.Optional[typing.Union[none_type, typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = Field(None, alias='supervisorJob')

    # The [Person](https://developers.intellihr.io/docs/v1/) information for the supervisor of this job or null if they have no supervisor.
    supervisor_person: typing.Optional[typing.Union[none_type, typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = Field(None, alias='supervisorPerson')

    # An instance of the [Employment Condition](https://developers.intellihr.io/docs/v1/) that is attached to the job, contains the dates it is effective for.
    employment_condition: typing.Optional[typing.Union[none_type, typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = Field(None, alias='employmentCondition')

    remuneration_schedule: typing.Optional[JobsDataRemunerationSchedule] = Field(None, alias='remunerationSchedule')

    # The name of this [Job](https://developers.intellihr.io/docs/v1/).
    name: typing.Optional[str] = Field(None, alias='name')

    position_title: typing.Optional[JobsDataPositionTitle] = Field(None, alias='positionTitle')

    # The full time equivalent of this [Job](https://developers.intellihr.io/docs/v1/). Indicating the workload of an employee that can be comparable across different contexts. This is null for people without an FTE.
    fte: typing.Optional[typing.Union[none_type, typing.Union[int, float]]] = Field(None, alias='fte')

    comments: typing.Optional[JobsDataComments] = Field(None, alias='comments')

    # The latest comment that annotates the reason for a [Job's](https://developers.intellihr.io/docs/v1/) change. It will return the latest comment based on the asAt value or null if none exist.
    lastest_job_change_comment: typing.Optional[typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]], none_type]] = Field(None, alias='lastestJobChangeComment')

    # The [Work Class](https://developers.intellihr.io/docs/v1/) of this [Job](https://developers.intellihr.io/docs/v1/). This is extra details about the [Work Type](https://developers.intellihr.io/docs/v1/).
    work_class: typing.Optional[str] = Field(None, alias='workClass')

    # This is the [Work Classification](https://developers.intellihr.io/docs/v1/) for this [Job](https://developers.intellihr.io/docs/v1/), it is used to differentiate between full-time and part time employees vs unpaid volunteers. Enum: `Permanent`, `Fixed Contract`, `Unpaid`, `Temporary/Casual`, `Independent Contract`.
    work_type: typing.Optional[str] = Field(None, alias='workType')

    # Whether this job is the primary job on the [Person](https://developers.intellihr.io/docs/v1/). Only one job on a [Person](https://developers.intellihr.io/docs/v1/) can be primary at a time.
    is_primary_job: typing.Optional[bool] = Field(None, alias='isPrimaryJob')

    # The current status of this job within this organisation. Enum: `Past Job`, `Future Job`, `Ending Job`, `Current Job`.
    job_status: typing.Optional[str] = Field(None, alias='jobStatus')

    # The [User](https://developers.intellihr.io/docs/v1/) who created this job. May be null for old [Jobs](https://developers.intellihr.io/docs/v1/). This field will remain null for API created jobs.
    created_by: typing.Optional[typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]], none_type]] = Field(None, alias='createdBy')

    # The last [User](https://developers.intellihr.io/docs/v1/) who updated this job. May be null for old [Jobs](https://developers.intellihr.io/docs/v1/). This field will remain null if the last update was performed by the API.
    updated_by: typing.Optional[typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]], none_type]] = Field(None, alias='updatedBy')

    # The start date of the current position the person is in. The gap between the `companyStartDate` and `positionStartDate` will be filled with \"Previous position title\" historical records, to correctly depict the person as having no information recorded for old job positions. This date will follow the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6).   YYYY-MM-DD date formatting is also supported, although by using this format the date will be stored as the start of day in UTC time, not the requesting tenants timezone.
    position_start_date: typing.Optional[str] = Field(None, alias='positionStartDate')

    # The date this [Job](https://developers.intellihr.io/docs/v1/) started or will start within the organisation. This date will follow the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6).
    company_start_date: typing.Optional[str] = Field(None, alias='companyStartDate')

    # The <b>exclusive</b> date this [Job](https://developers.intellihr.io/docs/v1/) ended or will end within the organisation. For example, if the person's last working date is on 2025-04-23, the `companyEndDate` should be set as 2025-04-24 to reflect the exclusive date. This date will follow the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6).
    company_end_date: typing.Optional[typing.Union[str, none_type]] = Field(None, alias='companyEndDate')

    # Whether the end date has been finalised within the intelliHR application.
    is_end_date_confirmed: typing.Optional[bool] = Field(None, alias='isEndDateConfirmed')

    # The type of turnover this end of job is classified as.
    turnover_type: typing.Optional[typing.Union[str, none_type]] = Field(None, alias='turnoverType')

    # The name of the turnover reason.
    turnover_reason: typing.Optional[typing.Union[str, none_type]] = Field(None, alias='turnoverReason')

    # The custom field values for this Job
    custom_fields: typing.Optional[CustomFieldsResponse] = Field(None, alias='customFields')

    # When this record was created. This date will follow the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6).
    created_at: typing.Optional[str] = Field(None, alias='createdAt')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
