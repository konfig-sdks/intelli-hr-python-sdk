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

from intelli_hr_python_sdk.type.people_create_request_addresses import PeopleCreateRequestAddresses
from intelli_hr_python_sdk.type.people_create_request_custom_fields import PeopleCreateRequestCustomFields
from intelli_hr_python_sdk.type.people_create_request_email_addresses import PeopleCreateRequestEmailAddresses
from intelli_hr_python_sdk.type.people_create_request_emergency_contact import PeopleCreateRequestEmergencyContact
from intelli_hr_python_sdk.type.people_create_request_medical_conditions import PeopleCreateRequestMedicalConditions
from intelli_hr_python_sdk.type.people_create_request_phone_numbers import PeopleCreateRequestPhoneNumbers
from intelli_hr_python_sdk.type.people_create_request_work_right import PeopleCreateRequestWorkRight

class RequiredPeopleCreateRequest(TypedDict):
    # The [Person's](https://developers.intellihr.io/docs/v1/) Last Name.
    lastName: str

class OptionalPeopleCreateRequest(TypedDict, total=False):
    # The title to refer to this [Person](https://developers.intellihr.io/docs/v1/) as, for example \"Mr\". This is null if not provided and is case insensitive.
    title: typing.Union[str, none_type]

    # The [Person's](https://developers.intellihr.io/docs/v1/) First Name.
    firstName: typing.Union[str, none_type]

    # The [Person's](https://developers.intellihr.io/docs/v1/) Middle Name.
    middleName: typing.Union[str, none_type]

    # The [Person's](https://developers.intellihr.io/docs/v1/) Preferred Name. Can generally be configured by employees for themselves.
    preferredName: typing.Union[str, none_type]

    # Date of Birth (YYYY-MM-DD).
    dateOfBirth: typing.Union[str, none_type]

    # Human readable string for the [Person's](https://developers.intellihr.io/docs/v1/) gender, e.g. `Male`. Searching is done case-insensitively and 'starts-with' e.g. passing `male` will match with a [Gender](https://developers.intellihr.io/docs/v1/) called \"Male\" as will \"m\" or \"M\". If multiple [Genders](https://developers.intellihr.io/docs/v1/) match the first will be chosen. The gender options available are: `Female`, `Male`, `Non-binary`, `Other`, `Undisclosed`.
    gender: str

    # A manually entered employee number that identifies a [Person](https://developers.intellihr.io/docs/v1/) in intelliHR. It may be hidden in the system's UI depending upon your tenant's configuration.
    employeeNumber: typing.Union[str, none_type]

    emergencyContact: PeopleCreateRequestEmergencyContact

    # WARNING: This property is deprecated
    # Information about this [Person's](https://developers.intellihr.io/docs/v1/) primary email address, or null if they have no email information.  The provided email address will be converted to lowercase. The field is also required when creating a user alongside with the person.
    primaryEmailAddress: typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]], none_type]

    # WARNING: This property is deprecated
    # Information about this [Person's](https://developers.intellihr.io/docs/v1/) primary phone number, or null if they have no phone information.
    primaryPhoneNumber: typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]], none_type]

    emailAddresses: PeopleCreateRequestEmailAddresses

    phoneNumbers: PeopleCreateRequestPhoneNumbers

    addresses: PeopleCreateRequestAddresses

    customFields: PeopleCreateRequestCustomFields

    medicalConditions: PeopleCreateRequestMedicalConditions

    workRight: PeopleCreateRequestWorkRight

    # The date this [Work Right](https://developers.intellihr.io/docs/v1/) will expire for this [Person](https://developers.intellihr.io/docs/v1/) (YYYY-MM-DD).
    workRightExpiryDate: typing.Union[str, none_type]

    # Details about this [Person's](https://developers.intellihr.io/docs/v1/) linked user account. Including this object will create a user account linked to this person, allowing them to login to the platform. If excluded the person will be created without an accompanying user account.
    userAccount: typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]], none_type]

class PeopleCreateRequest(RequiredPeopleCreateRequest, OptionalPeopleCreateRequest):
    pass
