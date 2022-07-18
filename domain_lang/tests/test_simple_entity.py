from __future__ import unicode_literals
from distutils.log import debug
import os
import pytest
from textx import (metamodel_for_language,
                   clear_language_registrations)

current_dir = os.path.dirname(__file__)

@pytest.fixture(scope='module')
def clear_all():
    clear_language_registrations()
    

def __retrieve_model(test_file):
    """Retrieve model for given language
    """
    mmF = metamodel_for_language('domain_lang')
    return mmF.model_from_file(os.path.join(current_dir,
                                             'models',
                                             test_file), debug=True)
    
    
def test_simple_entities(clear_all):
    """
    Testing simple entities
    """
    model = __retrieve_model("simple_entities.mdl")
    assert(model is not None)
    assert(len(model.entities) == 2)
    
def test_cardinality(clear_all):
    """
    Testing cardinality entities
    """
    model = __retrieve_model("entity_cardinality.mdl")
    assert(model is not None)
    assert(len(model.entities) == 6)
    

def test_enum(clear_all):
    """Testing enums

    Args:
        clear_all (_type_): _description_
    """
    model = __retrieve_model("simple_enums.mdl")
    assert(model is not None)
    assert(len(model.entities) == 1)
    assert(len(model.enums) == 1)

def test_data_types(clear_all):
    """Test complex type in a language

    Args:
        clear_all (_type_): _description_
    """
    model = __retrieve_model("data_type.mdl")

    assert(model is not None)
    assert(len(model.data_types) == 2)
    assert(len(model.enums) == 1)
    
