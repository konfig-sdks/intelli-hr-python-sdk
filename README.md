<div align="left">

[![Visit Intellihr](./header.png)](https://intellihr.com)

# Intellihr<a id="intellihr"></a>

You can find developer's guide and more documentation on [https://developers.intellihr.io](https://developers.intellihr.io)


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`intellihr.business_entities.create_new_entity`](#intellihrbusiness_entitiescreate_new_entity)
  * [`intellihr.business_entities.delete_by_id`](#intellihrbusiness_entitiesdelete_by_id)
  * [`intellihr.business_entities.find_by_id`](#intellihrbusiness_entitiesfind_by_id)
  * [`intellihr.business_entities.list_all`](#intellihrbusiness_entitieslist_all)
  * [`intellihr.business_entities.update_by_id`](#intellihrbusiness_entitiesupdate_by_id)
  * [`intellihr.business_units.create_new_unit`](#intellihrbusiness_unitscreate_new_unit)
  * [`intellihr.business_units.delete_by_id`](#intellihrbusiness_unitsdelete_by_id)
  * [`intellihr.business_units.find_by_id`](#intellihrbusiness_unitsfind_by_id)
  * [`intellihr.business_units.list_all`](#intellihrbusiness_unitslist_all)
  * [`intellihr.business_units.update_by_id`](#intellihrbusiness_unitsupdate_by_id)
  * [`intellihr.custom_field_definitions.create_definition`](#intellihrcustom_field_definitionscreate_definition)
  * [`intellihr.custom_field_definitions.delete_by_id`](#intellihrcustom_field_definitionsdelete_by_id)
  * [`intellihr.custom_field_definitions.find_definition_by_id`](#intellihrcustom_field_definitionsfind_definition_by_id)
  * [`intellihr.custom_field_definitions.list_all`](#intellihrcustom_field_definitionslist_all)
  * [`intellihr.custom_field_definitions.update_definition_by_id`](#intellihrcustom_field_definitionsupdate_definition_by_id)
  * [`intellihr.default_remuneration_components.find_by_id`](#intellihrdefault_remuneration_componentsfind_by_id)
  * [`intellihr.default_remuneration_components.list_all`](#intellihrdefault_remuneration_componentslist_all)
  * [`intellihr.employment_conditions.find_by_id`](#intellihremployment_conditionsfind_by_id)
  * [`intellihr.employment_conditions.list_all_employment_conditions`](#intellihremployment_conditionslist_all_employment_conditions)
  * [`intellihr.end_job.cancel_end_date`](#intellihrend_jobcancel_end_date)
  * [`intellihr.end_job.job_finalize`](#intellihrend_jobjob_finalize)
  * [`intellihr.extended_leave.create_new`](#intellihrextended_leavecreate_new)
  * [`intellihr.extended_leave.update_finalise`](#intellihrextended_leaveupdate_finalise)
  * [`intellihr.extended_leave_types.find_by_id`](#intellihrextended_leave_typesfind_by_id)
  * [`intellihr.extended_leave_types.list_all`](#intellihrextended_leave_typeslist_all)
  * [`intellihr.forms.find_by_id`](#intellihrformsfind_by_id)
  * [`intellihr.job_change_reasons.create_new_reason`](#intellihrjob_change_reasonscreate_new_reason)
  * [`intellihr.job_change_reasons.delete_by_id`](#intellihrjob_change_reasonsdelete_by_id)
  * [`intellihr.job_change_reasons.find_by_id`](#intellihrjob_change_reasonsfind_by_id)
  * [`intellihr.job_change_reasons.list_all`](#intellihrjob_change_reasonslist_all)
  * [`intellihr.job_change_reasons.update_by_id`](#intellihrjob_change_reasonsupdate_by_id)
  * [`intellihr.job_requirement_groups.create_new_group`](#intellihrjob_requirement_groupscreate_new_group)
  * [`intellihr.job_requirement_groups.delete_by_id`](#intellihrjob_requirement_groupsdelete_by_id)
  * [`intellihr.job_requirement_groups.find_by_id`](#intellihrjob_requirement_groupsfind_by_id)
  * [`intellihr.job_requirement_groups.list_all`](#intellihrjob_requirement_groupslist_all)
  * [`intellihr.job_requirement_groups.update_attributes`](#intellihrjob_requirement_groupsupdate_attributes)
  * [`intellihr.job_timeline.get_upcoming_changes`](#intellihrjob_timelineget_upcoming_changes)
  * [`intellihr.jobs.create_record`](#intellihrjobscreate_record)
  * [`intellihr.jobs.find_by_id`](#intellihrjobsfind_by_id)
  * [`intellihr.jobs.get_all`](#intellihrjobsget_all)
  * [`intellihr.jobs.update_attributes`](#intellihrjobsupdate_attributes)
  * [`intellihr.locations.create_new_location`](#intellihrlocationscreate_new_location)
  * [`intellihr.locations.delete_by_id`](#intellihrlocationsdelete_by_id)
  * [`intellihr.locations.find_location_by_id`](#intellihrlocationsfind_location_by_id)
  * [`intellihr.locations.list_all`](#intellihrlocationslist_all)
  * [`intellihr.locations.update_by_id`](#intellihrlocationsupdate_by_id)
  * [`intellihr.pay_grades.create_record`](#intellihrpay_gradescreate_record)
  * [`intellihr.pay_grades.delete_by_id`](#intellihrpay_gradesdelete_by_id)
  * [`intellihr.pay_grades.find_by_id`](#intellihrpay_gradesfind_by_id)
  * [`intellihr.pay_grades.get_all`](#intellihrpay_gradesget_all)
  * [`intellihr.pay_grades.update_record`](#intellihrpay_gradesupdate_record)
  * [`intellihr.people.create_new_person`](#intellihrpeoplecreate_new_person)
  * [`intellihr.people.find_by_id`](#intellihrpeoplefind_by_id)
  * [`intellihr.people.list_all_people`](#intellihrpeoplelist_all_people)
  * [`intellihr.people.update_person_by_id`](#intellihrpeopleupdate_person_by_id)
  * [`intellihr.people_documents.create_presigned_upload_url`](#intellihrpeople_documentscreate_presigned_upload_url)
  * [`intellihr.people_documents.list`](#intellihrpeople_documentslist)
  * [`intellihr.people_documents.update_document`](#intellihrpeople_documentsupdate_document)
  * [`intellihr.people_images.generate_temporary_image_url`](#intellihrpeople_imagesgenerate_temporary_image_url)
  * [`intellihr.people_images.get_temporary_image`](#intellihrpeople_imagesget_temporary_image)
  * [`intellihr.people_images.promote_image`](#intellihrpeople_imagespromote_image)
  * [`intellihr.people_skills.assign_skill_to_person`](#intellihrpeople_skillsassign_skill_to_person)
  * [`intellihr.people_skills.delete_assigned_skill_by_id`](#intellihrpeople_skillsdelete_assigned_skill_by_id)
  * [`intellihr.people_skills.find_skill_by_id`](#intellihrpeople_skillsfind_skill_by_id)
  * [`intellihr.people_skills.list_person_skills`](#intellihrpeople_skillslist_person_skills)
  * [`intellihr.people_skills.update_assigned_skill`](#intellihrpeople_skillsupdate_assigned_skill)
  * [`intellihr.permission_groups.find_group_by_id`](#intellihrpermission_groupsfind_group_by_id)
  * [`intellihr.permission_groups.list_all`](#intellihrpermission_groupslist_all)
  * [`intellihr.person_documents_(deprecated).create_presigned_upload_url`](#intellihrperson_documents_deprecatedcreate_presigned_upload_url)
  * [`intellihr.person_documents_(deprecated).update_document`](#intellihrperson_documents_deprecatedupdate_document)
  * [`intellihr.position_titles.create_new_record`](#intellihrposition_titlescreate_new_record)
  * [`intellihr.position_titles.delete_by_id`](#intellihrposition_titlesdelete_by_id)
  * [`intellihr.position_titles.list_all`](#intellihrposition_titleslist_all)
  * [`intellihr.position_titles.update_attributes`](#intellihrposition_titlesupdate_attributes)
  * [`intellihr.qualification_instances.create_new_instance`](#intellihrqualification_instancescreate_new_instance)
  * [`intellihr.qualification_instances.delete_by_id`](#intellihrqualification_instancesdelete_by_id)
  * [`intellihr.qualification_instances.find_by_id`](#intellihrqualification_instancesfind_by_id)
  * [`intellihr.qualification_instances.list_all`](#intellihrqualification_instanceslist_all)
  * [`intellihr.qualification_instances.update_instance_by_id`](#intellihrqualification_instancesupdate_instance_by_id)
  * [`intellihr.qualification_library_items.create_new_record`](#intellihrqualification_library_itemscreate_new_record)
  * [`intellihr.qualification_library_items.delete_by_id`](#intellihrqualification_library_itemsdelete_by_id)
  * [`intellihr.qualification_library_items.find_by_id`](#intellihrqualification_library_itemsfind_by_id)
  * [`intellihr.qualification_library_items.get_all_qualifications`](#intellihrqualification_library_itemsget_all_qualifications)
  * [`intellihr.qualification_library_items.update_record`](#intellihrqualification_library_itemsupdate_record)
  * [`intellihr.qualification_statuses.find_status_by_id`](#intellihrqualification_statusesfind_status_by_id)
  * [`intellihr.qualification_types.find_by_id`](#intellihrqualification_typesfind_by_id)
  * [`intellihr.qualification_types.list_all_qualification_types`](#intellihrqualification_typeslist_all_qualification_types)
  * [`intellihr.recruitment_sources.find_by_id`](#intellihrrecruitment_sourcesfind_by_id)
  * [`intellihr.recruitment_sources.list_all`](#intellihrrecruitment_sourceslist_all)
  * [`intellihr.representative_types.find_by_id`](#intellihrrepresentative_typesfind_by_id)
  * [`intellihr.representative_types.list_all`](#intellihrrepresentative_typeslist_all)
  * [`intellihr.skill_disciplines.create_new_discipline`](#intellihrskill_disciplinescreate_new_discipline)
  * [`intellihr.skill_disciplines.find_by_id`](#intellihrskill_disciplinesfind_by_id)
  * [`intellihr.skill_disciplines.list_all`](#intellihrskill_disciplineslist_all)
  * [`intellihr.skill_disciplines.update_discipline_by_id`](#intellihrskill_disciplinesupdate_discipline_by_id)
  * [`intellihr.skills.create_new_skill`](#intellihrskillscreate_new_skill)
  * [`intellihr.skills.find_skill_by_id`](#intellihrskillsfind_skill_by_id)
  * [`intellihr.skills.get_all`](#intellihrskillsget_all)
  * [`intellihr.skills.update_skill_by_id`](#intellihrskillsupdate_skill_by_id)
  * [`intellihr.training_providers.find_by_id`](#intellihrtraining_providersfind_by_id)
  * [`intellihr.training_providers.list_all`](#intellihrtraining_providerslist_all)
  * [`intellihr.training_statuses.list_all`](#intellihrtraining_statuseslist_all)
  * [`intellihr.training_types.find_by_id`](#intellihrtraining_typesfind_by_id)
  * [`intellihr.training_types.list_all`](#intellihrtraining_typeslist_all)
  * [`intellihr.trainings.create_new_training`](#intellihrtrainingscreate_new_training)
  * [`intellihr.trainings.delete_by_id`](#intellihrtrainingsdelete_by_id)
  * [`intellihr.trainings.find_training_by_id`](#intellihrtrainingsfind_training_by_id)
  * [`intellihr.trainings.list_all`](#intellihrtrainingslist_all)
  * [`intellihr.trainings.update_training_by_id`](#intellihrtrainingsupdate_training_by_id)
  * [`intellihr.users.create_user`](#intellihruserscreate_user)
  * [`intellihr.users.find_user_by_id`](#intellihrusersfind_user_by_id)
  * [`intellihr.users.get_all_users`](#intellihrusersget_all_users)
  * [`intellihr.users.update_by_id`](#intellihrusersupdate_by_id)
  * [`intellihr.webhook_events.find_event_by_id`](#intellihrwebhook_eventsfind_event_by_id)
  * [`intellihr.webhook_events.list_all_events`](#intellihrwebhook_eventslist_all_events)
  * [`intellihr.webhooks.create_webhook`](#intellihrwebhookscreate_webhook)
  * [`intellihr.webhooks.delete_by_id`](#intellihrwebhooksdelete_by_id)
  * [`intellihr.webhooks.find_by_id`](#intellihrwebhooksfind_by_id)
  * [`intellihr.webhooks.list_all`](#intellihrwebhookslist_all)
  * [`intellihr.webhooks.update_webhook`](#intellihrwebhooksupdate_webhook)
  * [`intellihr.work_classes.find_by_id`](#intellihrwork_classesfind_by_id)
  * [`intellihr.work_classes.list_all`](#intellihrwork_classeslist_all)
  * [`intellihr.work_rights.find_work_right_by_id`](#intellihrwork_rightsfind_work_right_by_id)
  * [`intellihr.work_rights.list_all`](#intellihrwork_rightslist_all)
  * [`intellihr.work_types.find_by_id`](#intellihrwork_typesfind_by_id)
  * [`intellihr.work_types.list_all`](#intellihrwork_typeslist_all)
  * [`intellihr.workflow_events.find_by_id`](#intellihrworkflow_eventsfind_by_id)
  * [`intellihr.workflows.trigger_by_id`](#intellihrworkflowstrigger_by_id)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=intelliHR&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from intelli_hr_python_sdk import IntelliHr, ApiException

intellihr = IntelliHr(

        api_key = 'YOUR_API_KEY',
)

try:
    # Create a new Business Entity
    create_new_entity_response = intellihr.business_entities.create_new_entity(
        name="IntelliHR",
        code="BE001",
        legal_name="IntelliHR Systems Limited",
        number="00 000 000 000",
        is_enabled=True,
        custom_fields={
        "key": {
        },
    },
    )
    print(create_new_entity_response)
except ApiException as e:
    print("Exception when calling BusinessEntitiesApi.create_new_entity: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python

import asyncio
from pprint import pprint
from intelli_hr_python_sdk import IntelliHr, ApiException

intellihr = IntelliHr(

        api_key = 'YOUR_API_KEY',
)

async def main():
    try:
        # Create a new Business Entity
        create_new_entity_response = await intellihr.business_entities.acreate_new_entity(
            name="IntelliHR",
            code="BE001",
            legal_name="IntelliHR Systems Limited",
            number="00 000 000 000",
            is_enabled=True,
            custom_fields={
        "key": {
        },
    },
        )
        print(create_new_entity_response)
    except ApiException as e:
        print("Exception when calling BusinessEntitiesApi.create_new_entity: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)

asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from intelli_hr_python_sdk import IntelliHr, ApiException

intellihr = IntelliHr(

        api_key = 'YOUR_API_KEY',
)

try:
    # Create a new Business Entity
    create_new_entity_response = intellihr.business_entities.raw.create_new_entity(
        name="IntelliHR",
        code="BE001",
        legal_name="IntelliHR Systems Limited",
        number="00 000 000 000",
        is_enabled=True,
        custom_fields={
        "key": {
        },
    },
    )
    pprint(create_new_entity_response.body)
    pprint(create_new_entity_response.body["data"])
    pprint(create_new_entity_response.body["meta"])
    pprint(create_new_entity_response.headers)
    pprint(create_new_entity_response.status)
    pprint(create_new_entity_response.round_trip_time)
except ApiException as e:
    print("Exception when calling BusinessEntitiesApi.create_new_entity: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `intellihr.business_entities.create_new_entity`<a id="intellihrbusiness_entitiescreate_new_entity"></a>

Returns the created [Business Entity](https://developers.intellihr.io/docs/v1/).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_entity_response = intellihr.business_entities.create_new_entity(
    name="IntelliHR",
    code="BE001",
    legal_name="IntelliHR Systems Limited",
    number="00 000 000 000",
    is_enabled=True,
    custom_fields={
        "key": {
        },
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name given to this [Business Entity](https://developers.intellihr.io/docs/v1/). This name would normally be shown to users of the system.

##### code: `str`<a id="code-str"></a>

Code given to this [Business Entity](https://developers.intellihr.io/docs/v1/)

##### legal_name: `str`<a id="legal_name-str"></a>

Legal name can be different from the name presented to a user. Usually used for administrative tasks.

##### number: `str`<a id="number-str"></a>

Legally registered [Business Entity](https://developers.intellihr.io/docs/v1/) number, e.g. in Australia this might be the ABN, or in America the RN.

##### is_enabled: `bool`<a id="is_enabled-bool"></a>

Specifies whether users can select this [Business Entity](https://developers.intellihr.io/docs/v1/) in dropdowns.

##### custom_fields: [`BusinessEntitiesCreateRequestCustomFields`](./intelli_hr_python_sdk/type/business_entities_create_request_custom_fields.py)<a id="custom_fields-businessentitiescreaterequestcustomfieldsintelli_hr_python_sdktypebusiness_entities_create_request_custom_fieldspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BusinessEntitiesCreateRequest`](./intelli_hr_python_sdk/type/business_entities_create_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`BusinessEntities`](./intelli_hr_python_sdk/pydantic/business_entities.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/business-entities` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.business_entities.delete_by_id`<a id="intellihrbusiness_entitiesdelete_by_id"></a>

Deletes the [Business Entity](https://developers.intellihr.io/docs/v1/)'s by the given ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
intellihr.business_entities.delete_by_id()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/business-entities/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.business_entities.find_by_id`<a id="intellihrbusiness_entitiesfind_by_id"></a>

Returns a single [Business Entity](https://developers.intellihr.io/docs/v1/) by its identifier.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_by_id_response = intellihr.business_entities.find_by_id()
```

#### 🔄 Return<a id="🔄-return"></a>

[`BusinessEntities`](./intelli_hr_python_sdk/pydantic/business_entities.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/business-entities/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.business_entities.list_all`<a id="intellihrbusiness_entitieslist_all"></a>

Returns a list of all [Business Entities](https://developers.intellihr.io/docs/v1/).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = intellihr.business_entities.list_all()
```

#### 🔄 Return<a id="🔄-return"></a>

[`BusinessEntitiesList`](./intelli_hr_python_sdk/pydantic/business_entities_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/business-entities` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.business_entities.update_by_id`<a id="intellihrbusiness_entitiesupdate_by_id"></a>

Returns the updated [Business Entity](https://developers.intellihr.io/docs/v1/).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_by_id_response = intellihr.business_entities.update_by_id(
    name="IntelliHR",
    code="BE001",
    legal_name="IntelliHR Systems Limited",
    number="00 000 000 000",
    is_enabled=True,
    custom_fields={
        "key": {
        },
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name given to this [Business Entity](https://developers.intellihr.io/docs/v1/). This name would normally be shown to users of the system.

##### code: `str`<a id="code-str"></a>

Code given to this [Business Entity](https://developers.intellihr.io/docs/v1/)

##### legal_name: `str`<a id="legal_name-str"></a>

Legal name can be different from the name presented to a user. Usually used for administrative tasks.

##### number: `str`<a id="number-str"></a>

Legally registered [Business Entity](https://developers.intellihr.io/docs/v1/) number, e.g. in Australia this might be the ABN, or in America the RN.

##### is_enabled: `bool`<a id="is_enabled-bool"></a>

Specifies whether users can select this [Business Entity](https://developers.intellihr.io/docs/v1/) in dropdowns.

##### custom_fields: [`BusinessEntitiesPatchRequestCustomFields`](./intelli_hr_python_sdk/type/business_entities_patch_request_custom_fields.py)<a id="custom_fields-businessentitiespatchrequestcustomfieldsintelli_hr_python_sdktypebusiness_entities_patch_request_custom_fieldspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BusinessEntitiesPatchRequest`](./intelli_hr_python_sdk/type/business_entities_patch_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`BusinessEntities`](./intelli_hr_python_sdk/pydantic/business_entities.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/business-entities/{id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.business_units.create_new_unit`<a id="intellihrbusiness_unitscreate_new_unit"></a>

Returns the created [Business Unit](https://developers.intellihr.io/docs/v1/).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_unit_response = intellihr.business_units.create_new_unit(
    name="Engineering",
    identifier="",
    code="BE001",
    notes="",
    parent_id=None,
    is_enabled=True,
    custom_fields={
        "key": {
        },
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name given to this [Business Unit](https://developers.intellihr.io/docs/v1/). This name would normally be shown to users of the system.

##### identifier: `str`<a id="identifier-str"></a>

Optional identifier that can be used for administrative tasks.

##### code: `str`<a id="code-str"></a>

Code given to this [Business Unit](https://developers.intellihr.io/docs/v1/)

##### notes: `str`<a id="notes-str"></a>

Notes attached to a [Business Unit](https://developers.intellihr.io/docs/v1/)

##### parent_id: Union[`str`, `none_type`]<a id="parent_id-unionstr-none_type"></a>


The identifier string for the parent [Business Unit](https://developers.intellihr.io/docs/v1/), or null if there is no parent (this is a top level business unit).

##### is_enabled: `bool`<a id="is_enabled-bool"></a>

Specifies whether users can select this [Business Unit](https://developers.intellihr.io/docs/v1/) in dropdowns.

##### custom_fields: [`BusinessUnitsCreateRequestCustomFields`](./intelli_hr_python_sdk/type/business_units_create_request_custom_fields.py)<a id="custom_fields-businessunitscreaterequestcustomfieldsintelli_hr_python_sdktypebusiness_units_create_request_custom_fieldspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BusinessUnitsCreateRequest`](./intelli_hr_python_sdk/type/business_units_create_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`BusinessUnits`](./intelli_hr_python_sdk/pydantic/business_units.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/business-units` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.business_units.delete_by_id`<a id="intellihrbusiness_unitsdelete_by_id"></a>

Deletes the [Business Unit](https://developers.intellihr.io/docs/v1/)'s by the given ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
intellihr.business_units.delete_by_id()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/business-units/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.business_units.find_by_id`<a id="intellihrbusiness_unitsfind_by_id"></a>

Returns a single [Business Unit](https://developers.intellihr.io/docs/v1/).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_by_id_response = intellihr.business_units.find_by_id()
```

#### 🔄 Return<a id="🔄-return"></a>

[`BusinessUnits`](./intelli_hr_python_sdk/pydantic/business_units.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/business-units/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.business_units.list_all`<a id="intellihrbusiness_unitslist_all"></a>

Returns a list of all [Business Units](https://developers.intellihr.io/docs/v1/) recorded in the system.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = intellihr.business_units.list_all(
    filters={
        "identifier": "Engineering",
        "name": "Engineering",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### filters: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./intelli_hr_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="filters-dictstr-unionbool-date-datetime-dict-float-int-list-str-noneintelli_hr_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Filters can be applied in the query string to limit the data returned from this endpoint. Filters are provided in the format `filters[<filter_name>][<operation_type>]=<filter_value>`.For example, a filter to get items matching a specific filter value would be `filters[identifier][eq]=Engineering`  Below is a list of operation types available on filters, note that each filter may not support every type:  • Equality `[eq]`: Checks for an exact match with the given filter value  The list of supported filters is given below.

#### 🔄 Return<a id="🔄-return"></a>

[`BusinessUnitsList`](./intelli_hr_python_sdk/pydantic/business_units_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/business-units` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.business_units.update_by_id`<a id="intellihrbusiness_unitsupdate_by_id"></a>

Returns the updated [Business Unit](https://developers.intellihr.io/docs/v1/).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_by_id_response = intellihr.business_units.update_by_id(
    name="Engineering",
    identifier="",
    code="BE001",
    notes="",
    parent_id=None,
    is_enabled=True,
    custom_fields={
        "key": {
        },
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name given to this [Business Unit](https://developers.intellihr.io/docs/v1/). This name would normally be shown to users of the system.

##### identifier: `str`<a id="identifier-str"></a>

Optional identifier that can be used for administrative tasks.

##### code: `str`<a id="code-str"></a>

Code given to this [Business Unit](https://developers.intellihr.io/docs/v1/)

##### notes: `str`<a id="notes-str"></a>

Notes attached to a [Business Unit](https://developers.intellihr.io/docs/v1/)

##### parent_id: Union[`str`, `none_type`]<a id="parent_id-unionstr-none_type"></a>


The identifier string for the parent [Business Unit](https://developers.intellihr.io/docs/v1/), or null if there is no parent (this is a top level business unit).

##### is_enabled: `bool`<a id="is_enabled-bool"></a>

Specifies whether users can select this [Business Unit](https://developers.intellihr.io/docs/v1/) in dropdowns.

##### custom_fields: [`BusinessUnitsPatchRequestCustomFields`](./intelli_hr_python_sdk/type/business_units_patch_request_custom_fields.py)<a id="custom_fields-businessunitspatchrequestcustomfieldsintelli_hr_python_sdktypebusiness_units_patch_request_custom_fieldspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BusinessUnitsPatchRequest`](./intelli_hr_python_sdk/type/business_units_patch_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`BusinessUnits`](./intelli_hr_python_sdk/pydantic/business_units.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/business-units/{id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.custom_field_definitions.create_definition`<a id="intellihrcustom_field_definitionscreate_definition"></a>

Returns the created [Custom Field Definition](https://developers.intellihr.io/docs/v1/)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_definition_response = intellihr.custom_field_definitions.create_definition(
    name="Custom Field",
    api_name="custom_field",
    model_type="PERSON",
    type="TEXT",
    description=None,
    is_sensitive=False,
    select_definition={
    },
    text_definition={
    },
    people_dropdown_definition=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name given to this [Custom Field Definition](https://developers.intellihr.io/docs/v1/). This name would normally be shown to users of the system.

##### api_name: `str`<a id="api_name-str"></a>

The api name given to this [Custom Field Definition](https://developers.intellihr.io/docs/v1/). This name is used to uniquely identify the custom field in the api and is used as the key when modifying the custom field on a record.

##### model_type: `str`<a id="model_type-str"></a>

The model that this custom field relates to and can be attached to. Enum: `ADDRESS`, `BUSINESS_ENTITY`, `BUSINESS_UNIT`, `EMAIL_ADDRESS`, `JOB`, `LOCATION`, `PERSON`, `POSITION_TITLE`, `PHONE_NUMBER`, `REMUNERATION`, `TRAINING`.

##### type: `str`<a id="type-str"></a>

The type of data this field records. Enum: `SINGLE_SELECT`, `MULTI_SELECT`, `TEXT`, `NUMBER`, `PEOPLE_DROPDOWN`.

##### description: Union[`str`, `none_type`]<a id="description-unionstr-none_type"></a>


The description of this [Custom Field Definition](https://developers.intellihr.io/docs/v1/). This is used as a tooltip on the create and update pages.

##### is_sensitive: `bool`<a id="is_sensitive-bool"></a>

Whether or not this [Custom Field Definition](https://developers.intellihr.io/docs/v1/) is marked as sensitive information.

##### select_definition: [`CustomFieldDefinitionCreateRequestSelectDefinition`](./intelli_hr_python_sdk/type/custom_field_definition_create_request_select_definition.py)<a id="select_definition-customfielddefinitioncreaterequestselectdefinitionintelli_hr_python_sdktypecustom_field_definition_create_request_select_definitionpy"></a>


##### text_definition: [`CustomFieldDefinitionCreateRequestTextDefinition`](./intelli_hr_python_sdk/type/custom_field_definition_create_request_text_definition.py)<a id="text_definition-customfielddefinitioncreaterequesttextdefinitionintelli_hr_python_sdktypecustom_field_definition_create_request_text_definitionpy"></a>


##### people_dropdown_definition: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./intelli_hr_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="people_dropdown_definition-unionbool-date-datetime-dict-float-int-list-str-noneintelli_hr_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>


This field is `required` when type `PEOPLE_DROPDOWN` is used

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CustomFieldDefinitionCreateRequest`](./intelli_hr_python_sdk/type/custom_field_definition_create_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CustomFieldDefinitions`](./intelli_hr_python_sdk/pydantic/custom_field_definitions.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/custom-field-definitions` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.custom_field_definitions.delete_by_id`<a id="intellihrcustom_field_definitionsdelete_by_id"></a>

Deletes the [Custom Field Definition](https://developers.intellihr.io/docs/v1/) by the given ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
intellihr.custom_field_definitions.delete_by_id()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/custom-field-definitions/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.custom_field_definitions.find_definition_by_id`<a id="intellihrcustom_field_definitionsfind_definition_by_id"></a>

Returns a single Custom Field Definition.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_definition_by_id_response = intellihr.custom_field_definitions.find_definition_by_id()
```

#### 🔄 Return<a id="🔄-return"></a>

[`CustomFieldDefinitions`](./intelli_hr_python_sdk/pydantic/custom_field_definitions.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/custom-field-definitions/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.custom_field_definitions.list_all`<a id="intellihrcustom_field_definitionslist_all"></a>

Returns a list of all Custom Field Definitions.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = intellihr.custom_field_definitions.list_all(
    filters={
        "model_type": "TRAINING",
        "is_enabled": True,
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### filters: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./intelli_hr_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="filters-dictstr-unionbool-date-datetime-dict-float-int-list-str-noneintelli_hr_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Filters can be applied in the query string to limit the data returned from this endpoint. Filters are provided in the format `filters[<filter_name>][<operation_type>]=<filter_value>`.For example, a filter to get items matching a specific filter value would be `filters[modelType][eq]=TRAINING`  Below is a list of operation types available on filters, note that each filter may not support every type:  • Equality `[eq]`: Checks for an exact match with the given filter value  The list of supported filters is given below.

#### 🔄 Return<a id="🔄-return"></a>

[`CustomFieldDefinitionsList`](./intelli_hr_python_sdk/pydantic/custom_field_definitions_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/custom-field-definitions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.custom_field_definitions.update_definition_by_id`<a id="intellihrcustom_field_definitionsupdate_definition_by_id"></a>

Returns the updated [Custom Field Definition](https://developers.intellihr.io/docs/v1/)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_definition_by_id_response = intellihr.custom_field_definitions.update_definition_by_id(
    description=None,
    name="Custom Field",
    is_enabled=False,
    is_sensitive=False,
    select_definition={
    },
    people_dropdown_definition=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### description: Union[`str`, `none_type`]<a id="description-unionstr-none_type"></a>


The description of this [Custom Field Definition](https://developers.intellihr.io/docs/v1/). This is used as a tooltip on the create and update pages.

##### name: `str`<a id="name-str"></a>

Name given to this [Custom Field Definition](https://developers.intellihr.io/docs/v1/). This name would normally be shown to users of the system.

##### is_enabled: `bool`<a id="is_enabled-bool"></a>

Whether or not this [Custom Field Definition](https://developers.intellihr.io/docs/v1/) is enabled to be used.

##### is_sensitive: `bool`<a id="is_sensitive-bool"></a>

Whether or not this [Custom Field Definition](https://developers.intellihr.io/docs/v1/) is marked as sensitive information.

##### select_definition: [`CustomFieldDefinitionPatchRequestSelectDefinition`](./intelli_hr_python_sdk/type/custom_field_definition_patch_request_select_definition.py)<a id="select_definition-customfielddefinitionpatchrequestselectdefinitionintelli_hr_python_sdktypecustom_field_definition_patch_request_select_definitionpy"></a>


##### people_dropdown_definition: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./intelli_hr_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="people_dropdown_definition-unionbool-date-datetime-dict-float-int-list-str-noneintelli_hr_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>


This field is used in conjunction with type `PEOPLE_DROPDOWN`

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CustomFieldDefinitionPatchRequest`](./intelli_hr_python_sdk/type/custom_field_definition_patch_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CustomFieldDefinitions`](./intelli_hr_python_sdk/pydantic/custom_field_definitions.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/custom-field-definitions/{id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.default_remuneration_components.find_by_id`<a id="intellihrdefault_remuneration_componentsfind_by_id"></a>

Returns a single default remuneration component.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_by_id_response = intellihr.default_remuneration_components.find_by_id()
```

#### 🔄 Return<a id="🔄-return"></a>

[`DefaultRemunerationComponents`](./intelli_hr_python_sdk/pydantic/default_remuneration_components.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/default-remuneration-components/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.default_remuneration_components.list_all`<a id="intellihrdefault_remuneration_componentslist_all"></a>

Returns a list of all [Default Remuneration Components](https://developers.intellihr.io/docs/v1/) recorded in the system.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = intellihr.default_remuneration_components.list_all()
```

#### 🔄 Return<a id="🔄-return"></a>

[`DefaultRemunerationComponentsList`](./intelli_hr_python_sdk/pydantic/default_remuneration_components_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/default-remuneration-components` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.employment_conditions.find_by_id`<a id="intellihremployment_conditionsfind_by_id"></a>

Returns a single employment condition.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_by_id_response = intellihr.employment_conditions.find_by_id()
```

#### 🔄 Return<a id="🔄-return"></a>

[`EmploymentConditions`](./intelli_hr_python_sdk/pydantic/employment_conditions.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/employment-conditions/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.employment_conditions.list_all_employment_conditions`<a id="intellihremployment_conditionslist_all_employment_conditions"></a>

Returns a list of all employment conditions.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_employment_conditions_response = intellihr.employment_conditions.list_all_employment_conditions()
```

#### 🔄 Return<a id="🔄-return"></a>

[`EmploymentConditionsList`](./intelli_hr_python_sdk/pydantic/employment_conditions_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/employment-conditions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.end_job.cancel_end_date`<a id="intellihrend_jobcancel_end_date"></a>

If a job end date has been finalised, this will cancel the finalisation

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
cancel_end_date_response = intellihr.end_job.cancel_end_date(
    UNKNOWN_PARAMETER_NAME=,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### UNKNOWN_PARAMETER_NAME: [``](./intelli_hr_python_sdk/type/.py)<a id="unknown_parameter_name-intelli_hr_python_sdktypepy"></a>

Whether to cancel the disabling of the users account upon the job end date, if user doesn't exist the Boolean has no effect yet the request will still succeed.

#### 🔄 Return<a id="🔄-return"></a>

[`JobEndRemoveResponse`](./intelli_hr_python_sdk/pydantic/job_end_remove_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/job-end/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.end_job.job_finalize`<a id="intellihrend_jobjob_finalize"></a>

Set an end date, and finalise a job.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
job_finalize_response = intellihr.end_job.job_finalize(
    end_date="2015-03-01T22:30:00+00:00",
    reassign_direct_reports_to="8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
    turnover_type="involuntary",
    turnover_reason="Medical reasons",
    UNKNOWN_PARAMETER_NAME=,
    UNKNOWN_PARAMETER_NAME2=,
    UNKNOWN_PARAMETER_NAME3=,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### end_date: `str`<a id="end_date-str"></a>

The <b>exclusive</b> date this [Job](https://developers.intellihr.io/docs/v1/) ended or will end within the organisation. For example, if the person's last working date is on 2025-04-23, the `endDate` should be set as 2025-04-24 to reflect the exclusive date. Required if not finalising an end date, or the job does not have an end date. This date will follow the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6).   YYYY-MM-DD date formatting is also supported, although by using this format the date will be stored as the start of day in UTC time, not the requesting tenants timezone.

##### reassign_direct_reports_to: `str`<a id="reassign_direct_reports_to-str"></a>

The identifier string for the [Job](https://developers.intellihr.io/docs/v1/) of the person that the direct report will be reassigned to.

##### turnover_type: `str`<a id="turnover_type-str"></a>

The type of turnover this end of job would be classified as: `voluntary`, `involuntary` or `unknown`. Required if finalising an end date.

##### turnover_reason: `str`<a id="turnover_reason-str"></a>

The name of the turnover reason.

##### UNKNOWN_PARAMETER_NAME: [``](./intelli_hr_python_sdk/type/.py)<a id="unknown_parameter_name-intelli_hr_python_sdktypepy"></a>

If true, do not finalise the job.

##### UNKNOWN_PARAMETER_NAME2: [``](./intelli_hr_python_sdk/type/.py)<a id="unknown_parameter_name2-intelli_hr_python_sdktypepy"></a>

If true, keeps the user account when finalising the job.

##### UNKNOWN_PARAMETER_NAME3: [``](./intelli_hr_python_sdk/type/.py)<a id="unknown_parameter_name3-intelli_hr_python_sdktypepy"></a>

When true, no events will be fired from this action

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`JobEndPatchRequest`](./intelli_hr_python_sdk/type/job_end_patch_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`JobEndPatchResponse`](./intelli_hr_python_sdk/pydantic/job_end_patch_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/job-end/{id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.extended_leave.create_new`<a id="intellihrextended_leavecreate_new"></a>

Create a new Extended Leave on an existing Job.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_response = intellihr.extended_leave.create_new(
    job_id="8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
    start_date="2015-03-01T22:30:00+00:00",
    end_date="2015-03-01T22:30:00+00:00",
    leave_type={
        "id": "8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
        "name": "Long Service",
    },
    fte="1",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### job_id: `str`<a id="job_id-str"></a>

The identifier string for the [Job](https://developers.intellihr.io/docs/v1/) that this extended leave belongs to.

##### start_date: `str`<a id="start_date-str"></a>

The date this [Extended Leave](https://developers.intellihr.io/docs/v1/) started or will start. This date will follow the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6).   YYYY-MM-DD date formatting is also supported, although by using this format the date will be stored as the start of day in UTC time, not the requesting tenants timezone.

##### end_date: `str`<a id="end_date-str"></a>

The date this [Extended Leave](https://developers.intellihr.io/docs/v1/) is expected to end. Leave is created without a finalised return date. In order to create more than one Extended Leave on a Job, the end date must be finalised on the most recent created Extended Leave. This date will follow the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6).   YYYY-MM-DD date formatting is also supported, although by using this format the date will be stored as the start of day in UTC time, not the requesting tenants timezone.

##### leave_type: [`LeaveCreateRequestLeaveType`](./intelli_hr_python_sdk/type/leave_create_request_leave_type.py)<a id="leave_type-leavecreaterequestleavetypeintelli_hr_python_sdktypeleave_create_request_leave_typepy"></a>


##### fte: `str`<a id="fte-str"></a>

The full time equivalent for this [Job](https://developers.intellihr.io/docs/v1/) if changing during this leave period.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LeaveCreateRequest`](./intelli_hr_python_sdk/type/leave_create_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`LeaveCreateResponse`](./intelli_hr_python_sdk/pydantic/leave_create_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/extended-leave` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.extended_leave.update_finalise`<a id="intellihrextended_leaveupdate_finalise"></a>

Update or Finalise an existing Extended Leave.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_finalise_response = intellihr.extended_leave.update_finalise(
    job_id="8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
    end_date="2015-03-01T22:30:00+00:00",
    should_not_finalise_end_date=False,
    start_date="2015-03-01T22:30:00+00:00",
    leave_type={
        "id": "8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
        "name": "Long Service",
    },
    fte="1",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### job_id: `str`<a id="job_id-str"></a>

The identifier string for the [Job](https://developers.intellihr.io/docs/v1/) that this extended leave belongs to.

##### end_date: `str`<a id="end_date-str"></a>

The date this [Extended Leave](https://developers.intellihr.io/docs/v1/) is expected to end. Leave is created without a finalised return date. In order to create more than one Extended Leave on a Job, the end date must be finalised on the most recent created Extended Leave. This date will follow the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6).   YYYY-MM-DD date formatting is also supported, although by using this format the date will be stored as the start of day in UTC time, not the requesting tenants timezone.

##### should_not_finalise_end_date: `bool`<a id="should_not_finalise_end_date-bool"></a>

Whether or not to finalise the end date for the [Extended Leave](https://developers.intellihr.io/docs/v1/). This boolean will change the input variables required if you are finalising an Extended Leave or just updating it. Finalising the end date prevents any further changes to this Extended Leave.

##### start_date: `str`<a id="start_date-str"></a>

The date this [Extended Leave](https://developers.intellihr.io/docs/v1/) started or will start. This field is only required if not finalising the Extended Leave end date, and will not be used if shouldNotFinaliseEndDate is not set or is set to false. This date will follow the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6).   YYYY-MM-DD date formatting is also supported, although by using this format the date will be stored as the start of day in UTC time, not the requesting tenants timezone.

##### leave_type: [`LeaveUpdateRequestLeaveType`](./intelli_hr_python_sdk/type/leave_update_request_leave_type.py)<a id="leave_type-leaveupdaterequestleavetypeintelli_hr_python_sdktypeleave_update_request_leave_typepy"></a>


##### fte: `str`<a id="fte-str"></a>

The full time equivalent for this [Job](https://developers.intellihr.io/docs/v1/) upon returning from Extended Leave. This field is only required when finalising the Extended Leave end date, and will not be used if shouldNotFinaliseEndDate is set to true.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LeaveUpdateRequest`](./intelli_hr_python_sdk/type/leave_update_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`LeaveUpdateResponse`](./intelli_hr_python_sdk/pydantic/leave_update_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/extended-leave/{id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.extended_leave_types.find_by_id`<a id="intellihrextended_leave_typesfind_by_id"></a>

Returns a single Extended Leave Type.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_by_id_response = intellihr.extended_leave_types.find_by_id()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ExtendedLeaveTypes`](./intelli_hr_python_sdk/pydantic/extended_leave_types.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/extended-leave-types/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.extended_leave_types.list_all`<a id="intellihrextended_leave_typeslist_all"></a>

Returns a list of all Extended Leave Types.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = intellihr.extended_leave_types.list_all()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ExtendedLeaveTypesList`](./intelli_hr_python_sdk/pydantic/extended_leave_types_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/extended-leave-types` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.forms.find_by_id`<a id="intellihrformsfind_by_id"></a>

Returns a single [Form](https://developers.intellihr.io/docs/v1/) instance by its identifier.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_by_id_response = intellihr.forms.find_by_id()
```

#### 🔄 Return<a id="🔄-return"></a>

[`Forms`](./intelli_hr_python_sdk/pydantic/forms.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/forms/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.job_change_reasons.create_new_reason`<a id="intellihrjob_change_reasonscreate_new_reason"></a>

Returns the created [Job Change Reason](https://developers.intellihr.io/docs/v1/).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_reason_response = intellihr.job_change_reasons.create_new_reason(
    name="Engineering",
    is_enabled=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name given to this [Job Change Reason](https://developers.intellihr.io/docs/v1/). This name would normally be shown to users of the system.

##### is_enabled: `bool`<a id="is_enabled-bool"></a>

Specifies whether users can select this [Job Change Reason](https://developers.intellihr.io/docs/v1/) in dropdowns.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`JobChangeReasonsCreateRequest`](./intelli_hr_python_sdk/type/job_change_reasons_create_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`JobChangeReasons`](./intelli_hr_python_sdk/pydantic/job_change_reasons.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/job-change-reasons` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.job_change_reasons.delete_by_id`<a id="intellihrjob_change_reasonsdelete_by_id"></a>

Deletes the [Job Change Reason](https://developers.intellihr.io/docs/v1/)'s by the given ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
intellihr.job_change_reasons.delete_by_id()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/job-change-reasons/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.job_change_reasons.find_by_id`<a id="intellihrjob_change_reasonsfind_by_id"></a>

Returns a single [Job Change Reason](https://developers.intellihr.io/docs/v1/).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_by_id_response = intellihr.job_change_reasons.find_by_id()
```

#### 🔄 Return<a id="🔄-return"></a>

[`JobChangeReasons`](./intelli_hr_python_sdk/pydantic/job_change_reasons.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/job-change-reasons/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.job_change_reasons.list_all`<a id="intellihrjob_change_reasonslist_all"></a>

Returns a list of all [Job Change Reasons](https://developers.intellihr.io/docs/v1/) recorded in the system.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = intellihr.job_change_reasons.list_all()
```

#### 🔄 Return<a id="🔄-return"></a>

[`JobChangeReasonsList`](./intelli_hr_python_sdk/pydantic/job_change_reasons_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/job-change-reasons` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.job_change_reasons.update_by_id`<a id="intellihrjob_change_reasonsupdate_by_id"></a>

Returns the updated [Job Change Reason](https://developers.intellihr.io/docs/v1/).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_by_id_response = intellihr.job_change_reasons.update_by_id(
    name="Engineering",
    is_enabled=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name given to this [Job Change Reason](https://developers.intellihr.io/docs/v1/). This name would normally be shown to users of the system.

##### is_enabled: `bool`<a id="is_enabled-bool"></a>

Specifies whether users can select this [Job Change Reason](https://developers.intellihr.io/docs/v1/) in dropdowns.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`JobChangeReasonsPatchRequest`](./intelli_hr_python_sdk/type/job_change_reasons_patch_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`JobChangeReasons`](./intelli_hr_python_sdk/pydantic/job_change_reasons.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/job-change-reasons/{id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.job_requirement_groups.create_new_group`<a id="intellihrjob_requirement_groupscreate_new_group"></a>

Create a new [Job Requirement Group](https://developers.intellihr.io/docs/v1/) record with the provided data.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_group_response = intellihr.job_requirement_groups.create_new_group(
    name="ABCDE12345",
    library_item_ids=[
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

The issue date of the [Job Requirement Group](https://developers.intellihr.io/docs/v1/)

##### library_item_ids: [`JobRequirementGroupsCreateRequestLibraryItemIds`](./intelli_hr_python_sdk/type/job_requirement_groups_create_request_library_item_ids.py)<a id="library_item_ids-jobrequirementgroupscreaterequestlibraryitemidsintelli_hr_python_sdktypejob_requirement_groups_create_request_library_item_idspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`JobRequirementGroupsCreateRequest`](./intelli_hr_python_sdk/type/job_requirement_groups_create_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`JobRequirementGroups`](./intelli_hr_python_sdk/pydantic/job_requirement_groups.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/job-requirement-groups` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.job_requirement_groups.delete_by_id`<a id="intellihrjob_requirement_groupsdelete_by_id"></a>

Deletes the [Job Requirement Group](https://developers.intellihr.io/docs/v1/) by the given ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
intellihr.job_requirement_groups.delete_by_id()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/job-requirement-groups/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.job_requirement_groups.find_by_id`<a id="intellihrjob_requirement_groupsfind_by_id"></a>

Returns a single [Job Requirement Group](https://developers.intellihr.io/docs/v1/) by its identifier.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_by_id_response = intellihr.job_requirement_groups.find_by_id()
```

#### 🔄 Return<a id="🔄-return"></a>

[`JobRequirementGroups`](./intelli_hr_python_sdk/pydantic/job_requirement_groups.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/job-requirement-groups/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.job_requirement_groups.list_all`<a id="intellihrjob_requirement_groupslist_all"></a>

List all Job Requirement Groups

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = intellihr.job_requirement_groups.list_all()
```

#### 🔄 Return<a id="🔄-return"></a>

[`JobRequirementGroupsList`](./intelli_hr_python_sdk/pydantic/job_requirement_groups_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/job-requirement-groups` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.job_requirement_groups.update_attributes`<a id="intellihrjob_requirement_groupsupdate_attributes"></a>

Patch attributes of an existing [Job Requirement Group](https://developers.intellihr.io/docs/v1/) record with the provided data.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_attributes_response = intellihr.job_requirement_groups.update_attributes(
    name="ABCDE12345",
    library_item_ids=[
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

The issue date of the [Job Requirement Group](https://developers.intellihr.io/docs/v1/)

##### library_item_ids: [`JobRequirementGroupsPatchRequestLibraryItemIds`](./intelli_hr_python_sdk/type/job_requirement_groups_patch_request_library_item_ids.py)<a id="library_item_ids-jobrequirementgroupspatchrequestlibraryitemidsintelli_hr_python_sdktypejob_requirement_groups_patch_request_library_item_idspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`JobRequirementGroupsPatchRequest`](./intelli_hr_python_sdk/type/job_requirement_groups_patch_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`JobRequirementGroups`](./intelli_hr_python_sdk/pydantic/job_requirement_groups.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/job-requirement-groups/{id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.job_timeline.get_upcoming_changes`<a id="intellihrjob_timelineget_upcoming_changes"></a>

Returns the upcoming changes and current information about a [Job](https://developers.intellihr.io/docs/v1/).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_upcoming_changes_response = intellihr.job_timeline.get_upcoming_changes(
    job_id="jobId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### job_id: `str`<a id="job_id-str"></a>

Id string param for relevant [Job](https://developers.intellihr.io/docs/v1/)

#### 🔄 Return<a id="🔄-return"></a>

[`JobIdTimelineGetResponse`](./intelli_hr_python_sdk/pydantic/job_id_timeline_get_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/jobs/{jobId}/timeline` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.jobs.create_record`<a id="intellihrjobscreate_record"></a>

Create a new Job record with the provided data.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_record_response = intellihr.jobs.create_record(
    person={
        "id": "8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
        "name": "Bruce Wayne",
        "primary_email_address": "bruce.wayne@example.com",
        "employee_number": "00001",
        "auto_increment_intellihr_id": "1000",
    },
    company_start_date="2015-03-01T22:30:00+00:00",
    name="Food Scientist",
    business_entity={
        "id": "8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
        "name": "IntelliHR",
        "legal_name": "IntelliHR Systems Limited",
        "number": "00 000 000 000",
    },
    business_unit={
        "id": "8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
        "name": "Engineering",
    },
    work_class={
        "id": "8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
        "name": "Casual",
    },
    company_end_date="2015-03-01T22:30:00+00:00",
    start_date="2015-03-01T22:30:00+00:00",
    end_date="2015-03-01T22:30:00+00:00",
    establishment={
        "id": "8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
        "name": "NewCo Software Engineer",
    },
    supervisor_person={
        "id": "8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
        "name": "Bruce Wayne",
        "primary_email_address": "bruce.wayne@example.com",
        "employee_number": "00001",
        "auto_increment_intellihr_id": "1000",
    },
    supervisor_job={
        "id": "8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
        "name": "Janitor",
    },
    location={
        "id": "8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
        "name": "Brisbane Office",
        "address": "1234 Queen Street, Brisbane City QLD 4000",
    },
    work_type={
        "id": "8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
        "name": "Permanent",
    },
    fte="1",
    pay_grade={
        "id": "8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
        "code": "L0",
        "name": "Founder",
    },
    employment_condition={
        "id": "8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
        "name": "Professional Employees Award 2010",
        "award_name": "MA000065: Professional Employees Award 2010 - Fair Work Commission",
    },
    remuneration_schedule={
        "type": "Annual Salary",
        "pay_cycle": "Fortnightly",
        "currency": "AUD",
        "hours_per_cycle": 80,
        "base_annual_salary": 50000,
        "base_hourly_rate": 24,
        "additions": [None],
        "additions_to_total": [None],
    },
    recruitment={
        "cost": 5000,
        "currency": "AUD",
    },
    custom_fields={
        "key": {
        },
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### person: [`JobCreateRequestPerson`](./intelli_hr_python_sdk/type/job_create_request_person.py)<a id="person-jobcreaterequestpersonintelli_hr_python_sdktypejob_create_request_personpy"></a>


##### company_start_date: `str`<a id="company_start_date-str"></a>

The date this [Job](https://developers.intellihr.io/docs/v1/) started or will start within the organisation. This date will follow the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6).   YYYY-MM-DD date formatting is also supported, although by using this format the date will be stored as the start of day in UTC time, not the requesting tenants timezone.

##### name: `str`<a id="name-str"></a>

The job name assigned to this [Job](https://developers.intellihr.io/docs/v1/). Will attempt to match to an existing [Position Title](https://developers.intellihr.io/docs/v1/), otherwise creates a new [Position Title](https://developers.intellihr.io/docs/v1/).

##### business_entity: [`JobCreateRequestBusinessEntity`](./intelli_hr_python_sdk/type/job_create_request_business_entity.py)<a id="business_entity-jobcreaterequestbusinessentityintelli_hr_python_sdktypejob_create_request_business_entitypy"></a>


##### business_unit: [`JobCreateRequestBusinessUnit`](./intelli_hr_python_sdk/type/job_create_request_business_unit.py)<a id="business_unit-jobcreaterequestbusinessunitintelli_hr_python_sdktypejob_create_request_business_unitpy"></a>


##### work_class: [`JobCreateRequestWorkClass`](./intelli_hr_python_sdk/type/job_create_request_work_class.py)<a id="work_class-jobcreaterequestworkclassintelli_hr_python_sdktypejob_create_request_work_classpy"></a>


##### company_end_date: `str`<a id="company_end_date-str"></a>

The <b>exclusive</b> date this [Job](https://developers.intellihr.io/docs/v1/) ended or will end within the organisation. For example, if the person's last working date is on 2025-04-23, the `companyEndDate` should be set as 2025-04-24 to reflect the exclusive date. This date will follow the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6).   YYYY-MM-DD date formatting is also supported, although by using this format the date will be stored as the start of day in UTC time, not the requesting tenants timezone.

##### start_date: `str`<a id="start_date-str"></a>

The date this [Job](https://developers.intellihr.io/docs/v1/) started or will start within the organisation. This date will follow the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6).   YYYY-MM-DD date formatting is also supported, although by using this format the date will be stored as the start of day in UTC time, not the requesting tenants timezone.

##### end_date: `str`<a id="end_date-str"></a>

The <b>exclusive</b> date this [Job](https://developers.intellihr.io/docs/v1/) ended or will end within the organisation. For example, if the person's last working date is on 2025-04-23, the `endDate` should be set as 2025-04-24 to reflect the exclusive date. This date will follow the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6).   YYYY-MM-DD date formatting is also supported, although by using this format the date will be stored as the start of day in UTC time, not the requesting tenants timezone.

##### establishment: [`JobCreateRequestEstablishment`](./intelli_hr_python_sdk/type/job_create_request_establishment.py)<a id="establishment-jobcreaterequestestablishmentintelli_hr_python_sdktypejob_create_request_establishmentpy"></a>


##### supervisor_person: [`JobCreateRequestSupervisorPerson`](./intelli_hr_python_sdk/type/job_create_request_supervisor_person.py)<a id="supervisor_person-jobcreaterequestsupervisorpersonintelli_hr_python_sdktypejob_create_request_supervisor_personpy"></a>


##### supervisor_job: [`JobCreateRequestSupervisorJob`](./intelli_hr_python_sdk/type/job_create_request_supervisor_job.py)<a id="supervisor_job-jobcreaterequestsupervisorjobintelli_hr_python_sdktypejob_create_request_supervisor_jobpy"></a>


##### location: [`JobCreateRequestLocation`](./intelli_hr_python_sdk/type/job_create_request_location.py)<a id="location-jobcreaterequestlocationintelli_hr_python_sdktypejob_create_request_locationpy"></a>


##### work_type: [`JobCreateRequestWorkType`](./intelli_hr_python_sdk/type/job_create_request_work_type.py)<a id="work_type-jobcreaterequestworktypeintelli_hr_python_sdktypejob_create_request_work_typepy"></a>


##### fte: `str`<a id="fte-str"></a>

The full time equivalent of this [Job](https://developers.intellihr.io/docs/v1/). Indicating the workload of an employee that can be comparable across different contexts. This is null for people without an FTE.

##### pay_grade: [`JobCreateRequestPayGrade`](./intelli_hr_python_sdk/type/job_create_request_pay_grade.py)<a id="pay_grade-jobcreaterequestpaygradeintelli_hr_python_sdktypejob_create_request_pay_gradepy"></a>


##### employment_condition: [`JobCreateRequestEmploymentCondition`](./intelli_hr_python_sdk/type/job_create_request_employment_condition.py)<a id="employment_condition-jobcreaterequestemploymentconditionintelli_hr_python_sdktypejob_create_request_employment_conditionpy"></a>


##### remuneration_schedule: [`JobCreateRequestRemunerationSchedule`](./intelli_hr_python_sdk/type/job_create_request_remuneration_schedule.py)<a id="remuneration_schedule-jobcreaterequestremunerationscheduleintelli_hr_python_sdktypejob_create_request_remuneration_schedulepy"></a>


##### recruitment: [`JobCreateRequestRecruitment`](./intelli_hr_python_sdk/type/job_create_request_recruitment.py)<a id="recruitment-jobcreaterequestrecruitmentintelli_hr_python_sdktypejob_create_request_recruitmentpy"></a>


##### custom_fields: [`JobCreateRequestCustomFields`](./intelli_hr_python_sdk/type/job_create_request_custom_fields.py)<a id="custom_fields-jobcreaterequestcustomfieldsintelli_hr_python_sdktypejob_create_request_custom_fieldspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`JobCreateRequest`](./intelli_hr_python_sdk/type/job_create_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`JobCreateResponse`](./intelli_hr_python_sdk/pydantic/job_create_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/jobs` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.jobs.find_by_id`<a id="intellihrjobsfind_by_id"></a>

Get a single Job record by UUIDv4 identifier.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_by_id_response = intellihr.jobs.find_by_id(
    as_at="2015-03-01T22:30:00+00:00",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### as_at: `str`<a id="as_at-str"></a>

Used to configure what date to return this job data for, as a [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6) datetime.   All data returned from the job endpoints represent the values of the Person's job attributes at a specific point in time.   By default, the current datetime is used, but this parameter can be used to configure a different datetime to see historical data.

#### 🔄 Return<a id="🔄-return"></a>

[`Jobs`](./intelli_hr_python_sdk/pydantic/jobs.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/jobs/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.jobs.get_all`<a id="intellihrjobsget_all"></a>

Returns a list of all [Job](https://developers.intellihr.io/docs/v1/) entity records as at the current date.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = intellihr.jobs.get_all(
    filters={
        "person_id": "dc996d73-a75e-499c-a96e-bd7d0df45f57,26d0ffc4-60f6-4672-a603-caaa4564af12",
        "person_name": "Batman",
        "primary_email": "bruce.wayne@example.com",
        "employee_number": "00001",
        "auto_increment_intellihr_id": 1000,
        "job_id": "dc996d73-a75e-499c-a96e-bd7d0df45f57,26d0ffc4-60f6-4672-a603-caaa4564af12",
        "job_name": "Food%20Scientist",
        "job_name_as_at": "2020-10-08T22%3A30%3A00%2B00%3A00",
        "job_status": "Current%20Job",
        "job_ending_within": "14",
        "job_ended_within": "14",
        "updated_within": "14",
        "work_type": "Fixed%20Contract",
        "is_primary_job": "true",
        "employment_condition_id": "8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
    },
    sort="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### filters: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./intelli_hr_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="filters-dictstr-unionbool-date-datetime-dict-float-int-list-str-noneintelli_hr_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Filters can be applied in the query string to limit the data returned from this endpoint. Filters are provided in the format `filters[<filter_name>][<operation_type>]=<filter_value>`.For example, a filter to get items matching a specific filter value would be `filters[personId][eq]=dc996d73-a75e-499c-a96e-bd7d0df45f57,26d0ffc4-60f6-4672-a603-caaa4564af12`  Below is a list of operation types available on filters, note that each filter may not support every type:  • Equality `[eq]`: Checks for an exact match with the given filter value  The list of supported filters is given below.

##### sort: `str`<a id="sort-str"></a>

Sorting can be applied in the query string to order the data returned from this endpoint. Sort can be prepended with a minus to return the data in descending (-) order. For example, a sort to get the most recent records first would be `-createdAt`.

#### 🔄 Return<a id="🔄-return"></a>

[`JobsList`](./intelli_hr_python_sdk/pydantic/jobs_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/jobs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.jobs.update_attributes`<a id="intellihrjobsupdate_attributes"></a>

Patch attributes of an existing Job record with the provided data.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_attributes_response = intellihr.jobs.update_attributes(
    effective_from=None,
    effective_to="2015-03-01T22:30:00+00:00",
    name="Food Scientist",
    business_entity={
        "id": "8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
        "name": "IntelliHR",
        "legal_name": "IntelliHR Systems Limited",
        "number": "00 000 000 000",
    },
    business_unit={
        "id": "8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
        "name": "Engineering",
    },
    establishment={
        "id": "8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
        "name": "NewCo Software Engineer",
    },
    job_change_reason={
        "id": "8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
    },
    supervisor_person={
        "id": "8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
        "name": "Bruce Wayne",
        "primary_email_address": "bruce.wayne@example.com",
        "employee_number": "00001",
        "auto_increment_intellihr_id": "1000",
    },
    supervisor_job={
        "id": "8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
        "name": "Janitor",
    },
    location={
        "id": "8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
        "name": "Brisbane Office",
        "address": "1234 Queen Street, Brisbane City QLD 4000",
    },
    work_class={
        "id": "8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
        "name": "Casual",
    },
    work_type={
        "id": "8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
        "name": "Permanent",
    },
    fte="1",
    pay_grade={
        "id": "8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
        "code": "L0",
        "name": "Founder",
    },
    employment_condition={
        "id": "8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
        "name": "Professional Employees Award 2010",
        "award_name": "MA000065: Professional Employees Award 2010 - Fair Work Commission",
    },
    remuneration_schedule={
        "type": "Annual Salary",
        "pay_cycle": "Fortnightly",
        "currency": "AUD",
        "hours_per_cycle": 80,
        "base_annual_salary": 50000,
        "base_hourly_rate": 24,
        "additions": [None],
        "additions_to_total": [None],
    },
    custom_fields={
        "key": {
        },
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### effective_from: Union[`str`, `none_type`]<a id="effective_from-unionstr-none_type"></a>


The date this [Job](https://developers.intellihr.io/docs/v1/) Update is effective from within the organisation. Note that this doesn't affect the start date of the overall job itself. A `null` value will indicate that this Update is effective from the start of the [Job](https://developers.intellihr.io/docs/v1/). This date will follow the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6).   YYYY-MM-DD date formatting is also supported, although by using this format the date will be stored as the start of day in UTC time, not the requesting tenants timezone.

##### effective_to: `str`<a id="effective_to-str"></a>

The date this [Job](https://developers.intellihr.io/docs/v1/) Update is effective to within the organisation. Note that this doesn't affect the end date of the overall job itself. This date will follow the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6).   YYYY-MM-DD date formatting is also supported, although by using this format the date will be stored as the start of day in UTC time, not the requesting tenants timezone.

##### name: `str`<a id="name-str"></a>

The job name to be updated. Will attempt to match to an existing [Position Title](https://developers.intellihr.io/docs/v1/), otherwise creates a new [Position Title](https://developers.intellihr.io/docs/v1/).

##### business_entity: [`JobPatchRequestBusinessEntity`](./intelli_hr_python_sdk/type/job_patch_request_business_entity.py)<a id="business_entity-jobpatchrequestbusinessentityintelli_hr_python_sdktypejob_patch_request_business_entitypy"></a>


##### business_unit: [`JobPatchRequestBusinessUnit`](./intelli_hr_python_sdk/type/job_patch_request_business_unit.py)<a id="business_unit-jobpatchrequestbusinessunitintelli_hr_python_sdktypejob_patch_request_business_unitpy"></a>


##### establishment: [`JobPatchRequestEstablishment`](./intelli_hr_python_sdk/type/job_patch_request_establishment.py)<a id="establishment-jobpatchrequestestablishmentintelli_hr_python_sdktypejob_patch_request_establishmentpy"></a>


##### job_change_reason: [`JobPatchRequestJobChangeReason`](./intelli_hr_python_sdk/type/job_patch_request_job_change_reason.py)<a id="job_change_reason-jobpatchrequestjobchangereasonintelli_hr_python_sdktypejob_patch_request_job_change_reasonpy"></a>


##### supervisor_person: [`JobPatchRequestSupervisorPerson`](./intelli_hr_python_sdk/type/job_patch_request_supervisor_person.py)<a id="supervisor_person-jobpatchrequestsupervisorpersonintelli_hr_python_sdktypejob_patch_request_supervisor_personpy"></a>


##### supervisor_job: [`JobPatchRequestSupervisorJob`](./intelli_hr_python_sdk/type/job_patch_request_supervisor_job.py)<a id="supervisor_job-jobpatchrequestsupervisorjobintelli_hr_python_sdktypejob_patch_request_supervisor_jobpy"></a>


##### location: [`JobPatchRequestLocation`](./intelli_hr_python_sdk/type/job_patch_request_location.py)<a id="location-jobpatchrequestlocationintelli_hr_python_sdktypejob_patch_request_locationpy"></a>


##### work_class: [`JobPatchRequestWorkClass`](./intelli_hr_python_sdk/type/job_patch_request_work_class.py)<a id="work_class-jobpatchrequestworkclassintelli_hr_python_sdktypejob_patch_request_work_classpy"></a>


##### work_type: [`JobPatchRequestWorkType`](./intelli_hr_python_sdk/type/job_patch_request_work_type.py)<a id="work_type-jobpatchrequestworktypeintelli_hr_python_sdktypejob_patch_request_work_typepy"></a>


##### fte: `str`<a id="fte-str"></a>

The full time equivalent of this [Job](https://developers.intellihr.io/docs/v1/). Indicating the workload of an employee that can be comparable across different contexts. This is null for people without an FTE.

##### pay_grade: [`JobPatchRequestPayGrade`](./intelli_hr_python_sdk/type/job_patch_request_pay_grade.py)<a id="pay_grade-jobpatchrequestpaygradeintelli_hr_python_sdktypejob_patch_request_pay_gradepy"></a>


##### employment_condition: [`JobPatchRequestEmploymentCondition`](./intelli_hr_python_sdk/type/job_patch_request_employment_condition.py)<a id="employment_condition-jobpatchrequestemploymentconditionintelli_hr_python_sdktypejob_patch_request_employment_conditionpy"></a>


##### remuneration_schedule: [`JobPatchRequestRemunerationSchedule`](./intelli_hr_python_sdk/type/job_patch_request_remuneration_schedule.py)<a id="remuneration_schedule-jobpatchrequestremunerationscheduleintelli_hr_python_sdktypejob_patch_request_remuneration_schedulepy"></a>


##### custom_fields: [`JobPatchRequestCustomFields`](./intelli_hr_python_sdk/type/job_patch_request_custom_fields.py)<a id="custom_fields-jobpatchrequestcustomfieldsintelli_hr_python_sdktypejob_patch_request_custom_fieldspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`JobPatchRequest`](./intelli_hr_python_sdk/type/job_patch_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`JobPatchResponse`](./intelli_hr_python_sdk/pydantic/job_patch_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/jobs/{id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.locations.create_new_location`<a id="intellihrlocationscreate_new_location"></a>

Returns the created [Location](https://developers.intellihr.io/docs/v1/).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_location_response = intellihr.locations.create_new_location(
    name="Brisbane Office",
    parent_id=None,
    code="BE001",
    address="1234 Queen Street, Brisbane City QLD 4000",
    is_enabled=True,
    custom_fields={
        "key": {
        },
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name given to this [Location](https://developers.intellihr.io/docs/v1/). This name would normally be shown to users of the system.

##### parent_id: Union[`str`, `none_type`]<a id="parent_id-unionstr-none_type"></a>


The identifier string for the parent [Location](https://developers.intellihr.io/docs/v1/), or null if there is no parent (this is a top level location).

##### code: `str`<a id="code-str"></a>

Code given to this [Location](https://developers.intellihr.io/docs/v1/)

##### address: `str`<a id="address-str"></a>

The address of this location.

##### is_enabled: `bool`<a id="is_enabled-bool"></a>

Specifies whether users can select this [Location](https://developers.intellihr.io/docs/v1/) in dropdowns.

##### custom_fields: [`LocationsCreateRequestCustomFields`](./intelli_hr_python_sdk/type/locations_create_request_custom_fields.py)<a id="custom_fields-locationscreaterequestcustomfieldsintelli_hr_python_sdktypelocations_create_request_custom_fieldspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LocationsCreateRequest`](./intelli_hr_python_sdk/type/locations_create_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Locations`](./intelli_hr_python_sdk/pydantic/locations.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/locations` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.locations.delete_by_id`<a id="intellihrlocationsdelete_by_id"></a>

Deletes the [Location](https://developers.intellihr.io/docs/v1/)'s by the given ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
intellihr.locations.delete_by_id()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/locations/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.locations.find_location_by_id`<a id="intellihrlocationsfind_location_by_id"></a>

Returns a single location.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_location_by_id_response = intellihr.locations.find_location_by_id()
```

#### 🔄 Return<a id="🔄-return"></a>

[`Locations`](./intelli_hr_python_sdk/pydantic/locations.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/locations/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.locations.list_all`<a id="intellihrlocationslist_all"></a>

Returns a list of all locations.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = intellihr.locations.list_all()
```

#### 🔄 Return<a id="🔄-return"></a>

[`LocationsList`](./intelli_hr_python_sdk/pydantic/locations_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/locations` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.locations.update_by_id`<a id="intellihrlocationsupdate_by_id"></a>

Returns the updated [Location](https://developers.intellihr.io/docs/v1/).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_by_id_response = intellihr.locations.update_by_id(
    parent_id=None,
    name="Brisbane Office",
    code="BE001",
    address="1234 Queen Street, Brisbane City QLD 4000",
    is_enabled=True,
    custom_fields={
        "key": {
        },
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### parent_id: Union[`str`, `none_type`]<a id="parent_id-unionstr-none_type"></a>


The identifier string for the parent [Location](https://developers.intellihr.io/docs/v1/), or null if there is no parent (this is a top level location).

##### name: `str`<a id="name-str"></a>

Name given to this [Location](https://developers.intellihr.io/docs/v1/). This name would normally be shown to users of the system.

##### code: `str`<a id="code-str"></a>

Code given to this [Location](https://developers.intellihr.io/docs/v1/)

##### address: `str`<a id="address-str"></a>

The address of this location.

##### is_enabled: `bool`<a id="is_enabled-bool"></a>

Specifies whether users can select this [Location](https://developers.intellihr.io/docs/v1/) in dropdowns.

##### custom_fields: [`LocationsPatchRequestCustomFields`](./intelli_hr_python_sdk/type/locations_patch_request_custom_fields.py)<a id="custom_fields-locationspatchrequestcustomfieldsintelli_hr_python_sdktypelocations_patch_request_custom_fieldspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LocationsPatchRequest`](./intelli_hr_python_sdk/type/locations_patch_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Locations`](./intelli_hr_python_sdk/pydantic/locations.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/locations/{id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.pay_grades.create_record`<a id="intellihrpay_gradescreate_record"></a>

Create a new Pay Grade record with the provided data.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_record_response = intellihr.pay_grades.create_record(
    name="Founder",
    description="The founder pay grade",
    code="L0",
    employment_condition={
        "id": "8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
        "name": "Professional Employees Award 2010",
        "award_name": "MA000065: Professional Employees Award 2010 - Fair Work Commission",
    },
    pay_grade_type="FIXED",
    is_overridable=False,
    permanent_hourly_rate=25.5,
    permanent_hourly_rate_currency="AUD",
    casual_hourly_rate=25.5,
    casual_hourly_rate_currency="AUD",
    annual_salary=25.5,
    annual_salary_currency="AUD",
    pay_steps=[
        None
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

The name assigned to this [Pay Grade](https://developers.intellihr.io/docs/v1/).

##### description: `str`<a id="description-str"></a>

Description of the [Pay Grade](https://developers.intellihr.io/docs/v1/).

##### code: `str`<a id="code-str"></a>

Administrative, short code associated to the [Pay Grade](https://developers.intellihr.io/docs/v1/).

##### employment_condition: [`PayGradeCreateRequestEmploymentCondition`](./intelli_hr_python_sdk/type/pay_grade_create_request_employment_condition.py)<a id="employment_condition-paygradecreaterequestemploymentconditionintelli_hr_python_sdktypepay_grade_create_request_employment_conditionpy"></a>


##### pay_grade_type: `str`<a id="pay_grade_type-str"></a>

The type of this [Pay Grade](https://developers.intellihr.io/docs/v1/). Enum: `FIXED` or `STEP`.

##### is_overridable: `bool`<a id="is_overridable-bool"></a>

Allow this [Pay Grade](https://developers.intellihr.io/docs/v1/) value to be overwritten.

##### permanent_hourly_rate: `Union[int, float]`<a id="permanent_hourly_rate-unionint-float"></a>

Stores the hourly rate for permanent [Jobs](https://developers.intellihr.io/docs/v1/). These inputs will be ignored if you also pass in pay Step values.

##### permanent_hourly_rate_currency: `str`<a id="permanent_hourly_rate_currency-str"></a>

The currency that the permanentHourlyRate is being paid in. An international currency code. Typically AUD for Australian dollar, USD for American dollar etc. See [Official list of codes](https://www.iban.com/currency-codes).

##### casual_hourly_rate: `Union[int, float]`<a id="casual_hourly_rate-unionint-float"></a>

Stores the hourly rate for casual [Jobs](https://developers.intellihr.io/docs/v1/). These inputs will be ignored if you also pass in pay Step values.

##### casual_hourly_rate_currency: `str`<a id="casual_hourly_rate_currency-str"></a>

The currency that the casualHourlyRate is being paid in. An international currency code. Typically AUD for Australian dollar, USD for American dollar etc. See [Official list of codes](https://www.iban.com/currency-codes).

##### annual_salary: `Union[int, float]`<a id="annual_salary-unionint-float"></a>

Stores the annual salary for [Jobs](https://developers.intellihr.io/docs/v1/). These inputs will be ignored if you also pass in pay Step values.

##### annual_salary_currency: `str`<a id="annual_salary_currency-str"></a>

The currency that the annualSalary is being paid in. An international currency code. Typically AUD for Australian dollar, USD for American dollar etc. See [Official list of codes](https://www.iban.com/currency-codes).

##### pay_steps: [`PayGradeCreateRequestPaySteps`](./intelli_hr_python_sdk/type/pay_grade_create_request_pay_steps.py)<a id="pay_steps-paygradecreaterequestpaystepsintelli_hr_python_sdktypepay_grade_create_request_pay_stepspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PayGradeCreateRequest`](./intelli_hr_python_sdk/type/pay_grade_create_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PayGrades`](./intelli_hr_python_sdk/pydantic/pay_grades.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/pay-grades` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.pay_grades.delete_by_id`<a id="intellihrpay_gradesdelete_by_id"></a>

Deletes the [Pay Grade](https://developers.intellihr.io/docs/v1/) by the given ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
intellihr.pay_grades.delete_by_id()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/pay-grades/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.pay_grades.find_by_id`<a id="intellihrpay_gradesfind_by_id"></a>

Returns a single pay grade.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_by_id_response = intellihr.pay_grades.find_by_id(
    as_at="2015-03-01T22:30:00+00:00",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### as_at: `str`<a id="as_at-str"></a>

Used to configure what date to return this data, as a [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6) datetime.   All data returned from the endpoints represent the values of the attributes at a specific point in time.   By default, the current datetime is used, but this parameter can be used to configure a different datetime to see historical data.

#### 🔄 Return<a id="🔄-return"></a>

[`PayGrades`](./intelli_hr_python_sdk/pydantic/pay_grades.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/pay-grades/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.pay_grades.get_all`<a id="intellihrpay_gradesget_all"></a>

Returns a list of all pay grades.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = intellihr.pay_grades.get_all(
    as_at="2015-03-01T22:30:00+00:00",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### as_at: `str`<a id="as_at-str"></a>

Used to configure what date to return this data, as a [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6) datetime.   All data returned from the endpoints represent the values of the attributes at a specific point in time.   By default, the current datetime is used, but this parameter can be used to configure a different datetime to see historical data.

#### 🔄 Return<a id="🔄-return"></a>

[`PayGradesList`](./intelli_hr_python_sdk/pydantic/pay_grades_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/pay-grades` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.pay_grades.update_record`<a id="intellihrpay_gradesupdate_record"></a>

Patch attributes of an existing Pay Grade record with the provided data.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_record_response = intellihr.pay_grades.update_record(
    effective_from="2015-03-01T22:30:00+00:00",
    description="The founder pay grade",
    effective_to="2015-03-01T22:30:00+00:00",
    is_enabled=True,
    name="Founder",
    code="L0",
    employment_condition={
        "id": "8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
        "name": "Professional Employees Award 2010",
        "award_name": "MA000065: Professional Employees Award 2010 - Fair Work Commission",
    },
    pay_grade_type="FIXED",
    is_overridable=True,
    permanent_hourly_rate=25.5,
    permanent_hourly_rate_currency="AUD",
    casual_hourly_rate=25.5,
    casual_hourly_rate_currency="AUD",
    annual_salary=25.5,
    annual_salary_currency="AUD",
    pay_steps=[
        None
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### effective_from: `str`<a id="effective_from-str"></a>

The date this [Pay Grade](https://developers.intellihr.io/docs/v1/) Update is effective from within the organisation. Note that this doesn't affect the availableFrom date of the overall Pay Grade itself.  Not providing an effectiveFrom will apply the changes from the beggining of time.. This date will follow the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6).   YYYY-MM-DD date formatting is also supported, although by using this format the date will be stored as the start of day in UTC time, not the requesting tenants timezone.

##### description: `str`<a id="description-str"></a>

Description of the [Pay Grade](https://developers.intellihr.io/docs/v1/).

##### effective_to: `str`<a id="effective_to-str"></a>

The date this [Pay Grade](https://developers.intellihr.io/docs/v1/) Update is effective to within the organisation.. This date will follow the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6).   YYYY-MM-DD date formatting is also supported, although by using this format the date will be stored as the start of day in UTC time, not the requesting tenants timezone.

##### is_enabled: `bool`<a id="is_enabled-bool"></a>

Toggle the availability of the [Pay Grade](https://developers.intellihr.io/docs/v1/) on or off within the organisation.

##### name: `str`<a id="name-str"></a>

The name assigned to this [Pay Grade](https://developers.intellihr.io/docs/v1/).

##### code: `str`<a id="code-str"></a>

Administrative, short code associated to the [Pay Grade](https://developers.intellihr.io/docs/v1/).

##### employment_condition: [`PayGradeUpdateRequestEmploymentCondition`](./intelli_hr_python_sdk/type/pay_grade_update_request_employment_condition.py)<a id="employment_condition-paygradeupdaterequestemploymentconditionintelli_hr_python_sdktypepay_grade_update_request_employment_conditionpy"></a>


##### pay_grade_type: `str`<a id="pay_grade_type-str"></a>

The type of this [Pay Grade](https://developers.intellihr.io/docs/v1/). Enum: `FIXED` or `STEP`.

##### is_overridable: `bool`<a id="is_overridable-bool"></a>

Allow this [Pay Grade](https://developers.intellihr.io/docs/v1/) value to be overwritten.

##### permanent_hourly_rate: `Union[int, float]`<a id="permanent_hourly_rate-unionint-float"></a>

Stores the hourly rate for permanent [Jobs](https://developers.intellihr.io/docs/v1/). These inputs will be ignored if you also pass in pay Step values.

##### permanent_hourly_rate_currency: `str`<a id="permanent_hourly_rate_currency-str"></a>

The currency that the permanentHourlyRate is being paid in. An international currency code. Typically AUD for Australian dollar, USD for American dollar etc. See [Official list of codes](https://www.iban.com/currency-codes).

##### casual_hourly_rate: `Union[int, float]`<a id="casual_hourly_rate-unionint-float"></a>

Stores the hourly rate for casual [Jobs](https://developers.intellihr.io/docs/v1/). These inputs will be ignored if you also pass in pay Step values.

##### casual_hourly_rate_currency: `str`<a id="casual_hourly_rate_currency-str"></a>

The currency that the casualHourlyRate is being paid in. An international currency code. Typically AUD for Australian dollar, USD for American dollar etc. See [Official list of codes](https://www.iban.com/currency-codes).

##### annual_salary: `Union[int, float]`<a id="annual_salary-unionint-float"></a>

Stores the annual salary for [Jobs](https://developers.intellihr.io/docs/v1/). These inputs will be ignored if you also pass in pay Step values.

##### annual_salary_currency: `str`<a id="annual_salary_currency-str"></a>

The currency that the annualSalary is being paid in. An international currency code. Typically AUD for Australian dollar, USD for American dollar etc. See [Official list of codes](https://www.iban.com/currency-codes).

##### pay_steps: [`PayGradeUpdateRequestPaySteps`](./intelli_hr_python_sdk/type/pay_grade_update_request_pay_steps.py)<a id="pay_steps-paygradeupdaterequestpaystepsintelli_hr_python_sdktypepay_grade_update_request_pay_stepspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PayGradeUpdateRequest`](./intelli_hr_python_sdk/type/pay_grade_update_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PayGrades`](./intelli_hr_python_sdk/pydantic/pay_grades.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/pay-grades/{id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.people.create_new_person`<a id="intellihrpeoplecreate_new_person"></a>

Create a person

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_person_response = intellihr.people.create_new_person(
    last_name="Wayne",
    title=None,
    first_name=None,
    middle_name=None,
    preferred_name=None,
    date_of_birth=None,
    gender="Other",
    employee_number=None,
    emergency_contact={
    },
    primary_email_address=None,
    primary_phone_number=None,
    email_addresses=[None],
    phone_numbers=[None],
    addresses=[None],
    custom_fields={
        "key": {
        },
    },
    medical_conditions=[
        {
            "body": "Mild Insomnia",
            "is_public": False,
        }
    ],
    work_right={
        "id": "8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
        "name": "Australian Citizen",
    },
    work_right_expiry_date=None,
    user_account=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### last_name: `str`<a id="last_name-str"></a>

The [Person's](https://developers.intellihr.io/docs/v1/) Last Name.

##### title: Union[`str`, `none_type`]<a id="title-unionstr-none_type"></a>


The title to refer to this [Person](https://developers.intellihr.io/docs/v1/) as, for example \\\"Mr\\\". This is null if not provided and is case insensitive.

##### first_name: Union[`str`, `none_type`]<a id="first_name-unionstr-none_type"></a>


The [Person's](https://developers.intellihr.io/docs/v1/) First Name.

##### middle_name: Union[`str`, `none_type`]<a id="middle_name-unionstr-none_type"></a>


The [Person's](https://developers.intellihr.io/docs/v1/) Middle Name.

##### preferred_name: Union[`str`, `none_type`]<a id="preferred_name-unionstr-none_type"></a>


The [Person's](https://developers.intellihr.io/docs/v1/) Preferred Name. Can generally be configured by employees for themselves.

##### date_of_birth: Union[`str`, `none_type`]<a id="date_of_birth-unionstr-none_type"></a>


Date of Birth (YYYY-MM-DD).

##### gender: `str`<a id="gender-str"></a>

Human readable string for the [Person's](https://developers.intellihr.io/docs/v1/) gender, e.g. `Male`. Searching is done case-insensitively and 'starts-with' e.g. passing `male` will match with a [Gender](https://developers.intellihr.io/docs/v1/) called \\\"Male\\\" as will \\\"m\\\" or \\\"M\\\". If multiple [Genders](https://developers.intellihr.io/docs/v1/) match the first will be chosen. The gender options available are: `Female`, `Male`, `Non-binary`, `Other`, `Undisclosed`.

##### employee_number: Union[`str`, `none_type`]<a id="employee_number-unionstr-none_type"></a>


A manually entered employee number that identifies a [Person](https://developers.intellihr.io/docs/v1/) in intelliHR. It may be hidden in the system's UI depending upon your tenant's configuration.

##### emergency_contact: [`PeopleCreateRequestEmergencyContact`](./intelli_hr_python_sdk/type/people_create_request_emergency_contact.py)<a id="emergency_contact-peoplecreaterequestemergencycontactintelli_hr_python_sdktypepeople_create_request_emergency_contactpy"></a>


##### primary_email_address: Union[`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`, `none_type`]<a id="primary_email_address-uniondictstr-unionbool-date-datetime-dict-float-int-list-str-none-none_type"></a>


Information about this [Person's](https://developers.intellihr.io/docs/v1/) primary email address, or null if they have no email information.  The provided email address will be converted to lowercase. The field is also required when creating a user alongside with the person.

##### primary_phone_number: Union[`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`, `none_type`]<a id="primary_phone_number-uniondictstr-unionbool-date-datetime-dict-float-int-list-str-none-none_type"></a>


Information about this [Person's](https://developers.intellihr.io/docs/v1/) primary phone number, or null if they have no phone information.

##### email_addresses: [`PeopleCreateRequestEmailAddresses`](./intelli_hr_python_sdk/type/people_create_request_email_addresses.py)<a id="email_addresses-peoplecreaterequestemailaddressesintelli_hr_python_sdktypepeople_create_request_email_addressespy"></a>

##### phone_numbers: [`PeopleCreateRequestPhoneNumbers`](./intelli_hr_python_sdk/type/people_create_request_phone_numbers.py)<a id="phone_numbers-peoplecreaterequestphonenumbersintelli_hr_python_sdktypepeople_create_request_phone_numberspy"></a>

##### addresses: [`PeopleCreateRequestAddresses`](./intelli_hr_python_sdk/type/people_create_request_addresses.py)<a id="addresses-peoplecreaterequestaddressesintelli_hr_python_sdktypepeople_create_request_addressespy"></a>

##### custom_fields: [`PeopleCreateRequestCustomFields`](./intelli_hr_python_sdk/type/people_create_request_custom_fields.py)<a id="custom_fields-peoplecreaterequestcustomfieldsintelli_hr_python_sdktypepeople_create_request_custom_fieldspy"></a>

##### medical_conditions: [`PeopleCreateRequestMedicalConditions`](./intelli_hr_python_sdk/type/people_create_request_medical_conditions.py)<a id="medical_conditions-peoplecreaterequestmedicalconditionsintelli_hr_python_sdktypepeople_create_request_medical_conditionspy"></a>

##### work_right: [`PeopleCreateRequestWorkRight`](./intelli_hr_python_sdk/type/people_create_request_work_right.py)<a id="work_right-peoplecreaterequestworkrightintelli_hr_python_sdktypepeople_create_request_work_rightpy"></a>


##### work_right_expiry_date: Union[`str`, `none_type`]<a id="work_right_expiry_date-unionstr-none_type"></a>


The date this [Work Right](https://developers.intellihr.io/docs/v1/) will expire for this [Person](https://developers.intellihr.io/docs/v1/) (YYYY-MM-DD).

##### user_account: Union[`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`, `none_type`]<a id="user_account-uniondictstr-unionbool-date-datetime-dict-float-int-list-str-none-none_type"></a>


Details about this [Person's](https://developers.intellihr.io/docs/v1/) linked user account. Including this object will create a user account linked to this person, allowing them to login to the platform. If excluded the person will be created without an accompanying user account.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PeopleCreateRequest`](./intelli_hr_python_sdk/type/people_create_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`People`](./intelli_hr_python_sdk/pydantic/people.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.people.find_by_id`<a id="intellihrpeoplefind_by_id"></a>

Get a single Person record by UUIDv4 identifier.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_by_id_response = intellihr.people.find_by_id()
```

#### 🔄 Return<a id="🔄-return"></a>

[`People`](./intelli_hr_python_sdk/pydantic/people.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.people.list_all_people`<a id="intellihrpeoplelist_all_people"></a>

Returns a list of all [People](https://developers.intellihr.io/docs/v1/) as at the current date.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_people_response = intellihr.people.list_all_people(
    filters={
        "job_id": "dc996d73-a75e-499c-a96e-bd7d0df45f57,26d0ffc4-60f6-4672-a603-caaa4564af12",
        "primary_email_address": "bruce.wayne@batman.org",
        "employee_number": "00001",
        "auto_increment_intellihr_id": 1000,
        "name": "Batman%20(Bruce)%20Wayne",
        "updated_within": 30,
        "is_on_extended_leave": "true",
    },
    sort="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### filters: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./intelli_hr_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="filters-dictstr-unionbool-date-datetime-dict-float-int-list-str-noneintelli_hr_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Filters can be applied in the query string to limit the data returned from this endpoint. Filters are provided in the format `filters[<filter_name>][<operation_type>]=<filter_value>`.For example, a filter to get items matching a specific filter value would be `filters[jobId][eq]=dc996d73-a75e-499c-a96e-bd7d0df45f57,26d0ffc4-60f6-4672-a603-caaa4564af12`  Below is a list of operation types available on filters, note that each filter may not support every type:  • Equality `[eq]`: Checks for an exact match with the given filter value  The list of supported filters is given below.

##### sort: `str`<a id="sort-str"></a>

Sorting can be applied in the query string to order the data returned from this endpoint. Sort can be prepended with a minus to return the data in descending (-) order. For example, a sort to get the most recent records first would be `-createdAt`.

#### 🔄 Return<a id="🔄-return"></a>

[`PeopleList`](./intelli_hr_python_sdk/pydantic/people_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.people.update_person_by_id`<a id="intellihrpeopleupdate_person_by_id"></a>

Update a person

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_person_by_id_response = intellihr.people.update_person_by_id(
    title=None,
    first_name=None,
    middle_name=None,
    last_name="Wayne",
    preferred_name=None,
    date_of_birth=None,
    gender="Other",
    employee_number=None,
    emergency_contact={
    },
    email_addresses=[None],
    phone_numbers=[None],
    addresses=[None],
    custom_fields={
        "key": {
        },
    },
    medical_conditions=[
        {
            "body": "Mild Insomnia",
            "is_public": False,
        }
    ],
    work_right=None,
    work_right_expiry_date=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### title: Union[`str`, `none_type`]<a id="title-unionstr-none_type"></a>


The title to refer to this [Person](https://developers.intellihr.io/docs/v1/) as, for example \\\"Mr\\\". This is null if not provided and is case insensitive.

##### first_name: Union[`str`, `none_type`]<a id="first_name-unionstr-none_type"></a>


The [Person's](https://developers.intellihr.io/docs/v1/) First Name.

##### middle_name: Union[`str`, `none_type`]<a id="middle_name-unionstr-none_type"></a>


The [Person's](https://developers.intellihr.io/docs/v1/) Middle Name.

##### last_name: `str`<a id="last_name-str"></a>

The [Person's](https://developers.intellihr.io/docs/v1/) Last Name.

##### preferred_name: Union[`str`, `none_type`]<a id="preferred_name-unionstr-none_type"></a>


The [Person's](https://developers.intellihr.io/docs/v1/) Preferred Name. Can generally be configured by employees for themselves.

##### date_of_birth: Union[`str`, `none_type`]<a id="date_of_birth-unionstr-none_type"></a>


Date of Birth (YYYY-MM-DD).

##### gender: `str`<a id="gender-str"></a>

Human readable string for the [Person's](https://developers.intellihr.io/docs/v1/) gender, e.g. `Male`. Searching is done case-insensitively and 'starts-with' e.g. passing `male` will match with a [Gender](https://developers.intellihr.io/docs/v1/) called \\\"Male\\\" as will \\\"m\\\" or \\\"M\\\". If multiple [Genders](https://developers.intellihr.io/docs/v1/) match the first will be chosen. The gender options available are: `Female`, `Male`, `Non-binary`, `Other`, `Undisclosed`.

##### employee_number: Union[`str`, `none_type`]<a id="employee_number-unionstr-none_type"></a>


A manually entered employee number that identifies a [Person](https://developers.intellihr.io/docs/v1/) in intelliHR. It may be hidden in the system's UI depending upon your tenant's configuration.

##### emergency_contact: [`PeopleUpdateRequestEmergencyContact`](./intelli_hr_python_sdk/type/people_update_request_emergency_contact.py)<a id="emergency_contact-peopleupdaterequestemergencycontactintelli_hr_python_sdktypepeople_update_request_emergency_contactpy"></a>


##### email_addresses: [`PeopleUpdateRequestEmailAddresses`](./intelli_hr_python_sdk/type/people_update_request_email_addresses.py)<a id="email_addresses-peopleupdaterequestemailaddressesintelli_hr_python_sdktypepeople_update_request_email_addressespy"></a>

##### phone_numbers: [`PeopleUpdateRequestPhoneNumbers`](./intelli_hr_python_sdk/type/people_update_request_phone_numbers.py)<a id="phone_numbers-peopleupdaterequestphonenumbersintelli_hr_python_sdktypepeople_update_request_phone_numberspy"></a>

##### addresses: [`PeopleUpdateRequestAddresses`](./intelli_hr_python_sdk/type/people_update_request_addresses.py)<a id="addresses-peopleupdaterequestaddressesintelli_hr_python_sdktypepeople_update_request_addressespy"></a>

##### custom_fields: [`PeopleUpdateRequestCustomFields`](./intelli_hr_python_sdk/type/people_update_request_custom_fields.py)<a id="custom_fields-peopleupdaterequestcustomfieldsintelli_hr_python_sdktypepeople_update_request_custom_fieldspy"></a>

##### medical_conditions: [`PeopleUpdateRequestMedicalConditions`](./intelli_hr_python_sdk/type/people_update_request_medical_conditions.py)<a id="medical_conditions-peopleupdaterequestmedicalconditionsintelli_hr_python_sdktypepeople_update_request_medical_conditionspy"></a>

##### work_right: Union[`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`, `none_type`]<a id="work_right-uniondictstr-unionbool-date-datetime-dict-float-int-list-str-none-none_type"></a>


[Work Right](https://developers.intellihr.io/docs/v1/) to whom this [Person](https://developers.intellihr.io/docs/v1/) belongs. This [Work Right](https://developers.intellihr.io/docs/v1/) is specified as a search object, which will match the work right which best fits the keys for this object. Multiple keys can be used together to further narrow search results. Null can be provided to remove a person's work right.

##### work_right_expiry_date: Union[`str`, `none_type`]<a id="work_right_expiry_date-unionstr-none_type"></a>


The date this [Work Right](https://developers.intellihr.io/docs/v1/) will expire for this [Person](https://developers.intellihr.io/docs/v1/) (YYYY-MM-DD).

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PeopleUpdateRequest`](./intelli_hr_python_sdk/type/people_update_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`People`](./intelli_hr_python_sdk/pydantic/people.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.people_documents.create_presigned_upload_url`<a id="intellihrpeople_documentscreate_presigned_upload_url"></a>

Create a presigned upload URL

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_presigned_upload_url_response = intellihr.people_documents.create_presigned_upload_url(
    filename="OfferLetter.pdf",
    mime="application/pdf",
    size=300,
    extension="pdf",
    person_id="personId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### filename: `str`<a id="filename-str"></a>

The filename of the document. This will be used for display name. Includes extension.

##### mime: `str`<a id="mime-str"></a>

The mime type of the document

##### size: `int`<a id="size-int"></a>

The size in bytes. We use this to validate the upload was successful so must match the actual file size

##### extension: `str`<a id="extension-str"></a>

The extension of the document, not including the dot

##### person_id: `str`<a id="person_id-str"></a>

personId parameter

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PeopleDocumentsCreateRequest`](./intelli_hr_python_sdk/type/people_documents_create_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PeopleDocumentsCreateResponse`](./intelli_hr_python_sdk/pydantic/people_documents_create_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{personId}/documents` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.people_documents.list`<a id="intellihrpeople_documentslist"></a>

Returns a list of all [Documents](https://developers.intellihr.io/docs/v1/) of a given [person]((https://developers.intellihr.io/docs/v1/).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = intellihr.people_documents.list(
    person_id="personId_example",
    limit=1,
    page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### person_id: `str`<a id="person_id-str"></a>

Id string param for relevant [Person](https://developers.intellihr.io/docs/v1/)

##### limit: `int`<a id="limit-int"></a>

The number of items per page

##### page: `int`<a id="page-int"></a>

The page number

#### 🔄 Return<a id="🔄-return"></a>

[`PeopleDocumentsFindResponse`](./intelli_hr_python_sdk/pydantic/people_documents_find_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{personId}/documents` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.people_documents.update_document`<a id="intellihrpeople_documentsupdate_document"></a>

Update a Document

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_document_response = intellihr.people_documents.update_document(
    person_id="personId_example",
    filename="OfferLetter.pdf",
    upload_status=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### person_id: `str`<a id="person_id-str"></a>

personId parameter

##### filename: `str`<a id="filename-str"></a>

The filename of the document. This will be used for display name. Includes extension.

##### upload_status: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./intelli_hr_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="upload_status-unionbool-date-datetime-dict-float-int-list-str-noneintelli_hr_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

The upload status of this [Document](https://developers.intellihr.io/docs/v1/). Enum: `SUCCESS`, `PENDING`, `FAILED`.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PeopleDocumentsPatchRequest`](./intelli_hr_python_sdk/type/people_documents_patch_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PeopleDocumentsPatchResponse`](./intelli_hr_python_sdk/pydantic/people_documents_patch_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{personId}/documents/{id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.people_images.generate_temporary_image_url`<a id="intellihrpeople_imagesgenerate_temporary_image_url"></a>

Generates an upload url for an temporary image of the specified type to an existing [Person](https://developers.intellihr.io/docs/v1/)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_temporary_image_url_response = intellihr.people_images.generate_temporary_image_url(
    person_id="personId_example",
    image_type="PERSON_PROFILE",
    extension="png",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### person_id: `str`<a id="person_id-str"></a>

Id string param for relevant [Person](https://developers.intellihr.io/docs/v1/)

##### image_type: `str`<a id="image_type-str"></a>

The Image Type. Enum: `PERSON_PROFILE`, `PROFILE_COVER`.

##### extension: `str`<a id="extension-str"></a>

The extension of the image, not including the dot

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PersonIdImageCreateRequest`](./intelli_hr_python_sdk/type/person_id_image_create_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PersonIdImageCreateResponse`](./intelli_hr_python_sdk/pydantic/person_id_image_create_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{personId}/images` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.people_images.get_temporary_image`<a id="intellihrpeople_imagesget_temporary_image"></a>

Returns the current temporary image of the specified type for the provided [Person](https://developers.intellihr.io/docs/v1/).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_temporary_image_response = intellihr.people_images.get_temporary_image(
    person_id="personId_example",
    image_type="PERSON_PROFILE",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### person_id: `str`<a id="person_id-str"></a>

Id string param for relevant [Person](https://developers.intellihr.io/docs/v1/)

##### image_type: `str`<a id="image_type-str"></a>

The Image Type. Enum: `PERSON_PROFILE`, `PROFILE_COVER`.

#### 🔄 Return<a id="🔄-return"></a>

[`PersonIdImageFindResponse`](./intelli_hr_python_sdk/pydantic/person_id_image_find_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{personId}/images` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.people_images.promote_image`<a id="intellihrpeople_imagespromote_image"></a>

Activates the temporary image as the active image on a [Person](https://developers.intellihr.io/docs/v1/), has some minor editing options.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
intellihr.people_images.promote_image(
    person_id="personId_example",
    image_type="PERSON_PROFILE",
    rotation=0,
    coordinates={
        "height": 0,
        "width": 0,
        "x": 0,
        "y": 0,
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### person_id: `str`<a id="person_id-str"></a>

Id string param for relevant [Person](https://developers.intellihr.io/docs/v1/)

##### image_type: `str`<a id="image_type-str"></a>

The Image Type. Enum: `PERSON_PROFILE`, `PROFILE_COVER`.

##### rotation: `int`<a id="rotation-int"></a>

the degree to rotate the image from 0-359

##### coordinates: [`PersonIdImagePatchRequestCoordinates`](./intelli_hr_python_sdk/type/person_id_image_patch_request_coordinates.py)<a id="coordinates-personidimagepatchrequestcoordinatesintelli_hr_python_sdktypeperson_id_image_patch_request_coordinatespy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PersonIdImagePatchRequest`](./intelli_hr_python_sdk/type/person_id_image_patch_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{personId}/images` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.people_skills.assign_skill_to_person`<a id="intellihrpeople_skillsassign_skill_to_person"></a>

Assigns a [Skill](https://developers.intellihr.io/docs/v1/) to an existing [Person](https://developers.intellihr.io/docs/v1/)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
assign_skill_to_person_response = intellihr.people_skills.assign_skill_to_person(
    skill_id="8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
    skill_level="Fortnightly",
    person_id="personId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### skill_id: `str`<a id="skill_id-str"></a>

The identifier string for the [Skill](https://developers.intellihr.io/docs/v1/).

##### skill_level: `str`<a id="skill_level-str"></a>

The Skill Level you wish to apply to this Skill. Enum: `Expert`, `Proficient`, `Interested`, `Basic`.

##### person_id: `str`<a id="person_id-str"></a>

Id string param for relevant [Person](https://developers.intellihr.io/docs/v1/)

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PersonIdCreateRequest`](./intelli_hr_python_sdk/type/person_id_create_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PersonId`](./intelli_hr_python_sdk/pydantic/person_id.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{personId}/skills` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.people_skills.delete_assigned_skill_by_id`<a id="intellihrpeople_skillsdelete_assigned_skill_by_id"></a>

Deletes the assigned [Skill](https://developers.intellihr.io/docs/v1/) from a [Person](https://developers.intellihr.io/docs/v1/).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
intellihr.people_skills.delete_assigned_skill_by_id(
    person_id="personId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### person_id: `str`<a id="person_id-str"></a>

Id string param for relevant [Person](https://developers.intellihr.io/docs/v1/)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{personId}/skills/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.people_skills.find_skill_by_id`<a id="intellihrpeople_skillsfind_skill_by_id"></a>

Returns a single [Skill](https://developers.intellihr.io/docs/v1/) for the provided [Person](https://developers.intellihr.io/docs/v1/).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_skill_by_id_response = intellihr.people_skills.find_skill_by_id(
    person_id="personId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### person_id: `str`<a id="person_id-str"></a>

Id string param for relevant [Person](https://developers.intellihr.io/docs/v1/)

#### 🔄 Return<a id="🔄-return"></a>

[`PersonId`](./intelli_hr_python_sdk/pydantic/person_id.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{personId}/skills/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.people_skills.list_person_skills`<a id="intellihrpeople_skillslist_person_skills"></a>

Returns a list of all [Skills](https://developers.intellihr.io/docs/v1/) for the provided [Person](https://developers.intellihr.io/docs/v1/).  Note that this endpoint is not Paginated.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_person_skills_response = intellihr.people_skills.list_person_skills(
    person_id="personId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### person_id: `str`<a id="person_id-str"></a>

Id string param for relevant [Person](https://developers.intellihr.io/docs/v1/)

#### 🔄 Return<a id="🔄-return"></a>

[`PersonIdList`](./intelli_hr_python_sdk/pydantic/person_id_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{personId}/skills` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.people_skills.update_assigned_skill`<a id="intellihrpeople_skillsupdate_assigned_skill"></a>

Update an assigned [Skill](https://developers.intellihr.io/docs/v1/) on a [Person](https://developers.intellihr.io/docs/v1/)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_assigned_skill_response = intellihr.people_skills.update_assigned_skill(
    person_id="personId_example",
    skill_level="Fortnightly",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### person_id: `str`<a id="person_id-str"></a>

Id string param for relevant [Person](https://developers.intellihr.io/docs/v1/)

##### skill_level: `str`<a id="skill_level-str"></a>

The Skill Level you wish to apply to this Skill. Enum: `Expert`, `Proficient`, `Interested`, `Basic`.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PersonIdPatchRequest`](./intelli_hr_python_sdk/type/person_id_patch_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PersonId`](./intelli_hr_python_sdk/pydantic/person_id.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{personId}/skills/{id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.permission_groups.find_group_by_id`<a id="intellihrpermission_groupsfind_group_by_id"></a>

Returns a single [Permission Groups](https://developers.intellihr.io/docs/v1/).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_group_by_id_response = intellihr.permission_groups.find_group_by_id()
```

#### 🔄 Return<a id="🔄-return"></a>

[`PermissionGroups`](./intelli_hr_python_sdk/pydantic/permission_groups.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/permission-groups/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.permission_groups.list_all`<a id="intellihrpermission_groupslist_all"></a>

Returns a list of all [Permission Groups](https://developers.intellihr.io/docs/v1/) recorded in the system.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = intellihr.permission_groups.list_all(
    filters={
        "is_enabled": True,
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### filters: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./intelli_hr_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="filters-dictstr-unionbool-date-datetime-dict-float-int-list-str-noneintelli_hr_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Filters can be applied in the query string to limit the data returned from this endpoint. Filters are provided in the format `filters[<filter_name>][<operation_type>]=<filter_value>`.For example, a filter to get items matching a specific filter value would be `filters[isEnabled][eq]=true`  Below is a list of operation types available on filters, note that each filter may not support every type:  • Equality `[eq]`: Checks for an exact match with the given filter value  The list of supported filters is given below.

#### 🔄 Return<a id="🔄-return"></a>

[`PermissionGroupsList`](./intelli_hr_python_sdk/pydantic/permission_groups_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/permission-groups` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.person_documents_(deprecated).create_presigned_upload_url`<a id="intellihrperson_documents_deprecatedcreate_presigned_upload_url"></a>

Create a presigned upload URL

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_presigned_upload_url_response = intellihr.person_documents_(deprecated).create_presigned_upload_url(
    person={
        "id": "8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
        "name": "Bruce Wayne",
        "primary_email_address": "bruce.wayne@example.com",
        "employee_number": "00001",
        "auto_increment_intellihr_id": "1000",
    },
    filename="OfferLetter.pdf",
    mime="application/pdf",
    size=300,
    extension="pdf",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### person: [`PersonDocumentsCreateRequestPerson`](./intelli_hr_python_sdk/type/person_documents_create_request_person.py)<a id="person-persondocumentscreaterequestpersonintelli_hr_python_sdktypeperson_documents_create_request_personpy"></a>


##### filename: `str`<a id="filename-str"></a>

The filename of the document. This will be used for display name. Includes extension.

##### mime: `str`<a id="mime-str"></a>

The mime type of the document

##### size: `int`<a id="size-int"></a>

The size in bytes. We use this to validate the upload was successful so must match the actual file size

##### extension: `str`<a id="extension-str"></a>

The extension of the document, not including the dot

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PersonDocumentsCreateRequest`](./intelli_hr_python_sdk/type/person_documents_create_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PersonDocumentsCreateResponse`](./intelli_hr_python_sdk/pydantic/person_documents_create_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/person-documents` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.person_documents_(deprecated).update_document`<a id="intellihrperson_documents_deprecatedupdate_document"></a>

Update a Document

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_document_response = intellihr.person_documents_(deprecated).update_document(
    person_id="8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
    filename="OfferLetter.pdf",
    upload_status=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### person_id: `str`<a id="person_id-str"></a>

The identifier string for the [Person](https://developers.intellihr.io/docs/v1/) to whom this [Document](https://developers.intellihr.io/docs/v1/) belongs.

##### filename: `str`<a id="filename-str"></a>

The filename of the document. This will be used for display name. Includes extension.

##### upload_status: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./intelli_hr_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="upload_status-unionbool-date-datetime-dict-float-int-list-str-noneintelli_hr_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

The upload status of this [Document](https://developers.intellihr.io/docs/v1/). Enum: `SUCCESS`, `PENDING`, `FAILED`.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PersonDocumentsPatchRequest`](./intelli_hr_python_sdk/type/person_documents_patch_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PersonDocumentsPatchResponse`](./intelli_hr_python_sdk/pydantic/person_documents_patch_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/person-documents/{id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.position_titles.create_new_record`<a id="intellihrposition_titlescreate_new_record"></a>

Create a new [Position Title](https://developers.intellihr.io/docs/v1/) record with the provided data.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_record_response = intellihr.position_titles.create_new_record(
    name="Engineering Manager",
    code=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name given to this [Position Title](https://developers.intellihr.io/docs/v1/). This name would normally be shown to users of the system.

##### code: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./intelli_hr_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="code-unionbool-date-datetime-dict-float-int-list-str-noneintelli_hr_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Code given to this [Position Title](https://developers.intellihr.io/docs/v1/).

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PositionTitlesCreateRequest`](./intelli_hr_python_sdk/type/position_titles_create_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PositionTitles`](./intelli_hr_python_sdk/pydantic/position_titles.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/position-titles` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.position_titles.delete_by_id`<a id="intellihrposition_titlesdelete_by_id"></a>

Deletes the [Position Titles](https://developers.intellihr.io/docs/v1/) by the given ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
intellihr.position_titles.delete_by_id()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/position-titles/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.position_titles.list_all`<a id="intellihrposition_titleslist_all"></a>

Returns a list of all [Position Titles](https://developers.intellihr.io/docs/v1/) recorded in the system.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = intellihr.position_titles.list_all(
    filters={
        "name": "Engineering Manager",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### filters: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./intelli_hr_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="filters-dictstr-unionbool-date-datetime-dict-float-int-list-str-noneintelli_hr_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Filters can be applied in the query string to limit the data returned from this endpoint. Filters are provided in the format `filters[<filter_name>][<operation_type>]=<filter_value>`.For example, a filter to get items matching a specific filter value would be `filters[name][eq]=Engineering Manager`  Below is a list of operation types available on filters, note that each filter may not support every type:  • Equality `[eq]`: Checks for an exact match with the given filter value  The list of supported filters is given below.

#### 🔄 Return<a id="🔄-return"></a>

[`PositionTitlesList`](./intelli_hr_python_sdk/pydantic/position_titles_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/position-titles` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.position_titles.update_attributes`<a id="intellihrposition_titlesupdate_attributes"></a>

Patch attributes of an existing [Position Titles](https://developers.intellihr.io/docs/v1/) record with the provided data.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_attributes_response = intellihr.position_titles.update_attributes(
    name="Engineering Manager",
    code=None,
    is_enabled=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name given to this [Position Title](https://developers.intellihr.io/docs/v1/). This name would normally be shown to users of the system.

##### code: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./intelli_hr_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="code-unionbool-date-datetime-dict-float-int-list-str-noneintelli_hr_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Code given to this [Position Title](https://developers.intellihr.io/docs/v1/).

##### is_enabled: `bool`<a id="is_enabled-bool"></a>

Specifies whether users can select this [Position Title](https://developers.intellihr.io/docs/v1/) in dropdowns.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PositionTitlesPatchRequest`](./intelli_hr_python_sdk/type/position_titles_patch_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PositionTitles`](./intelli_hr_python_sdk/pydantic/position_titles.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/position-titles/{id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.qualification_instances.create_new_instance`<a id="intellihrqualification_instancescreate_new_instance"></a>

Returns the created [Qualification Instance](https://developers.intellihr.io/docs/v1/).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_instance_response = intellihr.qualification_instances.create_new_instance(
    person_id="8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
    qualification_library_item_id="8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
    status="DRAFT",
    issuing_organisation=None,
    registration_number=None,
    issue_date=None,
    expiry_date=None,
    expiry_notification_queued_at=None,
    notes=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### person_id: `str`<a id="person_id-str"></a>

The identifier string for the Person Id.

##### qualification_library_item_id: `str`<a id="qualification_library_item_id-str"></a>

The identifier string for the Qualification Library Item Id.

##### status: `str`<a id="status-str"></a>

The status of this [Qualification Instance](https://developers.intellihr.io/docs/v1/)

##### issuing_organisation: Union[`str`, `none_type`]<a id="issuing_organisation-unionstr-none_type"></a>


The organisation that issued this qualification [Qualification Instance](https://developers.intellihr.io/docs/v1/)

##### registration_number: Union[`str`, `none_type`]<a id="registration_number-unionstr-none_type"></a>


The registration number of the [Qualification Instance](https://developers.intellihr.io/docs/v1/)

##### issue_date: Union[`str`, `none_type`]<a id="issue_date-unionstr-none_type"></a>


The issue date of the [Qualification Instance](https://developers.intellihr.io/docs/v1/). This date will follow the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6).

##### expiry_date: Union[`str`, `none_type`]<a id="expiry_date-unionstr-none_type"></a>


The expiry date of this Qualification. This date will follow the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6).

##### expiry_notification_queued_at: Union[`str`, `none_type`]<a id="expiry_notification_queued_at-unionstr-none_type"></a>


The due date for the recipient to complete this [Qualification Instance](https://developers.intellihr.io/docs/v1/). This date will follow the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6).

##### notes: Union[`str`, `none_type`]<a id="notes-unionstr-none_type"></a>


The notes stored on the [Qualification Instance](https://developers.intellihr.io/docs/v1/)

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`QualificationInstancesCreateRequest`](./intelli_hr_python_sdk/type/qualification_instances_create_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Qualifications`](./intelli_hr_python_sdk/pydantic/qualifications.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/qualifications` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.qualification_instances.delete_by_id`<a id="intellihrqualification_instancesdelete_by_id"></a>

Deletes the [Qualification Instance](https://developers.intellihr.io/docs/v1/) by the given ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
intellihr.qualification_instances.delete_by_id()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/qualifications/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.qualification_instances.find_by_id`<a id="intellihrqualification_instancesfind_by_id"></a>

Returns a single [Qualification Instance](https://developers.intellihr.io/docs/v1/) by its identifier.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_by_id_response = intellihr.qualification_instances.find_by_id()
```

#### 🔄 Return<a id="🔄-return"></a>

[`Qualifications`](./intelli_hr_python_sdk/pydantic/qualifications.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/qualifications/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.qualification_instances.list_all`<a id="intellihrqualification_instanceslist_all"></a>

List all Qualification Instances

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = intellihr.qualification_instances.list_all(
    filters={
        "person_id": "dc996d73-a75e-499c-a96e-bd7d0df45f57,26d0ffc4-60f6-4672-a603-caaa4564af12",
        "employee_number": "00001",
        "qualification_library_item_id": "dc996d73-a75e-499c-a96e-bd7d0df45f57,26d0ffc4-60f6-4672-a603-caaa4564af12",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### filters: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./intelli_hr_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="filters-dictstr-unionbool-date-datetime-dict-float-int-list-str-noneintelli_hr_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Filters can be applied in the query string to limit the data returned from this endpoint. Filters are provided in the format `filters[<filter_name>][<operation_type>]=<filter_value>`.For example, a filter to get items matching a specific filter value would be `filters[personId][eq]=dc996d73-a75e-499c-a96e-bd7d0df45f57,26d0ffc4-60f6-4672-a603-caaa4564af12`  Below is a list of operation types available on filters, note that each filter may not support every type:  • Equality `[eq]`: Checks for an exact match with the given filter value  The list of supported filters is given below.

#### 🔄 Return<a id="🔄-return"></a>

[`QualificationsList`](./intelli_hr_python_sdk/pydantic/qualifications_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/qualifications` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.qualification_instances.update_instance_by_id`<a id="intellihrqualification_instancesupdate_instance_by_id"></a>

Returns the updated [Qualification Instance](https://developers.intellihr.io/docs/v1/).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_instance_by_id_response = intellihr.qualification_instances.update_instance_by_id(
    status="DRAFT",
    issuing_organisation=None,
    registration_number=None,
    issue_date=None,
    expiry_date=None,
    expiry_notification_queued_at=None,
    notes=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### status: `str`<a id="status-str"></a>

The status of this [Qualification Instance](https://developers.intellihr.io/docs/v1/)

##### issuing_organisation: Union[`str`, `none_type`]<a id="issuing_organisation-unionstr-none_type"></a>


The organisation that issued this qualification [Qualification Instance](https://developers.intellihr.io/docs/v1/)

##### registration_number: Union[`str`, `none_type`]<a id="registration_number-unionstr-none_type"></a>


The registration number of the [Qualification Instance](https://developers.intellihr.io/docs/v1/)

##### issue_date: Union[`str`, `none_type`]<a id="issue_date-unionstr-none_type"></a>


The issue date of the [Qualification Instance](https://developers.intellihr.io/docs/v1/). This date will follow the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6).

##### expiry_date: Union[`str`, `none_type`]<a id="expiry_date-unionstr-none_type"></a>


The expiry date of this Qualification. This date will follow the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6).

##### expiry_notification_queued_at: Union[`str`, `none_type`]<a id="expiry_notification_queued_at-unionstr-none_type"></a>


The due date for the recipient to complete this [Qualification Instance](https://developers.intellihr.io/docs/v1/). This date will follow the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6).

##### notes: Union[`str`, `none_type`]<a id="notes-unionstr-none_type"></a>


The notes stored on the [Qualification Instance](https://developers.intellihr.io/docs/v1/)

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`QualificationInstancesPatchRequest`](./intelli_hr_python_sdk/type/qualification_instances_patch_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Qualifications`](./intelli_hr_python_sdk/pydantic/qualifications.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/qualifications/{id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.qualification_library_items.create_new_record`<a id="intellihrqualification_library_itemscreate_new_record"></a>

Create a new [Qualification Library Item](https://developers.intellihr.io/docs/v1/) record with the provided data.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_record_response = intellihr.qualification_library_items.create_new_record(
    name="string_example",
    qualification_type_id="8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
    qualification_expiry_type="EXPIRY_INAPPLICABLE",
    qualification_registration_number_visibility_type="REGISTRATION_NUMBER_INAPPLICABLE",
    qualification_attachment_requirement_type="DOCUMENTS_OPTIONAL",
    expiry_warning_period=3.14,
    send_expiry_warning=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

The name of this [Qualification Library Item](https://developers.intellihr.io/docs/v1/)

##### qualification_type_id: `str`<a id="qualification_type_id-str"></a>

The identifier string for the Qualification Type Id.

##### qualification_expiry_type: `str`<a id="qualification_expiry_type-str"></a>

The expiry type for this library item

##### qualification_registration_number_visibility_type: `str`<a id="qualification_registration_number_visibility_type-str"></a>

The expiry type for this library item

##### qualification_attachment_requirement_type: `str`<a id="qualification_attachment_requirement_type-str"></a>

If documents are required for this library item

##### expiry_warning_period: `Union[int, float]`<a id="expiry_warning_period-unionint-float"></a>

Period in days, that there is a warning before the expiry of the qualification. If qualificationExpiryType is set to EXPIRY_INAPPLICABLE, this value will be ignored.

##### send_expiry_warning: `bool`<a id="send_expiry_warning-bool"></a>

If this [Qualification Library Item](https://developers.intellihr.io/docs/v1/) will send expiry warning/s using the periods defined. If qualificationExpiryType is set to EXPIRY_INAPPLICABLE, this value will be ignored.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`QualificationLibraryItemsCreateRequest`](./intelli_hr_python_sdk/type/qualification_library_items_create_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`QualificationLibraryItems`](./intelli_hr_python_sdk/pydantic/qualification_library_items.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/qualification-library-items` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.qualification_library_items.delete_by_id`<a id="intellihrqualification_library_itemsdelete_by_id"></a>

Deletes the [Qualification Library Items](https://developers.intellihr.io/docs/v1/) by the given ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
intellihr.qualification_library_items.delete_by_id()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/qualification-library-items/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.qualification_library_items.find_by_id`<a id="intellihrqualification_library_itemsfind_by_id"></a>

Returns a single [Qualification Library Item](https://developers.intellihr.io/docs/v1/) by its identifier.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_by_id_response = intellihr.qualification_library_items.find_by_id()
```

#### 🔄 Return<a id="🔄-return"></a>

[`QualificationLibraryItemsList`](./intelli_hr_python_sdk/pydantic/qualification_library_items_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/qualification-library-items/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.qualification_library_items.get_all_qualifications`<a id="intellihrqualification_library_itemsget_all_qualifications"></a>

List all Qualification Library Items

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_qualifications_response = intellihr.qualification_library_items.get_all_qualifications()
```

#### 🔄 Return<a id="🔄-return"></a>

[`QualificationLibraryItems`](./intelli_hr_python_sdk/pydantic/qualification_library_items.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/qualification-library-items` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.qualification_library_items.update_record`<a id="intellihrqualification_library_itemsupdate_record"></a>

Patch attributes of an existing [Qualification Library Items](https://developers.intellihr.io/docs/v1/) record with the provided data.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_record_response = intellihr.qualification_library_items.update_record(
    name="string_example",
    qualification_type_id="8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
    qualification_expiry_type="EXPIRY_INAPPLICABLE",
    qualification_registration_number_visibility_type="REGISTRATION_NUMBER_INAPPLICABLE",
    qualification_attachment_requirement_type="DOCUMENTS_OPTIONAL",
    expiry_warning_period=3.14,
    send_expiry_warning=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

The name of this [Qualification Library Item](https://developers.intellihr.io/docs/v1/)

##### qualification_type_id: `str`<a id="qualification_type_id-str"></a>

The identifier string for the Qualification Type Id.

##### qualification_expiry_type: `str`<a id="qualification_expiry_type-str"></a>

The expiry type for this library item

##### qualification_registration_number_visibility_type: `str`<a id="qualification_registration_number_visibility_type-str"></a>

The expiry type for this library item

##### qualification_attachment_requirement_type: `str`<a id="qualification_attachment_requirement_type-str"></a>

If documents are required for this library item

##### expiry_warning_period: `Union[int, float]`<a id="expiry_warning_period-unionint-float"></a>

Period in days, that there is a warning before the expiry of the qualification. If qualificationExpiryType is set to EXPIRY_INAPPLICABLE, this value will be ignored.

##### send_expiry_warning: `bool`<a id="send_expiry_warning-bool"></a>

If this [Qualification Library Item](https://developers.intellihr.io/docs/v1/) will send expiry warning/s using the periods defined. If qualificationExpiryType is set to EXPIRY_INAPPLICABLE, this value will be ignored.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`QualificationLibraryItemsPatchRequest`](./intelli_hr_python_sdk/type/qualification_library_items_patch_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`QualificationLibraryItems`](./intelli_hr_python_sdk/pydantic/qualification_library_items.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/qualification-library-items/{id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.qualification_statuses.find_status_by_id`<a id="intellihrqualification_statusesfind_status_by_id"></a>

Returns a single [Qualification Status](https://developers.intellihr.io/docs/v1/) by its identifier.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_status_by_id_response = intellihr.qualification_statuses.find_status_by_id()
```

#### 🔄 Return<a id="🔄-return"></a>

[`QualificationStatuses`](./intelli_hr_python_sdk/pydantic/qualification_statuses.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/qualification-statuses/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.qualification_types.find_by_id`<a id="intellihrqualification_typesfind_by_id"></a>

Returns a single [Qualification Type](https://developers.intellihr.io/docs/v1/) by its identifier.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_by_id_response = intellihr.qualification_types.find_by_id()
```

#### 🔄 Return<a id="🔄-return"></a>

[`QualificationTypesList`](./intelli_hr_python_sdk/pydantic/qualification_types_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/qualification-types/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.qualification_types.list_all_qualification_types`<a id="intellihrqualification_typeslist_all_qualification_types"></a>

List all Qualification Types

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_qualification_types_response = intellihr.qualification_types.list_all_qualification_types()
```

#### 🔄 Return<a id="🔄-return"></a>

[`QualificationTypes`](./intelli_hr_python_sdk/pydantic/qualification_types.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/qualification-types` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.recruitment_sources.find_by_id`<a id="intellihrrecruitment_sourcesfind_by_id"></a>

Returns a single recruitment source.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_by_id_response = intellihr.recruitment_sources.find_by_id()
```

#### 🔄 Return<a id="🔄-return"></a>

[`RecruitmentSources`](./intelli_hr_python_sdk/pydantic/recruitment_sources.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/recruitment-sources/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.recruitment_sources.list_all`<a id="intellihrrecruitment_sourceslist_all"></a>

Returns a list of all recruitment sources.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = intellihr.recruitment_sources.list_all()
```

#### 🔄 Return<a id="🔄-return"></a>

[`RecruitmentSourcesList`](./intelli_hr_python_sdk/pydantic/recruitment_sources_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/recruitment-sources` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.representative_types.find_by_id`<a id="intellihrrepresentative_typesfind_by_id"></a>

Returns a single [Representative Type](https://developers.intellihr.io/docs/v1/) by its identifier.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_by_id_response = intellihr.representative_types.find_by_id()
```

#### 🔄 Return<a id="🔄-return"></a>

[`RepresentativeTypesList`](./intelli_hr_python_sdk/pydantic/representative_types_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/representative-types/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.representative_types.list_all`<a id="intellihrrepresentative_typeslist_all"></a>

List all Representative Types

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = intellihr.representative_types.list_all()
```

#### 🔄 Return<a id="🔄-return"></a>

[`RepresentativeTypes`](./intelli_hr_python_sdk/pydantic/representative_types.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/representative-types` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.skill_disciplines.create_new_discipline`<a id="intellihrskill_disciplinescreate_new_discipline"></a>

Create a Skill Discipline

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_discipline_response = intellihr.skill_disciplines.create_new_discipline(
    name="Accounting",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

The name of this [Skill Discipline](https://developers.intellihr.io/docs/v1/).

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SkillDisciplinesCreate`](./intelli_hr_python_sdk/type/skill_disciplines_create.py)
#### 🔄 Return<a id="🔄-return"></a>

[`SkillDisciplines`](./intelli_hr_python_sdk/pydantic/skill_disciplines.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/skill-disciplines` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.skill_disciplines.find_by_id`<a id="intellihrskill_disciplinesfind_by_id"></a>

Returns a single webhook.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_by_id_response = intellihr.skill_disciplines.find_by_id()
```

#### 🔄 Return<a id="🔄-return"></a>

[`SkillDisciplines`](./intelli_hr_python_sdk/pydantic/skill_disciplines.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/skill-disciplines/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.skill_disciplines.list_all`<a id="intellihrskill_disciplineslist_all"></a>

Returns a list of all [Skill Disciplines](https://developers.intellihr.io/docs/v1/) recorded in the system.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = intellihr.skill_disciplines.list_all(
    filters={
        "name": "Accounting",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### filters: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./intelli_hr_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="filters-dictstr-unionbool-date-datetime-dict-float-int-list-str-noneintelli_hr_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Filters can be applied in the query string to limit the data returned from this endpoint. Filters are provided in the format `filters[<filter_name>][<operation_type>]=<filter_value>`.For example, a filter to get items matching a specific filter value would be `filters[name][eq]=Accounting`  Below is a list of operation types available on filters, note that each filter may not support every type:  • Equality `[eq]`: Checks for an exact match with the given filter value  The list of supported filters is given below.

#### 🔄 Return<a id="🔄-return"></a>

[`SkillDisciplinesList`](./intelli_hr_python_sdk/pydantic/skill_disciplines_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/skill-disciplines` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.skill_disciplines.update_discipline_by_id`<a id="intellihrskill_disciplinesupdate_discipline_by_id"></a>

Patch a Skill Discipline

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_discipline_by_id_response = intellihr.skill_disciplines.update_discipline_by_id(
    name="Accounting",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

The name of this [Skill Discipline](https://developers.intellihr.io/docs/v1/).

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SkillDisciplinesPatch`](./intelli_hr_python_sdk/type/skill_disciplines_patch.py)
#### 🔄 Return<a id="🔄-return"></a>

[`SkillDisciplines`](./intelli_hr_python_sdk/pydantic/skill_disciplines.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/skill-disciplines/{id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.skills.create_new_skill`<a id="intellihrskillscreate_new_skill"></a>

Create a new Skill

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_skill_response = intellihr.skills.create_new_skill(
    description="The planning, execution, tracking, and analysis of a marketing initiative; sometimes centered around a new product launch or an event.",
    name="Campaign Management",
    is_business_critical=True,
    skill_discipline_id="8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### description: `str`<a id="description-str"></a>

A description of the [Skill](https://developers.intellihr.io/docs/v1/).

##### name: `str`<a id="name-str"></a>

User friendly name given to this [Skill](https://developers.intellihr.io/docs/v1/).

##### is_business_critical: `bool`<a id="is_business_critical-bool"></a>

Whether this [Skill](https://developers.intellihr.io/docs/v1/) is business critical.

##### skill_discipline_id: `str`<a id="skill_discipline_id-str"></a>

The identifier string for the [Skill Discipline](https://developers.intellihr.io/docs/v1/) to which this [Skill](https://developers.intellihr.io/docs/v1/) belongs.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SkillsCreateRequest`](./intelli_hr_python_sdk/type/skills_create_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Skills`](./intelli_hr_python_sdk/pydantic/skills.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/skills` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.skills.find_skill_by_id`<a id="intellihrskillsfind_skill_by_id"></a>

Returns a single [Skill](https://developers.intellihr.io/docs/v1/).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_skill_by_id_response = intellihr.skills.find_skill_by_id()
```

#### 🔄 Return<a id="🔄-return"></a>

[`Skills`](./intelli_hr_python_sdk/pydantic/skills.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/skills/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.skills.get_all`<a id="intellihrskillsget_all"></a>

Returns a list of all [Skills](https://developers.intellihr.io/docs/v1/).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = intellihr.skills.get_all(
    filters={
        "is_business_critical": True,
        "skill_discipline_id": "8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### filters: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./intelli_hr_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="filters-dictstr-unionbool-date-datetime-dict-float-int-list-str-noneintelli_hr_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Filters can be applied in the query string to limit the data returned from this endpoint. Filters are provided in the format `filters[<filter_name>][<operation_type>]=<filter_value>`.For example, a filter to get items matching a specific filter value would be `filters[isBusinessCritical][eq]=true`  Below is a list of operation types available on filters, note that each filter may not support every type:  • Equality `[eq]`: Checks for an exact match with the given filter value  The list of supported filters is given below.

#### 🔄 Return<a id="🔄-return"></a>

[`SkillsList`](./intelli_hr_python_sdk/pydantic/skills_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/skills` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.skills.update_skill_by_id`<a id="intellihrskillsupdate_skill_by_id"></a>

Update a Skill

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_skill_by_id_response = intellihr.skills.update_skill_by_id(
    description="The planning, execution, tracking, and analysis of a marketing initiative; sometimes centered around a new product launch or an event.",
    name="Campaign Management",
    is_business_critical=True,
    skill_discipline_id="8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### description: `str`<a id="description-str"></a>

A description of the [Skill](https://developers.intellihr.io/docs/v1/).

##### name: `str`<a id="name-str"></a>

User friendly name given to this [Skill](https://developers.intellihr.io/docs/v1/).

##### is_business_critical: `bool`<a id="is_business_critical-bool"></a>

Whether this [Skill](https://developers.intellihr.io/docs/v1/) is business critical.

##### skill_discipline_id: `str`<a id="skill_discipline_id-str"></a>

The identifier string for the [Skill Discipline](https://developers.intellihr.io/docs/v1/) to which this [Skill](https://developers.intellihr.io/docs/v1/) belongs.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SkillsPatchRequest`](./intelli_hr_python_sdk/type/skills_patch_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Skills`](./intelli_hr_python_sdk/pydantic/skills.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/skills/{id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.training_providers.find_by_id`<a id="intellihrtraining_providersfind_by_id"></a>

Returns a single [Training Provider](https://developers.intellihr.io/docs/v1/).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_by_id_response = intellihr.training_providers.find_by_id()
```

#### 🔄 Return<a id="🔄-return"></a>

[`TrainingProviders`](./intelli_hr_python_sdk/pydantic/training_providers.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/training-providers/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.training_providers.list_all`<a id="intellihrtraining_providerslist_all"></a>

Returns a list of all [Training Providers](https://developers.intellihr.io/docs/v1/).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = intellihr.training_providers.list_all()
```

#### 🔄 Return<a id="🔄-return"></a>

[`TrainingProvidersList`](./intelli_hr_python_sdk/pydantic/training_providers_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/training-providers` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.training_statuses.list_all`<a id="intellihrtraining_statuseslist_all"></a>

Returns a list of all [Training Statuses](https://developers.intellihr.io/docs/v1/).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = intellihr.training_statuses.list_all()
```

#### 🔄 Return<a id="🔄-return"></a>

[`TrainingStatusesList`](./intelli_hr_python_sdk/pydantic/training_statuses_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/training-statuses` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.training_types.find_by_id`<a id="intellihrtraining_typesfind_by_id"></a>

Returns a single [Training Type](https://developers.intellihr.io/docs/v1/).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_by_id_response = intellihr.training_types.find_by_id()
```

#### 🔄 Return<a id="🔄-return"></a>

[`TrainingTypes`](./intelli_hr_python_sdk/pydantic/training_types.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/training-types/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.training_types.list_all`<a id="intellihrtraining_typeslist_all"></a>

Returns a list of all [Training Types](https://developers.intellihr.io/docs/v1/).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = intellihr.training_types.list_all()
```

#### 🔄 Return<a id="🔄-return"></a>

[`TrainingTypesList`](./intelli_hr_python_sdk/pydantic/training_types_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/training-types` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.trainings.create_new_training`<a id="intellihrtrainingscreate_new_training"></a>

Create a new Training

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_training_response = intellihr.trainings.create_new_training(
    name="Accounting Compliance 101",
    person={
        "id": "8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
        "name": "Bruce Wayne",
        "primary_email_address": "bruce.wayne@example.com",
        "employee_number": "00001",
        "auto_increment_intellihr_id": "1000",
    },
    coordinator_person={
        "id": "8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
        "name": "Bruce Wayne",
        "primary_email_address": "bruce.wayne@example.com",
        "employee_number": "00001",
        "auto_increment_intellihr_id": "1000",
    },
    completion_date="2015-03-01T22:30:00+00:00",
    cost="600",
    currency="AUD",
    hours="12",
    job={
        "id": "8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
    },
    provider={
        "id": "8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
        "name": "HR Training Team",
    },
    type={
        "id": "8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
        "name": "Soft Skills",
    },
    custom_fields={
        "key": {
        },
    },
    status={
        "id": "8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
        "name": "Completed",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

User friendly name given to this [Training](https://developers.intellihr.io/docs/v1/) to identify it in the system.

##### person: [`TrainingsCreateRequestPerson`](./intelli_hr_python_sdk/type/trainings_create_request_person.py)<a id="person-trainingscreaterequestpersonintelli_hr_python_sdktypetrainings_create_request_personpy"></a>


##### coordinator_person: [`TrainingsCreateRequestCoordinatorPerson`](./intelli_hr_python_sdk/type/trainings_create_request_coordinator_person.py)<a id="coordinator_person-trainingscreaterequestcoordinatorpersonintelli_hr_python_sdktypetrainings_create_request_coordinator_personpy"></a>


##### completion_date: `str`<a id="completion_date-str"></a>

The timestamp the [Training](https://developers.intellihr.io/docs/v1/) was completed. This date will follow the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6).   YYYY-MM-DD date formatting is also supported, although by using this format the date will be stored as the start of day in UTC time, not the requesting tenants timezone.

##### cost: `str`<a id="cost-str"></a>

The cost of this [Training](https://developers.intellihr.io/docs/v1/).

##### currency: `str`<a id="currency-str"></a>

The currency used for this [Training](https://developers.intellihr.io/docs/v1/). Will default to the tenant default currency when not provided. An international currency code. Typically AUD for Australian dollar, USD for American dollar etc. See [Official list of codes](https://www.iban.com/currency-codes).

##### hours: `str`<a id="hours-str"></a>

How many hours were spent on this [Training](https://developers.intellihr.io/docs/v1/)

##### job: [`TrainingsCreateRequestJob`](./intelli_hr_python_sdk/type/trainings_create_request_job.py)<a id="job-trainingscreaterequestjobintelli_hr_python_sdktypetrainings_create_request_jobpy"></a>


##### provider: [`TrainingsCreateRequestProvider`](./intelli_hr_python_sdk/type/trainings_create_request_provider.py)<a id="provider-trainingscreaterequestproviderintelli_hr_python_sdktypetrainings_create_request_providerpy"></a>


##### type: [`TrainingsCreateRequestType`](./intelli_hr_python_sdk/type/trainings_create_request_type.py)<a id="type-trainingscreaterequesttypeintelli_hr_python_sdktypetrainings_create_request_typepy"></a>


##### custom_fields: [`TrainingsCreateRequestCustomFields`](./intelli_hr_python_sdk/type/trainings_create_request_custom_fields.py)<a id="custom_fields-trainingscreaterequestcustomfieldsintelli_hr_python_sdktypetrainings_create_request_custom_fieldspy"></a>

##### status: [`TrainingsCreateRequestStatus`](./intelli_hr_python_sdk/type/trainings_create_request_status.py)<a id="status-trainingscreaterequeststatusintelli_hr_python_sdktypetrainings_create_request_statuspy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TrainingsCreateRequest`](./intelli_hr_python_sdk/type/trainings_create_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Trainings`](./intelli_hr_python_sdk/pydantic/trainings.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/trainings` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.trainings.delete_by_id`<a id="intellihrtrainingsdelete_by_id"></a>

Deletes the provided [Training](https://developers.intellihr.io/docs/v1/) record.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
intellihr.trainings.delete_by_id()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/trainings/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.trainings.find_training_by_id`<a id="intellihrtrainingsfind_training_by_id"></a>

Returns a single [Training](https://developers.intellihr.io/docs/v1/).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_training_by_id_response = intellihr.trainings.find_training_by_id()
```

#### 🔄 Return<a id="🔄-return"></a>

[`Trainings`](./intelli_hr_python_sdk/pydantic/trainings.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/trainings/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.trainings.list_all`<a id="intellihrtrainingslist_all"></a>

Returns a list of all [Trainings](https://developers.intellihr.io/docs/v1/).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = intellihr.trainings.list_all(
    filters={
        "name": "Accounting%20Compliance%20101",
        "provider_id": "8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
        "provider_name": "HR%20Training%20Team",
        "type_id": "8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
        "type_name": "Soft%20Skills",
        "employee_number": "00001",
        "primary_email_address": "bruce.wayne@batman.org",
    },
    sort="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### filters: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./intelli_hr_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="filters-dictstr-unionbool-date-datetime-dict-float-int-list-str-noneintelli_hr_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Filters can be applied in the query string to limit the data returned from this endpoint. Filters are provided in the format `filters[<filter_name>][<operation_type>]=<filter_value>`.For example, a filter to get items matching a specific filter value would be `filters[name][eq]=Accounting%20Compliance%20101`  Below is a list of operation types available on filters, note that each filter may not support every type:  • Equality `[eq]`: Checks for an exact match with the given filter value  The list of supported filters is given below.

##### sort: `str`<a id="sort-str"></a>

Sorting can be applied in the query string to order the data returned from this endpoint. Sort can be prepended with a minus to return the data in descending (-) order. For example, a sort to get the most recent records first would be `-createdAt`.

#### 🔄 Return<a id="🔄-return"></a>

[`TrainingsList`](./intelli_hr_python_sdk/pydantic/trainings_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/trainings` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.trainings.update_training_by_id`<a id="intellihrtrainingsupdate_training_by_id"></a>

Update a Training

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_training_by_id_response = intellihr.trainings.update_training_by_id(
    coordinator_person={
        "id": "8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
        "name": "Bruce Wayne",
        "primary_email_address": "bruce.wayne@example.com",
        "employee_number": "00001",
        "auto_increment_intellihr_id": "1000",
    },
    completion_date="2015-03-01T22:30:00+00:00",
    cost="600",
    currency="AUD",
    hours="12",
    job={
        "id": "8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
    },
    name="Accounting Compliance 101",
    person={
        "id": "8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
        "name": "Bruce Wayne",
        "primary_email_address": "bruce.wayne@example.com",
        "employee_number": "00001",
        "auto_increment_intellihr_id": "1000",
    },
    provider={
        "id": "8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
        "name": "HR Training Team",
    },
    type={
        "id": "8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
        "name": "Soft Skills",
    },
    custom_fields={
        "key": {
        },
    },
    status={
        "id": "8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
        "name": "Completed",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### coordinator_person: [`TrainingsPatchRequestCoordinatorPerson`](./intelli_hr_python_sdk/type/trainings_patch_request_coordinator_person.py)<a id="coordinator_person-trainingspatchrequestcoordinatorpersonintelli_hr_python_sdktypetrainings_patch_request_coordinator_personpy"></a>


##### completion_date: `str`<a id="completion_date-str"></a>

The timestamp the [Training](https://developers.intellihr.io/docs/v1/) was completed. This date will follow the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6).   YYYY-MM-DD date formatting is also supported, although by using this format the date will be stored as the start of day in UTC time, not the requesting tenants timezone.

##### cost: `str`<a id="cost-str"></a>

The cost of this [Training](https://developers.intellihr.io/docs/v1/).

##### currency: `str`<a id="currency-str"></a>

The currency used for this [Training](https://developers.intellihr.io/docs/v1/). Will default to the tenant default currency when not provided. An international currency code. Typically AUD for Australian dollar, USD for American dollar etc. See [Official list of codes](https://www.iban.com/currency-codes).

##### hours: `str`<a id="hours-str"></a>

How many hours were spent on this [Training](https://developers.intellihr.io/docs/v1/)

##### job: [`TrainingsPatchRequestJob`](./intelli_hr_python_sdk/type/trainings_patch_request_job.py)<a id="job-trainingspatchrequestjobintelli_hr_python_sdktypetrainings_patch_request_jobpy"></a>


##### name: `str`<a id="name-str"></a>

User friendly name given to this [Training](https://developers.intellihr.io/docs/v1/) to identify it in the system.

##### person: [`TrainingsPatchRequestPerson`](./intelli_hr_python_sdk/type/trainings_patch_request_person.py)<a id="person-trainingspatchrequestpersonintelli_hr_python_sdktypetrainings_patch_request_personpy"></a>


##### provider: [`TrainingsPatchRequestProvider`](./intelli_hr_python_sdk/type/trainings_patch_request_provider.py)<a id="provider-trainingspatchrequestproviderintelli_hr_python_sdktypetrainings_patch_request_providerpy"></a>


##### type: [`TrainingsPatchRequestType`](./intelli_hr_python_sdk/type/trainings_patch_request_type.py)<a id="type-trainingspatchrequesttypeintelli_hr_python_sdktypetrainings_patch_request_typepy"></a>


##### custom_fields: [`TrainingsPatchRequestCustomFields`](./intelli_hr_python_sdk/type/trainings_patch_request_custom_fields.py)<a id="custom_fields-trainingspatchrequestcustomfieldsintelli_hr_python_sdktypetrainings_patch_request_custom_fieldspy"></a>

##### status: [`TrainingsPatchRequestStatus`](./intelli_hr_python_sdk/type/trainings_patch_request_status.py)<a id="status-trainingspatchrequeststatusintelli_hr_python_sdktypetrainings_patch_request_statuspy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TrainingsPatchRequest`](./intelli_hr_python_sdk/type/trainings_patch_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Trainings`](./intelli_hr_python_sdk/pydantic/trainings.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/trainings/{id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.users.create_user`<a id="intellihruserscreate_user"></a>

Create a User for a [Person](https://developers.intellihr.io/docs/v1/) that does not already have a User.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_user_response = intellihr.users.create_user(
    username="string_example",
    person={
        "id": "8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
    },
    is_enabled=True,
    permission_groups=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### username: `str`<a id="username-str"></a>

The unique name of this user.

##### person: [`UsersCreatePerson`](./intelli_hr_python_sdk/type/users_create_person.py)<a id="person-userscreatepersonintelli_hr_python_sdktypeusers_create_personpy"></a>


##### is_enabled: `bool`<a id="is_enabled-bool"></a>

Specifies whether this [User](https://developers.intellihr.io/docs/v1/) account is active. When disabled, you can no longer sign in using this account. Defaults to `false`.

##### permission_groups: Union[`List[str]`, `none_type`]<a id="permission_groups-unionliststr-none_type"></a>


The id's(UUIDv4) of the permission groups to assign this user to.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersCreate`](./intelli_hr_python_sdk/type/users_create.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Users`](./intelli_hr_python_sdk/pydantic/users.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.users.find_user_by_id`<a id="intellihrusersfind_user_by_id"></a>

Returns a single [User](https://developers.intellihr.io/docs/v1/).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_user_by_id_response = intellihr.users.find_user_by_id()
```

#### 🔄 Return<a id="🔄-return"></a>

[`Users`](./intelli_hr_python_sdk/pydantic/users.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.users.get_all_users`<a id="intellihrusersget_all_users"></a>

Returns a list of all [Users](https://developers.intellihr.io/docs/v1/).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_users_response = intellihr.users.get_all_users()
```

#### 🔄 Return<a id="🔄-return"></a>

[`UsersList`](./intelli_hr_python_sdk/pydantic/users_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.users.update_by_id`<a id="intellihrusersupdate_by_id"></a>

Returns the updated [User](https://developers.intellihr.io/docs/v1/).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_by_id_response = intellihr.users.update_by_id(
    is_enabled=True,
    username="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### is_enabled: `bool`<a id="is_enabled-bool"></a>

Specifies whether this [User](https://developers.intellihr.io/docs/v1/) account is active. When disabled, you can no longer sign in using this account.

##### username: `str`<a id="username-str"></a>

The unique name of this user.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersPatch`](./intelli_hr_python_sdk/type/users_patch.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Users`](./intelli_hr_python_sdk/pydantic/users.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.webhook_events.find_event_by_id`<a id="intellihrwebhook_eventsfind_event_by_id"></a>

Returns a single [Webhook Event](https://developers.intellihr.io/docs/v1/).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_event_by_id_response = intellihr.webhook_events.find_event_by_id()
```

#### 🔄 Return<a id="🔄-return"></a>

[`WebhookEvents`](./intelli_hr_python_sdk/pydantic/webhook_events.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webhook-events/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.webhook_events.list_all_events`<a id="intellihrwebhook_eventslist_all_events"></a>

Returns a list of all [Webhook Events](https://developers.intellihr.io/docs/v1/).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_events_response = intellihr.webhook_events.list_all_events()
```

#### 🔄 Return<a id="🔄-return"></a>

[`WebhookEventsList`](./intelli_hr_python_sdk/pydantic/webhook_events_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webhook-events` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.webhooks.create_webhook`<a id="intellihrwebhookscreate_webhook"></a>

Create a Webhook

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_webhook_response = intellihr.webhooks.create_webhook(
    url="string_example",
    webhook_event="string_example",
    is_enabled=True,
    source="custom",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### url: `str`<a id="url-str"></a>

The [Webhook](https://developers.intellihr.io/docs/v1/) endpoint which the request will be sent to when the subscribed [Webhook Event](https://developers.intellihr.io/docs/v1/) is triggered.

##### webhook_event: `str`<a id="webhook_event-str"></a>

The slug of the [Webhook Event](https://developers.intellihr.io/docs/v1/).

##### is_enabled: `bool`<a id="is_enabled-bool"></a>

Specifies whether users can select this [Webhook](https://developers.intellihr.io/docs/v1/). When disabled, this [Webhook](https://developers.intellihr.io/docs/v1/) will not be sent.

##### source: `str`<a id="source-str"></a>

A customizable string which can be used to identify what system created this [Webhook](https://developers.intellihr.io/docs/v1/). [Webhooks](https://developers.intellihr.io/docs/v1/) created through the intelliHR application will have source: 'custom'.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebhooksCreate`](./intelli_hr_python_sdk/type/webhooks_create.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Webhooks`](./intelli_hr_python_sdk/pydantic/webhooks.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webhooks` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.webhooks.delete_by_id`<a id="intellihrwebhooksdelete_by_id"></a>

Deletes the provided webhook.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
intellihr.webhooks.delete_by_id()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webhooks/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.webhooks.find_by_id`<a id="intellihrwebhooksfind_by_id"></a>

Returns a single webhook.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_by_id_response = intellihr.webhooks.find_by_id()
```

#### 🔄 Return<a id="🔄-return"></a>

[`Webhooks`](./intelli_hr_python_sdk/pydantic/webhooks.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webhooks/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.webhooks.list_all`<a id="intellihrwebhookslist_all"></a>

Returns a list of all webhooks.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = intellihr.webhooks.list_all()
```

#### 🔄 Return<a id="🔄-return"></a>

[`WebhooksList`](./intelli_hr_python_sdk/pydantic/webhooks_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webhooks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.webhooks.update_webhook`<a id="intellihrwebhooksupdate_webhook"></a>

Patch a Webhook

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_webhook_response = intellihr.webhooks.update_webhook(
    url="string_example",
    webhook_event="string_example",
    is_enabled=True,
    source="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### url: `str`<a id="url-str"></a>

The [Webhook](https://developers.intellihr.io/docs/v1/) endpoint which the request will be sent to when the subscribed [Webhook Event](https://developers.intellihr.io/docs/v1/) is triggered.

##### webhook_event: `str`<a id="webhook_event-str"></a>

The slug of the [Webhook Event](https://developers.intellihr.io/docs/v1/).

##### is_enabled: `bool`<a id="is_enabled-bool"></a>

Specifies whether users can select this [Webhook](https://developers.intellihr.io/docs/v1/). When disabled, this [Webhook](https://developers.intellihr.io/docs/v1/) will not be sent.

##### source: `str`<a id="source-str"></a>

A customizable string which can be used to identify what system created this [Webhook](https://developers.intellihr.io/docs/v1/). [Webhooks](https://developers.intellihr.io/docs/v1/) created through the intelliHR application will have source: 'custom'.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebhooksPatch`](./intelli_hr_python_sdk/type/webhooks_patch.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Webhooks`](./intelli_hr_python_sdk/pydantic/webhooks.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webhooks/{id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.work_classes.find_by_id`<a id="intellihrwork_classesfind_by_id"></a>

Returns a single work class.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_by_id_response = intellihr.work_classes.find_by_id()
```

#### 🔄 Return<a id="🔄-return"></a>

[`WorkClasses`](./intelli_hr_python_sdk/pydantic/work_classes.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/work-classes/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.work_classes.list_all`<a id="intellihrwork_classeslist_all"></a>

Returns a list of all [Work Classes](https://developers.intellihr.io/docs/v1/) recorded in the system.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = intellihr.work_classes.list_all()
```

#### 🔄 Return<a id="🔄-return"></a>

[`WorkClassesList`](./intelli_hr_python_sdk/pydantic/work_classes_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/work-classes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.work_rights.find_work_right_by_id`<a id="intellihrwork_rightsfind_work_right_by_id"></a>

Returns a single work right.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_work_right_by_id_response = intellihr.work_rights.find_work_right_by_id()
```

#### 🔄 Return<a id="🔄-return"></a>

[`WorkRights`](./intelli_hr_python_sdk/pydantic/work_rights.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/work-rights/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.work_rights.list_all`<a id="intellihrwork_rightslist_all"></a>

Returns a list of all [Work Rights](https://developers.intellihr.io/docs/v1/) recorded in the system.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = intellihr.work_rights.list_all()
```

#### 🔄 Return<a id="🔄-return"></a>

[`WorkRightsList`](./intelli_hr_python_sdk/pydantic/work_rights_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/work-rights` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.work_types.find_by_id`<a id="intellihrwork_typesfind_by_id"></a>

Returns a single work type.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_by_id_response = intellihr.work_types.find_by_id()
```

#### 🔄 Return<a id="🔄-return"></a>

[`WorkTypes`](./intelli_hr_python_sdk/pydantic/work_types.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/work-types/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.work_types.list_all`<a id="intellihrwork_typeslist_all"></a>

Returns a list of all [Work Types](https://developers.intellihr.io/docs/v1/) recorded in the system.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = intellihr.work_types.list_all()
```

#### 🔄 Return<a id="🔄-return"></a>

[`WorkTypesList`](./intelli_hr_python_sdk/pydantic/work_types_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/work-types` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.workflow_events.find_by_id`<a id="intellihrworkflow_eventsfind_by_id"></a>

Returns a single [Workflow Event](https://developers.intellihr.io/docs/v1/) by its identifier.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_by_id_response = intellihr.workflow_events.find_by_id()
```

#### 🔄 Return<a id="🔄-return"></a>

[`WorkflowEvents`](./intelli_hr_python_sdk/pydantic/workflow_events.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workflow-events/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `intellihr.workflows.trigger_by_id`<a id="intellihrworkflowstrigger_by_id"></a>

Trigger a Workflow and related Workflow Form Designs. 

This endpoint supports Workflows that are linked to Job onboarding, offboarding, role change and extended leave.

Currently the recipient and email address type for the individual forms will be automatically set based on the Respondent Type on the Form Design.  Form Designs with a Respondent Type of `Supervisor` for a job with no supervisor currently are not supported as no default option can be selected.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trigger_by_id_response = intellihr.workflows.trigger_by_id(
    job_id="8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
    workflow_form_designs=[
        {
            "id": "8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
        }
    ],
    id="8a5f3ea6-ea6b-4425-8a87-3c256bb7b6f9",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### job_id: `str`<a id="job_id-str"></a>

The identifier string for the [Job](https://developers.intellihr.io/docs/v1/) to trigger this Workflow for.

##### workflow_form_designs: [`WorkflowsPatchRequestWorkflowFormDesigns`](./intelli_hr_python_sdk/type/workflows_patch_request_workflow_form_designs.py)<a id="workflow_form_designs-workflowspatchrequestworkflowformdesignsintelli_hr_python_sdktypeworkflows_patch_request_workflow_form_designspy"></a>

##### id: `str`<a id="id-str"></a>

The id of the Workflow to trigger.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WorkflowsPatchRequest`](./intelli_hr_python_sdk/type/workflows_patch_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WorkflowsPatchResponse`](./intelli_hr_python_sdk/pydantic/workflows_patch_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workflows/{id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
