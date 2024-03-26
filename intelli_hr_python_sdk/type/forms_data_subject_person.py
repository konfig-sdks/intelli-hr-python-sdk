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


class RequiredFormsDataSubjectPerson(TypedDict):
    pass

class OptionalFormsDataSubjectPerson(TypedDict, total=False):
    # The identifier string for the [Person](https://developers.intellihr.io/docs/v1/).
    id: str

    # Name to display throughout the system for this [Person](https://developers.intellihr.io/docs/v1/). Generally follows the pattern preferredName (firstName) lastName, but can be configured on a tenant-wide basis to be a different format.
    displayName: str

    # A manually entered employee number that identifies a [Person](https://developers.intellihr.io/docs/v1/) in intelliHR. It may be hidden in the system's UI depending upon your tenant's configuration.
    employeeNumber: typing.Union[str, none_type]

    # An autogenerated number that uniquely identifies a [Person](https://developers.intellihr.io/docs/v1/) in intelliHR. It may be hidden in the system's UI depending upon your tenant's configuration.
    autoIncrementIntellihrId: typing.Union[int, float]

    # Link on the public api to get more information on this piece of data.
    link: str

class FormsDataSubjectPerson(RequiredFormsDataSubjectPerson, OptionalFormsDataSubjectPerson):
    pass
