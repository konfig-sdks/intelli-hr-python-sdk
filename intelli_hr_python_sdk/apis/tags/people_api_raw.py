# coding: utf-8

"""
    intelliHR Public API

    You can find developer's guide and more documentation on [https://developers.intellihr.io](https://developers.intellihr.io)

    The version of the OpenAPI document: V1
    Contact: support@intellihr.co
    Generated by: https://konfigthis.com
"""

from intelli_hr_python_sdk.paths.people.post import CreateNewPersonRaw
from intelli_hr_python_sdk.paths.people_id.get import FindByIdRaw
from intelli_hr_python_sdk.paths.people.get import ListAllPeopleRaw
from intelli_hr_python_sdk.paths.people_id.patch import UpdatePersonByIdRaw


class PeopleApiRaw(
    CreateNewPersonRaw,
    FindByIdRaw,
    ListAllPeopleRaw,
    UpdatePersonByIdRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
