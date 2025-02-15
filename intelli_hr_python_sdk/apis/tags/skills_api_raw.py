# coding: utf-8

"""
    intelliHR Public API

    You can find developer's guide and more documentation on [https://developers.intellihr.io](https://developers.intellihr.io)

    The version of the OpenAPI document: V1
    Contact: support@intellihr.co
    Generated by: https://konfigthis.com
"""

from intelli_hr_python_sdk.paths.skills.post import CreateNewSkillRaw
from intelli_hr_python_sdk.paths.skills_id.get import FindSkillByIdRaw
from intelli_hr_python_sdk.paths.skills.get import GetAllRaw
from intelli_hr_python_sdk.paths.skills_id.patch import UpdateSkillByIdRaw


class SkillsApiRaw(
    CreateNewSkillRaw,
    FindSkillByIdRaw,
    GetAllRaw,
    UpdateSkillByIdRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
