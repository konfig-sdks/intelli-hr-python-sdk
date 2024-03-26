# coding: utf-8

"""
    intelliHR Public API

    You can find developer's guide and more documentation on [https://developers.intellihr.io](https://developers.intellihr.io)

    The version of the OpenAPI document: V1
    Contact: support@intellihr.co
    Generated by: https://konfigthis.com
"""

from intelli_hr_python_sdk.paths.people.post import CreateNewPerson
from intelli_hr_python_sdk.paths.people_id.get import FindById
from intelli_hr_python_sdk.paths.people.get import ListAllPeople
from intelli_hr_python_sdk.paths.people_id.patch import UpdatePersonById
from intelli_hr_python_sdk.apis.tags.people_api_raw import PeopleApiRaw


class PeopleApi(
    CreateNewPerson,
    FindById,
    ListAllPeople,
    UpdatePersonById,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: PeopleApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = PeopleApiRaw(api_client)
