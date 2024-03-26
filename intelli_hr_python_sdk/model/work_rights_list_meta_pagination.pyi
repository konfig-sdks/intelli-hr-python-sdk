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


class WorkRightsListMetaPagination(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Contains information related to the pagination of the response
    """


    class MetaOapg:
        
        class properties:
            
            
            class total(
                schemas.IntSchema
            ):
                pass
            
            
            class count(
                schemas.IntSchema
            ):
                pass
            
            
            class per_page(
                schemas.IntSchema
            ):
                pass
            
            
            class current_page(
                schemas.IntSchema
            ):
                pass
            
            
            class total_pages(
                schemas.IntSchema
            ):
                pass
            __annotations__ = {
                "total": total,
                "count": count,
                "per_page": per_page,
                "current_page": current_page,
                "total_pages": total_pages,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total"]) -> MetaOapg.properties.total: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["count"]) -> MetaOapg.properties.count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["per_page"]) -> MetaOapg.properties.per_page: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["current_page"]) -> MetaOapg.properties.current_page: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_pages"]) -> MetaOapg.properties.total_pages: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["total", "count", "per_page", "current_page", "total_pages", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total"]) -> typing.Union[MetaOapg.properties.total, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["count"]) -> typing.Union[MetaOapg.properties.count, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["per_page"]) -> typing.Union[MetaOapg.properties.per_page, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["current_page"]) -> typing.Union[MetaOapg.properties.current_page, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_pages"]) -> typing.Union[MetaOapg.properties.total_pages, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["total", "count", "per_page", "current_page", "total_pages", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        total: typing.Union[MetaOapg.properties.total, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        count: typing.Union[MetaOapg.properties.count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        per_page: typing.Union[MetaOapg.properties.per_page, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        current_page: typing.Union[MetaOapg.properties.current_page, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        total_pages: typing.Union[MetaOapg.properties.total_pages, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WorkRightsListMetaPagination':
        return super().__new__(
            cls,
            *args,
            total=total,
            count=count,
            per_page=per_page,
            current_page=current_page,
            total_pages=total_pages,
            _configuration=_configuration,
            **kwargs,
        )
