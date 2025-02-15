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


class WorkflowsPatchRequestWorkflowFormDesigns(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    Information about the Workflow Form Designs within this [Workflow](https://developers.intellihr.io/docs/v1/).
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['WorkflowsPatchRequestWorkflowFormDesignsItem']:
            return WorkflowsPatchRequestWorkflowFormDesignsItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['WorkflowsPatchRequestWorkflowFormDesignsItem'], typing.List['WorkflowsPatchRequestWorkflowFormDesignsItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'WorkflowsPatchRequestWorkflowFormDesigns':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'WorkflowsPatchRequestWorkflowFormDesignsItem':
        return super().__getitem__(i)

from intelli_hr_python_sdk.model.workflows_patch_request_workflow_form_designs_item import WorkflowsPatchRequestWorkflowFormDesignsItem
