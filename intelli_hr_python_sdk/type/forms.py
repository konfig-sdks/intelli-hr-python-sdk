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

from intelli_hr_python_sdk.type.forms_data import FormsData
from intelli_hr_python_sdk.type.forms_meta import FormsMeta

class RequiredForms(TypedDict):
    pass

class OptionalForms(TypedDict, total=False):
    data: FormsData

    meta: FormsMeta

class Forms(RequiredForms, OptionalForms):
    pass
