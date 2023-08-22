import os
import uuid
from typing import Union

from django.db.models.fields.files import FieldFile, ImageFieldFile


def remove_field_file(instance_field: Union[FieldFile, ImageFieldFile]) -> None:
    """
    checks if there is a file related to given field
    and deletes it from file system
    """
    import os

    if instance_field and os.path.isfile(instance_field.path):
        os.remove(instance_field.path)


def generate_uuid_for_file_with_dir(original_file_name: str, upload_dir: str):
    """
    generates a uuid name for given file and concats it to given dir
    Example: <upload_dir>/193f511b-6061-4b03-b136-2d5fa1b3b39b<.extension>
    """
    extension = original_file_name.split(".")[-1]
    file_name = f"{uuid.uuid4()}.{extension}"
    return os.path.join(upload_dir, file_name)
