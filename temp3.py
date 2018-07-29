def is_downloadable(content_type):
    """
        Returns whether the file is downloadable or not from the file headers's content-type.

        :param content_type: content-type in the file header
        :returns: True if the file is downloadable else False
    """
    if 'text' in content_type.lower():
        return False
    if 'html' in content_type.lower():
        return False
    return True


print(is_downloadable.__doc__)