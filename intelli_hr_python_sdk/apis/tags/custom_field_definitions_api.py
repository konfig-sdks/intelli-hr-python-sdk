# coding: utf-8

"""
    intelliHR Public API

    You can find developer's guide and more documentation on [https://developers.intellihr.io](https://developers.intellihr.io)

    The version of the OpenAPI document: V1
    Contact: support@intellihr.co
    Generated by: https://konfigthis.com
"""

from intelli_hr_python_sdk.paths.custom_field_definitions.post import CreateDefinition
from intelli_hr_python_sdk.paths.custom_field_definitions_id.delete import DeleteById
from intelli_hr_python_sdk.paths.custom_field_definitions_id.get import FindDefinitionById
from intelli_hr_python_sdk.paths.custom_field_definitions.get import ListAll
from intelli_hr_python_sdk.paths.custom_field_definitions_id.patch import UpdateDefinitionById
from intelli_hr_python_sdk.apis.tags.custom_field_definitions_api_raw import CustomFieldDefinitionsApiRaw


class CustomFieldDefinitionsApi(
    CreateDefinition,
    DeleteById,
    FindDefinitionById,
    ListAll,
    UpdateDefinitionById,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: CustomFieldDefinitionsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = CustomFieldDefinitionsApiRaw(api_client)
