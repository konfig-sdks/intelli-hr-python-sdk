operation_parameter_map = {
    '/business-entities-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'code'
            },
            {
                'name': 'legalName'
            },
            {
                'name': 'number'
            },
            {
                'name': 'isEnabled'
            },
            {
                'name': 'customFields'
            },
        ]
    },
    '/business-entities/{id}-DELETE': {
        'parameters': [
        ]
    },
    '/business-entities/{id}-GET': {
        'parameters': [
        ]
    },
    '/business-entities-GET': {
        'parameters': [
        ]
    },
    '/business-entities/{id}-PATCH': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'code'
            },
            {
                'name': 'legalName'
            },
            {
                'name': 'number'
            },
            {
                'name': 'isEnabled'
            },
            {
                'name': 'customFields'
            },
        ]
    },
    '/business-units-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'identifier'
            },
            {
                'name': 'code'
            },
            {
                'name': 'notes'
            },
            {
                'name': 'parentId'
            },
            {
                'name': 'isEnabled'
            },
            {
                'name': 'customFields'
            },
        ]
    },
    '/business-units/{id}-DELETE': {
        'parameters': [
        ]
    },
    '/business-units/{id}-GET': {
        'parameters': [
        ]
    },
    '/business-units-GET': {
        'parameters': [
            {
                'name': 'filters'
            },
        ]
    },
    '/business-units/{id}-PATCH': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'identifier'
            },
            {
                'name': 'code'
            },
            {
                'name': 'notes'
            },
            {
                'name': 'parentId'
            },
            {
                'name': 'isEnabled'
            },
            {
                'name': 'customFields'
            },
        ]
    },
    '/custom-field-definitions-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'apiName'
            },
            {
                'name': 'modelType'
            },
            {
                'name': 'type'
            },
            {
                'name': 'description'
            },
            {
                'name': 'isSensitive'
            },
            {
                'name': 'selectDefinition'
            },
            {
                'name': 'textDefinition'
            },
            {
                'name': 'peopleDropdownDefinition'
            },
        ]
    },
    '/custom-field-definitions/{id}-DELETE': {
        'parameters': [
        ]
    },
    '/custom-field-definitions/{id}-GET': {
        'parameters': [
        ]
    },
    '/custom-field-definitions-GET': {
        'parameters': [
            {
                'name': 'filters'
            },
        ]
    },
    '/custom-field-definitions/{id}-PATCH': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
            {
                'name': 'isEnabled'
            },
            {
                'name': 'isSensitive'
            },
            {
                'name': 'selectDefinition'
            },
            {
                'name': 'peopleDropdownDefinition'
            },
        ]
    },
    '/default-remuneration-components/{id}-GET': {
        'parameters': [
        ]
    },
    '/default-remuneration-components-GET': {
        'parameters': [
        ]
    },
    '/employment-conditions/{id}-GET': {
        'parameters': [
        ]
    },
    '/employment-conditions-GET': {
        'parameters': [
        ]
    },
    '/job-end/{id}-DELETE': {
        'parameters': [
            {
                'name': 'cancelDisablingUserAccount'
            },
        ]
    },
    '/job-end/{id}-PATCH': {
        'parameters': [
            {
                'name': 'endDate'
            },
            {
                'name': 'reassignDirectReportsTo'
            },
            {
                'name': 'turnoverType'
            },
            {
                'name': 'turnoverReason'
            },
            {
                'name': 'shouldNotFinaliseEndDate'
            },
            {
                'name': 'shouldRetainUserAccount'
            },
            {
                'name': 'suppressEvents'
            },
        ]
    },
    '/extended-leave-POST': {
        'parameters': [
            {
                'name': 'jobId'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'leaveType'
            },
            {
                'name': 'fte'
            },
        ]
    },
    '/extended-leave/{id}-PATCH': {
        'parameters': [
            {
                'name': 'jobId'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'shouldNotFinaliseEndDate'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'leaveType'
            },
            {
                'name': 'fte'
            },
        ]
    },
    '/extended-leave-types/{id}-GET': {
        'parameters': [
        ]
    },
    '/extended-leave-types-GET': {
        'parameters': [
        ]
    },
    '/forms/{id}-GET': {
        'parameters': [
        ]
    },
    '/job-change-reasons-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'isEnabled'
            },
        ]
    },
    '/job-change-reasons/{id}-DELETE': {
        'parameters': [
        ]
    },
    '/job-change-reasons/{id}-GET': {
        'parameters': [
        ]
    },
    '/job-change-reasons-GET': {
        'parameters': [
        ]
    },
    '/job-change-reasons/{id}-PATCH': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'isEnabled'
            },
        ]
    },
    '/job-requirement-groups-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'libraryItemIds'
            },
        ]
    },
    '/job-requirement-groups/{id}-DELETE': {
        'parameters': [
        ]
    },
    '/job-requirement-groups/{id}-GET': {
        'parameters': [
        ]
    },
    '/job-requirement-groups-GET': {
        'parameters': [
        ]
    },
    '/job-requirement-groups/{id}-PATCH': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'libraryItemIds'
            },
        ]
    },
    '/jobs/{jobId}/timeline-GET': {
        'parameters': [
            {
                'name': 'jobId'
            },
        ]
    },
    '/jobs-POST': {
        'parameters': [
            {
                'name': 'person'
            },
            {
                'name': 'companyStartDate'
            },
            {
                'name': 'name'
            },
            {
                'name': 'businessEntity'
            },
            {
                'name': 'businessUnit'
            },
            {
                'name': 'workClass'
            },
            {
                'name': 'companyEndDate'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'establishment'
            },
            {
                'name': 'supervisorPerson'
            },
            {
                'name': 'supervisorJob'
            },
            {
                'name': 'location'
            },
            {
                'name': 'workType'
            },
            {
                'name': 'fte'
            },
            {
                'name': 'payGrade'
            },
            {
                'name': 'employmentCondition'
            },
            {
                'name': 'remunerationSchedule'
            },
            {
                'name': 'recruitment'
            },
            {
                'name': 'customFields'
            },
        ]
    },
    '/jobs/{id}-GET': {
        'parameters': [
            {
                'name': 'asAt'
            },
        ]
    },
    '/jobs-GET': {
        'parameters': [
            {
                'name': 'filters'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/jobs/{id}-PATCH': {
        'parameters': [
            {
                'name': 'effectiveFrom'
            },
            {
                'name': 'effectiveTo'
            },
            {
                'name': 'name'
            },
            {
                'name': 'businessEntity'
            },
            {
                'name': 'businessUnit'
            },
            {
                'name': 'establishment'
            },
            {
                'name': 'jobChangeReason'
            },
            {
                'name': 'supervisorPerson'
            },
            {
                'name': 'supervisorJob'
            },
            {
                'name': 'location'
            },
            {
                'name': 'workClass'
            },
            {
                'name': 'workType'
            },
            {
                'name': 'fte'
            },
            {
                'name': 'payGrade'
            },
            {
                'name': 'employmentCondition'
            },
            {
                'name': 'remunerationSchedule'
            },
            {
                'name': 'customFields'
            },
        ]
    },
    '/locations-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'parentId'
            },
            {
                'name': 'code'
            },
            {
                'name': 'address'
            },
            {
                'name': 'isEnabled'
            },
            {
                'name': 'customFields'
            },
        ]
    },
    '/locations/{id}-DELETE': {
        'parameters': [
        ]
    },
    '/locations/{id}-GET': {
        'parameters': [
        ]
    },
    '/locations-GET': {
        'parameters': [
        ]
    },
    '/locations/{id}-PATCH': {
        'parameters': [
            {
                'name': 'parentId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'code'
            },
            {
                'name': 'address'
            },
            {
                'name': 'isEnabled'
            },
            {
                'name': 'customFields'
            },
        ]
    },
    '/pay-grades-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'description'
            },
            {
                'name': 'code'
            },
            {
                'name': 'employmentCondition'
            },
            {
                'name': 'payGradeType'
            },
            {
                'name': 'isOverridable'
            },
            {
                'name': 'permanentHourlyRate'
            },
            {
                'name': 'permanentHourlyRateCurrency'
            },
            {
                'name': 'casualHourlyRate'
            },
            {
                'name': 'casualHourlyRateCurrency'
            },
            {
                'name': 'annualSalary'
            },
            {
                'name': 'annualSalaryCurrency'
            },
            {
                'name': 'paySteps'
            },
        ]
    },
    '/pay-grades/{id}-DELETE': {
        'parameters': [
        ]
    },
    '/pay-grades/{id}-GET': {
        'parameters': [
            {
                'name': 'asAt'
            },
        ]
    },
    '/pay-grades-GET': {
        'parameters': [
            {
                'name': 'asAt'
            },
        ]
    },
    '/pay-grades/{id}-PATCH': {
        'parameters': [
            {
                'name': 'effectiveFrom'
            },
            {
                'name': 'description'
            },
            {
                'name': 'effectiveTo'
            },
            {
                'name': 'isEnabled'
            },
            {
                'name': 'name'
            },
            {
                'name': 'code'
            },
            {
                'name': 'employmentCondition'
            },
            {
                'name': 'payGradeType'
            },
            {
                'name': 'isOverridable'
            },
            {
                'name': 'permanentHourlyRate'
            },
            {
                'name': 'permanentHourlyRateCurrency'
            },
            {
                'name': 'casualHourlyRate'
            },
            {
                'name': 'casualHourlyRateCurrency'
            },
            {
                'name': 'annualSalary'
            },
            {
                'name': 'annualSalaryCurrency'
            },
            {
                'name': 'paySteps'
            },
        ]
    },
    '/people-POST': {
        'parameters': [
            {
                'name': 'lastName'
            },
            {
                'name': 'title'
            },
            {
                'name': 'firstName'
            },
            {
                'name': 'middleName'
            },
            {
                'name': 'preferredName'
            },
            {
                'name': 'dateOfBirth'
            },
            {
                'name': 'gender'
            },
            {
                'name': 'employeeNumber'
            },
            {
                'name': 'emergencyContact'
            },
            {
                'name': 'primaryEmailAddress'
            },
            {
                'name': 'primaryPhoneNumber'
            },
            {
                'name': 'emailAddresses'
            },
            {
                'name': 'phoneNumbers'
            },
            {
                'name': 'addresses'
            },
            {
                'name': 'customFields'
            },
            {
                'name': 'medicalConditions'
            },
            {
                'name': 'workRight'
            },
            {
                'name': 'workRightExpiryDate'
            },
            {
                'name': 'userAccount'
            },
        ]
    },
    '/people/{id}-GET': {
        'parameters': [
        ]
    },
    '/people-GET': {
        'parameters': [
            {
                'name': 'filters'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/people/{id}-PATCH': {
        'parameters': [
            {
                'name': 'title'
            },
            {
                'name': 'firstName'
            },
            {
                'name': 'middleName'
            },
            {
                'name': 'lastName'
            },
            {
                'name': 'preferredName'
            },
            {
                'name': 'dateOfBirth'
            },
            {
                'name': 'gender'
            },
            {
                'name': 'employeeNumber'
            },
            {
                'name': 'emergencyContact'
            },
            {
                'name': 'emailAddresses'
            },
            {
                'name': 'phoneNumbers'
            },
            {
                'name': 'addresses'
            },
            {
                'name': 'customFields'
            },
            {
                'name': 'medicalConditions'
            },
            {
                'name': 'workRight'
            },
            {
                'name': 'workRightExpiryDate'
            },
        ]
    },
    '/people/{personId}/documents-POST': {
        'parameters': [
            {
                'name': 'filename'
            },
            {
                'name': 'mime'
            },
            {
                'name': 'size'
            },
            {
                'name': 'extension'
            },
            {
                'name': 'personId'
            },
        ]
    },
    '/people/{personId}/documents-GET': {
        'parameters': [
            {
                'name': 'personId'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'page'
            },
        ]
    },
    '/people/{personId}/documents/{id}-PATCH': {
        'parameters': [
            {
                'name': 'personId'
            },
            {
                'name': 'filename'
            },
            {
                'name': 'uploadStatus'
            },
        ]
    },
    '/people/{personId}/images-POST': {
        'parameters': [
            {
                'name': 'personId'
            },
            {
                'name': 'imageType'
            },
            {
                'name': 'extension'
            },
        ]
    },
    '/people/{personId}/images-GET': {
        'parameters': [
            {
                'name': 'personId'
            },
            {
                'name': 'imageType'
            },
        ]
    },
    '/people/{personId}/images-PATCH': {
        'parameters': [
            {
                'name': 'personId'
            },
            {
                'name': 'imageType'
            },
            {
                'name': 'rotation'
            },
            {
                'name': 'coordinates'
            },
        ]
    },
    '/people/{personId}/skills-POST': {
        'parameters': [
            {
                'name': 'skillId'
            },
            {
                'name': 'skillLevel'
            },
            {
                'name': 'personId'
            },
        ]
    },
    '/people/{personId}/skills/{id}-DELETE': {
        'parameters': [
            {
                'name': 'personId'
            },
        ]
    },
    '/people/{personId}/skills/{id}-GET': {
        'parameters': [
            {
                'name': 'personId'
            },
        ]
    },
    '/people/{personId}/skills-GET': {
        'parameters': [
            {
                'name': 'personId'
            },
        ]
    },
    '/people/{personId}/skills/{id}-PATCH': {
        'parameters': [
            {
                'name': 'personId'
            },
            {
                'name': 'skillLevel'
            },
        ]
    },
    '/permission-groups/{id}-GET': {
        'parameters': [
        ]
    },
    '/permission-groups-GET': {
        'parameters': [
            {
                'name': 'filters'
            },
        ]
    },
    '/person-documents-POST': {
        'parameters': [
            {
                'name': 'person'
            },
            {
                'name': 'filename'
            },
            {
                'name': 'mime'
            },
            {
                'name': 'size'
            },
            {
                'name': 'extension'
            },
        ]
    },
    '/person-documents/{id}-PATCH': {
        'parameters': [
            {
                'name': 'personId'
            },
            {
                'name': 'filename'
            },
            {
                'name': 'uploadStatus'
            },
        ]
    },
    '/position-titles-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'code'
            },
        ]
    },
    '/position-titles/{id}-DELETE': {
        'parameters': [
        ]
    },
    '/position-titles-GET': {
        'parameters': [
            {
                'name': 'filters'
            },
        ]
    },
    '/position-titles/{id}-PATCH': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'code'
            },
            {
                'name': 'isEnabled'
            },
        ]
    },
    '/qualifications-POST': {
        'parameters': [
            {
                'name': 'personId'
            },
            {
                'name': 'qualificationLibraryItemId'
            },
            {
                'name': 'status'
            },
            {
                'name': 'issuingOrganisation'
            },
            {
                'name': 'registrationNumber'
            },
            {
                'name': 'issueDate'
            },
            {
                'name': 'expiryDate'
            },
            {
                'name': 'expiryNotificationQueuedAt'
            },
            {
                'name': 'notes'
            },
        ]
    },
    '/qualifications/{id}-DELETE': {
        'parameters': [
        ]
    },
    '/qualifications/{id}-GET': {
        'parameters': [
        ]
    },
    '/qualifications-GET': {
        'parameters': [
            {
                'name': 'filters'
            },
        ]
    },
    '/qualifications/{id}-PATCH': {
        'parameters': [
            {
                'name': 'status'
            },
            {
                'name': 'issuingOrganisation'
            },
            {
                'name': 'registrationNumber'
            },
            {
                'name': 'issueDate'
            },
            {
                'name': 'expiryDate'
            },
            {
                'name': 'expiryNotificationQueuedAt'
            },
            {
                'name': 'notes'
            },
        ]
    },
    '/qualification-library-items-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'qualificationTypeId'
            },
            {
                'name': 'qualificationExpiryType'
            },
            {
                'name': 'qualificationRegistrationNumberVisibilityType'
            },
            {
                'name': 'qualificationAttachmentRequirementType'
            },
            {
                'name': 'expiryWarningPeriod'
            },
            {
                'name': 'sendExpiryWarning'
            },
        ]
    },
    '/qualification-library-items/{id}-DELETE': {
        'parameters': [
        ]
    },
    '/qualification-library-items/{id}-GET': {
        'parameters': [
        ]
    },
    '/qualification-library-items-GET': {
        'parameters': [
        ]
    },
    '/qualification-library-items/{id}-PATCH': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'qualificationTypeId'
            },
            {
                'name': 'qualificationExpiryType'
            },
            {
                'name': 'qualificationRegistrationNumberVisibilityType'
            },
            {
                'name': 'qualificationAttachmentRequirementType'
            },
            {
                'name': 'expiryWarningPeriod'
            },
            {
                'name': 'sendExpiryWarning'
            },
        ]
    },
    '/qualification-statuses/{id}-GET': {
        'parameters': [
        ]
    },
    '/qualification-types/{id}-GET': {
        'parameters': [
        ]
    },
    '/qualification-types-GET': {
        'parameters': [
        ]
    },
    '/recruitment-sources/{id}-GET': {
        'parameters': [
        ]
    },
    '/recruitment-sources-GET': {
        'parameters': [
        ]
    },
    '/representative-types/{id}-GET': {
        'parameters': [
        ]
    },
    '/representative-types-GET': {
        'parameters': [
        ]
    },
    '/skill-disciplines-POST': {
        'parameters': [
            {
                'name': 'name'
            },
        ]
    },
    '/skill-disciplines/{id}-GET': {
        'parameters': [
        ]
    },
    '/skill-disciplines-GET': {
        'parameters': [
            {
                'name': 'filters'
            },
        ]
    },
    '/skill-disciplines/{id}-PATCH': {
        'parameters': [
            {
                'name': 'name'
            },
        ]
    },
    '/skills-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
            {
                'name': 'isBusinessCritical'
            },
            {
                'name': 'skillDisciplineId'
            },
        ]
    },
    '/skills/{id}-GET': {
        'parameters': [
        ]
    },
    '/skills-GET': {
        'parameters': [
            {
                'name': 'filters'
            },
        ]
    },
    '/skills/{id}-PATCH': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
            {
                'name': 'isBusinessCritical'
            },
            {
                'name': 'skillDisciplineId'
            },
        ]
    },
    '/training-providers/{id}-GET': {
        'parameters': [
        ]
    },
    '/training-providers-GET': {
        'parameters': [
        ]
    },
    '/training-statuses-GET': {
        'parameters': [
        ]
    },
    '/training-types/{id}-GET': {
        'parameters': [
        ]
    },
    '/training-types-GET': {
        'parameters': [
        ]
    },
    '/trainings-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'person'
            },
            {
                'name': 'coordinatorPerson'
            },
            {
                'name': 'completionDate'
            },
            {
                'name': 'cost'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'hours'
            },
            {
                'name': 'job'
            },
            {
                'name': 'provider'
            },
            {
                'name': 'type'
            },
            {
                'name': 'customFields'
            },
            {
                'name': 'status'
            },
        ]
    },
    '/trainings/{id}-DELETE': {
        'parameters': [
        ]
    },
    '/trainings/{id}-GET': {
        'parameters': [
        ]
    },
    '/trainings-GET': {
        'parameters': [
            {
                'name': 'filters'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/trainings/{id}-PATCH': {
        'parameters': [
            {
                'name': 'coordinatorPerson'
            },
            {
                'name': 'completionDate'
            },
            {
                'name': 'cost'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'hours'
            },
            {
                'name': 'job'
            },
            {
                'name': 'name'
            },
            {
                'name': 'person'
            },
            {
                'name': 'provider'
            },
            {
                'name': 'type'
            },
            {
                'name': 'customFields'
            },
            {
                'name': 'status'
            },
        ]
    },
    '/users-POST': {
        'parameters': [
            {
                'name': 'username'
            },
            {
                'name': 'person'
            },
            {
                'name': 'isEnabled'
            },
            {
                'name': 'permissionGroups'
            },
        ]
    },
    '/users/{id}-GET': {
        'parameters': [
        ]
    },
    '/users-GET': {
        'parameters': [
        ]
    },
    '/users/{id}-PATCH': {
        'parameters': [
            {
                'name': 'isEnabled'
            },
            {
                'name': 'username'
            },
        ]
    },
    '/webhook-events/{id}-GET': {
        'parameters': [
        ]
    },
    '/webhook-events-GET': {
        'parameters': [
        ]
    },
    '/webhooks-POST': {
        'parameters': [
            {
                'name': 'url'
            },
            {
                'name': 'webhookEvent'
            },
            {
                'name': 'isEnabled'
            },
            {
                'name': 'source'
            },
        ]
    },
    '/webhooks/{id}-DELETE': {
        'parameters': [
        ]
    },
    '/webhooks/{id}-GET': {
        'parameters': [
        ]
    },
    '/webhooks-GET': {
        'parameters': [
        ]
    },
    '/webhooks/{id}-PATCH': {
        'parameters': [
            {
                'name': 'url'
            },
            {
                'name': 'webhookEvent'
            },
            {
                'name': 'isEnabled'
            },
            {
                'name': 'source'
            },
        ]
    },
    '/work-classes/{id}-GET': {
        'parameters': [
        ]
    },
    '/work-classes-GET': {
        'parameters': [
        ]
    },
    '/work-rights/{id}-GET': {
        'parameters': [
        ]
    },
    '/work-rights-GET': {
        'parameters': [
        ]
    },
    '/work-types/{id}-GET': {
        'parameters': [
        ]
    },
    '/work-types-GET': {
        'parameters': [
        ]
    },
    '/workflow-events/{id}-GET': {
        'parameters': [
        ]
    },
    '/workflows/{id}-PATCH': {
        'parameters': [
            {
                'name': 'jobId'
            },
            {
                'name': 'workflowFormDesigns'
            },
            {
                'name': 'id'
            },
        ]
    },
};