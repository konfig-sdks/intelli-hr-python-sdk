from intelli_hr_python_sdk.paths.locations_id.get import ApiForget
from intelli_hr_python_sdk.paths.locations_id.delete import ApiFordelete
from intelli_hr_python_sdk.paths.locations_id.patch import ApiForpatch


class LocationsId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
