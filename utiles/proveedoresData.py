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
# ./manage.py dumpscript proveedores.Proveedor
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

    # Processing model: proveedores.models.Proveedor

    from proveedores.models import Proveedor

    proveedores_proveedor_1 = Proveedor()
    proveedores_proveedor_1.cuit = '30-4219859-3'
    proveedores_proveedor_1.razon_social = 'ALEMANN S.R.L.'
    proveedores_proveedor_1.telefono = '123456789'
    proveedores_proveedor_1.email = 'empresa@proveedor.com'
    proveedores_proveedor_1.calle = 'Sarmiento'
    proveedores_proveedor_1.numero = '789'
    proveedores_proveedor_1.localidad =  importer.locate_object(Localidad, "id", Localidad, "id", 421, {'id': 421, 'cod_postal': '5000', 'localidad': 'CORDOBA', 'provincia_id': 6} ) 
    proveedores_proveedor_1.detalles = ''
    proveedores_proveedor_1 = importer.save_or_locate(proveedores_proveedor_1)

    proveedores_proveedor_2 = Proveedor()
    proveedores_proveedor_2.cuit = '30-59895662-2'
    proveedores_proveedor_2.razon_social = 'VIA PUBLICA CLAN S.A.'
    proveedores_proveedor_2.telefono = '123456789'
    proveedores_proveedor_2.email = 'empresa@proveedor.com'
    proveedores_proveedor_2.calle = 'Sarmiento'
    proveedores_proveedor_2.numero = '789'
    proveedores_proveedor_2.localidad =  importer.locate_object(Localidad, "id", Localidad, "id", 421, {'id': 421, 'cod_postal': '5000', 'localidad': 'CORDOBA', 'provincia_id': 6} ) 
    proveedores_proveedor_2.detalles = ''
    proveedores_proveedor_2 = importer.save_or_locate(proveedores_proveedor_2)

    proveedores_proveedor_3 = Proveedor()
    proveedores_proveedor_3.cuit = '30-50259063-0'
    proveedores_proveedor_3.razon_social = 'ATACAMA SA DE PUBLICIDAD'
    proveedores_proveedor_3.telefono = '123456789'
    proveedores_proveedor_3.email = 'empresa@proveedor.com'
    proveedores_proveedor_3.calle = 'Sarmiento'
    proveedores_proveedor_3.numero = '789'
    proveedores_proveedor_3.localidad =  importer.locate_object(Localidad, "id", Localidad, "id", 421, {'id': 421, 'cod_postal': '5000', 'localidad': 'CORDOBA', 'provincia_id': 6} ) 
    proveedores_proveedor_3.detalles = ''
    proveedores_proveedor_3 = importer.save_or_locate(proveedores_proveedor_3)

    proveedores_proveedor_4 = Proveedor()
    proveedores_proveedor_4.cuit = '30-60917843-0'
    proveedores_proveedor_4.razon_social = 'America TV S.A.'
    proveedores_proveedor_4.telefono = '123456789'
    proveedores_proveedor_4.email = 'empresa@proveedor.com'
    proveedores_proveedor_4.calle = 'San Juan'
    proveedores_proveedor_4.numero = '789'
    proveedores_proveedor_4.localidad =  importer.locate_object(Localidad, "id", Localidad, "id", 1584, {'id': 1584, 'cod_postal': '5800', 'localidad': 'RIO CUARTO', 'provincia_id': 6} ) 
    proveedores_proveedor_4.detalles = ''
    proveedores_proveedor_4 = importer.save_or_locate(proveedores_proveedor_4)

    proveedores_proveedor_5 = Proveedor()
    proveedores_proveedor_5.cuit = '30-64391342-5'
    proveedores_proveedor_5.razon_social = 'Red Celeste y Blanca S.A.'
    proveedores_proveedor_5.telefono = '123456789'
    proveedores_proveedor_5.email = 'empresa@proveedor.com'
    proveedores_proveedor_5.calle = 'San Juan'
    proveedores_proveedor_5.numero = '789'
    proveedores_proveedor_5.localidad =  importer.locate_object(Localidad, "id", Localidad, "id", 1584, {'id': 1584, 'cod_postal': '5800', 'localidad': 'RIO CUARTO', 'provincia_id': 6} ) 
    proveedores_proveedor_5.detalles = ''
    proveedores_proveedor_5 = importer.save_or_locate(proveedores_proveedor_5)

    proveedores_proveedor_6 = Proveedor()
    proveedores_proveedor_6.cuit = '30-54257223-6'
    proveedores_proveedor_6.razon_social = 'Junin TV S.A.'
    proveedores_proveedor_6.telefono = '123456789'
    proveedores_proveedor_6.email = 'empresa@proveedor.com'
    proveedores_proveedor_6.calle = 'San Juan'
    proveedores_proveedor_6.numero = '123'
    proveedores_proveedor_6.localidad =  importer.locate_object(Localidad, "id", Localidad, "id", 1584, {'id': 1584, 'cod_postal': '5800', 'localidad': 'RIO CUARTO', 'provincia_id': 6} ) 
    proveedores_proveedor_6.detalles = ''
    proveedores_proveedor_6 = importer.save_or_locate(proveedores_proveedor_6)

    proveedores_proveedor_7 = Proveedor()
    proveedores_proveedor_7.cuit = '30-68296025-2'
    proveedores_proveedor_7.razon_social = 'e.a. carnevale y cia s.a.'
    proveedores_proveedor_7.telefono = '123456789'
    proveedores_proveedor_7.email = 'empresa@proveedor.com'
    proveedores_proveedor_7.calle = 'Belgrano'
    proveedores_proveedor_7.numero = '123'
    proveedores_proveedor_7.localidad =  importer.locate_object(Localidad, "id", Localidad, "id", 1932, {'id': 1932, 'cod_postal': '5900', 'localidad': 'VILLA MARIA', 'provincia_id': 6} ) 
    proveedores_proveedor_7.detalles = ''
    proveedores_proveedor_7 = importer.save_or_locate(proveedores_proveedor_7)

    proveedores_proveedor_8 = Proveedor()
    proveedores_proveedor_8.cuit = '30-71083174-9'
    proveedores_proveedor_8.razon_social = 'GRUPO INVERSOR PUBLICITARIO SA'
    proveedores_proveedor_8.telefono = '123456789'
    proveedores_proveedor_8.email = 'empresa@proveedor.com'
    proveedores_proveedor_8.calle = 'Belgrano'
    proveedores_proveedor_8.numero = '123'
    proveedores_proveedor_8.localidad =  importer.locate_object(Localidad, "id", Localidad, "id", 1932, {'id': 1932, 'cod_postal': '5900', 'localidad': 'VILLA MARIA', 'provincia_id': 6} ) 
    proveedores_proveedor_8.detalles = ''
    proveedores_proveedor_8 = importer.save_or_locate(proveedores_proveedor_8)

    proveedores_proveedor_9 = Proveedor()
    proveedores_proveedor_9.cuit = '30-70863046-9'
    proveedores_proveedor_9.razon_social = 'Latin Outdoor SA'
    proveedores_proveedor_9.telefono = '123456789'
    proveedores_proveedor_9.email = 'empresa@proveedor.com'
    proveedores_proveedor_9.calle = 'Belgrano'
    proveedores_proveedor_9.numero = '123'
    proveedores_proveedor_9.localidad =  importer.locate_object(Localidad, "id", Localidad, "id", 1932, {'id': 1932, 'cod_postal': '5900', 'localidad': 'VILLA MARIA', 'provincia_id': 6} ) 
    proveedores_proveedor_9.detalles = ''
    proveedores_proveedor_9 = importer.save_or_locate(proveedores_proveedor_9)
