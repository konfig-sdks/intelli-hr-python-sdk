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


class QualificationInstancesCreateRequest(BaseModel):
    # The identifier string for the Person Id.
    person_id: str = Field(alias='personId')

    # The identifier string for the Qualification Library Item Id.
    qualification_library_item_id: str = Field(alias='qualificationLibraryItemId')

    # The status of this [Qualification Instance](https://developers.intellihr.io/docs/v1/)
    status: Literal["DRAFT", "AWAITING_APPROVAL", "DECLINED", "APPROVED", "REVOKED", "EXPIRED", "EXPIRING_SOON", "CURRENT", "FUTURE", "RENEWING", "NON_COMPLIANT"] = Field(alias='status')

    # The organisation that issued this qualification [Qualification Instance](https://developers.intellihr.io/docs/v1/)
    issuing_organisation: typing.Optional[typing.Union[str, none_type]] = Field(None, alias='issuingOrganisation')

    # The registration number of the [Qualification Instance](https://developers.intellihr.io/docs/v1/)
    registration_number: typing.Optional[typing.Union[str, none_type]] = Field(None, alias='registrationNumber')

    # The issue date of the [Qualification Instance](https://developers.intellihr.io/docs/v1/). This date will follow the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6).
    issue_date: typing.Optional[typing.Union[str, none_type]] = Field(None, alias='issueDate')

    # The expiry date of this Qualification. This date will follow the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6).
    expiry_date: typing.Optional[typing.Union[str, none_type]] = Field(None, alias='expiryDate')

    # The due date for the recipient to complete this [Qualification Instance](https://developers.intellihr.io/docs/v1/). This date will follow the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6).
    expiry_notification_queued_at: typing.Optional[typing.Union[str, none_type]] = Field(None, alias='expiryNotificationQueuedAt')

    # The notes stored on the [Qualification Instance](https://developers.intellihr.io/docs/v1/)
    notes: typing.Optional[typing.Union[str, none_type]] = Field(None, alias='notes')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
