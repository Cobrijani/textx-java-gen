import os
from textx.cli import textx
from click.testing import CliRunner

this_folder = os.path.abspath(os.path.dirname(__file__))


def test_entity_generate():
    """_summary_
    """
    
    fname = os.path.join(this_folder,
                         'models', 'Address.java')
    try:
        os.remove(fname)
    except OSError:
        pass
    
    model_file = os.path.join(this_folder,
                              'models', 'simple_entities.mdl')
    assert os.path.exists(model_file)
    
    
    runner = CliRunner()
    result = runner.invoke(textx, ['generate',
                                   '--target', 'java',
                                   '-o', 'out/',
                                   '--overwrite', model_file])
    
    assert result.exit_code == 0