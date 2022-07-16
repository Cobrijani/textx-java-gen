from __future__ import unicode_literals
import os
import pytest
from textx import (metamodel_for_language,
                   clear_language_registrations)

current_dir = os.path.dirname(__file__)

@pytest.fixture(scope='module')
def clear_all():
    clear_language_registrations()
    
    
    
def test_simple_entities(clear_all):
    """
    Testing simple entities
    """
    mmF = metamodel_for_language('domain_lang')
    model = mmF.model_from_file(os.path.join(current_dir,
                                             'models',
                                             'simple_entities.mdl'))
    assert(model is not None)
    assert(len(model.entities) == 2)
    
def test_cardinality(clear_all):
    """
    Testing cardinality entities
    """
    mmF = metamodel_for_language('domain_lang')
    model = mmF.model_from_file(os.path.join(current_dir,
                                             'models',
                                             'entity_cardinality.mdl'), debug=False)
    assert(model is not None)
    assert(len(model.entities) == 6)
