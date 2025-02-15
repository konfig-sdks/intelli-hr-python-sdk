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


class PersonIdImagePatchRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            imageType = schemas.StrSchema
            
            
            class rotation(
                schemas.IntSchema
            ):
            
            
                class MetaOapg:
                    inclusive_maximum = 359
                    inclusive_minimum = 0
        
            @staticmethod
            def coordinates() -> typing.Type['PersonIdImagePatchRequestCoordinates']:
                return PersonIdImagePatchRequestCoordinates
            __annotations__ = {
                "imageType": imageType,
                "rotation": rotation,
                "coordinates": coordinates,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["imageType"]) -> MetaOapg.properties.imageType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rotation"]) -> MetaOapg.properties.rotation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["coordinates"]) -> 'PersonIdImagePatchRequestCoordinates': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["imageType", "rotation", "coordinates", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["imageType"]) -> typing.Union[MetaOapg.properties.imageType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rotation"]) -> typing.Union[MetaOapg.properties.rotation, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["coordinates"]) -> typing.Union['PersonIdImagePatchRequestCoordinates', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["imageType", "rotation", "coordinates", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        imageType: typing.Union[MetaOapg.properties.imageType, str, schemas.Unset] = schemas.unset,
        rotation: typing.Union[MetaOapg.properties.rotation, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        coordinates: typing.Union['PersonIdImagePatchRequestCoordinates', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PersonIdImagePatchRequest':
        return super().__new__(
            cls,
            *args,
            imageType=imageType,
            rotation=rotation,
            coordinates=coordinates,
            _configuration=_configuration,
            **kwargs,
        )

from intelli_hr_python_sdk.model.person_id_image_patch_request_coordinates import PersonIdImagePatchRequestCoordinates
