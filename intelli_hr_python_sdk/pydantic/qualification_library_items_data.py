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

from intelli_hr_python_sdk.pydantic.qualification_library_items_data_qualification_type import QualificationLibraryItemsDataQualificationType

class QualificationLibraryItemsData(BaseModel):
    # The identifier string for the [Qualification Library Item](https://developers.intellihr.io/docs/v1/).
    id: typing.Optional[str] = Field(None, alias='id')

    # The name of this [Qualification Library Item](https://developers.intellihr.io/docs/v1/)
    name: typing.Optional[str] = Field(None, alias='name')

    qualification_type: typing.Optional[QualificationLibraryItemsDataQualificationType] = Field(None, alias='qualificationType')

    # The expiry type for this library item
    qualification_expiry_type: typing.Optional[Literal["EXPIRY_INAPPLICABLE", "EXPIRY_OPTIONAL", "EXPIRY_REQUIRED"]] = Field(None, alias='qualificationExpiryType')

    # The expiry type for this library item
    qualification_registration_number_visibility_type: typing.Optional[Literal["REGISTRATION_NUMBER_INAPPLICABLE", "REGISTRATION_NUMBER_OPTIONAL", "REGISTRATION_NUMBER_REQUIRED"]] = Field(None, alias='qualificationRegistrationNumberVisibilityType')

    # If documents are required for this library item
    qualification_attachment_requirement_type: typing.Optional[Literal["DOCUMENTS_OPTIONAL", "DOCUMENTS_REQUIRED"]] = Field(None, alias='qualificationAttachmentRequirementType')

    # Period in days, that there is a warning before the expiry of the qualification. If qualificationExpiryType is set to EXPIRY_INAPPLICABLE, this value will be ignored.
    expiry_warning_period: typing.Optional[typing.Union[int, float]] = Field(None, alias='expiryWarningPeriod')

    # WARNING: This property is deprecated
    # The expiry periods set for this [Qualification Library Item](https://developers.intellihr.io/docs/v1/)
    expiry_periods: typing.Optional[typing.Union[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]], none_type]] = Field(None, alias='expiryPeriods')

    # If this [Qualification Library Item](https://developers.intellihr.io/docs/v1/) will send expiry warning/s using the periods defined. If qualificationExpiryType is set to EXPIRY_INAPPLICABLE, this value will be ignored.
    send_expiry_warning: typing.Optional[bool] = Field(None, alias='sendExpiryWarning')

    # Number of qualification instances currently being used with this qualification library item
    qualification_instance_usage_count: typing.Optional[typing.Union[int, float]] = Field(None, alias='qualificationInstanceUsageCount')

    # Number of job requirement groups currently being used with this qualification library item
    job_requirement_group_usage_count: typing.Optional[typing.Union[int, float]] = Field(None, alias='jobRequirementGroupUsageCount')

    # Number of job requirements currently being used with this qualification library item
    job_requirement_usage_count: typing.Optional[typing.Union[int, float]] = Field(None, alias='jobRequirementUsageCount')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
