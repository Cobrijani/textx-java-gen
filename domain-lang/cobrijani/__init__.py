import os
from textx import language, metamodel_from_file

__version__ = "0.1.0.dev"

class SimpleType(object):
    """
    We are registering user SimpleType class to support
    simple types (integer, string) in our entity models
    Thus, user doesn't need to provide integer and string
    types in the model but can reference them in attribute types nevertheless.
    """

    def __init__(self, parent, name):
        self.parent = parent
        self.name = name

    def __str__(self):
        return self.name

@language('domain_lang', '*.mdl')
def domain_lang_language():
    "domain_lang language"
    current_dir = os.path.dirname(__file__)
    type_builtins = {
        'integer': SimpleType(None, 'integer'),
        'string': SimpleType(None, 'string')
    }
    mm = metamodel_from_file(os.path.join(current_dir, 'domain_lang.tx'), classes=[SimpleType], builtins=type_builtins)

    # Here if necessary register object processors or scope providers
    # http://textx.github.io/textX/stable/metamodel/#object-processors
    # http://textx.github.io/textX/stable/scoping/

    return mm
