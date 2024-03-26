# coding: utf-8

"""
    intelliHR Public API

    You can find developer's guide and more documentation on [https://developers.intellihr.io](https://developers.intellihr.io)

    The version of the OpenAPI document: V1
    Contact: support@intellihr.co
    Generated by: https://konfigthis.com
"""

from intelli_hr_python_sdk.paths.default_remuneration_components_id.get import FindById
from intelli_hr_python_sdk.paths.default_remuneration_components.get import ListAll
from intelli_hr_python_sdk.apis.tags.default_remuneration_components_api_raw import DefaultRemunerationComponentsApiRaw


class DefaultRemunerationComponentsApi(
    FindById,
    ListAll,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: DefaultRemunerationComponentsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = DefaultRemunerationComponentsApiRaw(api_client)
