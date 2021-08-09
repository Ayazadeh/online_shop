import os
import re

from django.core.exceptions import ValidationError


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpg', '.png', '.jpeg']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


def phone_validation(phone):
    pattern = r'(^09\d{9}$)|(^\+989\d{9}$)'
    if not bool(re.match(pattern, phone)):
        raise ValidationError('Phone number is wrong!!!')
