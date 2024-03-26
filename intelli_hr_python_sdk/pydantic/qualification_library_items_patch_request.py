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


class QualificationLibraryItemsPatchRequest(BaseModel):
    # The name of this [Qualification Library Item](https://developers.intellihr.io/docs/v1/)
    name: typing.Optional[str] = Field(None, alias='name')

    # The identifier string for the Qualification Type Id.
    qualification_type_id: typing.Optional[str] = Field(None, alias='qualificationTypeId')

    # The expiry type for this library item
    qualification_expiry_type: typing.Optional[Literal["EXPIRY_INAPPLICABLE", "EXPIRY_OPTIONAL", "EXPIRY_REQUIRED"]] = Field(None, alias='qualificationExpiryType')

    # The expiry type for this library item
    qualification_registration_number_visibility_type: typing.Optional[Literal["REGISTRATION_NUMBER_INAPPLICABLE", "REGISTRATION_NUMBER_OPTIONAL", "REGISTRATION_NUMBER_REQUIRED"]] = Field(None, alias='qualificationRegistrationNumberVisibilityType')

    # If documents are required for this library item
    qualification_attachment_requirement_type: typing.Optional[Literal["DOCUMENTS_OPTIONAL", "DOCUMENTS_REQUIRED"]] = Field(None, alias='qualificationAttachmentRequirementType')

    # Period in days, that there is a warning before the expiry of the qualification. If qualificationExpiryType is set to EXPIRY_INAPPLICABLE, this value will be ignored.
    expiry_warning_period: typing.Optional[typing.Union[int, float]] = Field(None, alias='expiryWarningPeriod')

    # If this [Qualification Library Item](https://developers.intellihr.io/docs/v1/) will send expiry warning/s using the periods defined. If qualificationExpiryType is set to EXPIRY_INAPPLICABLE, this value will be ignored.
    send_expiry_warning: typing.Optional[bool] = Field(None, alias='sendExpiryWarning')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
