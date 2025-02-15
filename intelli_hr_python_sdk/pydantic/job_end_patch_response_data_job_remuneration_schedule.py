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
from intelli_hr_python_sdk.pydantic.job_end_patch_response_data_job_remuneration_schedule_additions import JobEndPatchResponseDataJobRemunerationScheduleAdditions
from intelli_hr_python_sdk.pydantic.job_end_patch_response_data_job_remuneration_schedule_additions_to_total import JobEndPatchResponseDataJobRemunerationScheduleAdditionsToTotal
from intelli_hr_python_sdk.pydantic.job_end_patch_response_data_job_remuneration_schedule_breakdowns import JobEndPatchResponseDataJobRemunerationScheduleBreakdowns
from intelli_hr_python_sdk.pydantic.job_end_patch_response_data_job_remuneration_schedule_deductions import JobEndPatchResponseDataJobRemunerationScheduleDeductions
from intelli_hr_python_sdk.pydantic.job_end_patch_response_data_job_remuneration_schedule_employment_condition import JobEndPatchResponseDataJobRemunerationScheduleEmploymentCondition

class JobEndPatchResponseDataJobRemunerationSchedule(BaseModel):
    # The method in which this remuneration schedule is paid, if a person is unpaid then this will be `No Remuneration Schedule`. Enum: `Annual Salary`, `Hourly Rate`, `No Remuneration Schedule`.
    type: typing.Optional[str] = Field(None, alias='type')

    # The Base Salary paid yearly, this is an approximation if they are paid hourly. Note that if both baseAnnualSalary and baseHourlyRate are provided in a create or patch request, the baseHourlyRate will be ignored.
    base_annual_salary: typing.Optional[typing.Union[int, float]] = Field(None, alias='baseAnnualSalary')

    # The Base Rate paid hourly, this is an approximation if they are paid annually. Note that if both baseAnnualSalary and baseHourlyRate are provided in a create or patch request, the baseHourlyRate will be ignored.
    base_hourly_rate: typing.Optional[typing.Union[int, float]] = Field(None, alias='baseHourlyRate')

    # The currency that the base and total amounts that this job is being paid in. An international currency code. Typically AUD for Australian dollar, USD for American dollar etc. See [Official list of codes](https://www.iban.com/currency-codes).
    currency: typing.Optional[str] = Field(None, alias='currency')

    # How many hours worked per payCycle.    0 (zero) signifies that the hours are variable per pay cycle
    hours_per_cycle: typing.Optional[typing.Union[int, float]] = Field(None, alias='hoursPerCycle')

    # The cycle that the job is paid on. Enum: `Weekly`, `Fortnightly`, `Monthly`, `Bi-Monthly`.
    pay_cycle: typing.Optional[str] = Field(None, alias='payCycle')

    # The total package paid yearly including additions and deductions. This amount is calculated by adding the Base Annual Salary and additions minus the deductions.
    annual_package: typing.Optional[typing.Union[int, float]] = Field(None, alias='annualPackage')

    # The total package paid hourly including additions and deductions. This amount is calculated by dividing the Annual Package by the total number of hours per annum.
    hourly_package: typing.Optional[typing.Union[int, float]] = Field(None, alias='hourlyPackage')

    # If any conversion had to be performed between addition and deduction currencies when calculating the annual package.
    currency_conversion_occurred: typing.Optional[bool] = Field(None, alias='currencyConversionOccurred')

    # WARNING: This property is deprecated
    employment_condition: typing.Optional[JobEndPatchResponseDataJobRemunerationScheduleEmploymentCondition] = Field(None, alias='employmentCondition')

    additions: typing.Optional[JobEndPatchResponseDataJobRemunerationScheduleAdditions] = Field(None, alias='additions')

    # WARNING: This property is deprecated
    deductions: typing.Optional[JobEndPatchResponseDataJobRemunerationScheduleDeductions] = Field(None, alias='deductions')

    additions_to_total: typing.Optional[JobEndPatchResponseDataJobRemunerationScheduleAdditionsToTotal] = Field(None, alias='additionsToTotal')

    breakdowns: typing.Optional[JobEndPatchResponseDataJobRemunerationScheduleBreakdowns] = Field(None, alias='breakdowns')

    # The custom field values for this Remuneration Schedule
    custom_fields: typing.Optional[CustomFieldsResponse] = Field(None, alias='customFields')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
