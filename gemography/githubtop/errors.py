from rest_framework.exceptions import APIException


class SchemaChangedError(APIException):
    status_code = 500
    default_detail = 'Github API response schema changed.'
    default_code = 'schema_changed'
