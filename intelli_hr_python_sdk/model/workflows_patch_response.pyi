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


class WorkflowsPatchResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def data() -> typing.Type['WorkflowsPatchResponseData']:
                return WorkflowsPatchResponseData
        
            @staticmethod
            def meta() -> typing.Type['WorkflowsPatchResponseMeta']:
                return WorkflowsPatchResponseMeta
            __annotations__ = {
                "data": data,
                "meta": meta,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data"]) -> 'WorkflowsPatchResponseData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["meta"]) -> 'WorkflowsPatchResponseMeta': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["data", "meta", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> typing.Union['WorkflowsPatchResponseData', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["meta"]) -> typing.Union['WorkflowsPatchResponseMeta', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["data", "meta", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        data: typing.Union['WorkflowsPatchResponseData', schemas.Unset] = schemas.unset,
        meta: typing.Union['WorkflowsPatchResponseMeta', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WorkflowsPatchResponse':
        return super().__new__(
            cls,
            *args,
            data=data,
            meta=meta,
            _configuration=_configuration,
            **kwargs,
        )

from intelli_hr_python_sdk.model.workflows_patch_response_data import WorkflowsPatchResponseData
from intelli_hr_python_sdk.model.workflows_patch_response_meta import WorkflowsPatchResponseMeta
