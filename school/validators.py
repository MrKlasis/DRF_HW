from rest_framework.serializers import ValidationError


class LessonVideoValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        reg = 'youtube.com'
        tmp_val = dict(value).get(self.field)
        if tmp_val:
            if reg not in tmp_val:
                raise ValidationError('link is not available')
