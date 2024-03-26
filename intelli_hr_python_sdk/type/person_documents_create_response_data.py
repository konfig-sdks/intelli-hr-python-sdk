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


class RequiredPersonDocumentsCreateResponseData(TypedDict):
    pass

class OptionalPersonDocumentsCreateResponseData(TypedDict, total=False):
    # The identifier string for the [Person Document](https://developers.intellihr.io/docs/v1/).
    id: str

    # The identifier string for the [Person](https://developers.intellihr.io/docs/v1/) to whom this [Document](https://developers.intellihr.io/docs/v1/) belongs.
    personId: str

    # The presigned upload URL which enables you to upload a [Person Document](https://developers.intellihr.io/docs/v1/) to S3. This link will expire 20 minutes after creation. Instructions on how to upload an object with a presigned S3 URL can be found [here](https://docs.aws.amazon.com/AmazonS3/latest/dev/PresignedUrlUploadObject.html)
    presignedUploadUrl: str

class PersonDocumentsCreateResponseData(RequiredPersonDocumentsCreateResponseData, OptionalPersonDocumentsCreateResponseData):
    pass
