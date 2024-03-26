import typing_extensions

from intelli_hr_python_sdk.apis.tags import TagValues
from intelli_hr_python_sdk.apis.tags.business_entities_api import BusinessEntitiesApi
from intelli_hr_python_sdk.apis.tags.business_units_api import BusinessUnitsApi
from intelli_hr_python_sdk.apis.tags.custom_field_definitions_api import CustomFieldDefinitionsApi
from intelli_hr_python_sdk.apis.tags.job_change_reasons_api import JobChangeReasonsApi
from intelli_hr_python_sdk.apis.tags.job_requirement_groups_api import JobRequirementGroupsApi
from intelli_hr_python_sdk.apis.tags.locations_api import LocationsApi
from intelli_hr_python_sdk.apis.tags.pay_grades_api import PayGradesApi
from intelli_hr_python_sdk.apis.tags.people_skills_api import PeopleSkillsApi
from intelli_hr_python_sdk.apis.tags.qualification_instances_api import QualificationInstancesApi
from intelli_hr_python_sdk.apis.tags.qualification_library_items_api import QualificationLibraryItemsApi
from intelli_hr_python_sdk.apis.tags.trainings_api import TrainingsApi
from intelli_hr_python_sdk.apis.tags.webhooks_api import WebhooksApi
from intelli_hr_python_sdk.apis.tags.jobs_api import JobsApi
from intelli_hr_python_sdk.apis.tags.people_api import PeopleApi
from intelli_hr_python_sdk.apis.tags.position_titles_api import PositionTitlesApi
from intelli_hr_python_sdk.apis.tags.skills_api import SkillsApi
from intelli_hr_python_sdk.apis.tags.skill_disciplines_api import SkillDisciplinesApi
from intelli_hr_python_sdk.apis.tags.users_api import UsersApi
from intelli_hr_python_sdk.apis.tags.people_images_api import PeopleImagesApi
from intelli_hr_python_sdk.apis.tags.people_documents_api import PeopleDocumentsApi
from intelli_hr_python_sdk.apis.tags.default_remuneration_components_api import DefaultRemunerationComponentsApi
from intelli_hr_python_sdk.apis.tags.employment_conditions_api import EmploymentConditionsApi
from intelli_hr_python_sdk.apis.tags.extended_leave_api import ExtendedLeaveApi
from intelli_hr_python_sdk.apis.tags.extended_leave_types_api import ExtendedLeaveTypesApi
from intelli_hr_python_sdk.apis.tags.end_job_api import EndJobApi
from intelli_hr_python_sdk.apis.tags.permission_groups_api import PermissionGroupsApi
from intelli_hr_python_sdk.apis.tags.person_documents_deprecated_api import PersonDocumentsDeprecatedApi
from intelli_hr_python_sdk.apis.tags.qualification_types_api import QualificationTypesApi
from intelli_hr_python_sdk.apis.tags.recruitment_sources_api import RecruitmentSourcesApi
from intelli_hr_python_sdk.apis.tags.representative_types_api import RepresentativeTypesApi
from intelli_hr_python_sdk.apis.tags.training_providers_api import TrainingProvidersApi
from intelli_hr_python_sdk.apis.tags.training_types_api import TrainingTypesApi
from intelli_hr_python_sdk.apis.tags.work_classes_api import WorkClassesApi
from intelli_hr_python_sdk.apis.tags.work_rights_api import WorkRightsApi
from intelli_hr_python_sdk.apis.tags.work_types_api import WorkTypesApi
from intelli_hr_python_sdk.apis.tags.webhook_events_api import WebhookEventsApi
from intelli_hr_python_sdk.apis.tags.forms_api import FormsApi
from intelli_hr_python_sdk.apis.tags.job_timeline_api import JobTimelineApi
from intelli_hr_python_sdk.apis.tags.qualification_statuses_api import QualificationStatusesApi
from intelli_hr_python_sdk.apis.tags.training_statuses_api import TrainingStatusesApi
from intelli_hr_python_sdk.apis.tags.workflow_events_api import WorkflowEventsApi
from intelli_hr_python_sdk.apis.tags.workflows_api import WorkflowsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.BUSINESS_ENTITIES: BusinessEntitiesApi,
        TagValues.BUSINESS_UNITS: BusinessUnitsApi,
        TagValues.CUSTOM_FIELD_DEFINITIONS: CustomFieldDefinitionsApi,
        TagValues.JOB_CHANGE_REASONS: JobChangeReasonsApi,
        TagValues.JOB_REQUIREMENT_GROUPS: JobRequirementGroupsApi,
        TagValues.LOCATIONS: LocationsApi,
        TagValues.PAY_GRADES: PayGradesApi,
        TagValues.PEOPLE_SKILLS: PeopleSkillsApi,
        TagValues.QUALIFICATION_INSTANCES: QualificationInstancesApi,
        TagValues.QUALIFICATION_LIBRARY_ITEMS: QualificationLibraryItemsApi,
        TagValues.TRAININGS: TrainingsApi,
        TagValues.WEBHOOKS: WebhooksApi,
        TagValues.JOBS: JobsApi,
        TagValues.PEOPLE: PeopleApi,
        TagValues.POSITION_TITLES: PositionTitlesApi,
        TagValues.SKILLS: SkillsApi,
        TagValues.SKILL_DISCIPLINES: SkillDisciplinesApi,
        TagValues.USERS: UsersApi,
        TagValues.PEOPLE_IMAGES: PeopleImagesApi,
        TagValues.PEOPLE_DOCUMENTS: PeopleDocumentsApi,
        TagValues.DEFAULT_REMUNERATION_COMPONENTS: DefaultRemunerationComponentsApi,
        TagValues.EMPLOYMENT_CONDITIONS: EmploymentConditionsApi,
        TagValues.EXTENDED_LEAVE: ExtendedLeaveApi,
        TagValues.EXTENDED_LEAVE_TYPES: ExtendedLeaveTypesApi,
        TagValues.END_JOB: EndJobApi,
        TagValues.PERMISSION_GROUPS: PermissionGroupsApi,
        TagValues.PERSON_DOCUMENTS_DEPRECATED: PersonDocumentsDeprecatedApi,
        TagValues.QUALIFICATION_TYPES: QualificationTypesApi,
        TagValues.RECRUITMENT_SOURCES: RecruitmentSourcesApi,
        TagValues.REPRESENTATIVE_TYPES: RepresentativeTypesApi,
        TagValues.TRAINING_PROVIDERS: TrainingProvidersApi,
        TagValues.TRAINING_TYPES: TrainingTypesApi,
        TagValues.WORK_CLASSES: WorkClassesApi,
        TagValues.WORK_RIGHTS: WorkRightsApi,
        TagValues.WORK_TYPES: WorkTypesApi,
        TagValues.WEBHOOK_EVENTS: WebhookEventsApi,
        TagValues.FORMS: FormsApi,
        TagValues.JOB_TIMELINE: JobTimelineApi,
        TagValues.QUALIFICATION_STATUSES: QualificationStatusesApi,
        TagValues.TRAINING_STATUSES: TrainingStatusesApi,
        TagValues.WORKFLOW_EVENTS: WorkflowEventsApi,
        TagValues.WORKFLOWS: WorkflowsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.BUSINESS_ENTITIES: BusinessEntitiesApi,
        TagValues.BUSINESS_UNITS: BusinessUnitsApi,
        TagValues.CUSTOM_FIELD_DEFINITIONS: CustomFieldDefinitionsApi,
        TagValues.JOB_CHANGE_REASONS: JobChangeReasonsApi,
        TagValues.JOB_REQUIREMENT_GROUPS: JobRequirementGroupsApi,
        TagValues.LOCATIONS: LocationsApi,
        TagValues.PAY_GRADES: PayGradesApi,
        TagValues.PEOPLE_SKILLS: PeopleSkillsApi,
        TagValues.QUALIFICATION_INSTANCES: QualificationInstancesApi,
        TagValues.QUALIFICATION_LIBRARY_ITEMS: QualificationLibraryItemsApi,
        TagValues.TRAININGS: TrainingsApi,
        TagValues.WEBHOOKS: WebhooksApi,
        TagValues.JOBS: JobsApi,
        TagValues.PEOPLE: PeopleApi,
        TagValues.POSITION_TITLES: PositionTitlesApi,
        TagValues.SKILLS: SkillsApi,
        TagValues.SKILL_DISCIPLINES: SkillDisciplinesApi,
        TagValues.USERS: UsersApi,
        TagValues.PEOPLE_IMAGES: PeopleImagesApi,
        TagValues.PEOPLE_DOCUMENTS: PeopleDocumentsApi,
        TagValues.DEFAULT_REMUNERATION_COMPONENTS: DefaultRemunerationComponentsApi,
        TagValues.EMPLOYMENT_CONDITIONS: EmploymentConditionsApi,
        TagValues.EXTENDED_LEAVE: ExtendedLeaveApi,
        TagValues.EXTENDED_LEAVE_TYPES: ExtendedLeaveTypesApi,
        TagValues.END_JOB: EndJobApi,
        TagValues.PERMISSION_GROUPS: PermissionGroupsApi,
        TagValues.PERSON_DOCUMENTS_DEPRECATED: PersonDocumentsDeprecatedApi,
        TagValues.QUALIFICATION_TYPES: QualificationTypesApi,
        TagValues.RECRUITMENT_SOURCES: RecruitmentSourcesApi,
        TagValues.REPRESENTATIVE_TYPES: RepresentativeTypesApi,
        TagValues.TRAINING_PROVIDERS: TrainingProvidersApi,
        TagValues.TRAINING_TYPES: TrainingTypesApi,
        TagValues.WORK_CLASSES: WorkClassesApi,
        TagValues.WORK_RIGHTS: WorkRightsApi,
        TagValues.WORK_TYPES: WorkTypesApi,
        TagValues.WEBHOOK_EVENTS: WebhookEventsApi,
        TagValues.FORMS: FormsApi,
        TagValues.JOB_TIMELINE: JobTimelineApi,
        TagValues.QUALIFICATION_STATUSES: QualificationStatusesApi,
        TagValues.TRAINING_STATUSES: TrainingStatusesApi,
        TagValues.WORKFLOW_EVENTS: WorkflowEventsApi,
        TagValues.WORKFLOWS: WorkflowsApi,
    }
)
