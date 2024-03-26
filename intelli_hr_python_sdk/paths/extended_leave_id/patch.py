# coding: utf-8

"""
    intelliHR Public API

    You can find developer's guide and more documentation on [https://developers.intellihr.io](https://developers.intellihr.io)

    The version of the OpenAPI document: V1
    Contact: support@intellihr.co
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from intelli_hr_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from intelli_hr_python_sdk.api_response import AsyncGeneratorResponse
from intelli_hr_python_sdk import api_client, exceptions
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

from intelli_hr_python_sdk.model.leave_update_request_leave_type import LeaveUpdateRequestLeaveType as LeaveUpdateRequestLeaveTypeSchema
from intelli_hr_python_sdk.model.leave_update_response import LeaveUpdateResponse as LeaveUpdateResponseSchema
from intelli_hr_python_sdk.model.leave_update_request import LeaveUpdateRequest as LeaveUpdateRequestSchema

from intelli_hr_python_sdk.type.leave_update_response import LeaveUpdateResponse
from intelli_hr_python_sdk.type.leave_update_request import LeaveUpdateRequest
from intelli_hr_python_sdk.type.leave_update_request_leave_type import LeaveUpdateRequestLeaveType

from ...api_client import Dictionary
from intelli_hr_python_sdk.pydantic.leave_update_request import LeaveUpdateRequest as LeaveUpdateRequestPydantic
from intelli_hr_python_sdk.pydantic.leave_update_request_leave_type import LeaveUpdateRequestLeaveType as LeaveUpdateRequestLeaveTypePydantic
from intelli_hr_python_sdk.pydantic.leave_update_response import LeaveUpdateResponse as LeaveUpdateResponsePydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = LeaveUpdateRequestSchema


request_body_leave_update_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
_auth = [
    'ApiKey',
]
SchemaFor200ResponseBodyApplicationJson = LeaveUpdateResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: LeaveUpdateResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: LeaveUpdateResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
)


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
)


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    response_cls_async=ApiResponseFor500Async,
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '403': _response_for_403,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _update_finalise_mapped_args(
        self,
        job_id: str,
        end_date: str,
        should_not_finalise_end_date: typing.Optional[bool] = None,
        start_date: typing.Optional[str] = None,
        leave_type: typing.Optional[LeaveUpdateRequestLeaveType] = None,
        fte: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if job_id is not None:
            _body["jobId"] = job_id
        if should_not_finalise_end_date is not None:
            _body["shouldNotFinaliseEndDate"] = should_not_finalise_end_date
        if start_date is not None:
            _body["startDate"] = start_date
        if end_date is not None:
            _body["endDate"] = end_date
        if leave_type is not None:
            _body["leaveType"] = leave_type
        if fte is not None:
            _body["fte"] = fte
        args.body = _body
        return args

    async def _aupdate_finalise_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Update or Finalise Extended Leave
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'patch'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/extended-leave/{id}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_leave_update_request.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _update_finalise_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Update or Finalise Extended Leave
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'patch'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/extended-leave/{id}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_leave_update_request.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class UpdateFinaliseRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_finalise(
        self,
        job_id: str,
        end_date: str,
        should_not_finalise_end_date: typing.Optional[bool] = None,
        start_date: typing.Optional[str] = None,
        leave_type: typing.Optional[LeaveUpdateRequestLeaveType] = None,
        fte: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_finalise_mapped_args(
            job_id=job_id,
            end_date=end_date,
            should_not_finalise_end_date=should_not_finalise_end_date,
            start_date=start_date,
            leave_type=leave_type,
            fte=fte,
        )
        return await self._aupdate_finalise_oapg(
            body=args.body,
            **kwargs,
        )
    
    def update_finalise(
        self,
        job_id: str,
        end_date: str,
        should_not_finalise_end_date: typing.Optional[bool] = None,
        start_date: typing.Optional[str] = None,
        leave_type: typing.Optional[LeaveUpdateRequestLeaveType] = None,
        fte: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_finalise_mapped_args(
            job_id=job_id,
            end_date=end_date,
            should_not_finalise_end_date=should_not_finalise_end_date,
            start_date=start_date,
            leave_type=leave_type,
            fte=fte,
        )
        return self._update_finalise_oapg(
            body=args.body,
        )

class UpdateFinalise(BaseApi):

    async def aupdate_finalise(
        self,
        job_id: str,
        end_date: str,
        should_not_finalise_end_date: typing.Optional[bool] = None,
        start_date: typing.Optional[str] = None,
        leave_type: typing.Optional[LeaveUpdateRequestLeaveType] = None,
        fte: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> LeaveUpdateResponsePydantic:
        raw_response = await self.raw.aupdate_finalise(
            job_id=job_id,
            end_date=end_date,
            should_not_finalise_end_date=should_not_finalise_end_date,
            start_date=start_date,
            leave_type=leave_type,
            fte=fte,
            **kwargs,
        )
        if validate:
            return LeaveUpdateResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(LeaveUpdateResponsePydantic, raw_response.body)
    
    
    def update_finalise(
        self,
        job_id: str,
        end_date: str,
        should_not_finalise_end_date: typing.Optional[bool] = None,
        start_date: typing.Optional[str] = None,
        leave_type: typing.Optional[LeaveUpdateRequestLeaveType] = None,
        fte: typing.Optional[str] = None,
        validate: bool = False,
    ) -> LeaveUpdateResponsePydantic:
        raw_response = self.raw.update_finalise(
            job_id=job_id,
            end_date=end_date,
            should_not_finalise_end_date=should_not_finalise_end_date,
            start_date=start_date,
            leave_type=leave_type,
            fte=fte,
        )
        if validate:
            return LeaveUpdateResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(LeaveUpdateResponsePydantic, raw_response.body)


class ApiForpatch(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apatch(
        self,
        job_id: str,
        end_date: str,
        should_not_finalise_end_date: typing.Optional[bool] = None,
        start_date: typing.Optional[str] = None,
        leave_type: typing.Optional[LeaveUpdateRequestLeaveType] = None,
        fte: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_finalise_mapped_args(
            job_id=job_id,
            end_date=end_date,
            should_not_finalise_end_date=should_not_finalise_end_date,
            start_date=start_date,
            leave_type=leave_type,
            fte=fte,
        )
        return await self._aupdate_finalise_oapg(
            body=args.body,
            **kwargs,
        )
    
    def patch(
        self,
        job_id: str,
        end_date: str,
        should_not_finalise_end_date: typing.Optional[bool] = None,
        start_date: typing.Optional[str] = None,
        leave_type: typing.Optional[LeaveUpdateRequestLeaveType] = None,
        fte: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_finalise_mapped_args(
            job_id=job_id,
            end_date=end_date,
            should_not_finalise_end_date=should_not_finalise_end_date,
            start_date=start_date,
            leave_type=leave_type,
            fte=fte,
        )
        return self._update_finalise_oapg(
            body=args.body,
        )

