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
from intelli_hr_python_sdk.type.job_patch_response_data_remuneration_schedule_additions import JobPatchResponseDataRemunerationScheduleAdditions
from intelli_hr_python_sdk.type.job_patch_response_data_remuneration_schedule_additions_to_total import JobPatchResponseDataRemunerationScheduleAdditionsToTotal
from intelli_hr_python_sdk.type.job_patch_response_data_remuneration_schedule_breakdowns import JobPatchResponseDataRemunerationScheduleBreakdowns
from intelli_hr_python_sdk.type.job_patch_response_data_remuneration_schedule_deductions import JobPatchResponseDataRemunerationScheduleDeductions
from intelli_hr_python_sdk.type.job_patch_response_data_remuneration_schedule_employment_condition import JobPatchResponseDataRemunerationScheduleEmploymentCondition

class RequiredJobPatchResponseDataRemunerationSchedule(TypedDict):
    pass

class OptionalJobPatchResponseDataRemunerationSchedule(TypedDict, total=False):
    # The method in which this remuneration schedule is paid, if a person is unpaid then this will be `No Remuneration Schedule`. Enum: `Annual Salary`, `Hourly Rate`, `No Remuneration Schedule`.
    type: str

    # The Base Salary paid yearly, this is an approximation if they are paid hourly. Note that if both baseAnnualSalary and baseHourlyRate are provided in a create or patch request, the baseHourlyRate will be ignored.
    baseAnnualSalary: typing.Union[int, float]

    # The Base Rate paid hourly, this is an approximation if they are paid annually. Note that if both baseAnnualSalary and baseHourlyRate are provided in a create or patch request, the baseHourlyRate will be ignored.
    baseHourlyRate: typing.Union[int, float]

    # The currency that the base and total amounts that this job is being paid in. An international currency code. Typically AUD for Australian dollar, USD for American dollar etc. See [Official list of codes](https://www.iban.com/currency-codes).
    currency: str

    # How many hours worked per payCycle.    0 (zero) signifies that the hours are variable per pay cycle
    hoursPerCycle: typing.Union[int, float]

    # The cycle that the job is paid on. Enum: `Weekly`, `Fortnightly`, `Monthly`, `Bi-Monthly`.
    payCycle: str

    # The total package paid yearly including additions and deductions. This amount is calculated by adding the Base Annual Salary and additions minus the deductions.
    annualPackage: typing.Union[int, float]

    # The total package paid hourly including additions and deductions. This amount is calculated by dividing the Annual Package by the total number of hours per annum.
    hourlyPackage: typing.Union[int, float]

    # If any conversion had to be performed between addition and deduction currencies when calculating the annual package.
    currencyConversionOccurred: bool

    # WARNING: This property is deprecated
    employmentCondition: JobPatchResponseDataRemunerationScheduleEmploymentCondition

    additions: JobPatchResponseDataRemunerationScheduleAdditions

    # WARNING: This property is deprecated
    deductions: JobPatchResponseDataRemunerationScheduleDeductions

    additionsToTotal: JobPatchResponseDataRemunerationScheduleAdditionsToTotal

    breakdowns: JobPatchResponseDataRemunerationScheduleBreakdowns

    # The custom field values for this Remuneration Schedule
    customFields: CustomFieldsResponse

class JobPatchResponseDataRemunerationSchedule(RequiredJobPatchResponseDataRemunerationSchedule, OptionalJobPatchResponseDataRemunerationSchedule):
    pass
