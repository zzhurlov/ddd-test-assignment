import re


MAX_TITLE_LENGTH = 255
MAX_ADDRESS_LENGTH = 255


PHONE_REGEX = re.compile(r"^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$")
