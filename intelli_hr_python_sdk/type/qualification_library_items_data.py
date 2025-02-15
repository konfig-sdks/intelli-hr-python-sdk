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

from intelli_hr_python_sdk.type.qualification_library_items_data_qualification_type import QualificationLibraryItemsDataQualificationType

class RequiredQualificationLibraryItemsData(TypedDict):
    pass

class OptionalQualificationLibraryItemsData(TypedDict, total=False):
    # The identifier string for the [Qualification Library Item](https://developers.intellihr.io/docs/v1/).
    id: str

    # The name of this [Qualification Library Item](https://developers.intellihr.io/docs/v1/)
    name: str

    qualificationType: QualificationLibraryItemsDataQualificationType

    # The expiry type for this library item
    qualificationExpiryType: str

    # The expiry type for this library item
    qualificationRegistrationNumberVisibilityType: str

    # If documents are required for this library item
    qualificationAttachmentRequirementType: str

    # Period in days, that there is a warning before the expiry of the qualification. If qualificationExpiryType is set to EXPIRY_INAPPLICABLE, this value will be ignored.
    expiryWarningPeriod: typing.Union[int, float]

    # WARNING: This property is deprecated
    # The expiry periods set for this [Qualification Library Item](https://developers.intellihr.io/docs/v1/)
    expiryPeriods: typing.Union[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]], none_type]

    # If this [Qualification Library Item](https://developers.intellihr.io/docs/v1/) will send expiry warning/s using the periods defined. If qualificationExpiryType is set to EXPIRY_INAPPLICABLE, this value will be ignored.
    sendExpiryWarning: bool

    # Number of qualification instances currently being used with this qualification library item
    qualificationInstanceUsageCount: typing.Union[int, float]

    # Number of job requirement groups currently being used with this qualification library item
    jobRequirementGroupUsageCount: typing.Union[int, float]

    # Number of job requirements currently being used with this qualification library item
    jobRequirementUsageCount: typing.Union[int, float]

class QualificationLibraryItemsData(RequiredQualificationLibraryItemsData, OptionalQualificationLibraryItemsData):
    pass
