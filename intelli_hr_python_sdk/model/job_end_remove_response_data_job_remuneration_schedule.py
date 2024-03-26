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


class JobEndRemoveResponseDataJobRemunerationSchedule(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The current remuneration details for this [Job](https://developers.intellihr.io/docs/v1/), including information such as salary and hourly pay, all [Jobs](https://developers.intellihr.io/docs/v1/) have a remuneration schedule but for unpaid employees they will have a special `No Remuneration Schedule` schedule.
    """


    class MetaOapg:
        
        class properties:
            type = schemas.StrSchema
            baseAnnualSalary = schemas.NumberSchema
            baseHourlyRate = schemas.NumberSchema
            
            
            class currency(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'^[A-Z]{3}$',
                    }]
            hoursPerCycle = schemas.NumberSchema
            payCycle = schemas.StrSchema
            annualPackage = schemas.NumberSchema
            hourlyPackage = schemas.NumberSchema
            currencyConversionOccurred = schemas.BoolSchema
        
            @staticmethod
            def employmentCondition() -> typing.Type['JobEndRemoveResponseDataJobRemunerationScheduleEmploymentCondition']:
                return JobEndRemoveResponseDataJobRemunerationScheduleEmploymentCondition
        
            @staticmethod
            def additions() -> typing.Type['JobEndRemoveResponseDataJobRemunerationScheduleAdditions']:
                return JobEndRemoveResponseDataJobRemunerationScheduleAdditions
        
            @staticmethod
            def deductions() -> typing.Type['JobEndRemoveResponseDataJobRemunerationScheduleDeductions']:
                return JobEndRemoveResponseDataJobRemunerationScheduleDeductions
        
            @staticmethod
            def additionsToTotal() -> typing.Type['JobEndRemoveResponseDataJobRemunerationScheduleAdditionsToTotal']:
                return JobEndRemoveResponseDataJobRemunerationScheduleAdditionsToTotal
        
            @staticmethod
            def breakdowns() -> typing.Type['JobEndRemoveResponseDataJobRemunerationScheduleBreakdowns']:
                return JobEndRemoveResponseDataJobRemunerationScheduleBreakdowns
        
            @staticmethod
            def customFields() -> typing.Type['CustomFieldsResponse']:
                return CustomFieldsResponse
            __annotations__ = {
                "type": type,
                "baseAnnualSalary": baseAnnualSalary,
                "baseHourlyRate": baseHourlyRate,
                "currency": currency,
                "hoursPerCycle": hoursPerCycle,
                "payCycle": payCycle,
                "annualPackage": annualPackage,
                "hourlyPackage": hourlyPackage,
                "currencyConversionOccurred": currencyConversionOccurred,
                "employmentCondition": employmentCondition,
                "additions": additions,
                "deductions": deductions,
                "additionsToTotal": additionsToTotal,
                "breakdowns": breakdowns,
                "customFields": customFields,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["baseAnnualSalary"]) -> MetaOapg.properties.baseAnnualSalary: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["baseHourlyRate"]) -> MetaOapg.properties.baseHourlyRate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency"]) -> MetaOapg.properties.currency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hoursPerCycle"]) -> MetaOapg.properties.hoursPerCycle: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payCycle"]) -> MetaOapg.properties.payCycle: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["annualPackage"]) -> MetaOapg.properties.annualPackage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hourlyPackage"]) -> MetaOapg.properties.hourlyPackage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currencyConversionOccurred"]) -> MetaOapg.properties.currencyConversionOccurred: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employmentCondition"]) -> 'JobEndRemoveResponseDataJobRemunerationScheduleEmploymentCondition': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["additions"]) -> 'JobEndRemoveResponseDataJobRemunerationScheduleAdditions': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deductions"]) -> 'JobEndRemoveResponseDataJobRemunerationScheduleDeductions': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["additionsToTotal"]) -> 'JobEndRemoveResponseDataJobRemunerationScheduleAdditionsToTotal': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["breakdowns"]) -> 'JobEndRemoveResponseDataJobRemunerationScheduleBreakdowns': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customFields"]) -> 'CustomFieldsResponse': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "baseAnnualSalary", "baseHourlyRate", "currency", "hoursPerCycle", "payCycle", "annualPackage", "hourlyPackage", "currencyConversionOccurred", "employmentCondition", "additions", "deductions", "additionsToTotal", "breakdowns", "customFields", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["baseAnnualSalary"]) -> typing.Union[MetaOapg.properties.baseAnnualSalary, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["baseHourlyRate"]) -> typing.Union[MetaOapg.properties.baseHourlyRate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency"]) -> typing.Union[MetaOapg.properties.currency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hoursPerCycle"]) -> typing.Union[MetaOapg.properties.hoursPerCycle, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payCycle"]) -> typing.Union[MetaOapg.properties.payCycle, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["annualPackage"]) -> typing.Union[MetaOapg.properties.annualPackage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hourlyPackage"]) -> typing.Union[MetaOapg.properties.hourlyPackage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currencyConversionOccurred"]) -> typing.Union[MetaOapg.properties.currencyConversionOccurred, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employmentCondition"]) -> typing.Union['JobEndRemoveResponseDataJobRemunerationScheduleEmploymentCondition', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["additions"]) -> typing.Union['JobEndRemoveResponseDataJobRemunerationScheduleAdditions', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deductions"]) -> typing.Union['JobEndRemoveResponseDataJobRemunerationScheduleDeductions', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["additionsToTotal"]) -> typing.Union['JobEndRemoveResponseDataJobRemunerationScheduleAdditionsToTotal', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["breakdowns"]) -> typing.Union['JobEndRemoveResponseDataJobRemunerationScheduleBreakdowns', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customFields"]) -> typing.Union['CustomFieldsResponse', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "baseAnnualSalary", "baseHourlyRate", "currency", "hoursPerCycle", "payCycle", "annualPackage", "hourlyPackage", "currencyConversionOccurred", "employmentCondition", "additions", "deductions", "additionsToTotal", "breakdowns", "customFields", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        baseAnnualSalary: typing.Union[MetaOapg.properties.baseAnnualSalary, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        baseHourlyRate: typing.Union[MetaOapg.properties.baseHourlyRate, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        currency: typing.Union[MetaOapg.properties.currency, str, schemas.Unset] = schemas.unset,
        hoursPerCycle: typing.Union[MetaOapg.properties.hoursPerCycle, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        payCycle: typing.Union[MetaOapg.properties.payCycle, str, schemas.Unset] = schemas.unset,
        annualPackage: typing.Union[MetaOapg.properties.annualPackage, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        hourlyPackage: typing.Union[MetaOapg.properties.hourlyPackage, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        currencyConversionOccurred: typing.Union[MetaOapg.properties.currencyConversionOccurred, bool, schemas.Unset] = schemas.unset,
        employmentCondition: typing.Union['JobEndRemoveResponseDataJobRemunerationScheduleEmploymentCondition', schemas.Unset] = schemas.unset,
        additions: typing.Union['JobEndRemoveResponseDataJobRemunerationScheduleAdditions', schemas.Unset] = schemas.unset,
        deductions: typing.Union['JobEndRemoveResponseDataJobRemunerationScheduleDeductions', schemas.Unset] = schemas.unset,
        additionsToTotal: typing.Union['JobEndRemoveResponseDataJobRemunerationScheduleAdditionsToTotal', schemas.Unset] = schemas.unset,
        breakdowns: typing.Union['JobEndRemoveResponseDataJobRemunerationScheduleBreakdowns', schemas.Unset] = schemas.unset,
        customFields: typing.Union['CustomFieldsResponse', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'JobEndRemoveResponseDataJobRemunerationSchedule':
        return super().__new__(
            cls,
            *args,
            type=type,
            baseAnnualSalary=baseAnnualSalary,
            baseHourlyRate=baseHourlyRate,
            currency=currency,
            hoursPerCycle=hoursPerCycle,
            payCycle=payCycle,
            annualPackage=annualPackage,
            hourlyPackage=hourlyPackage,
            currencyConversionOccurred=currencyConversionOccurred,
            employmentCondition=employmentCondition,
            additions=additions,
            deductions=deductions,
            additionsToTotal=additionsToTotal,
            breakdowns=breakdowns,
            customFields=customFields,
            _configuration=_configuration,
            **kwargs,
        )

from intelli_hr_python_sdk.model.custom_fields_response import CustomFieldsResponse
from intelli_hr_python_sdk.model.job_end_remove_response_data_job_remuneration_schedule_additions import JobEndRemoveResponseDataJobRemunerationScheduleAdditions
from intelli_hr_python_sdk.model.job_end_remove_response_data_job_remuneration_schedule_additions_to_total import JobEndRemoveResponseDataJobRemunerationScheduleAdditionsToTotal
from intelli_hr_python_sdk.model.job_end_remove_response_data_job_remuneration_schedule_breakdowns import JobEndRemoveResponseDataJobRemunerationScheduleBreakdowns
from intelli_hr_python_sdk.model.job_end_remove_response_data_job_remuneration_schedule_deductions import JobEndRemoveResponseDataJobRemunerationScheduleDeductions
from intelli_hr_python_sdk.model.job_end_remove_response_data_job_remuneration_schedule_employment_condition import JobEndRemoveResponseDataJobRemunerationScheduleEmploymentCondition
