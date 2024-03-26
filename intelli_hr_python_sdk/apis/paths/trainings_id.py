from intelli_hr_python_sdk.paths.trainings_id.get import ApiForget
from intelli_hr_python_sdk.paths.trainings_id.delete import ApiFordelete
from intelli_hr_python_sdk.paths.trainings_id.patch import ApiForpatch


class TrainingsId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
