#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file has been automatically generated.
# Instead of changing it, create a file called import_helper.py
# and put there a class called ImportHelper(object) in it.
#
# This class will be specially casted so that instead of extending object,
# it will actually extend the class BasicImportHelper()
#
# That means you just have to overload the methods you want to
# change, leaving the other ones inteact.
#
# Something that you might want to do is use transactions, for example.
#
# Also, don't forget to add the necessary Django imports.
#
# This file was generated with the following command:
# ./manage.py dumpscript clientes
#
# to restore it, run
# manage.py runscript module_name.this_script_name
#
# example: if manage.py is at ./manage.py
# and the script is at ./some_folder/some_script.py
# you must make sure ./some_folder/__init__.py exists
# and run  ./manage.py runscript some_folder.some_script
import os, sys
from django.db import transaction

class BasicImportHelper(object):

    def pre_import(self):
        pass

    @transaction.atomic
    def run_import(self, import_data):
        import_data()

    def post_import(self):
        pass

    def locate_similar(self, current_object, search_data):
        # You will probably want to call this method from save_or_locate()
        # Example:
        #   new_obj = self.locate_similar(the_obj, {"national_id": the_obj.national_id } )

        the_obj = current_object.__class__.objects.get(**search_data)
        return the_obj

    def locate_object(self, original_class, original_pk_name, the_class, pk_name, pk_value, obj_content):
        # You may change this function to do specific lookup for specific objects
        #
        # original_class class of the django orm's object that needs to be located
        # original_pk_name the primary key of original_class
        # the_class      parent class of original_class which contains obj_content
        # pk_name        the primary key of original_class
        # pk_value       value of the primary_key
        # obj_content    content of the object which was not exported.
        #
        # You should use obj_content to locate the object on the target db
        #
        # An example where original_class and the_class are different is
        # when original_class is Farmer and the_class is Person. The table
        # may refer to a Farmer but you will actually need to locate Person
        # in order to instantiate that Farmer
        #
        # Example:
        #   if the_class == SurveyResultFormat or the_class == SurveyType or the_class == SurveyState:
        #       pk_name="name"
        #       pk_value=obj_content[pk_name]
        #   if the_class == StaffGroup:
        #       pk_value=8

        search_data = { pk_name: pk_value }
        the_obj = the_class.objects.get(**search_data)
        #print(the_obj)
        return the_obj


    def save_or_locate(self, the_obj):
        # Change this if you want to locate the object in the database
        try:
            the_obj.save()
        except:
            print("---------------")
            print("Error saving the following object:")
            print(the_obj.__class__)
            print(" ")
            print(the_obj.__dict__)
            print(" ")
            print(the_obj)
            print(" ")
            print("---------------")

            raise
        return the_obj


importer = None
try:
    import import_helper
    # We need this so ImportHelper can extend BasicImportHelper, although import_helper.py
    # has no knowlodge of this class
    importer = type("DynamicImportHelper", (import_helper.ImportHelper, BasicImportHelper ) , {} )()
except ImportError as e:
    # From Python 3.3 we can check e.name - string match is for backward compatibility.
    if 'import_helper' in str(e):
        importer = BasicImportHelper()
    else:
        raise

import datetime
from decimal import Decimal
from django.contrib.contenttypes.models import ContentType

try:
    import dateutil.parser
except ImportError:
    print("Please install python-dateutil")
    sys.exit(os.EX_USAGE)

def run():
    importer.pre_import()
    importer.run_import(import_data)
    importer.post_import()

def import_data():
    # Initial Imports
    from gestion.models import Localidad

    # Processing model: clientes.models.Cliente

    from clientes.models import Cliente

    clientes_cliente_1 = Cliente()
    clientes_cliente_1.nombre = 'Marcelo Elvio'
    clientes_cliente_1.apellido = 'Richetta'
    clientes_cliente_1.email = 'mrichetta@hotmail.com'
    clientes_cliente_1.telefono = '3534987654'
    clientes_cliente_1.calle = 'Santa Fe'
    clientes_cliente_1.numero = '565'
    clientes_cliente_1.localidad =  importer.locate_object(Localidad, "id", Localidad, "id", 1149, {'id': 1149, 'cod_postal': '5921', 'localidad': 'LAS PERDICES', 'provincia_id': 6} ) 
    clientes_cliente_1.detalles = ''
    clientes_cliente_1 = importer.save_or_locate(clientes_cliente_1)

    clientes_cliente_2 = Cliente()
    clientes_cliente_2.nombre = 'Marco'
    clientes_cliente_2.apellido = 'Richetta'
    clientes_cliente_2.email = 'marcorichetta@gmail.com'
    clientes_cliente_2.telefono = '3534220065'
    clientes_cliente_2.calle = 'Santa Fe'
    clientes_cliente_2.numero = '565'
    clientes_cliente_2.localidad =  importer.locate_object(Localidad, "id", Localidad, "id", 1149, {'id': 1149, 'cod_postal': '5921', 'localidad': 'LAS PERDICES', 'provincia_id': 6} ) 
    clientes_cliente_2.detalles = ''
    clientes_cliente_2 = importer.save_or_locate(clientes_cliente_2)

    clientes_cliente_3 = Cliente()
    clientes_cliente_3.nombre = 'Matias'
    clientes_cliente_3.apellido = 'Richetta'
    clientes_cliente_3.email = 'mrichetta@hotmail.com'
    clientes_cliente_3.telefono = '3534987654'
    clientes_cliente_3.calle = 'San Martin'
    clientes_cliente_3.numero = '123'
    clientes_cliente_3.localidad =  importer.locate_object(Localidad, "id", Localidad, "id", 421, {'id': 421, 'cod_postal': '5000', 'localidad': 'CORDOBA', 'provincia_id': 6} ) 
    clientes_cliente_3.detalles = ''
    clientes_cliente_3 = importer.save_or_locate(clientes_cliente_3)

    clientes_cliente_4 = Cliente()
    clientes_cliente_4.nombre = 'Melba'
    clientes_cliente_4.apellido = 'Coceres'
    clientes_cliente_4.email = 'melbacoceres@gmail.com'
    clientes_cliente_4.telefono = '3534123456'
    clientes_cliente_4.calle = 'Santa Fe'
    clientes_cliente_4.numero = '123'
    clientes_cliente_4.localidad =  importer.locate_object(Localidad, "id", Localidad, "id", 1149, {'id': 1149, 'cod_postal': '5921', 'localidad': 'LAS PERDICES', 'provincia_id': 6} ) 
    clientes_cliente_4.detalles = 'Mamá'
    clientes_cliente_4 = importer.save_or_locate(clientes_cliente_4)

    clientes_cliente_5 = Cliente()
    clientes_cliente_5.nombre = 'Natalia'
    clientes_cliente_5.apellido = 'Vera'
    clientes_cliente_5.email = 'nvera@hotmail.com'
    clientes_cliente_5.telefono = '123456789'
    clientes_cliente_5.calle = '25 de Mayo'
    clientes_cliente_5.numero = '1894'
    clientes_cliente_5.localidad =  importer.locate_object(Localidad, "id", Localidad, "id", 730, {'id': 730, 'cod_postal': '5809', 'localidad': 'GENERAL CABRERA', 'provincia_id': 6} ) 
    clientes_cliente_5.detalles = ''
    clientes_cliente_5 = importer.save_or_locate(clientes_cliente_5)