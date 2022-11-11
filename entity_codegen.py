"""
An example how to generate angularjs code from textX model using jinja2
template engine (http://jinja.pocoo.org/docs/dev/)
"""
from os import mkdir
from os.path import exists, dirname, join
import jinja2
from entity_test import get_entity_mm


def main(debug=False):

    this_folder = dirname(__file__)

    entity_mm = get_entity_mm(debug)

    # Build Person model from tiendita.ent file
    person_model = entity_mm.model_from_file(join(this_folder, 'tiendita.ent'))

    def is_entity(n):
        """
        Test to prove if some type is an entity
        """
        if n.type in person_model.entities:
            return True
        else:
            return False

    def sql_type(s):
        """
        Maps type names from PrimitiveType to SQL.
        """
        return {
                'integer': 'INTEGER',
                'string': 'TEXT',
		    'boolean': 'INTEGER'
        }.get(s.name, s.name)
	
    # Create output folder
    srcgen_folder = join(this_folder, 'srcgen')
    if not exists(srcgen_folder):
        mkdir(srcgen_folder)

    # Initialize template engine.
    jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(this_folder),
        trim_blocks=True,
        lstrip_blocks=True)
	
    # Register filter for mapping Entity type names to Java type names.

    jinja_env.tests['entity'] = is_entity

    jinja_env.filters['sql_type'] = sql_type

    jinja_env.add_extension('jinja2.ext.debug')

    #------- REPOSITORIES -------#
    # Load template
    template = jinja_env.get_template('repositories.template')

    for entity in person_model.entities:
        # For each entity generate python file
        with open(join(srcgen_folder,
                       "%s.py" % (entity.name.capitalize()+"_repo")), 'w') as f:
            f.write(template.render(entity=entity))

    #------- REST CONTROLLERS -------#
    template = jinja_env.get_template('restserv.template')

    for entity in person_model.entities:
        # For each entity generate python file
        with open(join(srcgen_folder,
                       "%s.py" % (entity.name.capitalize()+"_controller")), 'w') as f:
            f.write(template.render(entity=entity))


    # Load agregar template

    template = jinja_env.get_template('list.template')

    for entity in person_model.entities:
        # For each entity generate html file
        with open(join(srcgen_folder,
                       "listar%s.html" % entity.name.capitalize()), 'w') as f:
            f.write(template.render(entity=entity))

    # Load template
    template = jinja_env.get_template('editar.template')

    for entity in person_model.entities:
        # For each entity generate html file
        with open(join(srcgen_folder,
                       "editar%s.html" % entity.name.capitalize()), 'w') as f:
            f.write(template.render(entity=entity))

    # Load template
    template = jinja_env.get_template('agregarCtrl.template')

    for entity in person_model.entities:
        # For each entity generate js file
        with open(join(srcgen_folder,
                       "agregar%s.js" % entity.name.capitalize()), 'w') as f:
            f.write(template.render(entity=entity))

if __name__ == "__main__":
    main()
