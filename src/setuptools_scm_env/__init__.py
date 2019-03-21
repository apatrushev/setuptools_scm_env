import os


class Version(object):
    def __init__(self, tag):
        self.tag = tag
        self.preformatted = True


def main(*args, **kwargs):
    if "SETUPTOOLS_SCM_VERSION" in os.environ:
        return Version(os.environ.get("SETUPTOOLS_SCM_VERSION"))
