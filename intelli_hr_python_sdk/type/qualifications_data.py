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

from intelli_hr_python_sdk.type.qualifications_data_library_item import QualificationsDataLibraryItem
from intelli_hr_python_sdk.type.qualifications_data_person import QualificationsDataPerson
from intelli_hr_python_sdk.type.qualifications_data_qualification_status import QualificationsDataQualificationStatus

class RequiredQualificationsData(TypedDict):
    pass

class OptionalQualificationsData(TypedDict, total=False):
    # The identifier string for the [Qualification Instance](https://developers.intellihr.io/docs/v1/).
    id: str

    # The expiry date of this Qualification. This date will follow the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6).
    expiryDate: typing.Union[str, none_type]

    # The due date for the recipient to complete this [Qualification Instance](https://developers.intellihr.io/docs/v1/). This date will follow the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6).
    expiryNotificationQueuedAt: typing.Union[str, none_type]

    # The issue date of the [Qualification Instance](https://developers.intellihr.io/docs/v1/). This date will follow the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6).
    issueDate: typing.Union[str, none_type]

    # The organisation that issued this qualification [Qualification Instance](https://developers.intellihr.io/docs/v1/)
    issuingOrganisation: typing.Union[str, none_type]

    # The notes stored on the [Qualification Instance](https://developers.intellihr.io/docs/v1/)
    notes: typing.Union[str, none_type]

    person: QualificationsDataPerson

    # WARNING: This property is deprecated
    qualificationStatus: QualificationsDataQualificationStatus

    # The status of this [Qualification Instance](https://developers.intellihr.io/docs/v1/)
    status: str

    libraryItem: QualificationsDataLibraryItem

    # The registration number of the [Qualification Instance](https://developers.intellihr.io/docs/v1/)
    registrationNumber: typing.Union[str, none_type]

class QualificationsData(RequiredQualificationsData, OptionalQualificationsData):
    pass
