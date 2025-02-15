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

from intelli_hr_python_sdk.type.users_data_person import UsersDataPerson
from intelli_hr_python_sdk.type.users_data_user_permission_groups import UsersDataUserPermissionGroups

class RequiredUsersData(TypedDict):
    pass

class OptionalUsersData(TypedDict, total=False):
    # The identifier string for the [User](https://developers.intellihr.io/docs/v1/).
    id: str

    # The unique name of this user.
    username: str

    # Specifies whether this [User](https://developers.intellihr.io/docs/v1/) account is active. When disabled, you can no longer sign in using this account.
    isEnabled: bool

    # When this record was created. This date will follow the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6).
    createdAt: str

    # When this record was last updated. This date will follow the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6).
    updatedAt: str

    userPermissionGroups: UsersDataUserPermissionGroups

    person: UsersDataPerson

class UsersData(RequiredUsersData, OptionalUsersData):
    pass
