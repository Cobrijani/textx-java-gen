from textx import GeneratorDesc
import os
import jinja2
import sys

def __relations_type(value, cardinality):
    if cardinality == '[0..n]':
        return "java.util.Set<" + value + ">"
    else:
        return value
    
def __relations_init(cardinality):
    if cardinality == '[0..n]':
        return " = new java.util.HashSet<>()"
    else:
        return ""
    


def codegen_java_pu(
    metamodel, model, output_path, overwrite, debug=False, **custom_args
):
    """
    Generate java code
    """
    current_dir = os.path.dirname(__file__)

    jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(current_dir),
        trim_blocks=True,
        lstrip_blocks=True,
    )

    def javatype(s):
        """
        Maps type names from PrimitiveType to Java.
        """
        return {"integer": "int", "string": "String"}.get(s.name, s.name)

    # Register filter for mapping Entity type names to Java type names.
    jinja_env.filters["javatype"] = javatype
    jinja_env.filters['reltype'] = __relations_type
    jinja_env.filters['relinit'] = __relations_init

    # Load Java template
    template = jinja_env.get_template("entity_java.template")

    if not os.path.exists(output_path):
        sys.exit(output_path + " does not exist")

    for entity in model.entities:    
        with open(
            os.path.join(output_path, "%s.java" % entity.name), "w"
        ) as f:
            f.write(template.render(entity=entity))


gen_def = GeneratorDesc(
    language="domain_lang",
    target="java",
    description="Generate java",
    generator=codegen_java_pu,
)
