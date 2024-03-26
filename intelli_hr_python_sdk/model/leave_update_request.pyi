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


class LeaveUpdateRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "jobId",
            "endDate",
        }
        
        class properties:
            
            
            class jobId(
                schemas.StrSchema
            ):
                pass
            endDate = schemas.StrSchema
            shouldNotFinaliseEndDate = schemas.BoolSchema
            startDate = schemas.StrSchema
        
            @staticmethod
            def leaveType() -> typing.Type['LeaveUpdateRequestLeaveType']:
                return LeaveUpdateRequestLeaveType
            fte = schemas.StrSchema
            __annotations__ = {
                "jobId": jobId,
                "endDate": endDate,
                "shouldNotFinaliseEndDate": shouldNotFinaliseEndDate,
                "startDate": startDate,
                "leaveType": leaveType,
                "fte": fte,
            }
    
    jobId: MetaOapg.properties.jobId
    endDate: MetaOapg.properties.endDate
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["jobId"]) -> MetaOapg.properties.jobId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["endDate"]) -> MetaOapg.properties.endDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shouldNotFinaliseEndDate"]) -> MetaOapg.properties.shouldNotFinaliseEndDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startDate"]) -> MetaOapg.properties.startDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["leaveType"]) -> 'LeaveUpdateRequestLeaveType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fte"]) -> MetaOapg.properties.fte: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["jobId", "endDate", "shouldNotFinaliseEndDate", "startDate", "leaveType", "fte", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["jobId"]) -> MetaOapg.properties.jobId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["endDate"]) -> MetaOapg.properties.endDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shouldNotFinaliseEndDate"]) -> typing.Union[MetaOapg.properties.shouldNotFinaliseEndDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startDate"]) -> typing.Union[MetaOapg.properties.startDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["leaveType"]) -> typing.Union['LeaveUpdateRequestLeaveType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fte"]) -> typing.Union[MetaOapg.properties.fte, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["jobId", "endDate", "shouldNotFinaliseEndDate", "startDate", "leaveType", "fte", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        jobId: typing.Union[MetaOapg.properties.jobId, str, ],
        endDate: typing.Union[MetaOapg.properties.endDate, str, ],
        shouldNotFinaliseEndDate: typing.Union[MetaOapg.properties.shouldNotFinaliseEndDate, bool, schemas.Unset] = schemas.unset,
        startDate: typing.Union[MetaOapg.properties.startDate, str, schemas.Unset] = schemas.unset,
        leaveType: typing.Union['LeaveUpdateRequestLeaveType', schemas.Unset] = schemas.unset,
        fte: typing.Union[MetaOapg.properties.fte, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LeaveUpdateRequest':
        return super().__new__(
            cls,
            *args,
            jobId=jobId,
            endDate=endDate,
            shouldNotFinaliseEndDate=shouldNotFinaliseEndDate,
            startDate=startDate,
            leaveType=leaveType,
            fte=fte,
            _configuration=_configuration,
            **kwargs,
        )

from intelli_hr_python_sdk.model.leave_update_request_leave_type import LeaveUpdateRequestLeaveType
