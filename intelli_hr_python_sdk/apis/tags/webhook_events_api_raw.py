# coding: utf-8

"""
    intelliHR Public API

    You can find developer's guide and more documentation on [https://developers.intellihr.io](https://developers.intellihr.io)

    The version of the OpenAPI document: V1
    Contact: support@intellihr.co
    Generated by: https://konfigthis.com
"""

from intelli_hr_python_sdk.paths.webhook_events_id.get import FindEventByIdRaw
from intelli_hr_python_sdk.paths.webhook_events.get import ListAllEventsRaw


class WebhookEventsApiRaw(
    FindEventByIdRaw,
    ListAllEventsRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
