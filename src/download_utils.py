import re


def is_downloadable(content_type):
    """
    Returns whether the file is downloadable or not from the file's content-type

    :param content_type: content-type of the file header
    :return: True if the file is downloadable else False
    """
    if 'text' in content_type.lower():
        return False
    if 'html' in content_type.lower():
        return False
    return True


def get_filename_from_cd(cd):
    """
    Get filename from content-disposition.

    :param cd: content-disposition of the file header
    :return: file name
    """
    if not cd:
        return None
    name = re.findall('filename=(.+)', cd)
    if len(name) == 0:
        return None
    return re.sub(r'[^\x00-\x7f]', r'', name[0].replace('"', ''))
