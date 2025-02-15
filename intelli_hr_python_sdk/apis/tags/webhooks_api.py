# coding: utf-8

"""
    intelliHR Public API

    You can find developer's guide and more documentation on [https://developers.intellihr.io](https://developers.intellihr.io)

    The version of the OpenAPI document: V1
    Contact: support@intellihr.co
    Generated by: https://konfigthis.com
"""

from intelli_hr_python_sdk.paths.webhooks.post import CreateWebhook
from intelli_hr_python_sdk.paths.webhooks_id.delete import DeleteById
from intelli_hr_python_sdk.paths.webhooks_id.get import FindById
from intelli_hr_python_sdk.paths.webhooks.get import ListAll
from intelli_hr_python_sdk.paths.webhooks_id.patch import UpdateWebhook
from intelli_hr_python_sdk.apis.tags.webhooks_api_raw import WebhooksApiRaw


class WebhooksApi(
    CreateWebhook,
    DeleteById,
    FindById,
    ListAll,
    UpdateWebhook,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: WebhooksApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = WebhooksApiRaw(api_client)
