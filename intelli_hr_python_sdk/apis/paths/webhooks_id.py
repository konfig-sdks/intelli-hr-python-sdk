from intelli_hr_python_sdk.paths.webhooks_id.get import ApiForget
from intelli_hr_python_sdk.paths.webhooks_id.delete import ApiFordelete
from intelli_hr_python_sdk.paths.webhooks_id.patch import ApiForpatch


class WebhooksId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
