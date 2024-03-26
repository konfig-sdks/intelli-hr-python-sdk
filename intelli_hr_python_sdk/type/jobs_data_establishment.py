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


class RequiredJobsDataEstablishment(TypedDict):
    pass

class OptionalJobsDataEstablishment(TypedDict, total=False):
    # The identifier string for the [Establishment](https://developers.intellihr.io/docs/v1/) of this [Job](https://developers.intellihr.io/docs/v1/).
    id: str

    # Name given to this [Establishment](https://developers.intellihr.io/docs/v1/).
    name: str

    # Link on the public api to get more information on this piece of data.
    link: str

class JobsDataEstablishment(RequiredJobsDataEstablishment, OptionalJobsDataEstablishment):
    pass
