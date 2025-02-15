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

from intelli_hr_python_sdk.model.job_create_request_business_unit import JobCreateRequestBusinessUnit as JobCreateRequestBusinessUnitSchema
from intelli_hr_python_sdk.model.job_create_request_work_class import JobCreateRequestWorkClass as JobCreateRequestWorkClassSchema
from intelli_hr_python_sdk.model.job_create_request_person import JobCreateRequestPerson as JobCreateRequestPersonSchema
from intelli_hr_python_sdk.model.job_create_request_pay_grade import JobCreateRequestPayGrade as JobCreateRequestPayGradeSchema
from intelli_hr_python_sdk.model.job_create_request_establishment import JobCreateRequestEstablishment as JobCreateRequestEstablishmentSchema
from intelli_hr_python_sdk.model.job_create_request_custom_fields import JobCreateRequestCustomFields as JobCreateRequestCustomFieldsSchema
from intelli_hr_python_sdk.model.job_create_request_employment_condition import JobCreateRequestEmploymentCondition as JobCreateRequestEmploymentConditionSchema
from intelli_hr_python_sdk.model.job_create_request_supervisor_person import JobCreateRequestSupervisorPerson as JobCreateRequestSupervisorPersonSchema
from intelli_hr_python_sdk.model.job_create_request_recruitment import JobCreateRequestRecruitment as JobCreateRequestRecruitmentSchema
from intelli_hr_python_sdk.model.job_create_request_business_entity import JobCreateRequestBusinessEntity as JobCreateRequestBusinessEntitySchema
from intelli_hr_python_sdk.model.job_create_request_remuneration_schedule import JobCreateRequestRemunerationSchedule as JobCreateRequestRemunerationScheduleSchema
from intelli_hr_python_sdk.model.job_create_request_supervisor_job import JobCreateRequestSupervisorJob as JobCreateRequestSupervisorJobSchema
from intelli_hr_python_sdk.model.job_create_request import JobCreateRequest as JobCreateRequestSchema
from intelli_hr_python_sdk.model.job_create_request_location import JobCreateRequestLocation as JobCreateRequestLocationSchema
from intelli_hr_python_sdk.model.job_create_request_work_type import JobCreateRequestWorkType as JobCreateRequestWorkTypeSchema
from intelli_hr_python_sdk.model.job_create_response import JobCreateResponse as JobCreateResponseSchema

from intelli_hr_python_sdk.type.job_create_request_custom_fields import JobCreateRequestCustomFields
from intelli_hr_python_sdk.type.job_create_request_recruitment import JobCreateRequestRecruitment
from intelli_hr_python_sdk.type.job_create_request_person import JobCreateRequestPerson
from intelli_hr_python_sdk.type.job_create_request import JobCreateRequest
from intelli_hr_python_sdk.type.job_create_request_business_entity import JobCreateRequestBusinessEntity
from intelli_hr_python_sdk.type.job_create_request_supervisor_job import JobCreateRequestSupervisorJob
from intelli_hr_python_sdk.type.job_create_request_pay_grade import JobCreateRequestPayGrade
from intelli_hr_python_sdk.type.job_create_request_work_class import JobCreateRequestWorkClass
from intelli_hr_python_sdk.type.job_create_request_location import JobCreateRequestLocation
from intelli_hr_python_sdk.type.job_create_response import JobCreateResponse
from intelli_hr_python_sdk.type.job_create_request_employment_condition import JobCreateRequestEmploymentCondition
from intelli_hr_python_sdk.type.job_create_request_work_type import JobCreateRequestWorkType
from intelli_hr_python_sdk.type.job_create_request_establishment import JobCreateRequestEstablishment
from intelli_hr_python_sdk.type.job_create_request_business_unit import JobCreateRequestBusinessUnit
from intelli_hr_python_sdk.type.job_create_request_supervisor_person import JobCreateRequestSupervisorPerson
from intelli_hr_python_sdk.type.job_create_request_remuneration_schedule import JobCreateRequestRemunerationSchedule

