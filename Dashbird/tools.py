from django.conf import settings
import re
import os



class ChoicesFromDir(object):
    """
    A lazy iterator that list files in given directory, returning a list of
    pairs (matched_file, display_text).

    Primarily built to be used in `choices` model field attribute.
    """

    _DISPLAY_SPLIT_RE = re.compile(r'-| |_|\.')

    def __init__(self, path, match=None, display_func=None):
        """
        Construct a lazy listing directory iterator.
        If `match` is None, every file is kept.
        If `display_func` is None, then the file name will be set to ChoicesFromDir.display

        :param path: path to the directory, passed to os.listdir
        :param match: regular expression that catches kept files. Must contain one named group "name" that will
        be kept for display.
        :param display_func: function that takes a filename (string) and return a string.
        """
        self.path = path
        self.match = match if match else '.*'
        self.display_func = display_func if display_func else ChoicesFromDir.display

    def __iter__(self):
        match_re = re.compile(self.match)
        path = os.path.join(settings.BASE_DIR, self.path)

        for filename in os.listdir(path):
            matching = match_re.match(filename)
            if matching:
                if os.path.isfile(os.path.join(path, filename)):
                    yield (filename, self.display_func(matching.group('name')))


    @staticmethod
    def display(filename):
        """
        :param filename: Filename to display
        :return: A pretty display string for given filename
        """
        try:
            filename, ext = filename.rsplit('.', 1)
        except ValueError:
            filename, ext = filename, ''

        return ' '.join([chunk.title() for chunk in re.split(ChoicesFromDir._DISPLAY_SPLIT_RE, filename)])
