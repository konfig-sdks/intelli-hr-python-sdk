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


class RequiredJobEndPatchRequest(TypedDict):
    pass

class OptionalJobEndPatchRequest(TypedDict, total=False):
    # The <b>exclusive</b> date this [Job](https://developers.intellihr.io/docs/v1/) ended or will end within the organisation. For example, if the person's last working date is on 2025-04-23, the `endDate` should be set as 2025-04-24 to reflect the exclusive date. Required if not finalising an end date, or the job does not have an end date. This date will follow the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6).   YYYY-MM-DD date formatting is also supported, although by using this format the date will be stored as the start of day in UTC time, not the requesting tenants timezone.
    endDate: str

    # The identifier string for the [Job](https://developers.intellihr.io/docs/v1/) of the person that the direct report will be reassigned to.
    reassignDirectReportsTo: str

    # The type of turnover this end of job would be classified as: `voluntary`, `involuntary` or `unknown`. Required if finalising an end date.
    turnoverType: str

    # The name of the turnover reason.
    turnoverReason: str

class JobEndPatchRequest(RequiredJobEndPatchRequest, OptionalJobEndPatchRequest):
    pass
