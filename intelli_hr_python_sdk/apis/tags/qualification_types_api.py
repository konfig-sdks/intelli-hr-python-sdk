# coding: utf-8

"""
    intelliHR Public API

    You can find developer's guide and more documentation on [https://developers.intellihr.io](https://developers.intellihr.io)

    The version of the OpenAPI document: V1
    Contact: support@intellihr.co
    Generated by: https://konfigthis.com
"""

from intelli_hr_python_sdk.paths.qualification_types_id.get import FindById
from intelli_hr_python_sdk.paths.qualification_types.get import ListAllQualificationTypes
from intelli_hr_python_sdk.apis.tags.qualification_types_api_raw import QualificationTypesApiRaw


class QualificationTypesApi(
    FindById,
    ListAllQualificationTypes,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: QualificationTypesApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = QualificationTypesApiRaw(api_client)
