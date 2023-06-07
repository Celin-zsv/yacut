import string

REGULAR_EXPRESSION = '^[a-zA-Z0-9]{1,16}$'
SYMBOLS = string.ascii_letters + string.digits
SYMBOLS_COUNT = 6
MODEL_FIELD_TO_JSON_FIELD = {
    'original': 'url',
    'short': 'custom_id'}