from ...api_client import Dictionary
from intelli_hr_python_sdk.pydantic.job_create_request_remuneration_schedule import JobCreateRequestRemunerationSchedule as JobCreateRequestRemunerationSchedulePydantic
from intelli_hr_python_sdk.pydantic.job_create_response import JobCreateResponse as JobCreateResponsePydantic
from intelli_hr_python_sdk.pydantic.job_create_request import JobCreateRequest as JobCreateRequestPydantic
from intelli_hr_python_sdk.pydantic.job_create_request_employment_condition import JobCreateRequestEmploymentCondition as JobCreateRequestEmploymentConditionPydantic
from intelli_hr_python_sdk.pydantic.job_create_request_work_class import JobCreateRequestWorkClass as JobCreateRequestWorkClassPydantic
from intelli_hr_python_sdk.pydantic.job_create_request_work_type import JobCreateRequestWorkType as JobCreateRequestWorkTypePydantic
from intelli_hr_python_sdk.pydantic.job_create_request_supervisor_person import JobCreateRequestSupervisorPerson as JobCreateRequestSupervisorPersonPydantic
from intelli_hr_python_sdk.pydantic.job_create_request_location import JobCreateRequestLocation as JobCreateRequestLocationPydantic
from intelli_hr_python_sdk.pydantic.job_create_request_business_unit import JobCreateRequestBusinessUnit as JobCreateRequestBusinessUnitPydantic
from intelli_hr_python_sdk.pydantic.job_create_request_recruitment import JobCreateRequestRecruitment as JobCreateRequestRecruitmentPydantic
from intelli_hr_python_sdk.pydantic.job_create_request_person import JobCreateRequestPerson as JobCreateRequestPersonPydantic
from intelli_hr_python_sdk.pydantic.job_create_request_business_entity import JobCreateRequestBusinessEntity as JobCreateRequestBusinessEntityPydantic
from intelli_hr_python_sdk.pydantic.job_create_request_supervisor_job import JobCreateRequestSupervisorJob as JobCreateRequestSupervisorJobPydantic
from intelli_hr_python_sdk.pydantic.job_create_request_custom_fields import JobCreateRequestCustomFields as JobCreateRequestCustomFieldsPydantic
from intelli_hr_python_sdk.pydantic.job_create_request_pay_grade import JobCreateRequestPayGrade as JobCreateRequestPayGradePydantic
from intelli_hr_python_sdk.pydantic.job_create_request_establishment import JobCreateRequestEstablishment as JobCreateRequestEstablishmentPydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = JobCreateRequestSchema


