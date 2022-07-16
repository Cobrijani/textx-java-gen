from textx import GeneratorDesc
import os
import jinja2


def codegen_java_pu(metamodel, model, output_path, overwrite, debug=False,
                    **custom_args):
    """
    Generate java code
    """
    jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
        trim_blocks=True,
        lstrip_blocks=True)

    def javatype(s):
        """
        Maps type names from PrimitiveType to Java.
        """
        return {
            'integer': 'int',
            'string': 'String'
        }.get(s.name, s.name)
    # Register filter for mapping Entity type names to Java type names.
    jinja_env.filters['javatype'] = javatype

    # Load Java template
    template = jinja_env.get_template('entity_java.template')

    for entity in model.entities:
        with open(os.path.join(output_path,
                       "%s.java" % entity.name.capitalize()), 'w') as f:
            f.write(template.render(entity=entity))


gen_def = GeneratorDesc(
    language='domain_lang',
    target='java',
    description='Generate java',
    generator=codegen_java_pu)
