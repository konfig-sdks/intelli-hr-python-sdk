# coding: utf-8

"""
    intelliHR Public API

    You can find developer's guide and more documentation on [https://developers.intellihr.io](https://developers.intellihr.io)

    The version of the OpenAPI document: V1
    Contact: support@intellihr.co
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from intelli_hr_python_sdk import schemas  # noqa: F401


class UsersListDataItemUserPermissionGroups(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    The array of user permission groups containing the [Permission Group's](https://developers.intellihr.io/docs/v1/) assigned to this user.
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['UsersListDataItemUserPermissionGroupsItem']:
            return UsersListDataItemUserPermissionGroupsItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['UsersListDataItemUserPermissionGroupsItem'], typing.List['UsersListDataItemUserPermissionGroupsItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'UsersListDataItemUserPermissionGroups':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'UsersListDataItemUserPermissionGroupsItem':
        return super().__getitem__(i)

from intelli_hr_python_sdk.model.users_list_data_item_user_permission_groups_item import UsersListDataItemUserPermissionGroupsItem