request_body_job_create_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
_auth = [
    'ApiKey',
]
SchemaFor201ResponseBodyApplicationJson = JobCreateResponseSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: JobCreateResponse


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: JobCreateResponse


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
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
    '201': _response_for_201,
    '400': _response_for_400,
    '403': _response_for_403,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_record_mapped_args(
        self,
        person: JobCreateRequestPerson,
        company_start_date: str,
        name: str,
        business_entity: JobCreateRequestBusinessEntity,
        business_unit: JobCreateRequestBusinessUnit,
        work_class: JobCreateRequestWorkClass,
        company_end_date: typing.Optional[str] = None,
        start_date: typing.Optional[str] = None,
        end_date: typing.Optional[str] = None,
        establishment: typing.Optional[JobCreateRequestEstablishment] = None,
        supervisor_person: typing.Optional[JobCreateRequestSupervisorPerson] = None,
        supervisor_job: typing.Optional[JobCreateRequestSupervisorJob] = None,
        location: typing.Optional[JobCreateRequestLocation] = None,
        work_type: typing.Optional[JobCreateRequestWorkType] = None,
        fte: typing.Optional[str] = None,
        pay_grade: typing.Optional[JobCreateRequestPayGrade] = None,
        employment_condition: typing.Optional[JobCreateRequestEmploymentCondition] = None,
        remuneration_schedule: typing.Optional[JobCreateRequestRemunerationSchedule] = None,
        recruitment: typing.Optional[JobCreateRequestRecruitment] = None,
        custom_fields: typing.Optional[JobCreateRequestCustomFields] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if person is not None:
            _body["person"] = person
        if company_start_date is not None:
            _body["companyStartDate"] = company_start_date
        if company_end_date is not None:
            _body["companyEndDate"] = company_end_date
        if start_date is not None:
            _body["startDate"] = start_date
        if end_date is not None:
            _body["endDate"] = end_date
        if name is not None:
            _body["name"] = name
        if business_entity is not None:
            _body["businessEntity"] = business_entity
        if business_unit is not None:
            _body["businessUnit"] = business_unit
        if establishment is not None:
            _body["establishment"] = establishment
        if supervisor_person is not None:
            _body["supervisorPerson"] = supervisor_person
        if supervisor_job is not None:
            _body["supervisorJob"] = supervisor_job
        if location is not None:
            _body["location"] = location
        if work_class is not None:
            _body["workClass"] = work_class
        if work_type is not None:
            _body["workType"] = work_type
        if fte is not None:
            _body["fte"] = fte
        if pay_grade is not None:
            _body["payGrade"] = pay_grade
        if employment_condition is not None:
            _body["employmentCondition"] = employment_condition
        if remuneration_schedule is not None:
            _body["remunerationSchedule"] = remuneration_schedule
        if recruitment is not None:
            _body["recruitment"] = recruitment
        if custom_fields is not None:
            _body["customFields"] = custom_fields
        args.body = _body
        return args

    async def _acreate_record_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create a new Job
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
        method = 'post'.upper()
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
            path_template='/jobs',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_job_create_request.serialize(body, content_type)
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


    def _create_record_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create a new Job
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
        method = 'post'.upper()
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
            path_template='/jobs',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_job_create_request.serialize(body, content_type)
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


class CreateRecordRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_record(
        self,
        person: JobCreateRequestPerson,
        company_start_date: str,
        name: str,
        business_entity: JobCreateRequestBusinessEntity,
        business_unit: JobCreateRequestBusinessUnit,
        work_class: JobCreateRequestWorkClass,
        company_end_date: typing.Optional[str] = None,
        start_date: typing.Optional[str] = None,
        end_date: typing.Optional[str] = None,
        establishment: typing.Optional[JobCreateRequestEstablishment] = None,
        supervisor_person: typing.Optional[JobCreateRequestSupervisorPerson] = None,
        supervisor_job: typing.Optional[JobCreateRequestSupervisorJob] = None,
        location: typing.Optional[JobCreateRequestLocation] = None,
        work_type: typing.Optional[JobCreateRequestWorkType] = None,
        fte: typing.Optional[str] = None,
        pay_grade: typing.Optional[JobCreateRequestPayGrade] = None,
        employment_condition: typing.Optional[JobCreateRequestEmploymentCondition] = None,
        remuneration_schedule: typing.Optional[JobCreateRequestRemunerationSchedule] = None,
        recruitment: typing.Optional[JobCreateRequestRecruitment] = None,
        custom_fields: typing.Optional[JobCreateRequestCustomFields] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_record_mapped_args(
            person=person,
            company_start_date=company_start_date,
            name=name,
            business_entity=business_entity,
            business_unit=business_unit,
            work_class=work_class,
            company_end_date=company_end_date,
            start_date=start_date,
            end_date=end_date,
            establishment=establishment,
            supervisor_person=supervisor_person,
            supervisor_job=supervisor_job,
            location=location,
            work_type=work_type,
            fte=fte,
            pay_grade=pay_grade,
            employment_condition=employment_condition,
            remuneration_schedule=remuneration_schedule,
            recruitment=recruitment,
            custom_fields=custom_fields,
        )
        return await self._acreate_record_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_record(
        self,
        person: JobCreateRequestPerson,
        company_start_date: str,
        name: str,
        business_entity: JobCreateRequestBusinessEntity,
        business_unit: JobCreateRequestBusinessUnit,
        work_class: JobCreateRequestWorkClass,
        company_end_date: typing.Optional[str] = None,
        start_date: typing.Optional[str] = None,
        end_date: typing.Optional[str] = None,
        establishment: typing.Optional[JobCreateRequestEstablishment] = None,
        supervisor_person: typing.Optional[JobCreateRequestSupervisorPerson] = None,
        supervisor_job: typing.Optional[JobCreateRequestSupervisorJob] = None,
        location: typing.Optional[JobCreateRequestLocation] = None,
        work_type: typing.Optional[JobCreateRequestWorkType] = None,
        fte: typing.Optional[str] = None,
        pay_grade: typing.Optional[JobCreateRequestPayGrade] = None,
        employment_condition: typing.Optional[JobCreateRequestEmploymentCondition] = None,
        remuneration_schedule: typing.Optional[JobCreateRequestRemunerationSchedule] = None,
        recruitment: typing.Optional[JobCreateRequestRecruitment] = None,
        custom_fields: typing.Optional[JobCreateRequestCustomFields] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_record_mapped_args(
            person=person,
            company_start_date=company_start_date,
            name=name,
            business_entity=business_entity,
            business_unit=business_unit,
            work_class=work_class,
            company_end_date=company_end_date,
            start_date=start_date,
            end_date=end_date,
            establishment=establishment,
            supervisor_person=supervisor_person,
            supervisor_job=supervisor_job,
            location=location,
            work_type=work_type,
            fte=fte,
            pay_grade=pay_grade,
            employment_condition=employment_condition,
            remuneration_schedule=remuneration_schedule,
            recruitment=recruitment,
            custom_fields=custom_fields,
        )
        return self._create_record_oapg(
            body=args.body,
        )

class CreateRecord(BaseApi):

    async def acreate_record(
        self,
        person: JobCreateRequestPerson,
        company_start_date: str,
        name: str,
        business_entity: JobCreateRequestBusinessEntity,
        business_unit: JobCreateRequestBusinessUnit,
        work_class: JobCreateRequestWorkClass,
        company_end_date: typing.Optional[str] = None,
        start_date: typing.Optional[str] = None,
        end_date: typing.Optional[str] = None,
        establishment: typing.Optional[JobCreateRequestEstablishment] = None,
        supervisor_person: typing.Optional[JobCreateRequestSupervisorPerson] = None,
        supervisor_job: typing.Optional[JobCreateRequestSupervisorJob] = None,
        location: typing.Optional[JobCreateRequestLocation] = None,
        work_type: typing.Optional[JobCreateRequestWorkType] = None,
        fte: typing.Optional[str] = None,
        pay_grade: typing.Optional[JobCreateRequestPayGrade] = None,
        employment_condition: typing.Optional[JobCreateRequestEmploymentCondition] = None,
        remuneration_schedule: typing.Optional[JobCreateRequestRemunerationSchedule] = None,
        recruitment: typing.Optional[JobCreateRequestRecruitment] = None,
        custom_fields: typing.Optional[JobCreateRequestCustomFields] = None,
        validate: bool = False,
        **kwargs,
    ) -> JobCreateResponsePydantic:
        raw_response = await self.raw.acreate_record(
            person=person,
            company_start_date=company_start_date,
            name=name,
            business_entity=business_entity,
            business_unit=business_unit,
            work_class=work_class,
            company_end_date=company_end_date,
            start_date=start_date,
            end_date=end_date,
            establishment=establishment,
            supervisor_person=supervisor_person,
            supervisor_job=supervisor_job,
            location=location,
            work_type=work_type,
            fte=fte,
            pay_grade=pay_grade,
            employment_condition=employment_condition,
            remuneration_schedule=remuneration_schedule,
            recruitment=recruitment,
            custom_fields=custom_fields,
            **kwargs,
        )
        if validate:
            return JobCreateResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(JobCreateResponsePydantic, raw_response.body)
    
    
    def create_record(
        self,
        person: JobCreateRequestPerson,
        company_start_date: str,
        name: str,
        business_entity: JobCreateRequestBusinessEntity,
        business_unit: JobCreateRequestBusinessUnit,
        work_class: JobCreateRequestWorkClass,
        company_end_date: typing.Optional[str] = None,
        start_date: typing.Optional[str] = None,
        end_date: typing.Optional[str] = None,
        establishment: typing.Optional[JobCreateRequestEstablishment] = None,
        supervisor_person: typing.Optional[JobCreateRequestSupervisorPerson] = None,
        supervisor_job: typing.Optional[JobCreateRequestSupervisorJob] = None,
        location: typing.Optional[JobCreateRequestLocation] = None,
        work_type: typing.Optional[JobCreateRequestWorkType] = None,
        fte: typing.Optional[str] = None,
        pay_grade: typing.Optional[JobCreateRequestPayGrade] = None,
        employment_condition: typing.Optional[JobCreateRequestEmploymentCondition] = None,
        remuneration_schedule: typing.Optional[JobCreateRequestRemunerationSchedule] = None,
        recruitment: typing.Optional[JobCreateRequestRecruitment] = None,
        custom_fields: typing.Optional[JobCreateRequestCustomFields] = None,
        validate: bool = False,
    ) -> JobCreateResponsePydantic:
        raw_response = self.raw.create_record(
            person=person,
            company_start_date=company_start_date,
            name=name,
            business_entity=business_entity,
            business_unit=business_unit,
            work_class=work_class,
            company_end_date=company_end_date,
            start_date=start_date,
            end_date=end_date,
            establishment=establishment,
            supervisor_person=supervisor_person,
            supervisor_job=supervisor_job,
            location=location,
            work_type=work_type,
            fte=fte,
            pay_grade=pay_grade,
            employment_condition=employment_condition,
            remuneration_schedule=remuneration_schedule,
            recruitment=recruitment,
            custom_fields=custom_fields,
        )
        if validate:
            return JobCreateResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(JobCreateResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        person: JobCreateRequestPerson,
        company_start_date: str,
        name: str,
        business_entity: JobCreateRequestBusinessEntity,
        business_unit: JobCreateRequestBusinessUnit,
        work_class: JobCreateRequestWorkClass,
        company_end_date: typing.Optional[str] = None,
        start_date: typing.Optional[str] = None,
        end_date: typing.Optional[str] = None,
        establishment: typing.Optional[JobCreateRequestEstablishment] = None,
        supervisor_person: typing.Optional[JobCreateRequestSupervisorPerson] = None,
        supervisor_job: typing.Optional[JobCreateRequestSupervisorJob] = None,
        location: typing.Optional[JobCreateRequestLocation] = None,
        work_type: typing.Optional[JobCreateRequestWorkType] = None,
        fte: typing.Optional[str] = None,
        pay_grade: typing.Optional[JobCreateRequestPayGrade] = None,
        employment_condition: typing.Optional[JobCreateRequestEmploymentCondition] = None,
        remuneration_schedule: typing.Optional[JobCreateRequestRemunerationSchedule] = None,
        recruitment: typing.Optional[JobCreateRequestRecruitment] = None,
        custom_fields: typing.Optional[JobCreateRequestCustomFields] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_record_mapped_args(
            person=person,
            company_start_date=company_start_date,
            name=name,
            business_entity=business_entity,
            business_unit=business_unit,
            work_class=work_class,
            company_end_date=company_end_date,
            start_date=start_date,
            end_date=end_date,
            establishment=establishment,
            supervisor_person=supervisor_person,
            supervisor_job=supervisor_job,
            location=location,
            work_type=work_type,
            fte=fte,
            pay_grade=pay_grade,
            employment_condition=employment_condition,
            remuneration_schedule=remuneration_schedule,
            recruitment=recruitment,
            custom_fields=custom_fields,
        )
        return await self._acreate_record_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        person: JobCreateRequestPerson,
        company_start_date: str,
        name: str,
        business_entity: JobCreateRequestBusinessEntity,
        business_unit: JobCreateRequestBusinessUnit,
        work_class: JobCreateRequestWorkClass,
        company_end_date: typing.Optional[str] = None,
        start_date: typing.Optional[str] = None,
        end_date: typing.Optional[str] = None,
        establishment: typing.Optional[JobCreateRequestEstablishment] = None,
        supervisor_person: typing.Optional[JobCreateRequestSupervisorPerson] = None,
        supervisor_job: typing.Optional[JobCreateRequestSupervisorJob] = None,
        location: typing.Optional[JobCreateRequestLocation] = None,
        work_type: typing.Optional[JobCreateRequestWorkType] = None,
        fte: typing.Optional[str] = None,
        pay_grade: typing.Optional[JobCreateRequestPayGrade] = None,
        employment_condition: typing.Optional[JobCreateRequestEmploymentCondition] = None,
        remuneration_schedule: typing.Optional[JobCreateRequestRemunerationSchedule] = None,
        recruitment: typing.Optional[JobCreateRequestRecruitment] = None,
        custom_fields: typing.Optional[JobCreateRequestCustomFields] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_record_mapped_args(
            person=person,
            company_start_date=company_start_date,
            name=name,
            business_entity=business_entity,
            business_unit=business_unit,
            work_class=work_class,
            company_end_date=company_end_date,
            start_date=start_date,
            end_date=end_date,
            establishment=establishment,
            supervisor_person=supervisor_person,
            supervisor_job=supervisor_job,
            location=location,
            work_type=work_type,
            fte=fte,
            pay_grade=pay_grade,
            employment_condition=employment_condition,
            remuneration_schedule=remuneration_schedule,
            recruitment=recruitment,
            custom_fields=custom_fields,
        )
        return self._create_record_oapg(
            body=args.body,
        )

