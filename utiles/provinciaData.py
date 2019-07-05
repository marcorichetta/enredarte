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
# ./manage.py dumpscript gestion.Provincia
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

    # Processing model: gestion.models.Provincia

    from gestion.models import Provincia

    gestion_provincia_1 = Provincia()
    gestion_provincia_1.cod_provincia = 'AR-B'
    gestion_provincia_1.provincia = ' Buenos Aires'
    gestion_provincia_1 = importer.save_or_locate(gestion_provincia_1)

    gestion_provincia_2 = Provincia()
    gestion_provincia_2.cod_provincia = 'AR-C'
    gestion_provincia_2.provincia = ' Capital Federal'
    gestion_provincia_2 = importer.save_or_locate(gestion_provincia_2)

    gestion_provincia_3 = Provincia()
    gestion_provincia_3.cod_provincia = 'AR-K'
    gestion_provincia_3.provincia = ' Catamarca'
    gestion_provincia_3 = importer.save_or_locate(gestion_provincia_3)

    gestion_provincia_4 = Provincia()
    gestion_provincia_4.cod_provincia = 'AR-H'
    gestion_provincia_4.provincia = ' Chaco'
    gestion_provincia_4 = importer.save_or_locate(gestion_provincia_4)

    gestion_provincia_5 = Provincia()
    gestion_provincia_5.cod_provincia = 'AR-U'
    gestion_provincia_5.provincia = ' Chubut'
    gestion_provincia_5 = importer.save_or_locate(gestion_provincia_5)

    gestion_provincia_6 = Provincia()
    gestion_provincia_6.cod_provincia = 'AR-X'
    gestion_provincia_6.provincia = ' Córdoba'
    gestion_provincia_6 = importer.save_or_locate(gestion_provincia_6)

    gestion_provincia_7 = Provincia()
    gestion_provincia_7.cod_provincia = 'AR-W'
    gestion_provincia_7.provincia = ' Corrientes'
    gestion_provincia_7 = importer.save_or_locate(gestion_provincia_7)

    gestion_provincia_8 = Provincia()
    gestion_provincia_8.cod_provincia = 'AR-E'
    gestion_provincia_8.provincia = ' Entre Ríos'
    gestion_provincia_8 = importer.save_or_locate(gestion_provincia_8)

    gestion_provincia_9 = Provincia()
    gestion_provincia_9.cod_provincia = 'AR-P'
    gestion_provincia_9.provincia = ' Formosa'
    gestion_provincia_9 = importer.save_or_locate(gestion_provincia_9)

    gestion_provincia_10 = Provincia()
    gestion_provincia_10.cod_provincia = 'AR-Y'
    gestion_provincia_10.provincia = ' Jujuy'
    gestion_provincia_10 = importer.save_or_locate(gestion_provincia_10)

    gestion_provincia_11 = Provincia()
    gestion_provincia_11.cod_provincia = 'AR-L'
    gestion_provincia_11.provincia = ' La Pampa'
    gestion_provincia_11 = importer.save_or_locate(gestion_provincia_11)

    gestion_provincia_12 = Provincia()
    gestion_provincia_12.cod_provincia = 'AR-F'
    gestion_provincia_12.provincia = ' La Rioja'
    gestion_provincia_12 = importer.save_or_locate(gestion_provincia_12)

    gestion_provincia_13 = Provincia()
    gestion_provincia_13.cod_provincia = 'AR-M'
    gestion_provincia_13.provincia = ' Mendoza'
    gestion_provincia_13 = importer.save_or_locate(gestion_provincia_13)

    gestion_provincia_14 = Provincia()
    gestion_provincia_14.cod_provincia = 'AR-N'
    gestion_provincia_14.provincia = ' Misiones'
    gestion_provincia_14 = importer.save_or_locate(gestion_provincia_14)

    gestion_provincia_15 = Provincia()
    gestion_provincia_15.cod_provincia = 'AR-Q'
    gestion_provincia_15.provincia = ' Neuquén'
    gestion_provincia_15 = importer.save_or_locate(gestion_provincia_15)

    gestion_provincia_16 = Provincia()
    gestion_provincia_16.cod_provincia = 'AR-R'
    gestion_provincia_16.provincia = ' Río Negro'
    gestion_provincia_16 = importer.save_or_locate(gestion_provincia_16)

    gestion_provincia_17 = Provincia()
    gestion_provincia_17.cod_provincia = 'AR-A'
    gestion_provincia_17.provincia = ' Salta'
    gestion_provincia_17 = importer.save_or_locate(gestion_provincia_17)

    gestion_provincia_18 = Provincia()
    gestion_provincia_18.cod_provincia = 'AR-J'
    gestion_provincia_18.provincia = ' San Juan'
    gestion_provincia_18 = importer.save_or_locate(gestion_provincia_18)

    gestion_provincia_19 = Provincia()
    gestion_provincia_19.cod_provincia = 'AR-D'
    gestion_provincia_19.provincia = ' San Luis'
    gestion_provincia_19 = importer.save_or_locate(gestion_provincia_19)

    gestion_provincia_20 = Provincia()
    gestion_provincia_20.cod_provincia = 'AR-Z'
    gestion_provincia_20.provincia = ' Santa Cruz'
    gestion_provincia_20 = importer.save_or_locate(gestion_provincia_20)

    gestion_provincia_21 = Provincia()
    gestion_provincia_21.cod_provincia = 'AR-S'
    gestion_provincia_21.provincia = ' Santa Fe'
    gestion_provincia_21 = importer.save_or_locate(gestion_provincia_21)

    gestion_provincia_22 = Provincia()
    gestion_provincia_22.cod_provincia = 'AR-G'
    gestion_provincia_22.provincia = ' Santiago del Estero'
    gestion_provincia_22 = importer.save_or_locate(gestion_provincia_22)

    gestion_provincia_23 = Provincia()
    gestion_provincia_23.cod_provincia = 'AR-V'
    gestion_provincia_23.provincia = ' Tierra del Fuego'
    gestion_provincia_23 = importer.save_or_locate(gestion_provincia_23)

    gestion_provincia_24 = Provincia()
    gestion_provincia_24.cod_provincia = 'AR-T'
    gestion_provincia_24.provincia = ' Tucumán'
    gestion_provincia_24 = importer.save_or_locate(gestion_provincia_24)

