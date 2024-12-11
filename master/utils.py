import unicodedata
import re
from django.utils.functional import keep_lazy_text


@keep_lazy_text
def slugify(value, allow_unicode=False):
    """
    Convert to ASCII if 'allow_unicode' is False. Convert spaces to hyphens.
    Remove characters that aren't alphanumerics, underscores, or hyphens.
    Convert to lowercase. Also strip leading and trailing whitespace.
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize(
            'NFKD', value).encode(
            'ascii', 'ignore').decode('ascii')
    # For Plus:
    value = re.sub(r'[+]', ' plus', value)
    value = re.sub(r'[^\w\s-]', '', value).strip().lower()
    return re.sub(r'[-\s]+', '-', value)
