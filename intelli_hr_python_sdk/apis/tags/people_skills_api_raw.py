# coding: utf-8

"""
    intelliHR Public API

    You can find developer's guide and more documentation on [https://developers.intellihr.io](https://developers.intellihr.io)

    The version of the OpenAPI document: V1
    Contact: support@intellihr.co
    Generated by: https://konfigthis.com
"""

from intelli_hr_python_sdk.paths.people_person_id_skills.post import AssignSkillToPersonRaw
from intelli_hr_python_sdk.paths.people_person_id_skills_id.delete import DeleteAssignedSkillByIdRaw
from intelli_hr_python_sdk.paths.people_person_id_skills_id.get import FindSkillByIdRaw
from intelli_hr_python_sdk.paths.people_person_id_skills.get import ListPersonSkillsRaw
from intelli_hr_python_sdk.paths.people_person_id_skills_id.patch import UpdateAssignedSkillRaw


class PeopleSkillsApiRaw(
    AssignSkillToPersonRaw,
    DeleteAssignedSkillByIdRaw,
    FindSkillByIdRaw,
    ListPersonSkillsRaw,
    UpdateAssignedSkillRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
