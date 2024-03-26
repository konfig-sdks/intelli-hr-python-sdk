import typing_extensions

from intelli_hr_python_sdk.paths import PathValues
from intelli_hr_python_sdk.apis.paths.business_entities import BusinessEntities
from intelli_hr_python_sdk.apis.paths.business_entities_id import BusinessEntitiesId
from intelli_hr_python_sdk.apis.paths.business_units import BusinessUnits
from intelli_hr_python_sdk.apis.paths.business_units_id import BusinessUnitsId
from intelli_hr_python_sdk.apis.paths.custom_field_definitions import CustomFieldDefinitions
from intelli_hr_python_sdk.apis.paths.custom_field_definitions_id import CustomFieldDefinitionsId
from intelli_hr_python_sdk.apis.paths.default_remuneration_components import DefaultRemunerationComponents
from intelli_hr_python_sdk.apis.paths.default_remuneration_components_id import DefaultRemunerationComponentsId
from intelli_hr_python_sdk.apis.paths.employment_conditions import EmploymentConditions
from intelli_hr_python_sdk.apis.paths.employment_conditions_id import EmploymentConditionsId
from intelli_hr_python_sdk.apis.paths.extended_leave import ExtendedLeave
from intelli_hr_python_sdk.apis.paths.extended_leave_id import ExtendedLeaveId
from intelli_hr_python_sdk.apis.paths.extended_leave_types import ExtendedLeaveTypes
from intelli_hr_python_sdk.apis.paths.extended_leave_types_id import ExtendedLeaveTypesId
from intelli_hr_python_sdk.apis.paths.forms_id import FormsId
from intelli_hr_python_sdk.apis.paths.job_change_reasons import JobChangeReasons
from intelli_hr_python_sdk.apis.paths.job_change_reasons_id import JobChangeReasonsId
from intelli_hr_python_sdk.apis.paths.job_requirement_groups import JobRequirementGroups
from intelli_hr_python_sdk.apis.paths.job_requirement_groups_id import JobRequirementGroupsId
from intelli_hr_python_sdk.apis.paths.job_end_id import JobEndId
from intelli_hr_python_sdk.apis.paths.jobs import Jobs
from intelli_hr_python_sdk.apis.paths.jobs_id import JobsId
from intelli_hr_python_sdk.apis.paths.jobs_job_id_timeline import JobsJobIdTimeline
from intelli_hr_python_sdk.apis.paths.locations import Locations
from intelli_hr_python_sdk.apis.paths.locations_id import LocationsId
from intelli_hr_python_sdk.apis.paths.pay_grades import PayGrades
from intelli_hr_python_sdk.apis.paths.pay_grades_id import PayGradesId
from intelli_hr_python_sdk.apis.paths.people import People
from intelli_hr_python_sdk.apis.paths.people_id import PeopleId
from intelli_hr_python_sdk.apis.paths.people_person_id_images import PeoplePersonIdImages
from intelli_hr_python_sdk.apis.paths.people_person_id_skills import PeoplePersonIdSkills
from intelli_hr_python_sdk.apis.paths.people_person_id_skills_id import PeoplePersonIdSkillsId
from intelli_hr_python_sdk.apis.paths.permission_groups import PermissionGroups
from intelli_hr_python_sdk.apis.paths.permission_groups_id import PermissionGroupsId
from intelli_hr_python_sdk.apis.paths.people_person_id_documents import PeoplePersonIdDocuments
from intelli_hr_python_sdk.apis.paths.people_person_id_documents_id import PeoplePersonIdDocumentsId
from intelli_hr_python_sdk.apis.paths.person_documents import PersonDocuments
from intelli_hr_python_sdk.apis.paths.person_documents_id import PersonDocumentsId
from intelli_hr_python_sdk.apis.paths.position_titles import PositionTitles
from intelli_hr_python_sdk.apis.paths.position_titles_id import PositionTitlesId
from intelli_hr_python_sdk.apis.paths.qualifications import Qualifications
from intelli_hr_python_sdk.apis.paths.qualifications_id import QualificationsId
from intelli_hr_python_sdk.apis.paths.qualification_statuses_id import QualificationStatusesId
from intelli_hr_python_sdk.apis.paths.qualification_library_items import QualificationLibraryItems
from intelli_hr_python_sdk.apis.paths.qualification_library_items_id import QualificationLibraryItemsId
from intelli_hr_python_sdk.apis.paths.qualification_types import QualificationTypes
from intelli_hr_python_sdk.apis.paths.qualification_types_id import QualificationTypesId
from intelli_hr_python_sdk.apis.paths.recruitment_sources import RecruitmentSources
from intelli_hr_python_sdk.apis.paths.recruitment_sources_id import RecruitmentSourcesId
from intelli_hr_python_sdk.apis.paths.representative_types import RepresentativeTypes
from intelli_hr_python_sdk.apis.paths.representative_types_id import RepresentativeTypesId
from intelli_hr_python_sdk.apis.paths.skills import Skills
from intelli_hr_python_sdk.apis.paths.skills_id import SkillsId
from intelli_hr_python_sdk.apis.paths.skill_disciplines import SkillDisciplines
from intelli_hr_python_sdk.apis.paths.skill_disciplines_id import SkillDisciplinesId
from intelli_hr_python_sdk.apis.paths.training_providers import TrainingProviders
from intelli_hr_python_sdk.apis.paths.training_providers_id import TrainingProvidersId
from intelli_hr_python_sdk.apis.paths.trainings import Trainings
from intelli_hr_python_sdk.apis.paths.trainings_id import TrainingsId
from intelli_hr_python_sdk.apis.paths.training_statuses import TrainingStatuses
from intelli_hr_python_sdk.apis.paths.training_types import TrainingTypes
from intelli_hr_python_sdk.apis.paths.training_types_id import TrainingTypesId
from intelli_hr_python_sdk.apis.paths.users import Users
from intelli_hr_python_sdk.apis.paths.users_id import UsersId
from intelli_hr_python_sdk.apis.paths.work_classes import WorkClasses
from intelli_hr_python_sdk.apis.paths.work_classes_id import WorkClassesId
from intelli_hr_python_sdk.apis.paths.workflow_events_id import WorkflowEventsId
from intelli_hr_python_sdk.apis.paths.workflows_id import WorkflowsId
from intelli_hr_python_sdk.apis.paths.work_rights import WorkRights
from intelli_hr_python_sdk.apis.paths.work_rights_id import WorkRightsId
from intelli_hr_python_sdk.apis.paths.work_types import WorkTypes
from intelli_hr_python_sdk.apis.paths.work_types_id import WorkTypesId
from intelli_hr_python_sdk.apis.paths.webhook_events import WebhookEvents
from intelli_hr_python_sdk.apis.paths.webhook_events_id import WebhookEventsId
from intelli_hr_python_sdk.apis.paths.webhooks import Webhooks
from intelli_hr_python_sdk.apis.paths.webhooks_id import WebhooksId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.BUSINESSENTITIES: BusinessEntities,
        PathValues.BUSINESSENTITIES_ID: BusinessEntitiesId,
        PathValues.BUSINESSUNITS: BusinessUnits,
        PathValues.BUSINESSUNITS_ID: BusinessUnitsId,
        PathValues.CUSTOMFIELDDEFINITIONS: CustomFieldDefinitions,
        PathValues.CUSTOMFIELDDEFINITIONS_ID: CustomFieldDefinitionsId,
        PathValues.DEFAULTREMUNERATIONCOMPONENTS: DefaultRemunerationComponents,
        PathValues.DEFAULTREMUNERATIONCOMPONENTS_ID: DefaultRemunerationComponentsId,
        PathValues.EMPLOYMENTCONDITIONS: EmploymentConditions,
        PathValues.EMPLOYMENTCONDITIONS_ID: EmploymentConditionsId,
        PathValues.EXTENDEDLEAVE: ExtendedLeave,
        PathValues.EXTENDEDLEAVE_ID: ExtendedLeaveId,
        PathValues.EXTENDEDLEAVETYPES: ExtendedLeaveTypes,
        PathValues.EXTENDEDLEAVETYPES_ID: ExtendedLeaveTypesId,
        PathValues.FORMS_ID: FormsId,
        PathValues.JOBCHANGEREASONS: JobChangeReasons,
        PathValues.JOBCHANGEREASONS_ID: JobChangeReasonsId,
        PathValues.JOBREQUIREMENTGROUPS: JobRequirementGroups,
        PathValues.JOBREQUIREMENTGROUPS_ID: JobRequirementGroupsId,
        PathValues.JOBEND_ID: JobEndId,
        PathValues.JOBS: Jobs,
        PathValues.JOBS_ID: JobsId,
        PathValues.JOBS_JOB_ID_TIMELINE: JobsJobIdTimeline,
        PathValues.LOCATIONS: Locations,
        PathValues.LOCATIONS_ID: LocationsId,
        PathValues.PAYGRADES: PayGrades,
        PathValues.PAYGRADES_ID: PayGradesId,
        PathValues.PEOPLE: People,
        PathValues.PEOPLE_ID: PeopleId,
        PathValues.PEOPLE_PERSON_ID_IMAGES: PeoplePersonIdImages,
        PathValues.PEOPLE_PERSON_ID_SKILLS: PeoplePersonIdSkills,
        PathValues.PEOPLE_PERSON_ID_SKILLS_ID: PeoplePersonIdSkillsId,
        PathValues.PERMISSIONGROUPS: PermissionGroups,
        PathValues.PERMISSIONGROUPS_ID: PermissionGroupsId,
        PathValues.PEOPLE_PERSON_ID_DOCUMENTS: PeoplePersonIdDocuments,
        PathValues.PEOPLE_PERSON_ID_DOCUMENTS_ID: PeoplePersonIdDocumentsId,
        PathValues.PERSONDOCUMENTS: PersonDocuments,
        PathValues.PERSONDOCUMENTS_ID: PersonDocumentsId,
        PathValues.POSITIONTITLES: PositionTitles,
        PathValues.POSITIONTITLES_ID: PositionTitlesId,
        PathValues.QUALIFICATIONS: Qualifications,
        PathValues.QUALIFICATIONS_ID: QualificationsId,
        PathValues.QUALIFICATIONSTATUSES_ID: QualificationStatusesId,
        PathValues.QUALIFICATIONLIBRARYITEMS: QualificationLibraryItems,
        PathValues.QUALIFICATIONLIBRARYITEMS_ID: QualificationLibraryItemsId,
        PathValues.QUALIFICATIONTYPES: QualificationTypes,
        PathValues.QUALIFICATIONTYPES_ID: QualificationTypesId,
        PathValues.RECRUITMENTSOURCES: RecruitmentSources,
        PathValues.RECRUITMENTSOURCES_ID: RecruitmentSourcesId,
        PathValues.REPRESENTATIVETYPES: RepresentativeTypes,
        PathValues.REPRESENTATIVETYPES_ID: RepresentativeTypesId,
        PathValues.SKILLS: Skills,
        PathValues.SKILLS_ID: SkillsId,
        PathValues.SKILLDISCIPLINES: SkillDisciplines,
        PathValues.SKILLDISCIPLINES_ID: SkillDisciplinesId,
        PathValues.TRAININGPROVIDERS: TrainingProviders,
        PathValues.TRAININGPROVIDERS_ID: TrainingProvidersId,
        PathValues.TRAININGS: Trainings,
        PathValues.TRAININGS_ID: TrainingsId,
        PathValues.TRAININGSTATUSES: TrainingStatuses,
        PathValues.TRAININGTYPES: TrainingTypes,
        PathValues.TRAININGTYPES_ID: TrainingTypesId,
        PathValues.USERS: Users,
        PathValues.USERS_ID: UsersId,
        PathValues.WORKCLASSES: WorkClasses,
        PathValues.WORKCLASSES_ID: WorkClassesId,
        PathValues.WORKFLOWEVENTS_ID: WorkflowEventsId,
        PathValues.WORKFLOWS_ID: WorkflowsId,
        PathValues.WORKRIGHTS: WorkRights,
        PathValues.WORKRIGHTS_ID: WorkRightsId,
        PathValues.WORKTYPES: WorkTypes,
        PathValues.WORKTYPES_ID: WorkTypesId,
        PathValues.WEBHOOKEVENTS: WebhookEvents,
        PathValues.WEBHOOKEVENTS_ID: WebhookEventsId,
        PathValues.WEBHOOKS: Webhooks,
        PathValues.WEBHOOKS_ID: WebhooksId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.BUSINESSENTITIES: BusinessEntities,
        PathValues.BUSINESSENTITIES_ID: BusinessEntitiesId,
        PathValues.BUSINESSUNITS: BusinessUnits,
        PathValues.BUSINESSUNITS_ID: BusinessUnitsId,
        PathValues.CUSTOMFIELDDEFINITIONS: CustomFieldDefinitions,
        PathValues.CUSTOMFIELDDEFINITIONS_ID: CustomFieldDefinitionsId,
        PathValues.DEFAULTREMUNERATIONCOMPONENTS: DefaultRemunerationComponents,
        PathValues.DEFAULTREMUNERATIONCOMPONENTS_ID: DefaultRemunerationComponentsId,
        PathValues.EMPLOYMENTCONDITIONS: EmploymentConditions,
        PathValues.EMPLOYMENTCONDITIONS_ID: EmploymentConditionsId,
        PathValues.EXTENDEDLEAVE: ExtendedLeave,
        PathValues.EXTENDEDLEAVE_ID: ExtendedLeaveId,
        PathValues.EXTENDEDLEAVETYPES: ExtendedLeaveTypes,
        PathValues.EXTENDEDLEAVETYPES_ID: ExtendedLeaveTypesId,
        PathValues.FORMS_ID: FormsId,
        PathValues.JOBCHANGEREASONS: JobChangeReasons,
        PathValues.JOBCHANGEREASONS_ID: JobChangeReasonsId,
        PathValues.JOBREQUIREMENTGROUPS: JobRequirementGroups,
        PathValues.JOBREQUIREMENTGROUPS_ID: JobRequirementGroupsId,
        PathValues.JOBEND_ID: JobEndId,
        PathValues.JOBS: Jobs,
        PathValues.JOBS_ID: JobsId,
        PathValues.JOBS_JOB_ID_TIMELINE: JobsJobIdTimeline,
        PathValues.LOCATIONS: Locations,
        PathValues.LOCATIONS_ID: LocationsId,
        PathValues.PAYGRADES: PayGrades,
        PathValues.PAYGRADES_ID: PayGradesId,
        PathValues.PEOPLE: People,
        PathValues.PEOPLE_ID: PeopleId,
        PathValues.PEOPLE_PERSON_ID_IMAGES: PeoplePersonIdImages,
        PathValues.PEOPLE_PERSON_ID_SKILLS: PeoplePersonIdSkills,
        PathValues.PEOPLE_PERSON_ID_SKILLS_ID: PeoplePersonIdSkillsId,
        PathValues.PERMISSIONGROUPS: PermissionGroups,
        PathValues.PERMISSIONGROUPS_ID: PermissionGroupsId,
        PathValues.PEOPLE_PERSON_ID_DOCUMENTS: PeoplePersonIdDocuments,
        PathValues.PEOPLE_PERSON_ID_DOCUMENTS_ID: PeoplePersonIdDocumentsId,
        PathValues.PERSONDOCUMENTS: PersonDocuments,
        PathValues.PERSONDOCUMENTS_ID: PersonDocumentsId,
        PathValues.POSITIONTITLES: PositionTitles,
        PathValues.POSITIONTITLES_ID: PositionTitlesId,
        PathValues.QUALIFICATIONS: Qualifications,
        PathValues.QUALIFICATIONS_ID: QualificationsId,
        PathValues.QUALIFICATIONSTATUSES_ID: QualificationStatusesId,
        PathValues.QUALIFICATIONLIBRARYITEMS: QualificationLibraryItems,
        PathValues.QUALIFICATIONLIBRARYITEMS_ID: QualificationLibraryItemsId,
        PathValues.QUALIFICATIONTYPES: QualificationTypes,
        PathValues.QUALIFICATIONTYPES_ID: QualificationTypesId,
        PathValues.RECRUITMENTSOURCES: RecruitmentSources,
        PathValues.RECRUITMENTSOURCES_ID: RecruitmentSourcesId,
        PathValues.REPRESENTATIVETYPES: RepresentativeTypes,
        PathValues.REPRESENTATIVETYPES_ID: RepresentativeTypesId,
        PathValues.SKILLS: Skills,
        PathValues.SKILLS_ID: SkillsId,
        PathValues.SKILLDISCIPLINES: SkillDisciplines,
        PathValues.SKILLDISCIPLINES_ID: SkillDisciplinesId,
        PathValues.TRAININGPROVIDERS: TrainingProviders,
        PathValues.TRAININGPROVIDERS_ID: TrainingProvidersId,
        PathValues.TRAININGS: Trainings,
        PathValues.TRAININGS_ID: TrainingsId,
        PathValues.TRAININGSTATUSES: TrainingStatuses,
        PathValues.TRAININGTYPES: TrainingTypes,
        PathValues.TRAININGTYPES_ID: TrainingTypesId,
        PathValues.USERS: Users,
        PathValues.USERS_ID: UsersId,
        PathValues.WORKCLASSES: WorkClasses,
        PathValues.WORKCLASSES_ID: WorkClassesId,
        PathValues.WORKFLOWEVENTS_ID: WorkflowEventsId,
        PathValues.WORKFLOWS_ID: WorkflowsId,
        PathValues.WORKRIGHTS: WorkRights,
        PathValues.WORKRIGHTS_ID: WorkRightsId,
        PathValues.WORKTYPES: WorkTypes,
        PathValues.WORKTYPES_ID: WorkTypesId,
        PathValues.WEBHOOKEVENTS: WebhookEvents,
        PathValues.WEBHOOKEVENTS_ID: WebhookEventsId,
        PathValues.WEBHOOKS: Webhooks,
        PathValues.WEBHOOKS_ID: WebhooksId,
    }
)
