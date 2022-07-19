import os
import re
from unittest import result
from textx.cli import textx
from click.testing import CliRunner

this_folder = os.path.abspath(os.path.dirname(__file__))


def __assert_files_equal(actual_file, expected_file):
    """Assert that content of two files is equal

    Args:
        actual_file (str): actual file path
        expected_file (str): expected file path
    """
    with open(actual_file, "r") as actual, open(expected_file, "r") as expected:
        assert actual.read() == expected.read()


def __run_test_scenario(outdir, testcasefile):
    """Run the test given test scenario"""
    model_file = os.path.join(this_folder, "models", testcasefile)
    assert os.path.exists(model_file)

    runner = CliRunner()
    result = runner.invoke(
        textx, ["generate", model_file, "--target", "java", "-o", outdir]
    )

    return result


def test_simple_entities(tmpdir):
    """Create test case that tests generation of simple entities.

    Args:
        tmpdir (fixture): tmpdir
    """
    output = tmpdir.mkdir("test_dir")
    result = __run_test_scenario(output, "simple_entities.mdl")
    assert result.exit_code == 0

    __assert_files_equal(
        output.join("Address.java"),
        os.path.join(this_folder, "models/simple_entities/Address.java"),
    )
    __assert_files_equal(
        output.join("Person.java"),
        os.path.join(this_folder, "models/simple_entities/Person.java"),
    )


def test_entity_cardinality(tmpdir):
    """Create test case that tests generation of entities with cardinality.

    Args:
        tmpdir (fixture): tmpdir fixture
    """

    output = tmpdir.mkdir("test_dir")
    #output = os.path.join(this_folder, 'out')

    result = __run_test_scenario(output, "entity_cardinality.mdl")
    assert result.exit_code == 0

    for entity in [
        "ManyToOneNullableCardinality",
        "OneToManyCardinality",
        "OneToOneCardinality",
        "OneToOneNullable2Cardinality",
        "OneToOneNullableCardinality",
        "ProductItem",
    ]:
        print(output.join(entity + ".java"))
        print( os.path.join(this_folder, "models", "entity_cardinality", entity + ".java"))
        __assert_files_equal(
            output.join(entity + ".java"),
            os.path.join(this_folder, "models", "entity_cardinality", entity + ".java")
        )
