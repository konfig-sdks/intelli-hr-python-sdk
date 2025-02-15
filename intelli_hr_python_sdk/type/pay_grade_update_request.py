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

from intelli_hr_python_sdk.type.pay_grade_update_request_employment_condition import PayGradeUpdateRequestEmploymentCondition
from intelli_hr_python_sdk.type.pay_grade_update_request_pay_steps import PayGradeUpdateRequestPaySteps

class RequiredPayGradeUpdateRequest(TypedDict):
    # The date this [Pay Grade](https://developers.intellihr.io/docs/v1/) Update is effective from within the organisation. Note that this doesn't affect the availableFrom date of the overall Pay Grade itself.  Not providing an effectiveFrom will apply the changes from the beggining of time.. This date will follow the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6).   YYYY-MM-DD date formatting is also supported, although by using this format the date will be stored as the start of day in UTC time, not the requesting tenants timezone.
    effectiveFrom: str

class OptionalPayGradeUpdateRequest(TypedDict, total=False):
    # Description of the [Pay Grade](https://developers.intellihr.io/docs/v1/).
    description: str

    # The date this [Pay Grade](https://developers.intellihr.io/docs/v1/) Update is effective to within the organisation.. This date will follow the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6).   YYYY-MM-DD date formatting is also supported, although by using this format the date will be stored as the start of day in UTC time, not the requesting tenants timezone.
    effectiveTo: str

    # Toggle the availability of the [Pay Grade](https://developers.intellihr.io/docs/v1/) on or off within the organisation.
    isEnabled: bool

    # The name assigned to this [Pay Grade](https://developers.intellihr.io/docs/v1/).
    name: str

    # Administrative, short code associated to the [Pay Grade](https://developers.intellihr.io/docs/v1/).
    code: str

    employmentCondition: PayGradeUpdateRequestEmploymentCondition

    # The type of this [Pay Grade](https://developers.intellihr.io/docs/v1/). Enum: `FIXED` or `STEP`.
    payGradeType: str

    # Allow this [Pay Grade](https://developers.intellihr.io/docs/v1/) value to be overwritten.
    isOverridable: bool

    # Stores the hourly rate for permanent [Jobs](https://developers.intellihr.io/docs/v1/). These inputs will be ignored if you also pass in pay Step values.
    permanentHourlyRate: typing.Union[int, float]

    # The currency that the permanentHourlyRate is being paid in. An international currency code. Typically AUD for Australian dollar, USD for American dollar etc. See [Official list of codes](https://www.iban.com/currency-codes).
    permanentHourlyRateCurrency: str

    # Stores the hourly rate for casual [Jobs](https://developers.intellihr.io/docs/v1/). These inputs will be ignored if you also pass in pay Step values.
    casualHourlyRate: typing.Union[int, float]

    # The currency that the casualHourlyRate is being paid in. An international currency code. Typically AUD for Australian dollar, USD for American dollar etc. See [Official list of codes](https://www.iban.com/currency-codes).
    casualHourlyRateCurrency: str

    # Stores the annual salary for [Jobs](https://developers.intellihr.io/docs/v1/). These inputs will be ignored if you also pass in pay Step values.
    annualSalary: typing.Union[int, float]

    # The currency that the annualSalary is being paid in. An international currency code. Typically AUD for Australian dollar, USD for American dollar etc. See [Official list of codes](https://www.iban.com/currency-codes).
    annualSalaryCurrency: str

    paySteps: PayGradeUpdateRequestPaySteps

class PayGradeUpdateRequest(RequiredPayGradeUpdateRequest, OptionalPayGradeUpdateRequest):
    pass
