import string

REGULAR_EXPRESSION = '^[a-zA-Z0-9]{1,16}$'
SYMBOLS = string.ascii_letters + string.digits
SYMBOLS_COUNT = 6
URL_MAX_LENGTH = 2048  # max for Microsoft Internet Explorer
SHORT_MAX_LENGTH = 16
REQUIRED_FIELD = '\"url\" является обязательным полем!'
URL_REGULAR_EXPRESSION = r'(https?://[\w.:]+/?(?:[\w/?&=.~;\-+!*_#%])*)'
URL_ERROR = 'Некорректная ссылка'
URL_MAX_LENGTH_ERROR = f'Длина url превышает {URL_MAX_LENGTH} символов.'
SHORT_IS_BUSY_API = 'Имя "{short}" уже занято.'  # смысл в 2х константах с почти
SHORT_IS_BUSY_FORM = 'Имя {short} уже занято!'  # ...одинаковым значением: pytest
SHORT_NAME_ERROR = 'Указано недопустимое имя для короткой ссылки'
REQUEST_BODY_ERROR = 'Отсутствует тело запроса'
URL_OBJ_NOT_FOUND = 'Указанный id не найден'
JSON_KEY_FOR_ORIGINAL = 'url'
JSON_KEY_FOR_SHORT = 'custom_id'