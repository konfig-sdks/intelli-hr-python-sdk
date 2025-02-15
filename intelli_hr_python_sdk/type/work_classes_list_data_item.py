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

from intelli_hr_python_sdk.type.work_classes_list_data_item_work_type import WorkClassesListDataItemWorkType

class RequiredWorkClassesListDataItem(TypedDict):
    pass

class OptionalWorkClassesListDataItem(TypedDict, total=False):
    # The identifier string for the [Work Class](https://developers.intellihr.io/docs/v1/).
    id: str

    # Name given to this [Work Class](https://developers.intellihr.io/docs/v1/). This name would normally be shown to users of the system.
    name: str

    workType: WorkClassesListDataItemWorkType

    # Specifies whether users can select this [Work Type](https://developers.intellihr.io/docs/v1/) in dropdowns.
    isEnabled: bool

class WorkClassesListDataItem(RequiredWorkClassesListDataItem, OptionalWorkClassesListDataItem):
    pass
