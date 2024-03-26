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

from intelli_hr_python_sdk.model.person_id_image_patch_request_coordinates import PersonIdImagePatchRequestCoordinates as PersonIdImagePatchRequestCoordinatesSchema
from intelli_hr_python_sdk.model.person_id_image_patch_request import PersonIdImagePatchRequest as PersonIdImagePatchRequestSchema

from intelli_hr_python_sdk.type.person_id_image_patch_request_coordinates import PersonIdImagePatchRequestCoordinates
from intelli_hr_python_sdk.type.person_id_image_patch_request import PersonIdImagePatchRequest

from ...api_client import Dictionary
from intelli_hr_python_sdk.pydantic.person_id_image_patch_request import PersonIdImagePatchRequest as PersonIdImagePatchRequestPydantic
from intelli_hr_python_sdk.pydantic.person_id_image_patch_request_coordinates import PersonIdImagePatchRequestCoordinates as PersonIdImagePatchRequestCoordinatesPydantic

# Path params
PersonIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'personId': typing.Union[PersonIdSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_person_id = api_client.PathParameter(
    name="personId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=PersonIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = PersonIdImagePatchRequestSchema


request_body_person_id_image_patch_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)


@dataclass
class ApiResponseFor204(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor204Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_204 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor204,
    response_cls_async=ApiResponseFor204Async,
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


class BaseApi(api_client.Api):

    def _promote_image_mapped_args(
        self,
        person_id: str,
        image_type: typing.Optional[str] = None,
        rotation: typing.Optional[int] = None,
        coordinates: typing.Optional[PersonIdImagePatchRequestCoordinates] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if image_type is not None:
            _body["imageType"] = image_type
        if rotation is not None:
            _body["rotation"] = rotation
        if coordinates is not None:
            _body["coordinates"] = coordinates
        args.body = _body
        if person_id is not None:
            _path_params["personId"] = person_id
        args.path = _path_params
        return args

    async def _apromote_image_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor204Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Promote temporary image
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_person_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
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
            path_template='/people/{personId}/images',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_person_id_image_patch_request.serialize(body, content_type)
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


    def _promote_image_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor204,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Promote temporary image
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_person_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
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
            path_template='/people/{personId}/images',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_person_id_image_patch_request.serialize(body, content_type)
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


class PromoteImageRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def apromote_image(
        self,
        person_id: str,
        image_type: typing.Optional[str] = None,
        rotation: typing.Optional[int] = None,
        coordinates: typing.Optional[PersonIdImagePatchRequestCoordinates] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor204Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._promote_image_mapped_args(
            person_id=person_id,
            image_type=image_type,
            rotation=rotation,
            coordinates=coordinates,
        )
        return await self._apromote_image_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def promote_image(
        self,
        person_id: str,
        image_type: typing.Optional[str] = None,
        rotation: typing.Optional[int] = None,
        coordinates: typing.Optional[PersonIdImagePatchRequestCoordinates] = None,
    ) -> typing.Union[
        ApiResponseFor204,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._promote_image_mapped_args(
            person_id=person_id,
            image_type=image_type,
            rotation=rotation,
            coordinates=coordinates,
        )
        return self._promote_image_oapg(
            body=args.body,
            path_params=args.path,
        )

class PromoteImage(BaseApi):

    async def apromote_image(
        self,
        person_id: str,
        image_type: typing.Optional[str] = None,
        rotation: typing.Optional[int] = None,
        coordinates: typing.Optional[PersonIdImagePatchRequestCoordinates] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.apromote_image(
            person_id=person_id,
            image_type=image_type,
            rotation=rotation,
            coordinates=coordinates,
            **kwargs,
        )
    
    
    def promote_image(
        self,
        person_id: str,
        image_type: typing.Optional[str] = None,
        rotation: typing.Optional[int] = None,
        coordinates: typing.Optional[PersonIdImagePatchRequestCoordinates] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.promote_image(
            person_id=person_id,
            image_type=image_type,
            rotation=rotation,
            coordinates=coordinates,
        )


class ApiForpatch(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apatch(
        self,
        person_id: str,
        image_type: typing.Optional[str] = None,
        rotation: typing.Optional[int] = None,
        coordinates: typing.Optional[PersonIdImagePatchRequestCoordinates] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor204Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._promote_image_mapped_args(
            person_id=person_id,
            image_type=image_type,
            rotation=rotation,
            coordinates=coordinates,
        )
        return await self._apromote_image_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def patch(
        self,
        person_id: str,
        image_type: typing.Optional[str] = None,
        rotation: typing.Optional[int] = None,
        coordinates: typing.Optional[PersonIdImagePatchRequestCoordinates] = None,
    ) -> typing.Union[
        ApiResponseFor204,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._promote_image_mapped_args(
            person_id=person_id,
            image_type=image_type,
            rotation=rotation,
            coordinates=coordinates,
        )
        return self._promote_image_oapg(
            body=args.body,
            path_params=args.path,
        )

