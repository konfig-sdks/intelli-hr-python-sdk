# coding: utf-8

"""
    intelliHR Public API

    You can find developer's guide and more documentation on [https://developers.intellihr.io](https://developers.intellihr.io)

    The version of the OpenAPI document: V1
    Contact: support@intellihr.co
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel, ConfigDict

from intelli_hr_python_sdk.pydantic.workflow_events_data_workflows import WorkflowEventsDataWorkflows

class WorkflowEventsData(BaseModel):
    # Further descriptive text for this [Workflow Event](https://developers.intellihr.io/docs/v1/).
    description: typing.Optional[str] = Field(None, alias='description')

    # The identifier string for the [Workflow Events](https://developers.intellihr.io/docs/v1/).
    id: typing.Optional[str] = Field(None, alias='id')

    # Name given to this [Workflow Event](https://developers.intellihr.io/docs/v1/). This name would normally be shown to users of the system.
    name: typing.Optional[str] = Field(None, alias='name')

    # Action name given to this [Workflow Event](https://developers.intellihr.io/docs/v1/). This name would normally be shown to users of the system.
    action_name: typing.Optional[str] = Field(None, alias='actionName')

    workflows: typing.Optional[WorkflowEventsDataWorkflows] = Field(None, alias='workflows')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
