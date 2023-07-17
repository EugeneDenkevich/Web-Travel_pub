from django.core.exceptions import ValidationError
from .settings import (MAX_IMAGE_SIZE, MAX_IMAGE_SIZE_MB,
                       MAX_NUMBER_OF_GUESTS)


def validate_image_size(image):
    try:
        if image.size > MAX_IMAGE_SIZE:
            raise ValidationError(
                f'Максмимальный размер изображения должен быть не более {MAX_IMAGE_SIZE_MB} Mb.'
            )
    except FileNotFoundError:
        return
