import re
from django.core.exceptions import ValidationError


def zip_code_validation(zip_code):
    pattern = r'\d{10}'
    if not bool(re.match(pattern, zip_code)):
        raise ValidationError('zip_code most be 10 character and just number!!!')
