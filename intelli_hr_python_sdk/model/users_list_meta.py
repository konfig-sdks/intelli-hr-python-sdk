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


class UsersListMeta(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Contains miscellaneous meta information about the response.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def pagination() -> typing.Type['UsersListMetaPagination']:
                return UsersListMetaPagination
            
            
            class requestId(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 36
                    min_length = 36
            __annotations__ = {
                "pagination": pagination,
                "requestId": requestId,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pagination"]) -> 'UsersListMetaPagination': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["requestId"]) -> MetaOapg.properties.requestId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["pagination", "requestId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pagination"]) -> typing.Union['UsersListMetaPagination', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["requestId"]) -> typing.Union[MetaOapg.properties.requestId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["pagination", "requestId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        pagination: typing.Union['UsersListMetaPagination', schemas.Unset] = schemas.unset,
        requestId: typing.Union[MetaOapg.properties.requestId, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UsersListMeta':
        return super().__new__(
            cls,
            *args,
            pagination=pagination,
            requestId=requestId,
            _configuration=_configuration,
            **kwargs,
        )

from intelli_hr_python_sdk.model.users_list_meta_pagination import UsersListMetaPagination
