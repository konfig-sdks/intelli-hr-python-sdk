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

from intelli_hr_python_sdk.pydantic.job_requirement_groups_data_library_items import JobRequirementGroupsDataLibraryItems

class JobRequirementGroupsData(BaseModel):
    # The identifier string for the [Job Requirement Group](https://developers.intellihr.io/docs/v1/).
    id: typing.Optional[str] = Field(None, alias='id')

    # The issue date of the [Job Requirement Group](https://developers.intellihr.io/docs/v1/)
    name: typing.Optional[str] = Field(None, alias='name')

    library_items: typing.Optional[JobRequirementGroupsDataLibraryItems] = Field(None, alias='libraryItems')

    # The count of how many times this job requirement group is being used in job requirements
    job_requirement_usage_count: typing.Optional[typing.Union[int, float]] = Field(None, alias='jobRequirementUsageCount')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
