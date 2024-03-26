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


class RequiredRecruitmentSourcesListMetaPagination(TypedDict):
    pass

class OptionalRecruitmentSourcesListMetaPagination(TypedDict, total=False):
    # Total items count
    total: int

    # Number of items for current page
    count: int

    # Items per page limit
    per_page: int

    # Current page
    current_page: int

    # Total number of pages
    total_pages: int

class RecruitmentSourcesListMetaPagination(RequiredRecruitmentSourcesListMetaPagination, OptionalRecruitmentSourcesListMetaPagination):
    pass
