# coding: utf-8

"""
    intelliHR Public API

    You can find developer's guide and more documentation on [https://developers.intellihr.io](https://developers.intellihr.io)

    The version of the OpenAPI document: V1
    Contact: support@intellihr.co
    Generated by: https://konfigthis.com
"""

from intelli_hr_python_sdk.paths.job_end_id.delete import CancelEndDate
from intelli_hr_python_sdk.paths.job_end_id.patch import JobFinalize
from intelli_hr_python_sdk.apis.tags.end_job_api_raw import EndJobApiRaw


class EndJobApi(
    CancelEndDate,
    JobFinalize,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: EndJobApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = EndJobApiRaw(api_client)
