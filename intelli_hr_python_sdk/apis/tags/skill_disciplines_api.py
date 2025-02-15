# coding: utf-8

"""
    intelliHR Public API

    You can find developer's guide and more documentation on [https://developers.intellihr.io](https://developers.intellihr.io)

    The version of the OpenAPI document: V1
    Contact: support@intellihr.co
    Generated by: https://konfigthis.com
"""

from intelli_hr_python_sdk.paths.skill_disciplines.post import CreateNewDiscipline
from intelli_hr_python_sdk.paths.skill_disciplines_id.get import FindById
from intelli_hr_python_sdk.paths.skill_disciplines.get import ListAll
from intelli_hr_python_sdk.paths.skill_disciplines_id.patch import UpdateDisciplineById
from intelli_hr_python_sdk.apis.tags.skill_disciplines_api_raw import SkillDisciplinesApiRaw


class SkillDisciplinesApi(
    CreateNewDiscipline,
    FindById,
    ListAll,
    UpdateDisciplineById,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: SkillDisciplinesApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = SkillDisciplinesApiRaw(api_client)
