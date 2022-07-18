from textx import GeneratorDesc
import os
import jinja2
import sys

def codegen_java_pu(metamodel, model, output_path, overwrite, debug=False,
                    **custom_args):
    """
    Generate java code
    """
    current_dir = os.path.dirname(__file__)
        
    jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(current_dir),
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
    
    if not os.path.exists(output_path):
        print(output_path + " does not exist")
        sys.exit(1)
        return

    for entity in model.entities:
        with open(os.path.join(output_path,
                       "%s.java" % entity.name.capitalize()), 'w') as f:
            f.write(template.render(entity=entity))


gen_def = GeneratorDesc(
    language='domain_lang',
    target='java',
    description='Generate java',
    generator=codegen_java_pu)
