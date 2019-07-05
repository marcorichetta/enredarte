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
# ./manage.py dumpscript gestion.Localidad
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
    from gestion.models import Provincia

    # Processing model: gestion.models.Localidad

    from gestion.models import Localidad

    gestion_localidad_1 = Localidad()
    gestion_localidad_1.cod_postal = '5272'
    gestion_localidad_1.localidad = '9 DE JULIO'
    gestion_localidad_1.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1 = importer.save_or_locate(gestion_localidad_1)

    gestion_localidad_2 = Localidad()
    gestion_localidad_2.cod_postal = '5220'
    gestion_localidad_2.localidad = 'ABBURRA'
    gestion_localidad_2.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_2 = importer.save_or_locate(gestion_localidad_2)

    gestion_localidad_3 = Localidad()
    gestion_localidad_3.cod_postal = '5833'
    gestion_localidad_3.localidad = 'ACHIRAS'
    gestion_localidad_3.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_3 = importer.save_or_locate(gestion_localidad_3)

    gestion_localidad_4 = Localidad()
    gestion_localidad_4.cod_postal = '5875'
    gestion_localidad_4.localidad = 'ACHIRAS'
    gestion_localidad_4.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_4 = importer.save_or_locate(gestion_localidad_4)

    gestion_localidad_5 = Localidad()
    gestion_localidad_5.cod_postal = '5216'
    gestion_localidad_5.localidad = 'ACOLLARADO'
    gestion_localidad_5.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_5 = importer.save_or_locate(gestion_localidad_5)

    gestion_localidad_6 = Localidad()
    gestion_localidad_6.cod_postal = '5871'
    gestion_localidad_6.localidad = 'ACOSTILLA'
    gestion_localidad_6.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_6 = importer.save_or_locate(gestion_localidad_6)

    gestion_localidad_7 = Localidad()
    gestion_localidad_7.cod_postal = '5843'
    gestion_localidad_7.localidad = 'ADELIA MARIA'
    gestion_localidad_7.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_7 = importer.save_or_locate(gestion_localidad_7)

    gestion_localidad_8 = Localidad()
    gestion_localidad_8.cod_postal = '5209'
    gestion_localidad_8.localidad = 'AGUADA DEL MONTE'
    gestion_localidad_8.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_8 = importer.save_or_locate(gestion_localidad_8)

    gestion_localidad_9 = Localidad()
    gestion_localidad_9.cod_postal = '5285'
    gestion_localidad_9.localidad = 'AGUA DE CRESPIN'
    gestion_localidad_9.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_9 = importer.save_or_locate(gestion_localidad_9)

    gestion_localidad_10 = Localidad()
    gestion_localidad_10.cod_postal = '5221'
    gestion_localidad_10.localidad = 'AGUA DE LAS PIEDRAS'
    gestion_localidad_10.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_10 = importer.save_or_locate(gestion_localidad_10)

    gestion_localidad_11 = Localidad()
    gestion_localidad_11.cod_postal = '5243'
    gestion_localidad_11.localidad = 'AGUA DEL TALA'
    gestion_localidad_11.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_11 = importer.save_or_locate(gestion_localidad_11)

    gestion_localidad_12 = Localidad()
    gestion_localidad_12.cod_postal = '5107'
    gestion_localidad_12.localidad = 'AGUA DE ORO'
    gestion_localidad_12.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_12 = importer.save_or_locate(gestion_localidad_12)

    gestion_localidad_13 = Localidad()
    gestion_localidad_13.cod_postal = '5248'
    gestion_localidad_13.localidad = 'AGUA DE ORO'
    gestion_localidad_13.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_13 = importer.save_or_locate(gestion_localidad_13)

    gestion_localidad_14 = Localidad()
    gestion_localidad_14.cod_postal = '5155'
    gestion_localidad_14.localidad = 'AGUA DE TALA'
    gestion_localidad_14.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_14 = importer.save_or_locate(gestion_localidad_14)

    gestion_localidad_15 = Localidad()
    gestion_localidad_15.cod_postal = '5209'
    gestion_localidad_15.localidad = 'AGUADITA'
    gestion_localidad_15.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_15 = importer.save_or_locate(gestion_localidad_15)

    gestion_localidad_16 = Localidad()
    gestion_localidad_16.cod_postal = '5216'
    gestion_localidad_16.localidad = 'AGUA HEDIONDA'
    gestion_localidad_16.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_16 = importer.save_or_locate(gestion_localidad_16)

    gestion_localidad_17 = Localidad()
    gestion_localidad_17.cod_postal = '5212'
    gestion_localidad_17.localidad = 'AGUA PINTADA'
    gestion_localidad_17.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_17 = importer.save_or_locate(gestion_localidad_17)

    gestion_localidad_18 = Localidad()
    gestion_localidad_18.cod_postal = '5221'
    gestion_localidad_18.localidad = 'AGUASACHA'
    gestion_localidad_18.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_18 = importer.save_or_locate(gestion_localidad_18)

    gestion_localidad_19 = Localidad()
    gestion_localidad_19.cod_postal = '5284'
    gestion_localidad_19.localidad = 'AGUAS DE RAMON'
    gestion_localidad_19.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_19 = importer.save_or_locate(gestion_localidad_19)

    gestion_localidad_20 = Localidad()
    gestion_localidad_20.cod_postal = '5813'
    gestion_localidad_20.localidad = 'ALCIRA ESTACION GIGENA'
    gestion_localidad_20.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_20 = importer.save_or_locate(gestion_localidad_20)

    gestion_localidad_21 = Localidad()
    gestion_localidad_21.cod_postal = '2686'
    gestion_localidad_21.localidad = 'ALEJANDRO ROCA'
    gestion_localidad_21.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_21 = importer.save_or_locate(gestion_localidad_21)

    gestion_localidad_22 = Localidad()
    gestion_localidad_22.cod_postal = '2662'
    gestion_localidad_22.localidad = 'ALEJO LEDESMA'
    gestion_localidad_22.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_22 = importer.save_or_locate(gestion_localidad_22)

    gestion_localidad_23 = Localidad()
    gestion_localidad_23.cod_postal = '5885'
    gestion_localidad_23.localidad = 'ALGARROBAL'
    gestion_localidad_23.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_23 = importer.save_or_locate(gestion_localidad_23)

    gestion_localidad_24 = Localidad()
    gestion_localidad_24.cod_postal = '5221'
    gestion_localidad_24.localidad = 'ALGARROBO'
    gestion_localidad_24.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_24 = importer.save_or_locate(gestion_localidad_24)

    gestion_localidad_25 = Localidad()
    gestion_localidad_25.cod_postal = '5949'
    gestion_localidad_25.localidad = 'ALICIA'
    gestion_localidad_25.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_25 = importer.save_or_locate(gestion_localidad_25)

    gestion_localidad_26 = Localidad()
    gestion_localidad_26.cod_postal = '5854'
    gestion_localidad_26.localidad = 'ALMAFUERTE'
    gestion_localidad_26.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_26 = importer.save_or_locate(gestion_localidad_26)

    gestion_localidad_27 = Localidad()
    gestion_localidad_27.cod_postal = '5801'
    gestion_localidad_27.localidad = 'ALPA CORRAL'
    gestion_localidad_27.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_27 = importer.save_or_locate(gestion_localidad_27)

    gestion_localidad_28 = Localidad()
    gestion_localidad_28.cod_postal = '5813'
    gestion_localidad_28.localidad = 'ALPAPUCA'
    gestion_localidad_28.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_28 = importer.save_or_locate(gestion_localidad_28)

    gestion_localidad_29 = Localidad()
    gestion_localidad_29.cod_postal = '5186'
    gestion_localidad_29.localidad = 'ALTA GRACIA'
    gestion_localidad_29.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_29 = importer.save_or_locate(gestion_localidad_29)

    gestion_localidad_30 = Localidad()
    gestion_localidad_30.cod_postal = '5871'
    gestion_localidad_30.localidad = 'ALTAUTINA'
    gestion_localidad_30.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_30 = importer.save_or_locate(gestion_localidad_30)

    gestion_localidad_31 = Localidad()
    gestion_localidad_31.cod_postal = '5907'
    gestion_localidad_31.localidad = 'ALTO ALEGRE'
    gestion_localidad_31.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_31 = importer.save_or_locate(gestion_localidad_31)

    gestion_localidad_32 = Localidad()
    gestion_localidad_32.cod_postal = '5121'
    gestion_localidad_32.localidad = 'ALTO ALEGRE'
    gestion_localidad_32.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_32 = importer.save_or_locate(gestion_localidad_32)

    gestion_localidad_33 = Localidad()
    gestion_localidad_33.cod_postal = '5182'
    gestion_localidad_33.localidad = 'ALTO CASTRO'
    gestion_localidad_33.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_33 = importer.save_or_locate(gestion_localidad_33)

    gestion_localidad_34 = Localidad()
    gestion_localidad_34.cod_postal = '5145'
    gestion_localidad_34.localidad = 'ALTO DE CASTILLO'
    gestion_localidad_34.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_34 = importer.save_or_locate(gestion_localidad_34)

    gestion_localidad_35 = Localidad()
    gestion_localidad_35.cod_postal = '5119'
    gestion_localidad_35.localidad = 'ALTO DE FIERRO'
    gestion_localidad_35.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_35 = importer.save_or_locate(gestion_localidad_35)

    gestion_localidad_36 = Localidad()
    gestion_localidad_36.cod_postal = '5203'
    gestion_localidad_36.localidad = 'ALTO DE FLORES'
    gestion_localidad_36.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_36 = importer.save_or_locate(gestion_localidad_36)

    gestion_localidad_37 = Localidad()
    gestion_localidad_37.cod_postal = '5875'
    gestion_localidad_37.localidad = 'ALTO DE LAS MULAS'
    gestion_localidad_37.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_37 = importer.save_or_locate(gestion_localidad_37)

    gestion_localidad_38 = Localidad()
    gestion_localidad_38.cod_postal = '5119'
    gestion_localidad_38.localidad = 'ALTO DEL DURAZNO'
    gestion_localidad_38.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_38 = importer.save_or_locate(gestion_localidad_38)

    gestion_localidad_39 = Localidad()
    gestion_localidad_39.cod_postal = '5281'
    gestion_localidad_39.localidad = 'ALTO DE LOS QUEBRACHOS'
    gestion_localidad_39.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_39 = importer.save_or_locate(gestion_localidad_39)

    gestion_localidad_40 = Localidad()
    gestion_localidad_40.cod_postal = '5295'
    gestion_localidad_40.localidad = 'ALTO DEL TALA'
    gestion_localidad_40.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_40 = importer.save_or_locate(gestion_localidad_40)

    gestion_localidad_41 = Localidad()
    gestion_localidad_41.cod_postal = '5174'
    gestion_localidad_41.localidad = 'ALTO DE SAN PEDRO'
    gestion_localidad_41.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_41 = importer.save_or_locate(gestion_localidad_41)

    gestion_localidad_42 = Localidad()
    gestion_localidad_42.cod_postal = '5893'
    gestion_localidad_42.localidad = 'ALTO GRANDE'
    gestion_localidad_42.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_42 = importer.save_or_locate(gestion_localidad_42)

    gestion_localidad_43 = Localidad()
    gestion_localidad_43.cod_postal = '5885'
    gestion_localidad_43.localidad = 'ALTO RESBALOSO'
    gestion_localidad_43.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_43 = importer.save_or_locate(gestion_localidad_43)

    gestion_localidad_44 = Localidad()
    gestion_localidad_44.cod_postal = '2417'
    gestion_localidad_44.localidad = 'ALTOS DE CHIPION'
    gestion_localidad_44.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_44 = importer.save_or_locate(gestion_localidad_44)

    gestion_localidad_45 = Localidad()
    gestion_localidad_45.cod_postal = '5205'
    gestion_localidad_45.localidad = 'ALTO VERDE'
    gestion_localidad_45.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_45 = importer.save_or_locate(gestion_localidad_45)

    gestion_localidad_46 = Localidad()
    gestion_localidad_46.cod_postal = '5199'
    gestion_localidad_46.localidad = 'AMBOY'
    gestion_localidad_46.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_46 = importer.save_or_locate(gestion_localidad_46)

    gestion_localidad_47 = Localidad()
    gestion_localidad_47.cod_postal = '5299'
    gestion_localidad_47.localidad = 'AMBUL'
    gestion_localidad_47.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_47 = importer.save_or_locate(gestion_localidad_47)

    gestion_localidad_48 = Localidad()
    gestion_localidad_48.cod_postal = '5905'
    gestion_localidad_48.localidad = 'ANA ZUMARAN'
    gestion_localidad_48.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_48 = importer.save_or_locate(gestion_localidad_48)

    gestion_localidad_49 = Localidad()
    gestion_localidad_49.cod_postal = '5155'
    gestion_localidad_49.localidad = 'ANGOSTURA'
    gestion_localidad_49.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_49 = importer.save_or_locate(gestion_localidad_49)

    gestion_localidad_50 = Localidad()
    gestion_localidad_50.cod_postal = '5107'
    gestion_localidad_50.localidad = 'ANIMI'
    gestion_localidad_50.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_50 = importer.save_or_locate(gestion_localidad_50)

    gestion_localidad_51 = Localidad()
    gestion_localidad_51.cod_postal = '5189'
    gestion_localidad_51.localidad = 'ANISACATE'
    gestion_localidad_51.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_51 = importer.save_or_locate(gestion_localidad_51)

    gestion_localidad_52 = Localidad()
    gestion_localidad_52.cod_postal = '6271'
    gestion_localidad_52.localidad = 'ANTONIO CATALANO'
    gestion_localidad_52.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_52 = importer.save_or_locate(gestion_localidad_52)

    gestion_localidad_53 = Localidad()
    gestion_localidad_53.cod_postal = '5216'
    gestion_localidad_53.localidad = 'ARBOL BLANCO'
    gestion_localidad_53.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_53 = importer.save_or_locate(gestion_localidad_53)

    gestion_localidad_54 = Localidad()
    gestion_localidad_54.cod_postal = '2432'
    gestion_localidad_54.localidad = 'ARBOL CHATO'
    gestion_localidad_54.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_54 = importer.save_or_locate(gestion_localidad_54)

    gestion_localidad_55 = Localidad()
    gestion_localidad_55.cod_postal = '5873'
    gestion_localidad_55.localidad = 'ARBOLES BLANCOS'
    gestion_localidad_55.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_55 = importer.save_or_locate(gestion_localidad_55)

    gestion_localidad_56 = Localidad()
    gestion_localidad_56.cod_postal = '5297'
    gestion_localidad_56.localidad = 'ARCOYO'
    gestion_localidad_56.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_56 = importer.save_or_locate(gestion_localidad_56)

    gestion_localidad_57 = Localidad()
    gestion_localidad_57.cod_postal = '2624'
    gestion_localidad_57.localidad = 'ARIAS'
    gestion_localidad_57.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_57 = importer.save_or_locate(gestion_localidad_57)

    gestion_localidad_58 = Localidad()
    gestion_localidad_58.cod_postal = '2341'
    gestion_localidad_58.localidad = 'AROMITO'
    gestion_localidad_58.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_58 = importer.save_or_locate(gestion_localidad_58)

    gestion_localidad_59 = Localidad()
    gestion_localidad_59.cod_postal = '2434'
    gestion_localidad_59.localidad = 'ARROYITO'
    gestion_localidad_59.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_59 = importer.save_or_locate(gestion_localidad_59)

    gestion_localidad_60 = Localidad()
    gestion_localidad_60.cod_postal = '5297'
    gestion_localidad_60.localidad = 'ARROYO'
    gestion_localidad_60.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_60 = importer.save_or_locate(gestion_localidad_60)

    gestion_localidad_61 = Localidad()
    gestion_localidad_61.cod_postal = '5909'
    gestion_localidad_61.localidad = 'ARROYO ALGODON'
    gestion_localidad_61.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_61 = importer.save_or_locate(gestion_localidad_61)

    gestion_localidad_62 = Localidad()
    gestion_localidad_62.cod_postal = '5917'
    gestion_localidad_62.localidad = 'ARROYO CABRAL'
    gestion_localidad_62.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_62 = importer.save_or_locate(gestion_localidad_62)

    gestion_localidad_63 = Localidad()
    gestion_localidad_63.cod_postal = '2434'
    gestion_localidad_63.localidad = 'ARROYO DE ALVAREZ'
    gestion_localidad_63.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_63 = importer.save_or_locate(gestion_localidad_63)

    gestion_localidad_64 = Localidad()
    gestion_localidad_64.cod_postal = '5901'
    gestion_localidad_64.localidad = 'ARROYO DEL PINO'
    gestion_localidad_64.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_64 = importer.save_or_locate(gestion_localidad_64)

    gestion_localidad_65 = Localidad()
    gestion_localidad_65.cod_postal = '5889'
    gestion_localidad_65.localidad = 'ARROYO LA HIGUERA'
    gestion_localidad_65.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_65 = importer.save_or_locate(gestion_localidad_65)

    gestion_localidad_66 = Localidad()
    gestion_localidad_66.cod_postal = '5889'
    gestion_localidad_66.localidad = 'ARROYO LOS PATOS'
    gestion_localidad_66.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_66 = importer.save_or_locate(gestion_localidad_66)

    gestion_localidad_67 = Localidad()
    gestion_localidad_67.cod_postal = '5859'
    gestion_localidad_67.localidad = 'ARROYO SAN ANTONIO'
    gestion_localidad_67.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_67 = importer.save_or_locate(gestion_localidad_67)

    gestion_localidad_68 = Localidad()
    gestion_localidad_68.cod_postal = '5825'
    gestion_localidad_68.localidad = 'ARROYO SANTA CATALINA'
    gestion_localidad_68.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_68 = importer.save_or_locate(gestion_localidad_68)

    gestion_localidad_69 = Localidad()
    gestion_localidad_69.cod_postal = '5819'
    gestion_localidad_69.localidad = 'ARROYO SANTANA'
    gestion_localidad_69.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_69 = importer.save_or_locate(gestion_localidad_69)

    gestion_localidad_70 = Localidad()
    gestion_localidad_70.cod_postal = '5196'
    gestion_localidad_70.localidad = 'ARROYO SECO'
    gestion_localidad_70.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_70 = importer.save_or_locate(gestion_localidad_70)

    gestion_localidad_71 = Localidad()
    gestion_localidad_71.cod_postal = '5819'
    gestion_localidad_71.localidad = 'ARROYO TOLEDO'
    gestion_localidad_71.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_71 = importer.save_or_locate(gestion_localidad_71)

    gestion_localidad_72 = Localidad()
    gestion_localidad_72.cod_postal = '5825'
    gestion_localidad_72.localidad = 'ARSENAL JOSE MARIA ROJAS'
    gestion_localidad_72.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_72 = importer.save_or_locate(gestion_localidad_72)

    gestion_localidad_73 = Localidad()
    gestion_localidad_73.cod_postal = '5117'
    gestion_localidad_73.localidad = 'ASCOCHINGA'
    gestion_localidad_73.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_73 = importer.save_or_locate(gestion_localidad_73)

    gestion_localidad_74 = Localidad()
    gestion_localidad_74.cod_postal = '2671'
    gestion_localidad_74.localidad = 'ASSUNTA'
    gestion_localidad_74.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_74 = importer.save_or_locate(gestion_localidad_74)

    gestion_localidad_75 = Localidad()
    gestion_localidad_75.cod_postal = '5225'
    gestion_localidad_75.localidad = 'ATAHONA'
    gestion_localidad_75.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_75 = importer.save_or_locate(gestion_localidad_75)

    gestion_localidad_76 = Localidad()
    gestion_localidad_76.cod_postal = '5194'
    gestion_localidad_76.localidad = 'ATHOS PAMPA'
    gestion_localidad_76.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_76 = importer.save_or_locate(gestion_localidad_76)

    gestion_localidad_77 = Localidad()
    gestion_localidad_77.cod_postal = '5196'
    gestion_localidad_77.localidad = 'ATUMI PAMPA'
    gestion_localidad_77.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_77 = importer.save_or_locate(gestion_localidad_77)

    gestion_localidad_78 = Localidad()
    gestion_localidad_78.cod_postal = '5145'
    gestion_localidad_78.localidad = 'AUGUSTO VANDERSANDE'
    gestion_localidad_78.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_78 = importer.save_or_locate(gestion_localidad_78)

    gestion_localidad_79 = Localidad()
    gestion_localidad_79.cod_postal = '5901'
    gestion_localidad_79.localidad = 'AUSONIA'
    gestion_localidad_79.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_79 = importer.save_or_locate(gestion_localidad_79)

    gestion_localidad_80 = Localidad()
    gestion_localidad_80.cod_postal = '5212'
    gestion_localidad_80.localidad = 'AVELLANEDA'
    gestion_localidad_80.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_80 = importer.save_or_locate(gestion_localidad_80)

    gestion_localidad_81 = Localidad()
    gestion_localidad_81.cod_postal = '5813'
    gestion_localidad_81.localidad = 'BAJADA NUEVA'
    gestion_localidad_81.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_81 = importer.save_or_locate(gestion_localidad_81)

    gestion_localidad_82 = Localidad()
    gestion_localidad_82.cod_postal = '5189'
    gestion_localidad_82.localidad = 'BAJO CHICO'
    gestion_localidad_82.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_82 = importer.save_or_locate(gestion_localidad_82)

    gestion_localidad_83 = Localidad()
    gestion_localidad_83.cod_postal = '5101'
    gestion_localidad_83.localidad = 'BAJO CHICO BAJO GRANDE'
    gestion_localidad_83.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_83 = importer.save_or_locate(gestion_localidad_83)

    gestion_localidad_84 = Localidad()
    gestion_localidad_84.cod_postal = '5101'
    gestion_localidad_84.localidad = 'BAJO DE FERNANDEZ'
    gestion_localidad_84.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_84 = importer.save_or_locate(gestion_localidad_84)

    gestion_localidad_85 = Localidad()
    gestion_localidad_85.cod_postal = '5961'
    gestion_localidad_85.localidad = 'BAJO DE GOMEZ'
    gestion_localidad_85.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_85 = importer.save_or_locate(gestion_localidad_85)

    gestion_localidad_86 = Localidad()
    gestion_localidad_86.cod_postal = '2662'
    gestion_localidad_86.localidad = 'BAJO DEL BURRO'
    gestion_localidad_86.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_86 = importer.save_or_locate(gestion_localidad_86)

    gestion_localidad_87 = Localidad()
    gestion_localidad_87.cod_postal = '5189'
    gestion_localidad_87.localidad = 'BAJO DEL CARMEN'
    gestion_localidad_87.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_87 = importer.save_or_locate(gestion_localidad_87)

    gestion_localidad_88 = Localidad()
    gestion_localidad_88.cod_postal = '5221'
    gestion_localidad_88.localidad = 'BAJO DE OLMOS'
    gestion_localidad_88.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_88 = importer.save_or_locate(gestion_localidad_88)

    gestion_localidad_89 = Localidad()
    gestion_localidad_89.cod_postal = '5887'
    gestion_localidad_89.localidad = 'BAJO EL MOLINO'
    gestion_localidad_89.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_89 = importer.save_or_locate(gestion_localidad_89)

    gestion_localidad_90 = Localidad()
    gestion_localidad_90.cod_postal = '5961'
    gestion_localidad_90.localidad = 'BAJO GALINDEZ'
    gestion_localidad_90.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_90 = importer.save_or_locate(gestion_localidad_90)

    gestion_localidad_91 = Localidad()
    gestion_localidad_91.cod_postal = '5101'
    gestion_localidad_91.localidad = 'BAJO GRANDE'
    gestion_localidad_91.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_91 = importer.save_or_locate(gestion_localidad_91)

    gestion_localidad_92 = Localidad()
    gestion_localidad_92.cod_postal = '5231'
    gestion_localidad_92.localidad = 'BAJO HONDO'
    gestion_localidad_92.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_92 = importer.save_or_locate(gestion_localidad_92)

    gestion_localidad_93 = Localidad()
    gestion_localidad_93.cod_postal = '5270'
    gestion_localidad_93.localidad = 'BAJO LINDO'
    gestion_localidad_93.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_93 = importer.save_or_locate(gestion_localidad_93)

    gestion_localidad_94 = Localidad()
    gestion_localidad_94.cod_postal = '5248'
    gestion_localidad_94.localidad = 'BALBUENA'
    gestion_localidad_94.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_94 = importer.save_or_locate(gestion_localidad_94)

    gestion_localidad_95 = Localidad()
    gestion_localidad_95.cod_postal = '5871'
    gestion_localidad_95.localidad = 'BALDE DE LA MORA'
    gestion_localidad_95.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_95 = importer.save_or_locate(gestion_localidad_95)

    gestion_localidad_96 = Localidad()
    gestion_localidad_96.cod_postal = '5871'
    gestion_localidad_96.localidad = 'BALDE DE LA ORILLA'
    gestion_localidad_96.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_96 = importer.save_or_locate(gestion_localidad_96)

    gestion_localidad_97 = Localidad()
    gestion_localidad_97.cod_postal = '5871'
    gestion_localidad_97.localidad = 'BALDE LINDO'
    gestion_localidad_97.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_97 = importer.save_or_locate(gestion_localidad_97)

    gestion_localidad_98 = Localidad()
    gestion_localidad_98.cod_postal = '2572'
    gestion_localidad_98.localidad = 'BALLESTEROS'
    gestion_localidad_98.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_98 = importer.save_or_locate(gestion_localidad_98)

    gestion_localidad_99 = Localidad()
    gestion_localidad_99.cod_postal = '2572'
    gestion_localidad_99.localidad = 'BALLESTEROS SUD'
    gestion_localidad_99.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_99 = importer.save_or_locate(gestion_localidad_99)

    gestion_localidad_100 = Localidad()
    gestion_localidad_100.cod_postal = '5141'
    gestion_localidad_100.localidad = 'BALNEARIA'
    gestion_localidad_100.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_100 = importer.save_or_locate(gestion_localidad_100)

    gestion_localidad_101 = Localidad()
    gestion_localidad_101.cod_postal = '5137'
    gestion_localidad_101.localidad = 'BALNEARIO GUGLIERI'
    gestion_localidad_101.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_101 = importer.save_or_locate(gestion_localidad_101)

    gestion_localidad_102 = Localidad()
    gestion_localidad_102.cod_postal = '5875'
    gestion_localidad_102.localidad = 'BANDA DE VARELA'
    gestion_localidad_102.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_102 = importer.save_or_locate(gestion_localidad_102)

    gestion_localidad_103 = Localidad()
    gestion_localidad_103.cod_postal = '5248'
    gestion_localidad_103.localidad = 'BAÑADO DEL FUERTE'
    gestion_localidad_103.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_103 = importer.save_or_locate(gestion_localidad_103)

    gestion_localidad_104 = Localidad()
    gestion_localidad_104.cod_postal = '5871'
    gestion_localidad_104.localidad = 'BAÑADO DE PAJA'
    gestion_localidad_104.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_104 = importer.save_or_locate(gestion_localidad_104)

    gestion_localidad_105 = Localidad()
    gestion_localidad_105.cod_postal = '5285'
    gestion_localidad_105.localidad = 'BAÑADO DE SOTO'
    gestion_localidad_105.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_105 = importer.save_or_locate(gestion_localidad_105)

    gestion_localidad_106 = Localidad()
    gestion_localidad_106.cod_postal = '5212'
    gestion_localidad_106.localidad = 'BARRANCA YACO'
    gestion_localidad_106.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_106 = importer.save_or_locate(gestion_localidad_106)

    gestion_localidad_107 = Localidad()
    gestion_localidad_107.cod_postal = '2671'
    gestion_localidad_107.localidad = 'BARRETO'
    gestion_localidad_107.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_107 = importer.save_or_locate(gestion_localidad_107)

    gestion_localidad_108 = Localidad()
    gestion_localidad_108.cod_postal = '5246'
    gestion_localidad_108.localidad = 'BARRETO'
    gestion_localidad_108.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_108 = importer.save_or_locate(gestion_localidad_108)

    gestion_localidad_109 = Localidad()
    gestion_localidad_109.cod_postal = '5281'
    gestion_localidad_109.localidad = 'BARRIAL'
    gestion_localidad_109.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_109 = importer.save_or_locate(gestion_localidad_109)

    gestion_localidad_110 = Localidad()
    gestion_localidad_110.cod_postal = '5284'
    gestion_localidad_110.localidad = 'BARRIALITOS'
    gestion_localidad_110.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_110 = importer.save_or_locate(gestion_localidad_110)

    gestion_localidad_111 = Localidad()
    gestion_localidad_111.cod_postal = '2550'
    gestion_localidad_111.localidad = 'BARRIO BELGRANO'
    gestion_localidad_111.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_111 = importer.save_or_locate(gestion_localidad_111)

    gestion_localidad_112 = Localidad()
    gestion_localidad_112.cod_postal = '5123'
    gestion_localidad_112.localidad = 'BARRIO DEAN FUNES'
    gestion_localidad_112.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_112 = importer.save_or_locate(gestion_localidad_112)

    gestion_localidad_113 = Localidad()
    gestion_localidad_113.cod_postal = '5850'
    gestion_localidad_113.localidad = 'BARRIO DEL LIBERTADOR'
    gestion_localidad_113.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_113 = importer.save_or_locate(gestion_localidad_113)

    gestion_localidad_114 = Localidad()
    gestion_localidad_114.cod_postal = '5870'
    gestion_localidad_114.localidad = 'BARRIO LA FERIA'
    gestion_localidad_114.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_114 = importer.save_or_locate(gestion_localidad_114)

    gestion_localidad_115 = Localidad()
    gestion_localidad_115.cod_postal = '2594'
    gestion_localidad_115.localidad = 'BARRIO LA FORTUNA'
    gestion_localidad_115.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_115 = importer.save_or_locate(gestion_localidad_115)

    gestion_localidad_116 = Localidad()
    gestion_localidad_116.cod_postal = '5111'
    gestion_localidad_116.localidad = 'BARRIO LOZA'
    gestion_localidad_116.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_116 = importer.save_or_locate(gestion_localidad_116)

    gestion_localidad_117 = Localidad()
    gestion_localidad_117.cod_postal = '5143'
    gestion_localidad_117.localidad = 'BARRIO MULLER'
    gestion_localidad_117.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_117 = importer.save_or_locate(gestion_localidad_117)

    gestion_localidad_118 = Localidad()
    gestion_localidad_118.cod_postal = '5155'
    gestion_localidad_118.localidad = 'BATAN'
    gestion_localidad_118.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_118 = importer.save_or_locate(gestion_localidad_118)

    gestion_localidad_119 = Localidad()
    gestion_localidad_119.cod_postal = '5220'
    gestion_localidad_119.localidad = 'BELEN'
    gestion_localidad_119.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_119 = importer.save_or_locate(gestion_localidad_119)

    gestion_localidad_120 = Localidad()
    gestion_localidad_120.cod_postal = '5284'
    gestion_localidad_120.localidad = 'BELLA VISTA'
    gestion_localidad_120.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_120 = importer.save_or_locate(gestion_localidad_120)

    gestion_localidad_121 = Localidad()
    gestion_localidad_121.cod_postal = '2550'
    gestion_localidad_121.localidad = 'BELL VILLE'
    gestion_localidad_121.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_121 = importer.save_or_locate(gestion_localidad_121)

    gestion_localidad_122 = Localidad()
    gestion_localidad_122.cod_postal = '5807'
    gestion_localidad_122.localidad = 'BENGOLEA'
    gestion_localidad_122.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_122 = importer.save_or_locate(gestion_localidad_122)

    gestion_localidad_123 = Localidad()
    gestion_localidad_123.cod_postal = '2664'
    gestion_localidad_123.localidad = 'BENJAMIN GOULD'
    gestion_localidad_123.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_123 = importer.save_or_locate(gestion_localidad_123)

    gestion_localidad_124 = Localidad()
    gestion_localidad_124.cod_postal = '5817'
    gestion_localidad_124.localidad = 'BERROTARAN'
    gestion_localidad_124.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_124 = importer.save_or_locate(gestion_localidad_124)

    gestion_localidad_125 = Localidad()
    gestion_localidad_125.cod_postal = '5244'
    gestion_localidad_125.localidad = 'BEUCE'
    gestion_localidad_125.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_125 = importer.save_or_locate(gestion_localidad_125)

    gestion_localidad_126 = Localidad()
    gestion_localidad_126.cod_postal = '5158'
    gestion_localidad_126.localidad = 'BIALET MASSE'
    gestion_localidad_126.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_126 = importer.save_or_locate(gestion_localidad_126)

    gestion_localidad_127 = Localidad()
    gestion_localidad_127.cod_postal = '5125'
    gestion_localidad_127.localidad = 'BLAS DE ROSALES'
    gestion_localidad_127.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_127 = importer.save_or_locate(gestion_localidad_127)

    gestion_localidad_128 = Localidad()
    gestion_localidad_128.cod_postal = '5885'
    gestion_localidad_128.localidad = 'BOCA DEL RIO'
    gestion_localidad_128.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_128 = importer.save_or_locate(gestion_localidad_128)

    gestion_localidad_129 = Localidad()
    gestion_localidad_129.cod_postal = '5209'
    gestion_localidad_129.localidad = 'BORDO DE LOS ESPINOSA'
    gestion_localidad_129.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_129 = importer.save_or_locate(gestion_localidad_129)

    gestion_localidad_130 = Localidad()
    gestion_localidad_130.cod_postal = '5187'
    gestion_localidad_130.localidad = 'BOSQUE ALEGRE'
    gestion_localidad_130.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_130 = importer.save_or_locate(gestion_localidad_130)

    gestion_localidad_131 = Localidad()
    gestion_localidad_131.cod_postal = '5119'
    gestion_localidad_131.localidad = 'BOUWER'
    gestion_localidad_131.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_131 = importer.save_or_locate(gestion_localidad_131)

    gestion_localidad_132 = Localidad()
    gestion_localidad_132.cod_postal = '2419'
    gestion_localidad_132.localidad = 'BRINKMANN'
    gestion_localidad_132.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_132 = importer.save_or_locate(gestion_localidad_132)

    gestion_localidad_133 = Localidad()
    gestion_localidad_133.cod_postal = '5297'
    gestion_localidad_133.localidad = 'BUENA VISTA'
    gestion_localidad_133.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_133 = importer.save_or_locate(gestion_localidad_133)

    gestion_localidad_134 = Localidad()
    gestion_localidad_134.cod_postal = '5121'
    gestion_localidad_134.localidad = 'BUENA VISTA'
    gestion_localidad_134.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_134 = importer.save_or_locate(gestion_localidad_134)

    gestion_localidad_135 = Localidad()
    gestion_localidad_135.cod_postal = '5249'
    gestion_localidad_135.localidad = 'BUENA VISTA'
    gestion_localidad_135.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_135 = importer.save_or_locate(gestion_localidad_135)

    gestion_localidad_136 = Localidad()
    gestion_localidad_136.cod_postal = '5295'
    gestion_localidad_136.localidad = 'BUENA VISTA'
    gestion_localidad_136.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_136 = importer.save_or_locate(gestion_localidad_136)

    gestion_localidad_137 = Localidad()
    gestion_localidad_137.cod_postal = '5155'
    gestion_localidad_137.localidad = 'BUEN RETIRO'
    gestion_localidad_137.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_137 = importer.save_or_locate(gestion_localidad_137)

    gestion_localidad_138 = Localidad()
    gestion_localidad_138.cod_postal = '5135'
    gestion_localidad_138.localidad = 'BUEY MUERTO'
    gestion_localidad_138.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_138 = importer.save_or_locate(gestion_localidad_138)

    gestion_localidad_139 = Localidad()
    gestion_localidad_139.cod_postal = '5845'
    gestion_localidad_139.localidad = 'BULNES'
    gestion_localidad_139.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_139 = importer.save_or_locate(gestion_localidad_139)

    gestion_localidad_140 = Localidad()
    gestion_localidad_140.cod_postal = '6225'
    gestion_localidad_140.localidad = 'BURMEISTER'
    gestion_localidad_140.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_140 = importer.save_or_locate(gestion_localidad_140)

    gestion_localidad_141 = Localidad()
    gestion_localidad_141.cod_postal = '5155'
    gestion_localidad_141.localidad = 'CABALANGO'
    gestion_localidad_141.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_141 = importer.save_or_locate(gestion_localidad_141)

    gestion_localidad_142 = Localidad()
    gestion_localidad_142.cod_postal = '5109'
    gestion_localidad_142.localidad = 'CABANA'
    gestion_localidad_142.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_142 = importer.save_or_locate(gestion_localidad_142)

    gestion_localidad_143 = Localidad()
    gestion_localidad_143.cod_postal = '5229'
    gestion_localidad_143.localidad = 'CABEZA DE BUEY'
    gestion_localidad_143.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_143 = importer.save_or_locate(gestion_localidad_143)

    gestion_localidad_144 = Localidad()
    gestion_localidad_144.cod_postal = '5221'
    gestion_localidad_144.localidad = 'CABINDO'
    gestion_localidad_144.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_144 = importer.save_or_locate(gestion_localidad_144)

    gestion_localidad_145 = Localidad()
    gestion_localidad_145.cod_postal = '5209'
    gestion_localidad_145.localidad = 'CACHI YACO'
    gestion_localidad_145.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_145 = importer.save_or_locate(gestion_localidad_145)

    gestion_localidad_146 = Localidad()
    gestion_localidad_146.cod_postal = '5284'
    gestion_localidad_146.localidad = 'CACHIYULLO'
    gestion_localidad_146.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_146 = importer.save_or_locate(gestion_localidad_146)

    gestion_localidad_147 = Localidad()
    gestion_localidad_147.cod_postal = '5184'
    gestion_localidad_147.localidad = 'CAJON DEL RIO'
    gestion_localidad_147.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_147 = importer.save_or_locate(gestion_localidad_147)

    gestion_localidad_148 = Localidad()
    gestion_localidad_148.cod_postal = '5282'
    gestion_localidad_148.localidad = 'CALABALUMBA'
    gestion_localidad_148.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_148 = importer.save_or_locate(gestion_localidad_148)

    gestion_localidad_149 = Localidad()
    gestion_localidad_149.cod_postal = '5201'
    gestion_localidad_149.localidad = 'CALASUYA'
    gestion_localidad_149.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_149 = importer.save_or_locate(gestion_localidad_149)

    gestion_localidad_150 = Localidad()
    gestion_localidad_150.cod_postal = '5969'
    gestion_localidad_150.localidad = 'CALCHIN'
    gestion_localidad_150.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_150 = importer.save_or_locate(gestion_localidad_150)

    gestion_localidad_151 = Localidad()
    gestion_localidad_151.cod_postal = '5965'
    gestion_localidad_151.localidad = 'CALCHIN OESTE'
    gestion_localidad_151.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_151 = importer.save_or_locate(gestion_localidad_151)

    gestion_localidad_152 = Localidad()
    gestion_localidad_152.cod_postal = '5151'
    gestion_localidad_152.localidad = 'CALERA CENTRAL'
    gestion_localidad_152.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_152 = importer.save_or_locate(gestion_localidad_152)

    gestion_localidad_153 = Localidad()
    gestion_localidad_153.cod_postal = '5191'
    gestion_localidad_153.localidad = 'CALMAYO'
    gestion_localidad_153.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_153 = importer.save_or_locate(gestion_localidad_153)

    gestion_localidad_154 = Localidad()
    gestion_localidad_154.cod_postal = '5205'
    gestion_localidad_154.localidad = 'CAMARONES'
    gestion_localidad_154.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_154 = importer.save_or_locate(gestion_localidad_154)

    gestion_localidad_155 = Localidad()
    gestion_localidad_155.cod_postal = '2585'
    gestion_localidad_155.localidad = 'CAMILO ALDAO'
    gestion_localidad_155.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_155 = importer.save_or_locate(gestion_localidad_155)

    gestion_localidad_156 = Localidad()
    gestion_localidad_156.cod_postal = '5244'
    gestion_localidad_156.localidad = 'CAMINIAGA'
    gestion_localidad_156.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_156 = importer.save_or_locate(gestion_localidad_156)

    gestion_localidad_157 = Localidad()
    gestion_localidad_157.cod_postal = '5101'
    gestion_localidad_157.localidad = 'CAMINO A PUNTA DEL AGUA'
    gestion_localidad_157.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_157 = importer.save_or_locate(gestion_localidad_157)

    gestion_localidad_158 = Localidad()
    gestion_localidad_158.cod_postal = '5231'
    gestion_localidad_158.localidad = 'CAMOATI'
    gestion_localidad_158.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_158 = importer.save_or_locate(gestion_localidad_158)

    gestion_localidad_159 = Localidad()
    gestion_localidad_159.cod_postal = '5149'
    gestion_localidad_159.localidad = 'CAMPAMENTO MINNETTI'
    gestion_localidad_159.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_159 = importer.save_or_locate(gestion_localidad_159)

    gestion_localidad_160 = Localidad()
    gestion_localidad_160.cod_postal = '5209'
    gestion_localidad_160.localidad = 'CAMPO ALEGRE'
    gestion_localidad_160.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_160 = importer.save_or_locate(gestion_localidad_160)

    gestion_localidad_161 = Localidad()
    gestion_localidad_161.cod_postal = '5221'
    gestion_localidad_161.localidad = 'CAMPO ALEGRE'
    gestion_localidad_161.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_161 = importer.save_or_locate(gestion_localidad_161)

    gestion_localidad_162 = Localidad()
    gestion_localidad_162.cod_postal = '5229'
    gestion_localidad_162.localidad = 'CAMPO ALVAREZ'
    gestion_localidad_162.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_162 = importer.save_or_locate(gestion_localidad_162)

    gestion_localidad_163 = Localidad()
    gestion_localidad_163.cod_postal = '5915'
    gestion_localidad_163.localidad = 'CAMPO AMBROGGIO'
    gestion_localidad_163.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_163 = importer.save_or_locate(gestion_localidad_163)

    gestion_localidad_164 = Localidad()
    gestion_localidad_164.cod_postal = '5943'
    gestion_localidad_164.localidad = 'CAMPO BANDILLO'
    gestion_localidad_164.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_164 = importer.save_or_locate(gestion_localidad_164)

    gestion_localidad_165 = Localidad()
    gestion_localidad_165.cod_postal = '2421'
    gestion_localidad_165.localidad = 'CAMPO BEIRO'
    gestion_localidad_165.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_165 = importer.save_or_locate(gestion_localidad_165)

    gestion_localidad_166 = Localidad()
    gestion_localidad_166.cod_postal = '2426'
    gestion_localidad_166.localidad = 'CAMPO BOERO'
    gestion_localidad_166.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_166 = importer.save_or_locate(gestion_localidad_166)

    gestion_localidad_167 = Localidad()
    gestion_localidad_167.cod_postal = '5149'
    gestion_localidad_167.localidad = 'CAMPO BOURDICHON'
    gestion_localidad_167.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_167 = importer.save_or_locate(gestion_localidad_167)

    gestion_localidad_168 = Localidad()
    gestion_localidad_168.cod_postal = '2423'
    gestion_localidad_168.localidad = 'CAMPO CALVO'
    gestion_localidad_168.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_168 = importer.save_or_locate(gestion_localidad_168)

    gestion_localidad_169 = Localidad()
    gestion_localidad_169.cod_postal = '5139'
    gestion_localidad_169.localidad = 'CAMPO COYUNDA'
    gestion_localidad_169.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_169 = importer.save_or_locate(gestion_localidad_169)

    gestion_localidad_170 = Localidad()
    gestion_localidad_170.cod_postal = '5236'
    gestion_localidad_170.localidad = 'CAMPO DE LAS PIEDRAS'
    gestion_localidad_170.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_170 = importer.save_or_locate(gestion_localidad_170)

    gestion_localidad_171 = Localidad()
    gestion_localidad_171.cod_postal = '5801'
    gestion_localidad_171.localidad = 'CAMPO DE LA TORRE'
    gestion_localidad_171.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_171 = importer.save_or_locate(gestion_localidad_171)

    gestion_localidad_172 = Localidad()
    gestion_localidad_172.cod_postal = '2555'
    gestion_localidad_172.localidad = 'CAMPO GENERAL PAZ'
    gestion_localidad_172.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_172 = importer.save_or_locate(gestion_localidad_172)

    gestion_localidad_173 = Localidad()
    gestion_localidad_173.cod_postal = '5231'
    gestion_localidad_173.localidad = 'CAMPO GRANDE'
    gestion_localidad_173.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_173 = importer.save_or_locate(gestion_localidad_173)

    gestion_localidad_174 = Localidad()
    gestion_localidad_174.cod_postal = '2423'
    gestion_localidad_174.localidad = 'CAMPO LA LUISA'
    gestion_localidad_174.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_174 = importer.save_or_locate(gestion_localidad_174)

    gestion_localidad_175 = Localidad()
    gestion_localidad_175.cod_postal = '5221'
    gestion_localidad_175.localidad = 'CAMPO LA PIEDRA'
    gestion_localidad_175.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_175 = importer.save_or_locate(gestion_localidad_175)

    gestion_localidad_176 = Localidad()
    gestion_localidad_176.cod_postal = '5225'
    gestion_localidad_176.localidad = 'CAMPO RAMALLO'
    gestion_localidad_176.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_176 = importer.save_or_locate(gestion_localidad_176)

    gestion_localidad_177 = Localidad()
    gestion_localidad_177.cod_postal = '5987'
    gestion_localidad_177.localidad = 'CAMPO ROSSIANO'
    gestion_localidad_177.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_177 = importer.save_or_locate(gestion_localidad_177)

    gestion_localidad_178 = Localidad()
    gestion_localidad_178.cod_postal = '5821'
    gestion_localidad_178.localidad = 'CAMPO SAN ANTONIO'
    gestion_localidad_178.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_178 = importer.save_or_locate(gestion_localidad_178)

    gestion_localidad_179 = Localidad()
    gestion_localidad_179.cod_postal = '6271'
    gestion_localidad_179.localidad = 'CAMPO SAN JUAN'
    gestion_localidad_179.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_179 = importer.save_or_locate(gestion_localidad_179)

    gestion_localidad_180 = Localidad()
    gestion_localidad_180.cod_postal = '2679'
    gestion_localidad_180.localidad = 'CAMPO SOL DE MAYO'
    gestion_localidad_180.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_180 = importer.save_or_locate(gestion_localidad_180)

    gestion_localidad_181 = Localidad()
    gestion_localidad_181.cod_postal = '2650'
    gestion_localidad_181.localidad = 'CANALS'
    gestion_localidad_181.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_181 = importer.save_or_locate(gestion_localidad_181)

    gestion_localidad_182 = Localidad()
    gestion_localidad_182.cod_postal = '5287'
    gestion_localidad_182.localidad = 'CANDELARIA'
    gestion_localidad_182.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_182 = importer.save_or_locate(gestion_localidad_182)

    gestion_localidad_183 = Localidad()
    gestion_localidad_183.cod_postal = '5221'
    gestion_localidad_183.localidad = 'CANDELARIA SUD'
    gestion_localidad_183.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_183 = importer.save_or_locate(gestion_localidad_183)

    gestion_localidad_184 = Localidad()
    gestion_localidad_184.cod_postal = '5111'
    gestion_localidad_184.localidad = 'CANDONGA'
    gestion_localidad_184.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_184 = importer.save_or_locate(gestion_localidad_184)

    gestion_localidad_185 = Localidad()
    gestion_localidad_185.cod_postal = '5212'
    gestion_localidad_185.localidad = 'CANTERA LOS VIERAS'
    gestion_localidad_185.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_185 = importer.save_or_locate(gestion_localidad_185)

    gestion_localidad_186 = Localidad()
    gestion_localidad_186.cod_postal = '5186'
    gestion_localidad_186.localidad = 'CANTERAS ALTA GRACIA'
    gestion_localidad_186.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_186 = importer.save_or_locate(gestion_localidad_186)

    gestion_localidad_187 = Localidad()
    gestion_localidad_187.cod_postal = '5107'
    gestion_localidad_187.localidad = 'CANTERAS EL MANZANO'
    gestion_localidad_187.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_187 = importer.save_or_locate(gestion_localidad_187)

    gestion_localidad_188 = Localidad()
    gestion_localidad_188.cod_postal = '5107'
    gestion_localidad_188.localidad = 'CANTERAS EL SAUCE'
    gestion_localidad_188.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_188 = importer.save_or_locate(gestion_localidad_188)

    gestion_localidad_189 = Localidad()
    gestion_localidad_189.cod_postal = '5285'
    gestion_localidad_189.localidad = 'CANTERAS IGUAZU'
    gestion_localidad_189.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_189 = importer.save_or_locate(gestion_localidad_189)

    gestion_localidad_190 = Localidad()
    gestion_localidad_190.cod_postal = '5200'
    gestion_localidad_190.localidad = 'CANTERAS KILOMETRO 428'
    gestion_localidad_190.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_190 = importer.save_or_locate(gestion_localidad_190)

    gestion_localidad_191 = Localidad()
    gestion_localidad_191.cod_postal = '5151'
    gestion_localidad_191.localidad = 'CANTERAS LA CALERA'
    gestion_localidad_191.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_191 = importer.save_or_locate(gestion_localidad_191)

    gestion_localidad_192 = Localidad()
    gestion_localidad_192.cod_postal = '5238'
    gestion_localidad_192.localidad = 'CANTERAS LOS MORALES'
    gestion_localidad_192.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_192 = importer.save_or_locate(gestion_localidad_192)

    gestion_localidad_193 = Localidad()
    gestion_localidad_193.cod_postal = '5281'
    gestion_localidad_193.localidad = 'CANTERAS QUILPO'
    gestion_localidad_193.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_193 = importer.save_or_locate(gestion_localidad_193)

    gestion_localidad_194 = Localidad()
    gestion_localidad_194.cod_postal = '5248'
    gestion_localidad_194.localidad = 'CAÑA CRUZ'
    gestion_localidad_194.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_194 = importer.save_or_locate(gestion_localidad_194)

    gestion_localidad_195 = Localidad()
    gestion_localidad_195.cod_postal = '5135'
    gestion_localidad_195.localidad = 'CAÑADA ANCHA SANTA ROSA'
    gestion_localidad_195.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_195 = importer.save_or_locate(gestion_localidad_195)

    gestion_localidad_196 = Localidad()
    gestion_localidad_196.cod_postal = '5819'
    gestion_localidad_196.localidad = 'CAÑADA DE ALVAREZ'
    gestion_localidad_196.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_196 = importer.save_or_locate(gestion_localidad_196)

    gestion_localidad_197 = Localidad()
    gestion_localidad_197.cod_postal = '5249'
    gestion_localidad_197.localidad = 'CAÑADA DE CORIA'
    gestion_localidad_197.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_197 = importer.save_or_locate(gestion_localidad_197)

    gestion_localidad_198 = Localidad()
    gestion_localidad_198.cod_postal = '5101'
    gestion_localidad_198.localidad = 'CAÑADA DE CUEVAS'
    gestion_localidad_198.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_198 = importer.save_or_locate(gestion_localidad_198)

    gestion_localidad_199 = Localidad()
    gestion_localidad_199.cod_postal = '5221'
    gestion_localidad_199.localidad = 'CAÑADA DE JUME'
    gestion_localidad_199.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_199 = importer.save_or_locate(gestion_localidad_199)

    gestion_localidad_200 = Localidad()
    gestion_localidad_200.cod_postal = '5199'
    gestion_localidad_200.localidad = 'CAÑADA DE LAS CHACRAS'
    gestion_localidad_200.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_200 = importer.save_or_locate(gestion_localidad_200)

    gestion_localidad_201 = Localidad()
    gestion_localidad_201.cod_postal = '5291'
    gestion_localidad_201.localidad = 'CAÑADA DE LAS GATIADAS'
    gestion_localidad_201.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_201 = importer.save_or_locate(gestion_localidad_201)

    gestion_localidad_202 = Localidad()
    gestion_localidad_202.cod_postal = '5196'
    gestion_localidad_202.localidad = 'CAÑADA DEL DURAZNO'
    gestion_localidad_202.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_202 = importer.save_or_locate(gestion_localidad_202)

    gestion_localidad_203 = Localidad()
    gestion_localidad_203.cod_postal = '5297'
    gestion_localidad_203.localidad = 'CAÑADA DEL PUERTO'
    gestion_localidad_203.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_203 = importer.save_or_locate(gestion_localidad_203)

    gestion_localidad_204 = Localidad()
    gestion_localidad_204.cod_postal = '5817'
    gestion_localidad_204.localidad = 'CAÑADA DEL SAUCE'
    gestion_localidad_204.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_204 = importer.save_or_locate(gestion_localidad_204)

    gestion_localidad_205 = Localidad()
    gestion_localidad_205.cod_postal = '5200'
    gestion_localidad_205.localidad = 'CAÑADA DEL SIMBOL'
    gestion_localidad_205.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_205 = importer.save_or_locate(gestion_localidad_205)

    gestion_localidad_206 = Localidad()
    gestion_localidad_206.cod_postal = '5859'
    gestion_localidad_206.localidad = 'CAÑADA DEL TALA'
    gestion_localidad_206.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_206 = importer.save_or_locate(gestion_localidad_206)

    gestion_localidad_207 = Localidad()
    gestion_localidad_207.cod_postal = '5244'
    gestion_localidad_207.localidad = 'CAÑADA DEL TALA'
    gestion_localidad_207.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_207 = importer.save_or_locate(gestion_localidad_207)

    gestion_localidad_208 = Localidad()
    gestion_localidad_208.cod_postal = '5229'
    gestion_localidad_208.localidad = 'CAÑADA DE LUQUE'
    gestion_localidad_208.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_208 = importer.save_or_locate(gestion_localidad_208)

    gestion_localidad_209 = Localidad()
    gestion_localidad_209.cod_postal = '5961'
    gestion_localidad_209.localidad = 'CAÑADA DE MACHADO'
    gestion_localidad_209.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_209 = importer.save_or_locate(gestion_localidad_209)

    gestion_localidad_210 = Localidad()
    gestion_localidad_210.cod_postal = '5963'
    gestion_localidad_210.localidad = 'CAÑADA DE MACHADO SUD'
    gestion_localidad_210.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_210 = importer.save_or_locate(gestion_localidad_210)

    gestion_localidad_211 = Localidad()
    gestion_localidad_211.cod_postal = '5221'
    gestion_localidad_211.localidad = 'CAÑADA DE MATEO'
    gestion_localidad_211.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_211 = importer.save_or_locate(gestion_localidad_211)

    gestion_localidad_212 = Localidad()
    gestion_localidad_212.cod_postal = '5218'
    gestion_localidad_212.localidad = 'CAÑADA DE MAYO'
    gestion_localidad_212.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_212 = importer.save_or_locate(gestion_localidad_212)

    gestion_localidad_213 = Localidad()
    gestion_localidad_213.cod_postal = '5299'
    gestion_localidad_213.localidad = 'CAÑADA DE POCHO'
    gestion_localidad_213.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_213 = importer.save_or_locate(gestion_localidad_213)

    gestion_localidad_214 = Localidad()
    gestion_localidad_214.cod_postal = '5221'
    gestion_localidad_214.localidad = 'CAÑADA DE RIO PINTO'
    gestion_localidad_214.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_214 = importer.save_or_locate(gestion_localidad_214)

    gestion_localidad_215 = Localidad()
    gestion_localidad_215.cod_postal = '5299'
    gestion_localidad_215.localidad = 'CAÑADA DE SALAS'
    gestion_localidad_215.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_215 = importer.save_or_locate(gestion_localidad_215)

    gestion_localidad_216 = Localidad()
    gestion_localidad_216.cod_postal = '5873'
    gestion_localidad_216.localidad = 'CAÑADA GRANDE'
    gestion_localidad_216.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_216 = importer.save_or_locate(gestion_localidad_216)

    gestion_localidad_217 = Localidad()
    gestion_localidad_217.cod_postal = '5891'
    gestion_localidad_217.localidad = 'CAÑADA GRANDE'
    gestion_localidad_217.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_217 = importer.save_or_locate(gestion_localidad_217)

    gestion_localidad_218 = Localidad()
    gestion_localidad_218.cod_postal = '5280'
    gestion_localidad_218.localidad = 'CAÑADA HONDA'
    gestion_localidad_218.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_218 = importer.save_or_locate(gestion_localidad_218)

    gestion_localidad_219 = Localidad()
    gestion_localidad_219.cod_postal = '5227'
    gestion_localidad_219.localidad = 'CAÑADA HONDA'
    gestion_localidad_219.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_219 = importer.save_or_locate(gestion_localidad_219)

    gestion_localidad_220 = Localidad()
    gestion_localidad_220.cod_postal = '5889'
    gestion_localidad_220.localidad = 'CAÑADA LARGA'
    gestion_localidad_220.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_220 = importer.save_or_locate(gestion_localidad_220)

    gestion_localidad_221 = Localidad()
    gestion_localidad_221.cod_postal = '5131'
    gestion_localidad_221.localidad = 'CAÑADA SAN ANTONIO'
    gestion_localidad_221.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_221 = importer.save_or_locate(gestion_localidad_221)

    gestion_localidad_222 = Localidad()
    gestion_localidad_222.cod_postal = '5221'
    gestion_localidad_222.localidad = 'CAÑADAS HONDAS'
    gestion_localidad_222.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_222 = importer.save_or_locate(gestion_localidad_222)

    gestion_localidad_223 = Localidad()
    gestion_localidad_223.cod_postal = '6275'
    gestion_localidad_223.localidad = 'CAÑADA VERDE'
    gestion_localidad_223.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_223 = importer.save_or_locate(gestion_localidad_223)

    gestion_localidad_224 = Localidad()
    gestion_localidad_224.cod_postal = '5184'
    gestion_localidad_224.localidad = 'CAÑADON DE LOS MOGOTES'
    gestion_localidad_224.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_224 = importer.save_or_locate(gestion_localidad_224)

    gestion_localidad_225 = Localidad()
    gestion_localidad_225.cod_postal = '2645'
    gestion_localidad_225.localidad = 'CAP GRAL BERNARDO O HIGGINS'
    gestion_localidad_225.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_225 = importer.save_or_locate(gestion_localidad_225)

    gestion_localidad_226 = Localidad()
    gestion_localidad_226.cod_postal = '5101'
    gestion_localidad_226.localidad = 'CAPILLA DE COSME'
    gestion_localidad_226.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_226 = importer.save_or_locate(gestion_localidad_226)

    gestion_localidad_227 = Localidad()
    gestion_localidad_227.cod_postal = '5125'
    gestion_localidad_227.localidad = 'CAPILLA DE DOLORES'
    gestion_localidad_227.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_227 = importer.save_or_locate(gestion_localidad_227)

    gestion_localidad_228 = Localidad()
    gestion_localidad_228.cod_postal = '5963'
    gestion_localidad_228.localidad = 'CAPILLA DEL CARMEN'
    gestion_localidad_228.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_228 = importer.save_or_locate(gestion_localidad_228)

    gestion_localidad_229 = Localidad()
    gestion_localidad_229.cod_postal = '5184'
    gestion_localidad_229.localidad = 'CAPILLA DEL MONTE'
    gestion_localidad_229.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_229 = importer.save_or_locate(gestion_localidad_229)

    gestion_localidad_230 = Localidad()
    gestion_localidad_230.cod_postal = '5101'
    gestion_localidad_230.localidad = 'CAPILLA DE LOS REMEDIOS'
    gestion_localidad_230.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_230 = importer.save_or_locate(gestion_localidad_230)

    gestion_localidad_231 = Localidad()
    gestion_localidad_231.cod_postal = '5873'
    gestion_localidad_231.localidad = 'CAPILLA DE ROMERO'
    gestion_localidad_231.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_231 = importer.save_or_locate(gestion_localidad_231)

    gestion_localidad_232 = Localidad()
    gestion_localidad_232.cod_postal = '2559'
    gestion_localidad_232.localidad = 'CAPILLA DE SAN ANTONIO'
    gestion_localidad_232.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_232 = importer.save_or_locate(gestion_localidad_232)

    gestion_localidad_233 = Localidad()
    gestion_localidad_233.cod_postal = '5231'
    gestion_localidad_233.localidad = 'CAPILLA DE SITON'
    gestion_localidad_233.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_233 = importer.save_or_locate(gestion_localidad_233)

    gestion_localidad_234 = Localidad()
    gestion_localidad_234.cod_postal = '5813'
    gestion_localidad_234.localidad = 'CAPILLA DE TEGUA'
    gestion_localidad_234.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_234 = importer.save_or_locate(gestion_localidad_234)

    gestion_localidad_235 = Localidad()
    gestion_localidad_235.cod_postal = '5129'
    gestion_localidad_235.localidad = 'CAPILLA LA ESPERANZA'
    gestion_localidad_235.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_235 = importer.save_or_locate(gestion_localidad_235)

    gestion_localidad_236 = Localidad()
    gestion_localidad_236.cod_postal = '2432'
    gestion_localidad_236.localidad = 'CAPILLA SAN ANTONIO'
    gestion_localidad_236.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_236 = importer.save_or_locate(gestion_localidad_236)

    gestion_localidad_237 = Localidad()
    gestion_localidad_237.cod_postal = '5936'
    gestion_localidad_237.localidad = 'CAPILLA SAN ANTONIO DE YUCAT'
    gestion_localidad_237.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_237 = importer.save_or_locate(gestion_localidad_237)

    gestion_localidad_238 = Localidad()
    gestion_localidad_238.cod_postal = '2415'
    gestion_localidad_238.localidad = 'CAPILLA SANTA ROSA'
    gestion_localidad_238.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_238 = importer.save_or_locate(gestion_localidad_238)

    gestion_localidad_239 = Localidad()
    gestion_localidad_239.cod_postal = '5196'
    gestion_localidad_239.localidad = 'CARAHUASI'
    gestion_localidad_239.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_239 = importer.save_or_locate(gestion_localidad_239)

    gestion_localidad_240 = Localidad()
    gestion_localidad_240.cod_postal = '5925'
    gestion_localidad_240.localidad = 'CARLOMAGNO'
    gestion_localidad_240.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_240 = importer.save_or_locate(gestion_localidad_240)

    gestion_localidad_241 = Localidad()
    gestion_localidad_241.cod_postal = '5805'
    gestion_localidad_241.localidad = 'CARNERILLO'
    gestion_localidad_241.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_241 = importer.save_or_locate(gestion_localidad_241)

    gestion_localidad_242 = Localidad()
    gestion_localidad_242.cod_postal = '5246'
    gestion_localidad_242.localidad = 'CARNERO YACO'
    gestion_localidad_242.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_242 = importer.save_or_locate(gestion_localidad_242)

    gestion_localidad_243 = Localidad()
    gestion_localidad_243.cod_postal = '5223'
    gestion_localidad_243.localidad = 'CAROYA'
    gestion_localidad_243.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_243 = importer.save_or_locate(gestion_localidad_243)

    gestion_localidad_244 = Localidad()
    gestion_localidad_244.cod_postal = '5915'
    gestion_localidad_244.localidad = 'CARRILOBO'
    gestion_localidad_244.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_244 = importer.save_or_locate(gestion_localidad_244)

    gestion_localidad_245 = Localidad()
    gestion_localidad_245.cod_postal = '5285'
    gestion_localidad_245.localidad = 'CARRIZAL'
    gestion_localidad_245.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_245 = importer.save_or_locate(gestion_localidad_245)

    gestion_localidad_246 = Localidad()
    gestion_localidad_246.cod_postal = '5299'
    gestion_localidad_246.localidad = 'CARRIZAL'
    gestion_localidad_246.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_246 = importer.save_or_locate(gestion_localidad_246)

    gestion_localidad_247 = Localidad()
    gestion_localidad_247.cod_postal = '5871'
    gestion_localidad_247.localidad = 'CARTABEROL'
    gestion_localidad_247.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_247 = importer.save_or_locate(gestion_localidad_247)

    gestion_localidad_248 = Localidad()
    gestion_localidad_248.cod_postal = '5151'
    gestion_localidad_248.localidad = 'CASA BAMBA'
    gestion_localidad_248.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_248 = importer.save_or_locate(gestion_localidad_248)

    gestion_localidad_249 = Localidad()
    gestion_localidad_249.cod_postal = '5299'
    gestion_localidad_249.localidad = 'CASA BLANCA'
    gestion_localidad_249.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_249 = importer.save_or_locate(gestion_localidad_249)

    gestion_localidad_250 = Localidad()
    gestion_localidad_250.cod_postal = '5891'
    gestion_localidad_250.localidad = 'CASA DE PIEDRA'
    gestion_localidad_250.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_250 = importer.save_or_locate(gestion_localidad_250)

    gestion_localidad_251 = Localidad()
    gestion_localidad_251.cod_postal = '5162'
    gestion_localidad_251.localidad = 'CASA GRANDE'
    gestion_localidad_251.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_251 = importer.save_or_locate(gestion_localidad_251)

    gestion_localidad_252 = Localidad()
    gestion_localidad_252.cod_postal = '5155'
    gestion_localidad_252.localidad = 'CASA NUEVA'
    gestion_localidad_252.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_252 = importer.save_or_locate(gestion_localidad_252)

    gestion_localidad_253 = Localidad()
    gestion_localidad_253.cod_postal = '5175'
    gestion_localidad_253.localidad = 'CASA SERRANA HUERTA GRANDE'
    gestion_localidad_253.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_253 = importer.save_or_locate(gestion_localidad_253)

    gestion_localidad_254 = Localidad()
    gestion_localidad_254.cod_postal = '5246'
    gestion_localidad_254.localidad = 'CASAS VEJAS'
    gestion_localidad_254.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_254 = importer.save_or_locate(gestion_localidad_254)

    gestion_localidad_255 = Localidad()
    gestion_localidad_255.cod_postal = '5236'
    gestion_localidad_255.localidad = 'CASAS VIEJAS'
    gestion_localidad_255.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_255 = importer.save_or_locate(gestion_localidad_255)

    gestion_localidad_256 = Localidad()
    gestion_localidad_256.cod_postal = '5285'
    gestion_localidad_256.localidad = 'CASAS VIEJAS'
    gestion_localidad_256.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_256 = importer.save_or_locate(gestion_localidad_256)

    gestion_localidad_257 = Localidad()
    gestion_localidad_257.cod_postal = '5178'
    gestion_localidad_257.localidad = 'CASCADAS'
    gestion_localidad_257.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_257 = importer.save_or_locate(gestion_localidad_257)

    gestion_localidad_258 = Localidad()
    gestion_localidad_258.cod_postal = '5209'
    gestion_localidad_258.localidad = 'CASPICHUMA'
    gestion_localidad_258.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_258 = importer.save_or_locate(gestion_localidad_258)

    gestion_localidad_259 = Localidad()
    gestion_localidad_259.cod_postal = '5209'
    gestion_localidad_259.localidad = 'CASPICUCHANA'
    gestion_localidad_259.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_259 = importer.save_or_locate(gestion_localidad_259)

    gestion_localidad_260 = Localidad()
    gestion_localidad_260.cod_postal = '5149'
    gestion_localidad_260.localidad = 'CASSAFFOUSTH ESTACION FCGB'
    gestion_localidad_260.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_260 = importer.save_or_locate(gestion_localidad_260)

    gestion_localidad_261 = Localidad()
    gestion_localidad_261.cod_postal = '5135'
    gestion_localidad_261.localidad = 'CASTELLANOS'
    gestion_localidad_261.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_261 = importer.save_or_locate(gestion_localidad_261)

    gestion_localidad_262 = Localidad()
    gestion_localidad_262.cod_postal = '2625'
    gestion_localidad_262.localidad = 'CAVANAGH'
    gestion_localidad_262.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_262 = importer.save_or_locate(gestion_localidad_262)

    gestion_localidad_263 = Localidad()
    gestion_localidad_263.cod_postal = '5901'
    gestion_localidad_263.localidad = 'CAYUQUEO'
    gestion_localidad_263.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_263 = importer.save_or_locate(gestion_localidad_263)

    gestion_localidad_264 = Localidad()
    gestion_localidad_264.cod_postal = '5191'
    gestion_localidad_264.localidad = 'CERRO BLANCO'
    gestion_localidad_264.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_264 = importer.save_or_locate(gestion_localidad_264)

    gestion_localidad_265 = Localidad()
    gestion_localidad_265.cod_postal = '5293'
    gestion_localidad_265.localidad = 'CERRO BOLA'
    gestion_localidad_265.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_265 = importer.save_or_locate(gestion_localidad_265)

    gestion_localidad_266 = Localidad()
    gestion_localidad_266.cod_postal = '5244'
    gestion_localidad_266.localidad = 'CERRO COLORADO'
    gestion_localidad_266.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_266 = importer.save_or_locate(gestion_localidad_266)

    gestion_localidad_267 = Localidad()
    gestion_localidad_267.cod_postal = '5821'
    gestion_localidad_267.localidad = 'CERRO COLORADO'
    gestion_localidad_267.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_267 = importer.save_or_locate(gestion_localidad_267)

    gestion_localidad_268 = Localidad()
    gestion_localidad_268.cod_postal = '5200'
    gestion_localidad_268.localidad = 'CERRO DE LA CRUZ'
    gestion_localidad_268.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_268 = importer.save_or_locate(gestion_localidad_268)

    gestion_localidad_269 = Localidad()
    gestion_localidad_269.cod_postal = '5221'
    gestion_localidad_269.localidad = 'CERRO NEGRO'
    gestion_localidad_269.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_269 = importer.save_or_locate(gestion_localidad_269)

    gestion_localidad_270 = Localidad()
    gestion_localidad_270.cod_postal = '5297'
    gestion_localidad_270.localidad = 'CERRO NEGRO'
    gestion_localidad_270.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_270 = importer.save_or_locate(gestion_localidad_270)

    gestion_localidad_271 = Localidad()
    gestion_localidad_271.cod_postal = '5821'
    gestion_localidad_271.localidad = 'CERRO SAN LORENZO'
    gestion_localidad_271.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_271 = importer.save_or_locate(gestion_localidad_271)

    gestion_localidad_272 = Localidad()
    gestion_localidad_272.cod_postal = '5859'
    gestion_localidad_272.localidad = 'CERROS ASPEROS'
    gestion_localidad_272.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_272 = importer.save_or_locate(gestion_localidad_272)

    gestion_localidad_273 = Localidad()
    gestion_localidad_273.cod_postal = '5282'
    gestion_localidad_273.localidad = 'CHACHA DEL REY'
    gestion_localidad_273.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_273 = importer.save_or_locate(gestion_localidad_273)

    gestion_localidad_274 = Localidad()
    gestion_localidad_274.cod_postal = '5284'
    gestion_localidad_274.localidad = 'CHACRAS'
    gestion_localidad_274.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_274 = importer.save_or_locate(gestion_localidad_274)

    gestion_localidad_275 = Localidad()
    gestion_localidad_275.cod_postal = '5284'
    gestion_localidad_275.localidad = 'CHACRAS DEL POTRERO'
    gestion_localidad_275.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_275 = importer.save_or_locate(gestion_localidad_275)

    gestion_localidad_276 = Localidad()
    gestion_localidad_276.cod_postal = '5244'
    gestion_localidad_276.localidad = 'CHACRAS DEL SAUCE'
    gestion_localidad_276.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_276 = importer.save_or_locate(gestion_localidad_276)

    gestion_localidad_277 = Localidad()
    gestion_localidad_277.cod_postal = '5242'
    gestion_localidad_277.localidad = 'CHACRAS VIEJAS'
    gestion_localidad_277.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_277 = importer.save_or_locate(gestion_localidad_277)

    gestion_localidad_278 = Localidad()
    gestion_localidad_278.cod_postal = '5837'
    gestion_localidad_278.localidad = 'CHAJAN'
    gestion_localidad_278.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_278 = importer.save_or_locate(gestion_localidad_278)

    gestion_localidad_279 = Localidad()
    gestion_localidad_279.cod_postal = '5229'
    gestion_localidad_279.localidad = 'CHALACEA'
    gestion_localidad_279.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_279 = importer.save_or_locate(gestion_localidad_279)

    gestion_localidad_280 = Localidad()
    gestion_localidad_280.cod_postal = '5299'
    gestion_localidad_280.localidad = 'CHAMICO'
    gestion_localidad_280.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_280 = importer.save_or_locate(gestion_localidad_280)

    gestion_localidad_281 = Localidad()
    gestion_localidad_281.cod_postal = '5871'
    gestion_localidad_281.localidad = 'CHANCANI'
    gestion_localidad_281.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_281 = importer.save_or_locate(gestion_localidad_281)

    gestion_localidad_282 = Localidad()
    gestion_localidad_282.cod_postal = '5291'
    gestion_localidad_282.localidad = 'CHAÑARIACO'
    gestion_localidad_282.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_282 = importer.save_or_locate(gestion_localidad_282)

    gestion_localidad_283 = Localidad()
    gestion_localidad_283.cod_postal = '5829'
    gestion_localidad_283.localidad = 'CHAÑARITOS'
    gestion_localidad_283.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_283 = importer.save_or_locate(gestion_localidad_283)

    gestion_localidad_284 = Localidad()
    gestion_localidad_284.cod_postal = '5246'
    gestion_localidad_284.localidad = 'CHAÑAR VIEJO'
    gestion_localidad_284.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_284 = importer.save_or_locate(gestion_localidad_284)

    gestion_localidad_285 = Localidad()
    gestion_localidad_285.cod_postal = '5870'
    gestion_localidad_285.localidad = 'CHAQUINCHUNA'
    gestion_localidad_285.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_285 = importer.save_or_locate(gestion_localidad_285)

    gestion_localidad_286 = Localidad()
    gestion_localidad_286.cod_postal = '5287'
    gestion_localidad_286.localidad = 'CHARACATO'
    gestion_localidad_286.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_286 = importer.save_or_locate(gestion_localidad_286)

    gestion_localidad_287 = Localidad()
    gestion_localidad_287.cod_postal = '5282'
    gestion_localidad_287.localidad = 'CHARBONIER'
    gestion_localidad_287.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_287 = importer.save_or_locate(gestion_localidad_287)

    gestion_localidad_288 = Localidad()
    gestion_localidad_288.cod_postal = '5127'
    gestion_localidad_288.localidad = 'CHARCAS NORTE'
    gestion_localidad_288.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_288 = importer.save_or_locate(gestion_localidad_288)

    gestion_localidad_289 = Localidad()
    gestion_localidad_289.cod_postal = '5807'
    gestion_localidad_289.localidad = 'CHARRAS'
    gestion_localidad_289.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_289 = importer.save_or_locate(gestion_localidad_289)

    gestion_localidad_290 = Localidad()
    gestion_localidad_290.cod_postal = '2675'
    gestion_localidad_290.localidad = 'CHAZON'
    gestion_localidad_290.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_290 = importer.save_or_locate(gestion_localidad_290)

    gestion_localidad_291 = Localidad()
    gestion_localidad_291.cod_postal = '5246'
    gestion_localidad_291.localidad = 'CHILE CORRAL AL AGUADA'
    gestion_localidad_291.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_291 = importer.save_or_locate(gestion_localidad_291)

    gestion_localidad_292 = Localidad()
    gestion_localidad_292.cod_postal = '2561'
    gestion_localidad_292.localidad = 'CHILIBROSTE'
    gestion_localidad_292.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_292 = importer.save_or_locate(gestion_localidad_292)

    gestion_localidad_293 = Localidad()
    gestion_localidad_293.cod_postal = '5246'
    gestion_localidad_293.localidad = 'CHILLI CORRAL'
    gestion_localidad_293.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_293 = importer.save_or_locate(gestion_localidad_293)

    gestion_localidad_294 = Localidad()
    gestion_localidad_294.cod_postal = '5244'
    gestion_localidad_294.localidad = 'CHIPITIN'
    gestion_localidad_294.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_294 = importer.save_or_locate(gestion_localidad_294)

    gestion_localidad_295 = Localidad()
    gestion_localidad_295.cod_postal = '5871'
    gestion_localidad_295.localidad = 'CHUA'
    gestion_localidad_295.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_295 = importer.save_or_locate(gestion_localidad_295)

    gestion_localidad_296 = Localidad()
    gestion_localidad_296.cod_postal = '5875'
    gestion_localidad_296.localidad = 'CHUCHIRAS'
    gestion_localidad_296.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_296 = importer.save_or_locate(gestion_localidad_296)

    gestion_localidad_297 = Localidad()
    gestion_localidad_297.cod_postal = '5805'
    gestion_localidad_297.localidad = 'CHUCUL'
    gestion_localidad_297.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_297 = importer.save_or_locate(gestion_localidad_297)

    gestion_localidad_298 = Localidad()
    gestion_localidad_298.cod_postal = '5218'
    gestion_localidad_298.localidad = 'CHUÑA'
    gestion_localidad_298.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_298 = importer.save_or_locate(gestion_localidad_298)

    gestion_localidad_299 = Localidad()
    gestion_localidad_299.cod_postal = '5201'
    gestion_localidad_299.localidad = 'CHUÑA HUASI'
    gestion_localidad_299.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_299 = importer.save_or_locate(gestion_localidad_299)

    gestion_localidad_300 = Localidad()
    gestion_localidad_300.cod_postal = '5246'
    gestion_localidad_300.localidad = 'CHURQUI CAÑADA'
    gestion_localidad_300.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_300 = importer.save_or_locate(gestion_localidad_300)

    gestion_localidad_301 = Localidad()
    gestion_localidad_301.cod_postal = '5891'
    gestion_localidad_301.localidad = 'CIENAGA DE ALLENDE'
    gestion_localidad_301.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_301 = importer.save_or_locate(gestion_localidad_301)

    gestion_localidad_302 = Localidad()
    gestion_localidad_302.cod_postal = '5297'
    gestion_localidad_302.localidad = 'CIENAGA DE BRITOS'
    gestion_localidad_302.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_302 = importer.save_or_locate(gestion_localidad_302)

    gestion_localidad_303 = Localidad()
    gestion_localidad_303.cod_postal = '5289'
    gestion_localidad_303.localidad = 'CIENAGA DEL CORO'
    gestion_localidad_303.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_303 = importer.save_or_locate(gestion_localidad_303)

    gestion_localidad_304 = Localidad()
    gestion_localidad_304.cod_postal = '2559'
    gestion_localidad_304.localidad = 'CINTRA'
    gestion_localidad_304.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_304 = importer.save_or_locate(gestion_localidad_304)

    gestion_localidad_305 = Localidad()
    gestion_localidad_305.cod_postal = '5119'
    gestion_localidad_305.localidad = 'CNIA HOGAR VELEZ SARSFIELD'
    gestion_localidad_305.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_305 = importer.save_or_locate(gestion_localidad_305)

    gestion_localidad_306 = Localidad()
    gestion_localidad_306.cod_postal = '5857'
    gestion_localidad_306.localidad = 'CNIA VACACIONES DE EMPLEADO'
    gestion_localidad_306.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_306 = importer.save_or_locate(gestion_localidad_306)

    gestion_localidad_307 = Localidad()
    gestion_localidad_307.cod_postal = '5965'
    gestion_localidad_307.localidad = 'COLAZO'
    gestion_localidad_307.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_307 = importer.save_or_locate(gestion_localidad_307)

    gestion_localidad_308 = Localidad()
    gestion_localidad_308.cod_postal = '2349'
    gestion_localidad_308.localidad = 'COLONIA 10 DE JULIO'
    gestion_localidad_308.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_308 = importer.save_or_locate(gestion_localidad_308)

    gestion_localidad_309 = Localidad()
    gestion_localidad_309.cod_postal = '2581'
    gestion_localidad_309.localidad = 'COLONIA 25 LOS SURGENTES'
    gestion_localidad_309.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_309 = importer.save_or_locate(gestion_localidad_309)

    gestion_localidad_310 = Localidad()
    gestion_localidad_310.cod_postal = '5196'
    gestion_localidad_310.localidad = 'COLONIA ALEMANA'
    gestion_localidad_310.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_310 = importer.save_or_locate(gestion_localidad_310)

    gestion_localidad_311 = Localidad()
    gestion_localidad_311.cod_postal = '5987'
    gestion_localidad_311.localidad = 'COLONIA ALMADA'
    gestion_localidad_311.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_311 = importer.save_or_locate(gestion_localidad_311)

    gestion_localidad_312 = Localidad()
    gestion_localidad_312.cod_postal = '5941'
    gestion_localidad_312.localidad = 'COLONIA ANGELITA'
    gestion_localidad_312.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_312 = importer.save_or_locate(gestion_localidad_312)

    gestion_localidad_313 = Localidad()
    gestion_localidad_313.cod_postal = '2413'
    gestion_localidad_313.localidad = 'COLONIA ANITA'
    gestion_localidad_313.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_313 = importer.save_or_locate(gestion_localidad_313)

    gestion_localidad_314 = Localidad()
    gestion_localidad_314.cod_postal = '2436'
    gestion_localidad_314.localidad = 'COLONIA ARROYO DE ALVAREZ'
    gestion_localidad_314.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_314 = importer.save_or_locate(gestion_localidad_314)

    gestion_localidad_315 = Localidad()
    gestion_localidad_315.cod_postal = '2662'
    gestion_localidad_315.localidad = 'COLONIA BALLESTEROS'
    gestion_localidad_315.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_315 = importer.save_or_locate(gestion_localidad_315)

    gestion_localidad_316 = Localidad()
    gestion_localidad_316.cod_postal = '5155'
    gestion_localidad_316.localidad = 'COLONIA BANCO PCIA BS AS'
    gestion_localidad_316.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_316 = importer.save_or_locate(gestion_localidad_316)

    gestion_localidad_317 = Localidad()
    gestion_localidad_317.cod_postal = '2659'
    gestion_localidad_317.localidad = 'COLONIA BARGE'
    gestion_localidad_317.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_317 = importer.save_or_locate(gestion_localidad_317)

    gestion_localidad_318 = Localidad()
    gestion_localidad_318.cod_postal = '2421'
    gestion_localidad_318.localidad = 'COLONIA BEIRO'
    gestion_localidad_318.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_318 = importer.save_or_locate(gestion_localidad_318)

    gestion_localidad_319 = Localidad()
    gestion_localidad_319.cod_postal = '2651'
    gestion_localidad_319.localidad = 'COLONIA BISMARCK'
    gestion_localidad_319.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_319 = importer.save_or_locate(gestion_localidad_319)

    gestion_localidad_320 = Localidad()
    gestion_localidad_320.cod_postal = '6270'
    gestion_localidad_320.localidad = 'COLONIA BOERO'
    gestion_localidad_320.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_320 = importer.save_or_locate(gestion_localidad_320)

    gestion_localidad_321 = Localidad()
    gestion_localidad_321.cod_postal = '2419'
    gestion_localidad_321.localidad = 'COLONIA BOTTURI'
    gestion_localidad_321.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_321 = importer.save_or_locate(gestion_localidad_321)

    gestion_localidad_322 = Localidad()
    gestion_localidad_322.cod_postal = '2651'
    gestion_localidad_322.localidad = 'COLONIA BREMEN'
    gestion_localidad_322.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_322 = importer.save_or_locate(gestion_localidad_322)

    gestion_localidad_323 = Localidad()
    gestion_localidad_323.cod_postal = '2580'
    gestion_localidad_323.localidad = 'COLONIA CALCHAQUI'
    gestion_localidad_323.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_323 = importer.save_or_locate(gestion_localidad_323)

    gestion_localidad_324 = Localidad()
    gestion_localidad_324.cod_postal = '5137'
    gestion_localidad_324.localidad = 'COLONIA CAÑADON'
    gestion_localidad_324.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_324 = importer.save_or_locate(gestion_localidad_324)

    gestion_localidad_325 = Localidad()
    gestion_localidad_325.cod_postal = '5223'
    gestion_localidad_325.localidad = 'COLONIA CAROYA'
    gestion_localidad_325.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_325 = importer.save_or_locate(gestion_localidad_325)

    gestion_localidad_326 = Localidad()
    gestion_localidad_326.cod_postal = '2415'
    gestion_localidad_326.localidad = 'COLONIA CEFERINA'
    gestion_localidad_326.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_326 = importer.save_or_locate(gestion_localidad_326)

    gestion_localidad_327 = Localidad()
    gestion_localidad_327.cod_postal = '2436'
    gestion_localidad_327.localidad = 'COLONIA CORTADERA'
    gestion_localidad_327.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_327 = importer.save_or_locate(gestion_localidad_327)

    gestion_localidad_328 = Localidad()
    gestion_localidad_328.cod_postal = '5101'
    gestion_localidad_328.localidad = 'COLONIA COSME SUD'
    gestion_localidad_328.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_328 = importer.save_or_locate(gestion_localidad_328)

    gestion_localidad_329 = Localidad()
    gestion_localidad_329.cod_postal = '2435'
    gestion_localidad_329.localidad = 'COLONIA COYUNDA'
    gestion_localidad_329.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_329 = importer.save_or_locate(gestion_localidad_329)

    gestion_localidad_330 = Localidad()
    gestion_localidad_330.cod_postal = '2424'
    gestion_localidad_330.localidad = 'COLONIA CRISTINA'
    gestion_localidad_330.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_330 = importer.save_or_locate(gestion_localidad_330)

    gestion_localidad_331 = Localidad()
    gestion_localidad_331.cod_postal = '5847'
    gestion_localidad_331.localidad = 'COLONIA DEAN FUNES'
    gestion_localidad_331.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_331 = importer.save_or_locate(gestion_localidad_331)

    gestion_localidad_332 = Localidad()
    gestion_localidad_332.cod_postal = '2428'
    gestion_localidad_332.localidad = 'COLONIA DEL BANCO NACION'
    gestion_localidad_332.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_332 = importer.save_or_locate(gestion_localidad_332)

    gestion_localidad_333 = Localidad()
    gestion_localidad_333.cod_postal = '5809'
    gestion_localidad_333.localidad = 'COLONIA DOLORES'
    gestion_localidad_333.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_333 = importer.save_or_locate(gestion_localidad_333)

    gestion_localidad_334 = Localidad()
    gestion_localidad_334.cod_postal = '6270'
    gestion_localidad_334.localidad = 'COLONIA DOROTEA'
    gestion_localidad_334.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_334 = importer.save_or_locate(gestion_localidad_334)

    gestion_localidad_335 = Localidad()
    gestion_localidad_335.cod_postal = '2421'
    gestion_localidad_335.localidad = 'COLONIA DOS HERMANOS'
    gestion_localidad_335.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_335 = importer.save_or_locate(gestion_localidad_335)

    gestion_localidad_336 = Localidad()
    gestion_localidad_336.cod_postal = '5801'
    gestion_localidad_336.localidad = 'COLONIA EL CARMEN PARAJE'
    gestion_localidad_336.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_336 = importer.save_or_locate(gestion_localidad_336)

    gestion_localidad_337 = Localidad()
    gestion_localidad_337.cod_postal = '2594'
    gestion_localidad_337.localidad = 'COLONIA EL CHAJA'
    gestion_localidad_337.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_337 = importer.save_or_locate(gestion_localidad_337)

    gestion_localidad_338 = Localidad()
    gestion_localidad_338.cod_postal = '5133'
    gestion_localidad_338.localidad = 'COLONIA EL FORTIN'
    gestion_localidad_338.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_338 = importer.save_or_locate(gestion_localidad_338)

    gestion_localidad_339 = Localidad()
    gestion_localidad_339.cod_postal = '2424'
    gestion_localidad_339.localidad = 'COLONIA EL MILAGRO'
    gestion_localidad_339.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_339 = importer.save_or_locate(gestion_localidad_339)

    gestion_localidad_340 = Localidad()
    gestion_localidad_340.cod_postal = '2424'
    gestion_localidad_340.localidad = 'COLONIA EL TRABAJO'
    gestion_localidad_340.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_340 = importer.save_or_locate(gestion_localidad_340)

    gestion_localidad_341 = Localidad()
    gestion_localidad_341.cod_postal = '2413'
    gestion_localidad_341.localidad = 'COLONIA EUGENIA'
    gestion_localidad_341.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_341 = importer.save_or_locate(gestion_localidad_341)

    gestion_localidad_342 = Localidad()
    gestion_localidad_342.cod_postal = '5987'
    gestion_localidad_342.localidad = 'COLONIA GARZON'
    gestion_localidad_342.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_342 = importer.save_or_locate(gestion_localidad_342)

    gestion_localidad_343 = Localidad()
    gestion_localidad_343.cod_postal = '5945'
    gestion_localidad_343.localidad = 'COLONIA GENERAL DEHEZA'
    gestion_localidad_343.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_343 = importer.save_or_locate(gestion_localidad_343)

    gestion_localidad_344 = Localidad()
    gestion_localidad_344.cod_postal = '2415'
    gestion_localidad_344.localidad = 'COLONIA GORCHS'
    gestion_localidad_344.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_344 = importer.save_or_locate(gestion_localidad_344)

    gestion_localidad_345 = Localidad()
    gestion_localidad_345.cod_postal = '5933'
    gestion_localidad_345.localidad = 'COLONIA HAMBURGO'
    gestion_localidad_345.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_345 = importer.save_or_locate(gestion_localidad_345)

    gestion_localidad_346 = Localidad()
    gestion_localidad_346.cod_postal = '5131'
    gestion_localidad_346.localidad = 'COLONIA HOLANDESA'
    gestion_localidad_346.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_346 = importer.save_or_locate(gestion_localidad_346)

    gestion_localidad_347 = Localidad()
    gestion_localidad_347.cod_postal = '2645'
    gestion_localidad_347.localidad = 'COLONIA ITALIANA'
    gestion_localidad_347.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_347 = importer.save_or_locate(gestion_localidad_347)

    gestion_localidad_348 = Localidad()
    gestion_localidad_348.cod_postal = '2413'
    gestion_localidad_348.localidad = 'COLONIA ITURRASPE'
    gestion_localidad_348.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_348 = importer.save_or_locate(gestion_localidad_348)

    gestion_localidad_349 = Localidad()
    gestion_localidad_349.cod_postal = '5137'
    gestion_localidad_349.localidad = 'COLONIA LA ARGENTINA'
    gestion_localidad_349.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_349 = importer.save_or_locate(gestion_localidad_349)

    gestion_localidad_350 = Localidad()
    gestion_localidad_350.cod_postal = '6140'
    gestion_localidad_350.localidad = 'COLONIA LA ARGENTINA'
    gestion_localidad_350.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_350 = importer.save_or_locate(gestion_localidad_350)

    gestion_localidad_351 = Localidad()
    gestion_localidad_351.cod_postal = '5196'
    gestion_localidad_351.localidad = 'COLONIA LA CALLE'
    gestion_localidad_351.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_351 = importer.save_or_locate(gestion_localidad_351)

    gestion_localidad_352 = Localidad()
    gestion_localidad_352.cod_postal = '6141'
    gestion_localidad_352.localidad = 'COLONIA LA CARMENSITA'
    gestion_localidad_352.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_352 = importer.save_or_locate(gestion_localidad_352)

    gestion_localidad_353 = Localidad()
    gestion_localidad_353.cod_postal = '5847'
    gestion_localidad_353.localidad = 'COLONIA LA CELESTINA'
    gestion_localidad_353.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_353 = importer.save_or_locate(gestion_localidad_353)

    gestion_localidad_354 = Localidad()
    gestion_localidad_354.cod_postal = '2559'
    gestion_localidad_354.localidad = 'COLONIA LA LEONCITA'
    gestion_localidad_354.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_354 = importer.save_or_locate(gestion_localidad_354)

    gestion_localidad_355 = Localidad()
    gestion_localidad_355.cod_postal = '2650'
    gestion_localidad_355.localidad = 'COLONIA LA LOLA'
    gestion_localidad_355.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_355 = importer.save_or_locate(gestion_localidad_355)

    gestion_localidad_356 = Localidad()
    gestion_localidad_356.cod_postal = '6132'
    gestion_localidad_356.localidad = 'COLONIA LA MAGDALENA DE ORO'
    gestion_localidad_356.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_356 = importer.save_or_locate(gestion_localidad_356)

    gestion_localidad_357 = Localidad()
    gestion_localidad_357.cod_postal = '2423'
    gestion_localidad_357.localidad = 'COLONIA LA MOROCHA'
    gestion_localidad_357.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_357 = importer.save_or_locate(gestion_localidad_357)

    gestion_localidad_358 = Localidad()
    gestion_localidad_358.cod_postal = '2580'
    gestion_localidad_358.localidad = 'COLONIA LA MURIUCHA'
    gestion_localidad_358.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_358 = importer.save_or_locate(gestion_localidad_358)

    gestion_localidad_359 = Localidad()
    gestion_localidad_359.cod_postal = '2645'
    gestion_localidad_359.localidad = 'COLONIA LA PALESTINA'
    gestion_localidad_359.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_359 = importer.save_or_locate(gestion_localidad_359)

    gestion_localidad_360 = Localidad()
    gestion_localidad_360.cod_postal = '5801'
    gestion_localidad_360.localidad = 'COLONIA LA PIEDRA'
    gestion_localidad_360.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_360 = importer.save_or_locate(gestion_localidad_360)

    gestion_localidad_361 = Localidad()
    gestion_localidad_361.cod_postal = '5933'
    gestion_localidad_361.localidad = 'COLONIA LA PRIMAVERA'
    gestion_localidad_361.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_361 = importer.save_or_locate(gestion_localidad_361)

    gestion_localidad_362 = Localidad()
    gestion_localidad_362.cod_postal = '6134'
    gestion_localidad_362.localidad = 'COLONIA LA PROVIDENCIA'
    gestion_localidad_362.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_362 = importer.save_or_locate(gestion_localidad_362)

    gestion_localidad_363 = Localidad()
    gestion_localidad_363.cod_postal = '5135'
    gestion_localidad_363.localidad = 'COLONIA LAS CUATRO ESQUINAS'
    gestion_localidad_363.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_363 = importer.save_or_locate(gestion_localidad_363)

    gestion_localidad_364 = Localidad()
    gestion_localidad_364.cod_postal = '2433'
    gestion_localidad_364.localidad = 'COLONIA LAS PICHANAS'
    gestion_localidad_364.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_364 = importer.save_or_locate(gestion_localidad_364)

    gestion_localidad_365 = Localidad()
    gestion_localidad_365.cod_postal = '2435'
    gestion_localidad_365.localidad = 'COLONIA LA TORDILLA'
    gestion_localidad_365.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_365 = importer.save_or_locate(gestion_localidad_365)

    gestion_localidad_366 = Localidad()
    gestion_localidad_366.cod_postal = '2417'
    gestion_localidad_366.localidad = 'COLONIA LA TRINCHERA'
    gestion_localidad_366.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_366 = importer.save_or_locate(gestion_localidad_366)

    gestion_localidad_367 = Localidad()
    gestion_localidad_367.cod_postal = '2415'
    gestion_localidad_367.localidad = 'COLONIA LAVARELLO'
    gestion_localidad_367.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_367 = importer.save_or_locate(gestion_localidad_367)

    gestion_localidad_368 = Localidad()
    gestion_localidad_368.cod_postal = '2662'
    gestion_localidad_368.localidad = 'COLONIA LEDESMA'
    gestion_localidad_368.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_368 = importer.save_or_locate(gestion_localidad_368)

    gestion_localidad_369 = Localidad()
    gestion_localidad_369.cod_postal = '2189'
    gestion_localidad_369.localidad = 'COLONIA LOS VASCOS'
    gestion_localidad_369.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_369 = importer.save_or_locate(gestion_localidad_369)

    gestion_localidad_370 = Localidad()
    gestion_localidad_370.cod_postal = '5850'
    gestion_localidad_370.localidad = 'COLONIA LUQUE'
    gestion_localidad_370.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_370 = importer.save_or_locate(gestion_localidad_370)

    gestion_localidad_371 = Localidad()
    gestion_localidad_371.cod_postal = '2684'
    gestion_localidad_371.localidad = 'COLONIA MAIPU'
    gestion_localidad_371.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_371 = importer.save_or_locate(gestion_localidad_371)

    gestion_localidad_372 = Localidad()
    gestion_localidad_372.cod_postal = '2424'
    gestion_localidad_372.localidad = 'COLONIA MARINA'
    gestion_localidad_372.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_372 = importer.save_or_locate(gestion_localidad_372)

    gestion_localidad_373 = Localidad()
    gestion_localidad_373.cod_postal = '2559'
    gestion_localidad_373.localidad = 'COLONIA MASCHI'
    gestion_localidad_373.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_373 = importer.save_or_locate(gestion_localidad_373)

    gestion_localidad_374 = Localidad()
    gestion_localidad_374.cod_postal = '2349'
    gestion_localidad_374.localidad = 'COLONIA MAUNIER'
    gestion_localidad_374.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_374 = importer.save_or_locate(gestion_localidad_374)

    gestion_localidad_375 = Localidad()
    gestion_localidad_375.cod_postal = '2349'
    gestion_localidad_375.localidad = 'COLONIA MILESSI'
    gestion_localidad_375.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_375 = importer.save_or_locate(gestion_localidad_375)

    gestion_localidad_376 = Localidad()
    gestion_localidad_376.cod_postal = '5875'
    gestion_localidad_376.localidad = 'COLONIA MONTES NEGROS'
    gestion_localidad_376.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_376 = importer.save_or_locate(gestion_localidad_376)

    gestion_localidad_377 = Localidad()
    gestion_localidad_377.cod_postal = '2415'
    gestion_localidad_377.localidad = 'COLONIA NUEVO PIAMONTE'
    gestion_localidad_377.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_377 = importer.save_or_locate(gestion_localidad_377)

    gestion_localidad_378 = Localidad()
    gestion_localidad_378.cod_postal = '5841'
    gestion_localidad_378.localidad = 'COLONIA ORCOVI'
    gestion_localidad_378.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_378 = importer.save_or_locate(gestion_localidad_378)

    gestion_localidad_379 = Localidad()
    gestion_localidad_379.cod_postal = '2415'
    gestion_localidad_379.localidad = 'COLONIA PALO LABRADO'
    gestion_localidad_379.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_379 = importer.save_or_locate(gestion_localidad_379)

    gestion_localidad_380 = Localidad()
    gestion_localidad_380.cod_postal = '5801'
    gestion_localidad_380.localidad = 'COLONIA PASO CARRIL'
    gestion_localidad_380.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_380 = importer.save_or_locate(gestion_localidad_380)

    gestion_localidad_381 = Localidad()
    gestion_localidad_381.cod_postal = '2413'
    gestion_localidad_381.localidad = 'COLONIA PRODAMONTE'
    gestion_localidad_381.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_381 = importer.save_or_locate(gestion_localidad_381)

    gestion_localidad_382 = Localidad()
    gestion_localidad_382.cod_postal = '2645'
    gestion_localidad_382.localidad = 'COLONIA PROGRESO'
    gestion_localidad_382.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_382 = importer.save_or_locate(gestion_localidad_382)

    gestion_localidad_383 = Localidad()
    gestion_localidad_383.cod_postal = '2423'
    gestion_localidad_383.localidad = 'COLONIA PROSPERIDAD'
    gestion_localidad_383.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_383 = importer.save_or_locate(gestion_localidad_383)

    gestion_localidad_384 = Localidad()
    gestion_localidad_384.cod_postal = '2436'
    gestion_localidad_384.localidad = 'COLONIAS'
    gestion_localidad_384.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_384 = importer.save_or_locate(gestion_localidad_384)

    gestion_localidad_385 = Localidad()
    gestion_localidad_385.cod_postal = '5125'
    gestion_localidad_385.localidad = 'COLONIA SAGRADA FAMILIA'
    gestion_localidad_385.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_385 = importer.save_or_locate(gestion_localidad_385)

    gestion_localidad_386 = Localidad()
    gestion_localidad_386.cod_postal = '2426'
    gestion_localidad_386.localidad = 'COLONIA SAN BARTOLOME'
    gestion_localidad_386.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_386 = importer.save_or_locate(gestion_localidad_386)

    gestion_localidad_387 = Localidad()
    gestion_localidad_387.cod_postal = '5189'
    gestion_localidad_387.localidad = 'COLONIA SAN IGNACIO'
    gestion_localidad_387.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_387 = importer.save_or_locate(gestion_localidad_387)

    gestion_localidad_388 = Localidad()
    gestion_localidad_388.cod_postal = '5189'
    gestion_localidad_388.localidad = 'COLONIA SAN ISIDRO'
    gestion_localidad_388.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_388 = importer.save_or_locate(gestion_localidad_388)

    gestion_localidad_389 = Localidad()
    gestion_localidad_389.cod_postal = '2421'
    gestion_localidad_389.localidad = 'COLONIA SAN PEDRO'
    gestion_localidad_389.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_389 = importer.save_or_locate(gestion_localidad_389)

    gestion_localidad_390 = Localidad()
    gestion_localidad_390.cod_postal = '2433'
    gestion_localidad_390.localidad = 'COLONIA SAN RAFAEL'
    gestion_localidad_390.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_390 = importer.save_or_locate(gestion_localidad_390)

    gestion_localidad_391 = Localidad()
    gestion_localidad_391.cod_postal = '6123'
    gestion_localidad_391.localidad = 'COLONIA SANTA ANA'
    gestion_localidad_391.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_391 = importer.save_or_locate(gestion_localidad_391)

    gestion_localidad_392 = Localidad()
    gestion_localidad_392.cod_postal = '5851'
    gestion_localidad_392.localidad = 'COLONIA SANTA CATALINA'
    gestion_localidad_392.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_392 = importer.save_or_locate(gestion_localidad_392)

    gestion_localidad_393 = Localidad()
    gestion_localidad_393.cod_postal = '5933'
    gestion_localidad_393.localidad = 'COLONIA SANTA MARGARITA'
    gestion_localidad_393.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_393 = importer.save_or_locate(gestion_localidad_393)

    gestion_localidad_394 = Localidad()
    gestion_localidad_394.cod_postal = '2423'
    gestion_localidad_394.localidad = 'COLONIA SANTA MARIA'
    gestion_localidad_394.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_394 = importer.save_or_locate(gestion_localidad_394)

    gestion_localidad_395 = Localidad()
    gestion_localidad_395.cod_postal = '5805'
    gestion_localidad_395.localidad = 'COLONIA SANTA PAULA'
    gestion_localidad_395.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_395 = importer.save_or_locate(gestion_localidad_395)

    gestion_localidad_396 = Localidad()
    gestion_localidad_396.cod_postal = '5936'
    gestion_localidad_396.localidad = 'COLONIA SANTA RITA'
    gestion_localidad_396.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_396 = importer.save_or_locate(gestion_localidad_396)

    gestion_localidad_397 = Localidad()
    gestion_localidad_397.cod_postal = '2411'
    gestion_localidad_397.localidad = 'COLONIA SANTA RITA'
    gestion_localidad_397.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_397 = importer.save_or_locate(gestion_localidad_397)

    gestion_localidad_398 = Localidad()
    gestion_localidad_398.cod_postal = '5907'
    gestion_localidad_398.localidad = 'COLONIA SILVIO PELLICO'
    gestion_localidad_398.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_398 = importer.save_or_locate(gestion_localidad_398)

    gestion_localidad_399 = Localidad()
    gestion_localidad_399.cod_postal = '2421'
    gestion_localidad_399.localidad = 'COLONIA TACURALES'
    gestion_localidad_399.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_399 = importer.save_or_locate(gestion_localidad_399)

    gestion_localidad_400 = Localidad()
    gestion_localidad_400.cod_postal = '5101'
    gestion_localidad_400.localidad = 'COLONIA TIROLESA'
    gestion_localidad_400.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_400 = importer.save_or_locate(gestion_localidad_400)

    gestion_localidad_401 = Localidad()
    gestion_localidad_401.cod_postal = '5139'
    gestion_localidad_401.localidad = 'COLONIA TORO PUJIO'
    gestion_localidad_401.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_401 = importer.save_or_locate(gestion_localidad_401)

    gestion_localidad_402 = Localidad()
    gestion_localidad_402.cod_postal = '2417'
    gestion_localidad_402.localidad = 'COLONIA UDINE'
    gestion_localidad_402.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_402 = importer.save_or_locate(gestion_localidad_402)

    gestion_localidad_403 = Localidad()
    gestion_localidad_403.cod_postal = '6121'
    gestion_localidad_403.localidad = 'COLONIA VALLE GRANDE'
    gestion_localidad_403.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_403 = importer.save_or_locate(gestion_localidad_403)

    gestion_localidad_404 = Localidad()
    gestion_localidad_404.cod_postal = '2413'
    gestion_localidad_404.localidad = 'COLONIA VALTELINA'
    gestion_localidad_404.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_404 = importer.save_or_locate(gestion_localidad_404)

    gestion_localidad_405 = Localidad()
    gestion_localidad_405.cod_postal = '2592'
    gestion_localidad_405.localidad = 'COLONIA VEINTICINCO'
    gestion_localidad_405.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_405 = importer.save_or_locate(gestion_localidad_405)

    gestion_localidad_406 = Localidad()
    gestion_localidad_406.cod_postal = '5221'
    gestion_localidad_406.localidad = 'COLONIA VICENTE AGUERO'
    gestion_localidad_406.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_406 = importer.save_or_locate(gestion_localidad_406)

    gestion_localidad_407 = Localidad()
    gestion_localidad_407.cod_postal = '5865'
    gestion_localidad_407.localidad = 'COLONIA VIDELA'
    gestion_localidad_407.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_407 = importer.save_or_locate(gestion_localidad_407)

    gestion_localidad_408 = Localidad()
    gestion_localidad_408.cod_postal = '2419'
    gestion_localidad_408.localidad = 'COLONIA VIGNAUD'
    gestion_localidad_408.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_408 = importer.save_or_locate(gestion_localidad_408)

    gestion_localidad_409 = Localidad()
    gestion_localidad_409.cod_postal = '5137'
    gestion_localidad_409.localidad = 'COLONIA YARETA'
    gestion_localidad_409.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_409 = importer.save_or_locate(gestion_localidad_409)

    gestion_localidad_410 = Localidad()
    gestion_localidad_410.cod_postal = '5917'
    gestion_localidad_410.localidad = 'COLONIA YUCAT SUD'
    gestion_localidad_410.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_410 = importer.save_or_locate(gestion_localidad_410)

    gestion_localidad_411 = Localidad()
    gestion_localidad_411.cod_postal = '5220'
    gestion_localidad_411.localidad = 'COLUMBO'
    gestion_localidad_411.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_411 = importer.save_or_locate(gestion_localidad_411)

    gestion_localidad_412 = Localidad()
    gestion_localidad_412.cod_postal = '5129'
    gestion_localidad_412.localidad = 'COMECHINGONES'
    gestion_localidad_412.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_412 = importer.save_or_locate(gestion_localidad_412)

    gestion_localidad_413 = Localidad()
    gestion_localidad_413.cod_postal = '5153'
    gestion_localidad_413.localidad = 'COMECHINGONES'
    gestion_localidad_413.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_413 = importer.save_or_locate(gestion_localidad_413)

    gestion_localidad_414 = Localidad()
    gestion_localidad_414.cod_postal = '5875'
    gestion_localidad_414.localidad = 'COME TIERRA'
    gestion_localidad_414.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_414 = importer.save_or_locate(gestion_localidad_414)

    gestion_localidad_415 = Localidad()
    gestion_localidad_415.cod_postal = '5871'
    gestion_localidad_415.localidad = 'CONCEPCION'
    gestion_localidad_415.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_415 = importer.save_or_locate(gestion_localidad_415)

    gestion_localidad_416 = Localidad()
    gestion_localidad_416.cod_postal = '5871'
    gestion_localidad_416.localidad = 'CONDOR HUASI'
    gestion_localidad_416.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_416 = importer.save_or_locate(gestion_localidad_416)

    gestion_localidad_417 = Localidad()
    gestion_localidad_417.cod_postal = '5873'
    gestion_localidad_417.localidad = 'CONLARA'
    gestion_localidad_417.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_417 = importer.save_or_locate(gestion_localidad_417)

    gestion_localidad_418 = Localidad()
    gestion_localidad_418.cod_postal = '5125'
    gestion_localidad_418.localidad = 'CONSTITUCION'
    gestion_localidad_418.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_418 = importer.save_or_locate(gestion_localidad_418)

    gestion_localidad_419 = Localidad()
    gestion_localidad_419.cod_postal = '5201'
    gestion_localidad_419.localidad = 'COPACABANA'
    gestion_localidad_419.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_419 = importer.save_or_locate(gestion_localidad_419)

    gestion_localidad_420 = Localidad()
    gestion_localidad_420.cod_postal = '5153'
    gestion_localidad_420.localidad = 'COPINA'
    gestion_localidad_420.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_420 = importer.save_or_locate(gestion_localidad_420)

    gestion_localidad_421 = Localidad()
    gestion_localidad_421.cod_postal = '5000'
    gestion_localidad_421.localidad = 'CORDOBA'
    gestion_localidad_421.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_421 = importer.save_or_locate(gestion_localidad_421)

    gestion_localidad_422 = Localidad()
    gestion_localidad_422.cod_postal = '5184'
    gestion_localidad_422.localidad = 'CORIMAYO'
    gestion_localidad_422.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_422 = importer.save_or_locate(gestion_localidad_422)

    gestion_localidad_423 = Localidad()
    gestion_localidad_423.cod_postal = '5200'
    gestion_localidad_423.localidad = 'CORITO'
    gestion_localidad_423.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_423 = importer.save_or_locate(gestion_localidad_423)

    gestion_localidad_424 = Localidad()
    gestion_localidad_424.cod_postal = '5811'
    gestion_localidad_424.localidad = 'CORONEL BAIGORRIA'
    gestion_localidad_424.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_424 = importer.save_or_locate(gestion_localidad_424)

    gestion_localidad_425 = Localidad()
    gestion_localidad_425.cod_postal = '5847'
    gestion_localidad_425.localidad = 'CORONEL MOLDES'
    gestion_localidad_425.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_425 = importer.save_or_locate(gestion_localidad_425)

    gestion_localidad_426 = Localidad()
    gestion_localidad_426.cod_postal = '5221'
    gestion_localidad_426.localidad = 'CORRAL DE BARRANCA'
    gestion_localidad_426.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_426 = importer.save_or_locate(gestion_localidad_426)

    gestion_localidad_427 = Localidad()
    gestion_localidad_427.cod_postal = '2645'
    gestion_localidad_427.localidad = 'CORRAL DE BUSTOS'
    gestion_localidad_427.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_427 = importer.save_or_locate(gestion_localidad_427)

    gestion_localidad_428 = Localidad()
    gestion_localidad_428.cod_postal = '5870'
    gestion_localidad_428.localidad = 'CORRAL DE CABALLOS'
    gestion_localidad_428.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_428 = importer.save_or_locate(gestion_localidad_428)

    gestion_localidad_429 = Localidad()
    gestion_localidad_429.cod_postal = '5135'
    gestion_localidad_429.localidad = 'CORRAL DE GOMEZ'
    gestion_localidad_429.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_429 = importer.save_or_locate(gestion_localidad_429)

    gestion_localidad_430 = Localidad()
    gestion_localidad_430.cod_postal = '5139'
    gestion_localidad_430.localidad = 'CORRAL DE GOMEZ'
    gestion_localidad_430.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_430 = importer.save_or_locate(gestion_localidad_430)

    gestion_localidad_431 = Localidad()
    gestion_localidad_431.cod_postal = '5940'
    gestion_localidad_431.localidad = 'CORRAL DE GUARDIA'
    gestion_localidad_431.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_431 = importer.save_or_locate(gestion_localidad_431)

    gestion_localidad_432 = Localidad()
    gestion_localidad_432.cod_postal = '5913'
    gestion_localidad_432.localidad = 'CORRAL DEL BAJO'
    gestion_localidad_432.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_432 = importer.save_or_locate(gestion_localidad_432)

    gestion_localidad_433 = Localidad()
    gestion_localidad_433.cod_postal = '5249'
    gestion_localidad_433.localidad = 'CORRAL DEL REY'
    gestion_localidad_433.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_433 = importer.save_or_locate(gestion_localidad_433)

    gestion_localidad_434 = Localidad()
    gestion_localidad_434.cod_postal = '5945'
    gestion_localidad_434.localidad = 'CORRAL DE MULAS'
    gestion_localidad_434.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_434 = importer.save_or_locate(gestion_localidad_434)

    gestion_localidad_435 = Localidad()
    gestion_localidad_435.cod_postal = '5853'
    gestion_localidad_435.localidad = 'CORRALITO'
    gestion_localidad_435.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_435 = importer.save_or_locate(gestion_localidad_435)

    gestion_localidad_436 = Localidad()
    gestion_localidad_436.cod_postal = '5879'
    gestion_localidad_436.localidad = 'CORRALITO SAN JAVIER'
    gestion_localidad_436.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_436 = importer.save_or_locate(gestion_localidad_436)

    gestion_localidad_437 = Localidad()
    gestion_localidad_437.cod_postal = '5246'
    gestion_localidad_437.localidad = 'CORRAL VIEJO'
    gestion_localidad_437.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_437 = importer.save_or_locate(gestion_localidad_437)

    gestion_localidad_438 = Localidad()
    gestion_localidad_438.cod_postal = '2661'
    gestion_localidad_438.localidad = 'CORTADERAS'
    gestion_localidad_438.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_438 = importer.save_or_locate(gestion_localidad_438)

    gestion_localidad_439 = Localidad()
    gestion_localidad_439.cod_postal = '5166'
    gestion_localidad_439.localidad = 'COSQUIN'
    gestion_localidad_439.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_439 = importer.save_or_locate(gestion_localidad_439)

    gestion_localidad_440 = Localidad()
    gestion_localidad_440.cod_postal = '5963'
    gestion_localidad_440.localidad = 'COSTA ALEGRE'
    gestion_localidad_440.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_440 = importer.save_or_locate(gestion_localidad_440)

    gestion_localidad_441 = Localidad()
    gestion_localidad_441.cod_postal = '5137'
    gestion_localidad_441.localidad = 'COSTA DEL CASTAÑO'
    gestion_localidad_441.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_441 = importer.save_or_locate(gestion_localidad_441)

    gestion_localidad_442 = Localidad()
    gestion_localidad_442.cod_postal = '6271'
    gestion_localidad_442.localidad = 'COSTA DEL RIO QUINTO'
    gestion_localidad_442.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_442 = importer.save_or_locate(gestion_localidad_442)

    gestion_localidad_443 = Localidad()
    gestion_localidad_443.cod_postal = '5801'
    gestion_localidad_443.localidad = 'COSTA DEL TAMBO'
    gestion_localidad_443.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_443 = importer.save_or_locate(gestion_localidad_443)

    gestion_localidad_444 = Localidad()
    gestion_localidad_444.cod_postal = '5961'
    gestion_localidad_444.localidad = 'COSTA SACATE'
    gestion_localidad_444.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_444 = importer.save_or_locate(gestion_localidad_444)

    gestion_localidad_445 = Localidad()
    gestion_localidad_445.cod_postal = '2419'
    gestion_localidad_445.localidad = 'COTAGAITA'
    gestion_localidad_445.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_445 = importer.save_or_locate(gestion_localidad_445)

    gestion_localidad_446 = Localidad()
    gestion_localidad_446.cod_postal = '2424'
    gestion_localidad_446.localidad = 'CRISTINA'
    gestion_localidad_446.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_446 = importer.save_or_locate(gestion_localidad_446)

    gestion_localidad_447 = Localidad()
    gestion_localidad_447.cod_postal = '2189'
    gestion_localidad_447.localidad = 'CRUZ ALTA'
    gestion_localidad_447.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_447 = importer.save_or_locate(gestion_localidad_447)

    gestion_localidad_448 = Localidad()
    gestion_localidad_448.cod_postal = '5178'
    gestion_localidad_448.localidad = 'CRUZ CHICA'
    gestion_localidad_448.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_448 = importer.save_or_locate(gestion_localidad_448)

    gestion_localidad_449 = Localidad()
    gestion_localidad_449.cod_postal = '5287'
    gestion_localidad_449.localidad = 'CRUZ DE CAÑA'
    gestion_localidad_449.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_449 = importer.save_or_locate(gestion_localidad_449)

    gestion_localidad_450 = Localidad()
    gestion_localidad_450.cod_postal = '5875'
    gestion_localidad_450.localidad = 'CRUZ DE CAÑA'
    gestion_localidad_450.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_450 = importer.save_or_locate(gestion_localidad_450)

    gestion_localidad_451 = Localidad()
    gestion_localidad_451.cod_postal = '5280'
    gestion_localidad_451.localidad = 'CRUZ DEL EJE'
    gestion_localidad_451.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_451 = importer.save_or_locate(gestion_localidad_451)

    gestion_localidad_452 = Localidad()
    gestion_localidad_452.cod_postal = '5221'
    gestion_localidad_452.localidad = 'CRUZ DEL QUEMADO'
    gestion_localidad_452.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_452 = importer.save_or_locate(gestion_localidad_452)

    gestion_localidad_453 = Localidad()
    gestion_localidad_453.cod_postal = '5212'
    gestion_localidad_453.localidad = 'CRUZ MOJADA'
    gestion_localidad_453.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_453 = importer.save_or_locate(gestion_localidad_453)

    gestion_localidad_454 = Localidad()
    gestion_localidad_454.cod_postal = '2551'
    gestion_localidad_454.localidad = 'CUATRO CAMINOS'
    gestion_localidad_454.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_454 = importer.save_or_locate(gestion_localidad_454)

    gestion_localidad_455 = Localidad()
    gestion_localidad_455.cod_postal = '5801'
    gestion_localidad_455.localidad = 'CUATRO VIENTOS'
    gestion_localidad_455.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_455 = importer.save_or_locate(gestion_localidad_455)

    gestion_localidad_456 = Localidad()
    gestion_localidad_456.cod_postal = '5155'
    gestion_localidad_456.localidad = 'CUCHILLA NEVADA'
    gestion_localidad_456.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_456 = importer.save_or_locate(gestion_localidad_456)

    gestion_localidad_457 = Localidad()
    gestion_localidad_457.cod_postal = '5295'
    gestion_localidad_457.localidad = 'CUCHILLO YACO'
    gestion_localidad_457.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_457 = importer.save_or_locate(gestion_localidad_457)

    gestion_localidad_458 = Localidad()
    gestion_localidad_458.cod_postal = '5153'
    gestion_localidad_458.localidad = 'CUESTA BLANCA'
    gestion_localidad_458.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_458 = importer.save_or_locate(gestion_localidad_458)

    gestion_localidad_459 = Localidad()
    gestion_localidad_459.cod_postal = '6120'
    gestion_localidad_459.localidad = 'CURAPALIGUE'
    gestion_localidad_459.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_459 = importer.save_or_locate(gestion_localidad_459)

    gestion_localidad_460 = Localidad()
    gestion_localidad_460.cod_postal = '5919'
    gestion_localidad_460.localidad = 'DALMACIO VELEZ SARSFIELD'
    gestion_localidad_460.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_460 = importer.save_or_locate(gestion_localidad_460)

    gestion_localidad_461 = Localidad()
    gestion_localidad_461.cod_postal = '5200'
    gestion_localidad_461.localidad = 'DEAN FUNES'
    gestion_localidad_461.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_461 = importer.save_or_locate(gestion_localidad_461)

    gestion_localidad_462 = Localidad()
    gestion_localidad_462.cod_postal = '6271'
    gestion_localidad_462.localidad = 'DE LA SERNA'
    gestion_localidad_462.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_462 = importer.save_or_locate(gestion_localidad_462)

    gestion_localidad_463 = Localidad()
    gestion_localidad_463.cod_postal = '6271'
    gestion_localidad_463.localidad = 'DEL CAMPILLO'
    gestion_localidad_463.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_463 = importer.save_or_locate(gestion_localidad_463)

    gestion_localidad_464 = Localidad()
    gestion_localidad_464.cod_postal = '2684'
    gestion_localidad_464.localidad = 'DEMARCHI'
    gestion_localidad_464.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_464 = importer.save_or_locate(gestion_localidad_464)

    gestion_localidad_465 = Localidad()
    gestion_localidad_465.cod_postal = '5284'
    gestion_localidad_465.localidad = 'DESAGUADERO'
    gestion_localidad_465.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_465 = importer.save_or_locate(gestion_localidad_465)

    gestion_localidad_466 = Localidad()
    gestion_localidad_466.cod_postal = '5121'
    gestion_localidad_466.localidad = 'DESPEÑADEROS'
    gestion_localidad_466.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_466 = importer.save_or_locate(gestion_localidad_466)

    gestion_localidad_467 = Localidad()
    gestion_localidad_467.cod_postal = '5229'
    gestion_localidad_467.localidad = 'DESVIO CHALACEA'
    gestion_localidad_467.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_467 = importer.save_or_locate(gestion_localidad_467)

    gestion_localidad_468 = Localidad()
    gestion_localidad_468.cod_postal = '5299'
    gestion_localidad_468.localidad = 'DESVIO EL VOLCAN'
    gestion_localidad_468.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_468 = importer.save_or_locate(gestion_localidad_468)

    gestion_localidad_469 = Localidad()
    gestion_localidad_469.cod_postal = '2625'
    gestion_localidad_469.localidad = 'DESVIO KILOMETRO 57'
    gestion_localidad_469.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_469 = importer.save_or_locate(gestion_localidad_469)

    gestion_localidad_470 = Localidad()
    gestion_localidad_470.cod_postal = '2424'
    gestion_localidad_470.localidad = 'DEVOTO'
    gestion_localidad_470.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_470 = importer.save_or_locate(gestion_localidad_470)

    gestion_localidad_471 = Localidad()
    gestion_localidad_471.cod_postal = '5135'
    gestion_localidad_471.localidad = 'DIEGO DE ROJAS'
    gestion_localidad_471.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_471 = importer.save_or_locate(gestion_localidad_471)

    gestion_localidad_472 = Localidad()
    gestion_localidad_472.cod_postal = '5875'
    gestion_localidad_472.localidad = 'DIEZ RIOS'
    gestion_localidad_472.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_472 = importer.save_or_locate(gestion_localidad_472)

    gestion_localidad_473 = Localidad()
    gestion_localidad_473.cod_postal = '5189'
    gestion_localidad_473.localidad = 'DIQUE CHICO'
    gestion_localidad_473.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_473 = importer.save_or_locate(gestion_localidad_473)

    gestion_localidad_474 = Localidad()
    gestion_localidad_474.cod_postal = '5168'
    gestion_localidad_474.localidad = 'DIQUE LAS VAQUERIAS'
    gestion_localidad_474.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_474 = importer.save_or_locate(gestion_localidad_474)

    gestion_localidad_475 = Localidad()
    gestion_localidad_475.cod_postal = '5885'
    gestion_localidad_475.localidad = 'DIQUE LA VIÑA'
    gestion_localidad_475.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_475 = importer.save_or_locate(gestion_localidad_475)

    gestion_localidad_476 = Localidad()
    gestion_localidad_476.cod_postal = '5192'
    gestion_localidad_476.localidad = 'DIQUE LOS MOLINOS'
    gestion_localidad_476.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_476 = importer.save_or_locate(gestion_localidad_476)

    gestion_localidad_477 = Localidad()
    gestion_localidad_477.cod_postal = '5149'
    gestion_localidad_477.localidad = 'DIQUE SAN ROQUE'
    gestion_localidad_477.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_477 = importer.save_or_locate(gestion_localidad_477)

    gestion_localidad_478 = Localidad()
    gestion_localidad_478.cod_postal = '5221'
    gestion_localidad_478.localidad = 'DOCTOR NICASIO SALAS OROÑO'
    gestion_localidad_478.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_478 = importer.save_or_locate(gestion_localidad_478)

    gestion_localidad_479 = Localidad()
    gestion_localidad_479.cod_postal = '5131'
    gestion_localidad_479.localidad = 'DOLORES NUÑEZ DEL PRADO'
    gestion_localidad_479.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_479 = importer.save_or_locate(gestion_localidad_479)

    gestion_localidad_480 = Localidad()
    gestion_localidad_480.cod_postal = '5182'
    gestion_localidad_480.localidad = 'DOLORES SAN ESTEBAN'
    gestion_localidad_480.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_480 = importer.save_or_locate(gestion_localidad_480)

    gestion_localidad_481 = Localidad()
    gestion_localidad_481.cod_postal = '5164'
    gestion_localidad_481.localidad = 'DOMINGO FUNES'
    gestion_localidad_481.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_481 = importer.save_or_locate(gestion_localidad_481)

    gestion_localidad_482 = Localidad()
    gestion_localidad_482.cod_postal = '5189'
    gestion_localidad_482.localidad = 'DOS ARROYOS'
    gestion_localidad_482.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_482 = importer.save_or_locate(gestion_localidad_482)

    gestion_localidad_483 = Localidad()
    gestion_localidad_483.cod_postal = '5813'
    gestion_localidad_483.localidad = 'DOS LAGUNAS'
    gestion_localidad_483.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_483 = importer.save_or_locate(gestion_localidad_483)

    gestion_localidad_484 = Localidad()
    gestion_localidad_484.cod_postal = '5155'
    gestion_localidad_484.localidad = 'DOS RIOS'
    gestion_localidad_484.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_484 = importer.save_or_locate(gestion_localidad_484)

    gestion_localidad_485 = Localidad()
    gestion_localidad_485.cod_postal = '5297'
    gestion_localidad_485.localidad = 'DOS RIOS'
    gestion_localidad_485.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_485 = importer.save_or_locate(gestion_localidad_485)

    gestion_localidad_486 = Localidad()
    gestion_localidad_486.cod_postal = '2349'
    gestion_localidad_486.localidad = 'DOS ROSAS'
    gestion_localidad_486.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_486 = importer.save_or_locate(gestion_localidad_486)

    gestion_localidad_487 = Localidad()
    gestion_localidad_487.cod_postal = '5119'
    gestion_localidad_487.localidad = 'DUARTE QUIROS'
    gestion_localidad_487.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_487 = importer.save_or_locate(gestion_localidad_487)

    gestion_localidad_488 = Localidad()
    gestion_localidad_488.cod_postal = '5149'
    gestion_localidad_488.localidad = 'DUMESNIL'
    gestion_localidad_488.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_488 = importer.save_or_locate(gestion_localidad_488)

    gestion_localidad_489 = Localidad()
    gestion_localidad_489.cod_postal = '5244'
    gestion_localidad_489.localidad = 'DURAZNO'
    gestion_localidad_489.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_489 = importer.save_or_locate(gestion_localidad_489)

    gestion_localidad_490 = Localidad()
    gestion_localidad_490.cod_postal = '5184'
    gestion_localidad_490.localidad = 'EL AGUILA BLANCA'
    gestion_localidad_490.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_490 = importer.save_or_locate(gestion_localidad_490)

    gestion_localidad_491 = Localidad()
    gestion_localidad_491.cod_postal = '5131'
    gestion_localidad_491.localidad = 'EL ALCALDE'
    gestion_localidad_491.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_491 = importer.save_or_locate(gestion_localidad_491)

    gestion_localidad_492 = Localidad()
    gestion_localidad_492.cod_postal = '5885'
    gestion_localidad_492.localidad = 'EL ALGADOBAL'
    gestion_localidad_492.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_492 = importer.save_or_locate(gestion_localidad_492)

    gestion_localidad_493 = Localidad()
    gestion_localidad_493.cod_postal = '5249'
    gestion_localidad_493.localidad = 'EL ALGARROBAL'
    gestion_localidad_493.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_493 = importer.save_or_locate(gestion_localidad_493)

    gestion_localidad_494 = Localidad()
    gestion_localidad_494.cod_postal = '5221'
    gestion_localidad_494.localidad = 'EL ALGARROBO'
    gestion_localidad_494.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_494 = importer.save_or_locate(gestion_localidad_494)

    gestion_localidad_495 = Localidad()
    gestion_localidad_495.cod_postal = '5107'
    gestion_localidad_495.localidad = 'EL ALGODONAL'
    gestion_localidad_495.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_495 = importer.save_or_locate(gestion_localidad_495)

    gestion_localidad_496 = Localidad()
    gestion_localidad_496.cod_postal = '5885'
    gestion_localidad_496.localidad = 'EL ALTO'
    gestion_localidad_496.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_496 = importer.save_or_locate(gestion_localidad_496)

    gestion_localidad_497 = Localidad()
    gestion_localidad_497.cod_postal = '5887'
    gestion_localidad_497.localidad = 'EL ALTO'
    gestion_localidad_497.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_497 = importer.save_or_locate(gestion_localidad_497)

    gestion_localidad_498 = Localidad()
    gestion_localidad_498.cod_postal = '5947'
    gestion_localidad_498.localidad = 'EL ARAÑADO'
    gestion_localidad_498.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_498 = importer.save_or_locate(gestion_localidad_498)

    gestion_localidad_499 = Localidad()
    gestion_localidad_499.cod_postal = '6127'
    gestion_localidad_499.localidad = 'EL ARBOL'
    gestion_localidad_499.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_499 = importer.save_or_locate(gestion_localidad_499)

    gestion_localidad_500 = Localidad()
    gestion_localidad_500.cod_postal = '5137'
    gestion_localidad_500.localidad = 'EL BAGUAL'
    gestion_localidad_500.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_500 = importer.save_or_locate(gestion_localidad_500)

    gestion_localidad_501 = Localidad()
    gestion_localidad_501.cod_postal = '5889'
    gestion_localidad_501.localidad = 'EL BAJO'
    gestion_localidad_501.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_501 = importer.save_or_locate(gestion_localidad_501)

    gestion_localidad_502 = Localidad()
    gestion_localidad_502.cod_postal = '5870'
    gestion_localidad_502.localidad = 'EL BALDECITO'
    gestion_localidad_502.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_502 = importer.save_or_locate(gestion_localidad_502)

    gestion_localidad_503 = Localidad()
    gestion_localidad_503.cod_postal = '5182'
    gestion_localidad_503.localidad = 'EL BALDECITO'
    gestion_localidad_503.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_503 = importer.save_or_locate(gestion_localidad_503)

    gestion_localidad_504 = Localidad()
    gestion_localidad_504.cod_postal = '5214'
    gestion_localidad_504.localidad = 'EL BAÑADO'
    gestion_localidad_504.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_504 = importer.save_or_locate(gestion_localidad_504)

    gestion_localidad_505 = Localidad()
    gestion_localidad_505.cod_postal = '5244'
    gestion_localidad_505.localidad = 'EL BAÑADO'
    gestion_localidad_505.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_505 = importer.save_or_locate(gestion_localidad_505)

    gestion_localidad_506 = Localidad()
    gestion_localidad_506.cod_postal = '5248'
    gestion_localidad_506.localidad = 'EL BAÑADO'
    gestion_localidad_506.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_506 = importer.save_or_locate(gestion_localidad_506)

    gestion_localidad_507 = Localidad()
    gestion_localidad_507.cod_postal = '5801'
    gestion_localidad_507.localidad = 'EL BAÑADO'
    gestion_localidad_507.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_507 = importer.save_or_locate(gestion_localidad_507)

    gestion_localidad_508 = Localidad()
    gestion_localidad_508.cod_postal = '5270'
    gestion_localidad_508.localidad = 'EL BARREAL'
    gestion_localidad_508.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_508 = importer.save_or_locate(gestion_localidad_508)

    gestion_localidad_509 = Localidad()
    gestion_localidad_509.cod_postal = '5813'
    gestion_localidad_509.localidad = 'EL BARREAL'
    gestion_localidad_509.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_509 = importer.save_or_locate(gestion_localidad_509)

    gestion_localidad_510 = Localidad()
    gestion_localidad_510.cod_postal = '5285'
    gestion_localidad_510.localidad = 'EL BARRIAL'
    gestion_localidad_510.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_510 = importer.save_or_locate(gestion_localidad_510)

    gestion_localidad_511 = Localidad()
    gestion_localidad_511.cod_postal = '5871'
    gestion_localidad_511.localidad = 'EL BORDO'
    gestion_localidad_511.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_511 = importer.save_or_locate(gestion_localidad_511)

    gestion_localidad_512 = Localidad()
    gestion_localidad_512.cod_postal = '5229'
    gestion_localidad_512.localidad = 'EL BOSQUE'
    gestion_localidad_512.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_512 = importer.save_or_locate(gestion_localidad_512)

    gestion_localidad_513 = Localidad()
    gestion_localidad_513.cod_postal = '5281'
    gestion_localidad_513.localidad = 'EL BRETE'
    gestion_localidad_513.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_513 = importer.save_or_locate(gestion_localidad_513)

    gestion_localidad_514 = Localidad()
    gestion_localidad_514.cod_postal = '5172'
    gestion_localidad_514.localidad = 'EL CALLEJON'
    gestion_localidad_514.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_514 = importer.save_or_locate(gestion_localidad_514)

    gestion_localidad_515 = Localidad()
    gestion_localidad_515.cod_postal = '5821'
    gestion_localidad_515.localidad = 'EL CANO'
    gestion_localidad_515.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_515 = importer.save_or_locate(gestion_localidad_515)

    gestion_localidad_516 = Localidad()
    gestion_localidad_516.cod_postal = '5284'
    gestion_localidad_516.localidad = 'EL CARACOL'
    gestion_localidad_516.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_516 = importer.save_or_locate(gestion_localidad_516)

    gestion_localidad_517 = Localidad()
    gestion_localidad_517.cod_postal = '2550'
    gestion_localidad_517.localidad = 'EL CARMEN'
    gestion_localidad_517.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_517 = importer.save_or_locate(gestion_localidad_517)

    gestion_localidad_518 = Localidad()
    gestion_localidad_518.cod_postal = '5197'
    gestion_localidad_518.localidad = 'EL CARMEN'
    gestion_localidad_518.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_518 = importer.save_or_locate(gestion_localidad_518)

    gestion_localidad_519 = Localidad()
    gestion_localidad_519.cod_postal = '5145'
    gestion_localidad_519.localidad = 'EL CARMEN GUIÑAZU'
    gestion_localidad_519.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_519 = importer.save_or_locate(gestion_localidad_519)

    gestion_localidad_520 = Localidad()
    gestion_localidad_520.cod_postal = '5963'
    gestion_localidad_520.localidad = 'EL CARRILITO'
    gestion_localidad_520.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_520 = importer.save_or_locate(gestion_localidad_520)

    gestion_localidad_521 = Localidad()
    gestion_localidad_521.cod_postal = '5135'
    gestion_localidad_521.localidad = 'EL CARRIZAL'
    gestion_localidad_521.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_521 = importer.save_or_locate(gestion_localidad_521)

    gestion_localidad_522 = Localidad()
    gestion_localidad_522.cod_postal = '5282'
    gestion_localidad_522.localidad = 'EL CARRIZAL'
    gestion_localidad_522.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_522 = importer.save_or_locate(gestion_localidad_522)

    gestion_localidad_523 = Localidad()
    gestion_localidad_523.cod_postal = '5299'
    gestion_localidad_523.localidad = 'EL CARRIZAL'
    gestion_localidad_523.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_523 = importer.save_or_locate(gestion_localidad_523)

    gestion_localidad_524 = Localidad()
    gestion_localidad_524.cod_postal = '5963'
    gestion_localidad_524.localidad = 'EL CARRIZAL'
    gestion_localidad_524.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_524 = importer.save_or_locate(gestion_localidad_524)

    gestion_localidad_525 = Localidad()
    gestion_localidad_525.cod_postal = '5201'
    gestion_localidad_525.localidad = 'EL CARRIZAL CHUÑAHUASI'
    gestion_localidad_525.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_525 = importer.save_or_locate(gestion_localidad_525)

    gestion_localidad_526 = Localidad()
    gestion_localidad_526.cod_postal = '5205'
    gestion_localidad_526.localidad = 'EL CERRITO'
    gestion_localidad_526.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_526 = importer.save_or_locate(gestion_localidad_526)

    gestion_localidad_527 = Localidad()
    gestion_localidad_527.cod_postal = '5875'
    gestion_localidad_527.localidad = 'EL CERRO'
    gestion_localidad_527.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_527 = importer.save_or_locate(gestion_localidad_527)

    gestion_localidad_528 = Localidad()
    gestion_localidad_528.cod_postal = '5272'
    gestion_localidad_528.localidad = 'EL CHACHO'
    gestion_localidad_528.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_528 = importer.save_or_locate(gestion_localidad_528)

    gestion_localidad_529 = Localidad()
    gestion_localidad_529.cod_postal = '5218'
    gestion_localidad_529.localidad = 'EL CHANCHITO'
    gestion_localidad_529.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_529 = importer.save_or_locate(gestion_localidad_529)

    gestion_localidad_530 = Localidad()
    gestion_localidad_530.cod_postal = '5145'
    gestion_localidad_530.localidad = 'EL CHINGOLO'
    gestion_localidad_530.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_530 = importer.save_or_locate(gestion_localidad_530)

    gestion_localidad_531 = Localidad()
    gestion_localidad_531.cod_postal = '5813'
    gestion_localidad_531.localidad = 'EL CHIQUILLAN'
    gestion_localidad_531.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_531 = importer.save_or_locate(gestion_localidad_531)

    gestion_localidad_532 = Localidad()
    gestion_localidad_532.cod_postal = '5248'
    gestion_localidad_532.localidad = 'EL CORO'
    gestion_localidad_532.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_532 = importer.save_or_locate(gestion_localidad_532)

    gestion_localidad_533 = Localidad()
    gestion_localidad_533.cod_postal = '5212'
    gestion_localidad_533.localidad = 'EL CORO'
    gestion_localidad_533.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_533 = importer.save_or_locate(gestion_localidad_533)

    gestion_localidad_534 = Localidad()
    gestion_localidad_534.cod_postal = '5889'
    gestion_localidad_534.localidad = 'EL CORTE'
    gestion_localidad_534.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_534 = importer.save_or_locate(gestion_localidad_534)

    gestion_localidad_535 = Localidad()
    gestion_localidad_535.cod_postal = '5236'
    gestion_localidad_535.localidad = 'EL CRESTON DE PIEDRA'
    gestion_localidad_535.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_535 = importer.save_or_locate(gestion_localidad_535)

    gestion_localidad_536 = Localidad()
    gestion_localidad_536.cod_postal = '5129'
    gestion_localidad_536.localidad = 'EL CRISPIN'
    gestion_localidad_536.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_536 = importer.save_or_locate(gestion_localidad_536)

    gestion_localidad_537 = Localidad()
    gestion_localidad_537.cod_postal = '5172'
    gestion_localidad_537.localidad = 'EL CUADRADO'
    gestion_localidad_537.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_537 = importer.save_or_locate(gestion_localidad_537)

    gestion_localidad_538 = Localidad()
    gestion_localidad_538.cod_postal = '2434'
    gestion_localidad_538.localidad = 'EL DESCANSO'
    gestion_localidad_538.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_538 = importer.save_or_locate(gestion_localidad_538)

    gestion_localidad_539 = Localidad()
    gestion_localidad_539.cod_postal = '5205'
    gestion_localidad_539.localidad = 'EL DESMONTE'
    gestion_localidad_539.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_539 = importer.save_or_locate(gestion_localidad_539)

    gestion_localidad_540 = Localidad()
    gestion_localidad_540.cod_postal = '5151'
    gestion_localidad_540.localidad = 'EL DIQUECITO'
    gestion_localidad_540.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_540 = importer.save_or_locate(gestion_localidad_540)

    gestion_localidad_541 = Localidad()
    gestion_localidad_541.cod_postal = '5212'
    gestion_localidad_541.localidad = 'EL DIVISADERO'
    gestion_localidad_541.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_541 = importer.save_or_locate(gestion_localidad_541)

    gestion_localidad_542 = Localidad()
    gestion_localidad_542.cod_postal = '2651'
    gestion_localidad_542.localidad = 'EL DORADO'
    gestion_localidad_542.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_542 = importer.save_or_locate(gestion_localidad_542)

    gestion_localidad_543 = Localidad()
    gestion_localidad_543.cod_postal = '5801'
    gestion_localidad_543.localidad = 'EL DURAZNITO'
    gestion_localidad_543.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_543 = importer.save_or_locate(gestion_localidad_543)

    gestion_localidad_544 = Localidad()
    gestion_localidad_544.cod_postal = '5155'
    gestion_localidad_544.localidad = 'EL DURAZNO'
    gestion_localidad_544.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_544 = importer.save_or_locate(gestion_localidad_544)

    gestion_localidad_545 = Localidad()
    gestion_localidad_545.cod_postal = '5231'
    gestion_localidad_545.localidad = 'EL DURAZNO'
    gestion_localidad_545.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_545 = importer.save_or_locate(gestion_localidad_545)

    gestion_localidad_546 = Localidad()
    gestion_localidad_546.cod_postal = '5249'
    gestion_localidad_546.localidad = 'EL DURAZNO'
    gestion_localidad_546.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_546 = importer.save_or_locate(gestion_localidad_546)

    gestion_localidad_547 = Localidad()
    gestion_localidad_547.cod_postal = '5293'
    gestion_localidad_547.localidad = 'EL DURAZNO'
    gestion_localidad_547.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_547 = importer.save_or_locate(gestion_localidad_547)

    gestion_localidad_548 = Localidad()
    gestion_localidad_548.cod_postal = '5815'
    gestion_localidad_548.localidad = 'ELENA'
    gestion_localidad_548.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_548 = importer.save_or_locate(gestion_localidad_548)

    gestion_localidad_549 = Localidad()
    gestion_localidad_549.cod_postal = '5133'
    gestion_localidad_549.localidad = 'EL ESPINAL'
    gestion_localidad_549.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_549 = importer.save_or_locate(gestion_localidad_549)

    gestion_localidad_550 = Localidad()
    gestion_localidad_550.cod_postal = '5813'
    gestion_localidad_550.localidad = 'EL ESPINILLAL'
    gestion_localidad_550.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_550 = importer.save_or_locate(gestion_localidad_550)

    gestion_localidad_551 = Localidad()
    gestion_localidad_551.cod_postal = '5131'
    gestion_localidad_551.localidad = 'EL ESPINILLO'
    gestion_localidad_551.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_551 = importer.save_or_locate(gestion_localidad_551)

    gestion_localidad_552 = Localidad()
    gestion_localidad_552.cod_postal = '5212'
    gestion_localidad_552.localidad = 'EL ESTANQUE'
    gestion_localidad_552.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_552 = importer.save_or_locate(gestion_localidad_552)

    gestion_localidad_553 = Localidad()
    gestion_localidad_553.cod_postal = '5951'
    gestion_localidad_553.localidad = 'EL FLORENTINO'
    gestion_localidad_553.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_553 = importer.save_or_locate(gestion_localidad_553)

    gestion_localidad_554 = Localidad()
    gestion_localidad_554.cod_postal = '2432'
    gestion_localidad_554.localidad = 'EL FLORIDA'
    gestion_localidad_554.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_554 = importer.save_or_locate(gestion_localidad_554)

    gestion_localidad_555 = Localidad()
    gestion_localidad_555.cod_postal = '5951'
    gestion_localidad_555.localidad = 'EL FORTIN'
    gestion_localidad_555.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_555 = importer.save_or_locate(gestion_localidad_555)

    gestion_localidad_556 = Localidad()
    gestion_localidad_556.cod_postal = '5282'
    gestion_localidad_556.localidad = 'EL FRANCES'
    gestion_localidad_556.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_556 = importer.save_or_locate(gestion_localidad_556)

    gestion_localidad_557 = Localidad()
    gestion_localidad_557.cod_postal = '2428'
    gestion_localidad_557.localidad = 'EL FUERTECITO'
    gestion_localidad_557.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_557 = importer.save_or_locate(gestion_localidad_557)

    gestion_localidad_558 = Localidad()
    gestion_localidad_558.cod_postal = '5248'
    gestion_localidad_558.localidad = 'EL GABINO'
    gestion_localidad_558.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_558 = importer.save_or_locate(gestion_localidad_558)

    gestion_localidad_559 = Localidad()
    gestion_localidad_559.cod_postal = '5249'
    gestion_localidad_559.localidad = 'EL GALLEGO'
    gestion_localidad_559.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_559 = importer.save_or_locate(gestion_localidad_559)

    gestion_localidad_560 = Localidad()
    gestion_localidad_560.cod_postal = '5101'
    gestion_localidad_560.localidad = 'EL GATEADO'
    gestion_localidad_560.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_560 = importer.save_or_locate(gestion_localidad_560)

    gestion_localidad_561 = Localidad()
    gestion_localidad_561.cod_postal = '5285'
    gestion_localidad_561.localidad = 'EL GUAICO'
    gestion_localidad_561.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_561 = importer.save_or_locate(gestion_localidad_561)

    gestion_localidad_562 = Localidad()
    gestion_localidad_562.cod_postal = '5231'
    gestion_localidad_562.localidad = 'EL GUANACO'
    gestion_localidad_562.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_562 = importer.save_or_locate(gestion_localidad_562)

    gestion_localidad_563 = Localidad()
    gestion_localidad_563.cod_postal = '5244'
    gestion_localidad_563.localidad = 'EL GUINDO'
    gestion_localidad_563.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_563 = importer.save_or_locate(gestion_localidad_563)

    gestion_localidad_564 = Localidad()
    gestion_localidad_564.cod_postal = '5212'
    gestion_localidad_564.localidad = 'EL IALITA'
    gestion_localidad_564.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_564 = importer.save_or_locate(gestion_localidad_564)

    gestion_localidad_565 = Localidad()
    gestion_localidad_565.cod_postal = '5248'
    gestion_localidad_565.localidad = 'EL JORDAN'
    gestion_localidad_565.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_565 = importer.save_or_locate(gestion_localidad_565)

    gestion_localidad_566 = Localidad()
    gestion_localidad_566.cod_postal = '5218'
    gestion_localidad_566.localidad = 'EL JUME'
    gestion_localidad_566.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_566 = importer.save_or_locate(gestion_localidad_566)

    gestion_localidad_567 = Localidad()
    gestion_localidad_567.cod_postal = '5947'
    gestion_localidad_567.localidad = 'EL JUMIAL'
    gestion_localidad_567.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_567 = importer.save_or_locate(gestion_localidad_567)

    gestion_localidad_568 = Localidad()
    gestion_localidad_568.cod_postal = '5248'
    gestion_localidad_568.localidad = 'EL LAUREL'
    gestion_localidad_568.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_568 = importer.save_or_locate(gestion_localidad_568)

    gestion_localidad_569 = Localidad()
    gestion_localidad_569.cod_postal = '5873'
    gestion_localidad_569.localidad = 'EL MANANTIAL'
    gestion_localidad_569.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_569 = importer.save_or_locate(gestion_localidad_569)

    gestion_localidad_570 = Localidad()
    gestion_localidad_570.cod_postal = '5819'
    gestion_localidad_570.localidad = 'EL MANANTIAL'
    gestion_localidad_570.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_570 = importer.save_or_locate(gestion_localidad_570)

    gestion_localidad_571 = Localidad()
    gestion_localidad_571.cod_postal = '5249'
    gestion_localidad_571.localidad = 'EL MANGRULLO'
    gestion_localidad_571.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_571 = importer.save_or_locate(gestion_localidad_571)

    gestion_localidad_572 = Localidad()
    gestion_localidad_572.cod_postal = '5107'
    gestion_localidad_572.localidad = 'EL MANZANO'
    gestion_localidad_572.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_572 = importer.save_or_locate(gestion_localidad_572)

    gestion_localidad_573 = Localidad()
    gestion_localidad_573.cod_postal = '5871'
    gestion_localidad_573.localidad = 'EL MEDANITO'
    gestion_localidad_573.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_573 = importer.save_or_locate(gestion_localidad_573)

    gestion_localidad_574 = Localidad()
    gestion_localidad_574.cod_postal = '5891'
    gestion_localidad_574.localidad = 'EL MIRADOR'
    gestion_localidad_574.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_574 = importer.save_or_locate(gestion_localidad_574)

    gestion_localidad_575 = Localidad()
    gestion_localidad_575.cod_postal = '5218'
    gestion_localidad_575.localidad = 'EL MOJONCITO'
    gestion_localidad_575.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_575 = importer.save_or_locate(gestion_localidad_575)

    gestion_localidad_576 = Localidad()
    gestion_localidad_576.cod_postal = '5220'
    gestion_localidad_576.localidad = 'EL MOLINO'
    gestion_localidad_576.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_576 = importer.save_or_locate(gestion_localidad_576)

    gestion_localidad_577 = Localidad()
    gestion_localidad_577.cod_postal = '5214'
    gestion_localidad_577.localidad = 'EL MOLINO'
    gestion_localidad_577.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_577 = importer.save_or_locate(gestion_localidad_577)

    gestion_localidad_578 = Localidad()
    gestion_localidad_578.cod_postal = '5272'
    gestion_localidad_578.localidad = 'EL MOYANO'
    gestion_localidad_578.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_578 = importer.save_or_locate(gestion_localidad_578)

    gestion_localidad_579 = Localidad()
    gestion_localidad_579.cod_postal = '6127'
    gestion_localidad_579.localidad = 'EL NOY'
    gestion_localidad_579.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_579 = importer.save_or_locate(gestion_localidad_579)

    gestion_localidad_580 = Localidad()
    gestion_localidad_580.cod_postal = '5123'
    gestion_localidad_580.localidad = 'EL OCHENTA'
    gestion_localidad_580.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_580 = importer.save_or_locate(gestion_localidad_580)

    gestion_localidad_581 = Localidad()
    gestion_localidad_581.cod_postal = '5203'
    gestion_localidad_581.localidad = 'EL OJO DE AGUA'
    gestion_localidad_581.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_581 = importer.save_or_locate(gestion_localidad_581)

    gestion_localidad_582 = Localidad()
    gestion_localidad_582.cod_postal = '2563'
    gestion_localidad_582.localidad = 'EL OVERO'
    gestion_localidad_582.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_582 = importer.save_or_locate(gestion_localidad_582)

    gestion_localidad_583 = Localidad()
    gestion_localidad_583.cod_postal = '6273'
    gestion_localidad_583.localidad = 'EL PAMPERO'
    gestion_localidad_583.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_583 = importer.save_or_locate(gestion_localidad_583)

    gestion_localidad_584 = Localidad()
    gestion_localidad_584.cod_postal = '2580'
    gestion_localidad_584.localidad = 'EL PANAL'
    gestion_localidad_584.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_584 = importer.save_or_locate(gestion_localidad_584)

    gestion_localidad_585 = Localidad()
    gestion_localidad_585.cod_postal = '5885'
    gestion_localidad_585.localidad = 'EL PANTANILLO'
    gestion_localidad_585.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_585 = importer.save_or_locate(gestion_localidad_585)

    gestion_localidad_586 = Localidad()
    gestion_localidad_586.cod_postal = '5246'
    gestion_localidad_586.localidad = 'EL PANTANILLO'
    gestion_localidad_586.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_586 = importer.save_or_locate(gestion_localidad_586)

    gestion_localidad_587 = Localidad()
    gestion_localidad_587.cod_postal = '5244'
    gestion_localidad_587.localidad = 'EL PANTANO'
    gestion_localidad_587.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_587 = importer.save_or_locate(gestion_localidad_587)

    gestion_localidad_588 = Localidad()
    gestion_localidad_588.cod_postal = '5197'
    gestion_localidad_588.localidad = 'EL PARADOR DE LA MONTAÑA'
    gestion_localidad_588.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_588 = importer.save_or_locate(gestion_localidad_588)

    gestion_localidad_589 = Localidad()
    gestion_localidad_589.cod_postal = '2559'
    gestion_localidad_589.localidad = 'EL PARAISO'
    gestion_localidad_589.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_589 = importer.save_or_locate(gestion_localidad_589)

    gestion_localidad_590 = Localidad()
    gestion_localidad_590.cod_postal = '5218'
    gestion_localidad_590.localidad = 'EL PARAISO'
    gestion_localidad_590.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_590 = importer.save_or_locate(gestion_localidad_590)

    gestion_localidad_591 = Localidad()
    gestion_localidad_591.cod_postal = '5203'
    gestion_localidad_591.localidad = 'EL PASO'
    gestion_localidad_591.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_591 = importer.save_or_locate(gestion_localidad_591)

    gestion_localidad_592 = Localidad()
    gestion_localidad_592.cod_postal = '5871'
    gestion_localidad_592.localidad = 'EL PASO DE LA PAMPA'
    gestion_localidad_592.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_592 = importer.save_or_locate(gestion_localidad_592)

    gestion_localidad_593 = Localidad()
    gestion_localidad_593.cod_postal = '5151'
    gestion_localidad_593.localidad = 'EL PASTOR'
    gestion_localidad_593.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_593 = importer.save_or_locate(gestion_localidad_593)

    gestion_localidad_594 = Localidad()
    gestion_localidad_594.cod_postal = '5151'
    gestion_localidad_594.localidad = 'EL PAYADOR'
    gestion_localidad_594.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_594 = importer.save_or_locate(gestion_localidad_594)

    gestion_localidad_595 = Localidad()
    gestion_localidad_595.cod_postal = '5236'
    gestion_localidad_595.localidad = 'EL PEDACITO'
    gestion_localidad_595.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_595 = importer.save_or_locate(gestion_localidad_595)

    gestion_localidad_596 = Localidad()
    gestion_localidad_596.cod_postal = '5244'
    gestion_localidad_596.localidad = 'EL PERCHEL'
    gestion_localidad_596.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_596 = importer.save_or_locate(gestion_localidad_596)

    gestion_localidad_597 = Localidad()
    gestion_localidad_597.cod_postal = '5166'
    gestion_localidad_597.localidad = 'EL PERCHEL'
    gestion_localidad_597.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_597 = importer.save_or_locate(gestion_localidad_597)

    gestion_localidad_598 = Localidad()
    gestion_localidad_598.cod_postal = '5885'
    gestion_localidad_598.localidad = 'EL PERCHEL'
    gestion_localidad_598.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_598 = importer.save_or_locate(gestion_localidad_598)

    gestion_localidad_599 = Localidad()
    gestion_localidad_599.cod_postal = '5201'
    gestion_localidad_599.localidad = 'EL PERTIGO'
    gestion_localidad_599.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_599 = importer.save_or_locate(gestion_localidad_599)

    gestion_localidad_600 = Localidad()
    gestion_localidad_600.cod_postal = '5155'
    gestion_localidad_600.localidad = 'EL PERUEL'
    gestion_localidad_600.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_600 = importer.save_or_locate(gestion_localidad_600)

    gestion_localidad_601 = Localidad()
    gestion_localidad_601.cod_postal = '5155'
    gestion_localidad_601.localidad = 'EL PILCADO'
    gestion_localidad_601.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_601 = importer.save_or_locate(gestion_localidad_601)

    gestion_localidad_602 = Localidad()
    gestion_localidad_602.cod_postal = '5178'
    gestion_localidad_602.localidad = 'EL PINGO'
    gestion_localidad_602.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_602 = importer.save_or_locate(gestion_localidad_602)

    gestion_localidad_603 = Localidad()
    gestion_localidad_603.cod_postal = '5933'
    gestion_localidad_603.localidad = 'EL PORTEÑO'
    gestion_localidad_603.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_603 = importer.save_or_locate(gestion_localidad_603)

    gestion_localidad_604 = Localidad()
    gestion_localidad_604.cod_postal = '5196'
    gestion_localidad_604.localidad = 'EL PORTEZUELO'
    gestion_localidad_604.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_604 = importer.save_or_locate(gestion_localidad_604)

    gestion_localidad_605 = Localidad()
    gestion_localidad_605.cod_postal = '5200'
    gestion_localidad_605.localidad = 'EL PORTILLO'
    gestion_localidad_605.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_605 = importer.save_or_locate(gestion_localidad_605)

    gestion_localidad_606 = Localidad()
    gestion_localidad_606.cod_postal = '2651'
    gestion_localidad_606.localidad = 'EL PORVENIR'
    gestion_localidad_606.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_606 = importer.save_or_locate(gestion_localidad_606)

    gestion_localidad_607 = Localidad()
    gestion_localidad_607.cod_postal = '5801'
    gestion_localidad_607.localidad = 'EL POTOSI'
    gestion_localidad_607.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_607 = importer.save_or_locate(gestion_localidad_607)

    gestion_localidad_608 = Localidad()
    gestion_localidad_608.cod_postal = '5295'
    gestion_localidad_608.localidad = 'EL POTRERO'
    gestion_localidad_608.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_608 = importer.save_or_locate(gestion_localidad_608)

    gestion_localidad_609 = Localidad()
    gestion_localidad_609.cod_postal = '5155'
    gestion_localidad_609.localidad = 'EL POTRERO'
    gestion_localidad_609.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_609 = importer.save_or_locate(gestion_localidad_609)

    gestion_localidad_610 = Localidad()
    gestion_localidad_610.cod_postal = '5233'
    gestion_localidad_610.localidad = 'EL POZO'
    gestion_localidad_610.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_610 = importer.save_or_locate(gestion_localidad_610)

    gestion_localidad_611 = Localidad()
    gestion_localidad_611.cod_postal = '5248'
    gestion_localidad_611.localidad = 'EL PRADO'
    gestion_localidad_611.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_611 = importer.save_or_locate(gestion_localidad_611)

    gestion_localidad_612 = Localidad()
    gestion_localidad_612.cod_postal = '5249'
    gestion_localidad_612.localidad = 'EL PROGRESO'
    gestion_localidad_612.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_612 = importer.save_or_locate(gestion_localidad_612)

    gestion_localidad_613 = Localidad()
    gestion_localidad_613.cod_postal = '5875'
    gestion_localidad_613.localidad = 'EL PUEBLITO'
    gestion_localidad_613.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_613 = importer.save_or_locate(gestion_localidad_613)

    gestion_localidad_614 = Localidad()
    gestion_localidad_614.cod_postal = '5107'
    gestion_localidad_614.localidad = 'EL PUEBLITO'
    gestion_localidad_614.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_614 = importer.save_or_locate(gestion_localidad_614)

    gestion_localidad_615 = Localidad()
    gestion_localidad_615.cod_postal = '5172'
    gestion_localidad_615.localidad = 'EL PUENTE'
    gestion_localidad_615.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_615 = importer.save_or_locate(gestion_localidad_615)

    gestion_localidad_616 = Localidad()
    gestion_localidad_616.cod_postal = '5284'
    gestion_localidad_616.localidad = 'EL PUESTO'
    gestion_localidad_616.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_616 = importer.save_or_locate(gestion_localidad_616)

    gestion_localidad_617 = Localidad()
    gestion_localidad_617.cod_postal = '5249'
    gestion_localidad_617.localidad = 'EL PUESTO'
    gestion_localidad_617.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_617 = importer.save_or_locate(gestion_localidad_617)

    gestion_localidad_618 = Localidad()
    gestion_localidad_618.cod_postal = '5218'
    gestion_localidad_618.localidad = 'EL PUESTO LOS CABRERA'
    gestion_localidad_618.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_618 = importer.save_or_locate(gestion_localidad_618)

    gestion_localidad_619 = Localidad()
    gestion_localidad_619.cod_postal = '5101'
    gestion_localidad_619.localidad = 'EL QUEBRACHAL'
    gestion_localidad_619.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_619 = importer.save_or_locate(gestion_localidad_619)

    gestion_localidad_620 = Localidad()
    gestion_localidad_620.cod_postal = '5109'
    gestion_localidad_620.localidad = 'EL QUEBRACHITO'
    gestion_localidad_620.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_620 = importer.save_or_locate(gestion_localidad_620)

    gestion_localidad_621 = Localidad()
    gestion_localidad_621.cod_postal = '5218'
    gestion_localidad_621.localidad = 'EL QUEBRACHO'
    gestion_localidad_621.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_621 = importer.save_or_locate(gestion_localidad_621)

    gestion_localidad_622 = Localidad()
    gestion_localidad_622.cod_postal = '5249'
    gestion_localidad_622.localidad = 'EL QUEBRACHO'
    gestion_localidad_622.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_622 = importer.save_or_locate(gestion_localidad_622)

    gestion_localidad_623 = Localidad()
    gestion_localidad_623.cod_postal = '5101'
    gestion_localidad_623.localidad = 'EL QUEBRACHO'
    gestion_localidad_623.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_623 = importer.save_or_locate(gestion_localidad_623)

    gestion_localidad_624 = Localidad()
    gestion_localidad_624.cod_postal = '5854'
    gestion_localidad_624.localidad = 'EL QUEBRACHO'
    gestion_localidad_624.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_624 = importer.save_or_locate(gestion_localidad_624)

    gestion_localidad_625 = Localidad()
    gestion_localidad_625.cod_postal = '5270'
    gestion_localidad_625.localidad = 'EL QUICHO'
    gestion_localidad_625.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_625 = importer.save_or_locate(gestion_localidad_625)

    gestion_localidad_626 = Localidad()
    gestion_localidad_626.cod_postal = '5218'
    gestion_localidad_626.localidad = 'EL RANCHITO'
    gestion_localidad_626.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_626 = importer.save_or_locate(gestion_localidad_626)

    gestion_localidad_627 = Localidad()
    gestion_localidad_627.cod_postal = '6121'
    gestion_localidad_627.localidad = 'EL RASTREADOR'
    gestion_localidad_627.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_627 = importer.save_or_locate(gestion_localidad_627)

    gestion_localidad_628 = Localidad()
    gestion_localidad_628.cod_postal = '5220'
    gestion_localidad_628.localidad = 'EL REYMUNDO'
    gestion_localidad_628.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_628 = importer.save_or_locate(gestion_localidad_628)

    gestion_localidad_629 = Localidad()
    gestion_localidad_629.cod_postal = '5282'
    gestion_localidad_629.localidad = 'EL RINCON'
    gestion_localidad_629.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_629 = importer.save_or_locate(gestion_localidad_629)

    gestion_localidad_630 = Localidad()
    gestion_localidad_630.cod_postal = '5871'
    gestion_localidad_630.localidad = 'EL RINCON'
    gestion_localidad_630.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_630 = importer.save_or_locate(gestion_localidad_630)

    gestion_localidad_631 = Localidad()
    gestion_localidad_631.cod_postal = '5231'
    gestion_localidad_631.localidad = 'EL RINCON'
    gestion_localidad_631.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_631 = importer.save_or_locate(gestion_localidad_631)

    gestion_localidad_632 = Localidad()
    gestion_localidad_632.cod_postal = '5285'
    gestion_localidad_632.localidad = 'EL RIO'
    gestion_localidad_632.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_632 = importer.save_or_locate(gestion_localidad_632)

    gestion_localidad_633 = Localidad()
    gestion_localidad_633.cod_postal = '5201'
    gestion_localidad_633.localidad = 'EL RODEITO'
    gestion_localidad_633.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_633 = importer.save_or_locate(gestion_localidad_633)

    gestion_localidad_634 = Localidad()
    gestion_localidad_634.cod_postal = '5249'
    gestion_localidad_634.localidad = 'EL RODEO'
    gestion_localidad_634.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_634 = importer.save_or_locate(gestion_localidad_634)

    gestion_localidad_635 = Localidad()
    gestion_localidad_635.cod_postal = '5291'
    gestion_localidad_635.localidad = 'EL RODEO'
    gestion_localidad_635.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_635 = importer.save_or_locate(gestion_localidad_635)

    gestion_localidad_636 = Localidad()
    gestion_localidad_636.cod_postal = '5246'
    gestion_localidad_636.localidad = 'EL RODEO'
    gestion_localidad_636.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_636 = importer.save_or_locate(gestion_localidad_636)

    gestion_localidad_637 = Localidad()
    gestion_localidad_637.cod_postal = '5205'
    gestion_localidad_637.localidad = 'EL ROSARIO'
    gestion_localidad_637.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_637 = importer.save_or_locate(gestion_localidad_637)

    gestion_localidad_638 = Localidad()
    gestion_localidad_638.cod_postal = '5282'
    gestion_localidad_638.localidad = 'EL SALTO'
    gestion_localidad_638.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_638 = importer.save_or_locate(gestion_localidad_638)

    gestion_localidad_639 = Localidad()
    gestion_localidad_639.cod_postal = '5854'
    gestion_localidad_639.localidad = 'EL SALTO NORTE'
    gestion_localidad_639.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_639 = importer.save_or_locate(gestion_localidad_639)

    gestion_localidad_640 = Localidad()
    gestion_localidad_640.cod_postal = '5196'
    gestion_localidad_640.localidad = 'EL SAUCE'
    gestion_localidad_640.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_640 = importer.save_or_locate(gestion_localidad_640)

    gestion_localidad_641 = Localidad()
    gestion_localidad_641.cod_postal = '5289'
    gestion_localidad_641.localidad = 'EL SAUCE'
    gestion_localidad_641.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_641 = importer.save_or_locate(gestion_localidad_641)

    gestion_localidad_642 = Localidad()
    gestion_localidad_642.cod_postal = '5887'
    gestion_localidad_642.localidad = 'EL SAUZAL'
    gestion_localidad_642.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_642 = importer.save_or_locate(gestion_localidad_642)

    gestion_localidad_643 = Localidad()
    gestion_localidad_643.cod_postal = '5244'
    gestion_localidad_643.localidad = 'EL SEBIL'
    gestion_localidad_643.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_643 = importer.save_or_locate(gestion_localidad_643)

    gestion_localidad_644 = Localidad()
    gestion_localidad_644.cod_postal = '5248'
    gestion_localidad_644.localidad = 'EL SILVERIO'
    gestion_localidad_644.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_644 = importer.save_or_locate(gestion_localidad_644)

    gestion_localidad_645 = Localidad()
    gestion_localidad_645.cod_postal = '5249'
    gestion_localidad_645.localidad = 'EL SIMBOL'
    gestion_localidad_645.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_645 = importer.save_or_locate(gestion_localidad_645)

    gestion_localidad_646 = Localidad()
    gestion_localidad_646.cod_postal = '5281'
    gestion_localidad_646.localidad = 'EL SIMBOLAR'
    gestion_localidad_646.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_646 = importer.save_or_locate(gestion_localidad_646)

    gestion_localidad_647 = Localidad()
    gestion_localidad_647.cod_postal = '5291'
    gestion_localidad_647.localidad = 'EL SUNCHAL'
    gestion_localidad_647.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_647 = importer.save_or_locate(gestion_localidad_647)

    gestion_localidad_648 = Localidad()
    gestion_localidad_648.cod_postal = '5885'
    gestion_localidad_648.localidad = 'EL TAJAMAR'
    gestion_localidad_648.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_648 = importer.save_or_locate(gestion_localidad_648)

    gestion_localidad_649 = Localidad()
    gestion_localidad_649.cod_postal = '5201'
    gestion_localidad_649.localidad = 'EL TALA'
    gestion_localidad_649.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_649 = importer.save_or_locate(gestion_localidad_649)

    gestion_localidad_650 = Localidad()
    gestion_localidad_650.cod_postal = '5107'
    gestion_localidad_650.localidad = 'EL TALAR'
    gestion_localidad_650.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_650 = importer.save_or_locate(gestion_localidad_650)

    gestion_localidad_651 = Localidad()
    gestion_localidad_651.cod_postal = '5212'
    gestion_localidad_651.localidad = 'EL TALITA'
    gestion_localidad_651.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_651 = importer.save_or_locate(gestion_localidad_651)

    gestion_localidad_652 = Localidad()
    gestion_localidad_652.cod_postal = '5236'
    gestion_localidad_652.localidad = 'EL TALITA VILLA GRAL MITRE'
    gestion_localidad_652.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_652 = importer.save_or_locate(gestion_localidad_652)

    gestion_localidad_653 = Localidad()
    gestion_localidad_653.cod_postal = '5212'
    gestion_localidad_653.localidad = 'EL TAMBERO'
    gestion_localidad_653.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_653 = importer.save_or_locate(gestion_localidad_653)

    gestion_localidad_654 = Localidad()
    gestion_localidad_654.cod_postal = '5801'
    gestion_localidad_654.localidad = 'EL TAMBO'
    gestion_localidad_654.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_654 = importer.save_or_locate(gestion_localidad_654)

    gestion_localidad_655 = Localidad()
    gestion_localidad_655.cod_postal = '2432'
    gestion_localidad_655.localidad = 'EL TIO'
    gestion_localidad_655.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_655 = importer.save_or_locate(gestion_localidad_655)

    gestion_localidad_656 = Localidad()
    gestion_localidad_656.cod_postal = '5149'
    gestion_localidad_656.localidad = 'EL TOMILLO'
    gestion_localidad_656.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_656 = importer.save_or_locate(gestion_localidad_656)

    gestion_localidad_657 = Localidad()
    gestion_localidad_657.cod_postal = '5864'
    gestion_localidad_657.localidad = 'EL TORREON'
    gestion_localidad_657.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_657 = importer.save_or_locate(gestion_localidad_657)

    gestion_localidad_658 = Localidad()
    gestion_localidad_658.cod_postal = '5137'
    gestion_localidad_658.localidad = 'EL TOSTADO'
    gestion_localidad_658.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_658 = importer.save_or_locate(gestion_localidad_658)

    gestion_localidad_659 = Localidad()
    gestion_localidad_659.cod_postal = '2424'
    gestion_localidad_659.localidad = 'EL TRABAJO'
    gestion_localidad_659.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_659 = importer.save_or_locate(gestion_localidad_659)

    gestion_localidad_660 = Localidad()
    gestion_localidad_660.cod_postal = '2572'
    gestion_localidad_660.localidad = 'EL TRIANGULO'
    gestion_localidad_660.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_660 = importer.save_or_locate(gestion_localidad_660)

    gestion_localidad_661 = Localidad()
    gestion_localidad_661.cod_postal = '5249'
    gestion_localidad_661.localidad = 'EL TULE'
    gestion_localidad_661.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_661 = importer.save_or_locate(gestion_localidad_661)

    gestion_localidad_662 = Localidad()
    gestion_localidad_662.cod_postal = '5216'
    gestion_localidad_662.localidad = 'EL TUSCAL'
    gestion_localidad_662.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_662 = importer.save_or_locate(gestion_localidad_662)

    gestion_localidad_663 = Localidad()
    gestion_localidad_663.cod_postal = '5182'
    gestion_localidad_663.localidad = 'EL VADO'
    gestion_localidad_663.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_663 = importer.save_or_locate(gestion_localidad_663)

    gestion_localidad_664 = Localidad()
    gestion_localidad_664.cod_postal = '5172'
    gestion_localidad_664.localidad = 'EL VALLECITO'
    gestion_localidad_664.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_664 = importer.save_or_locate(gestion_localidad_664)

    gestion_localidad_665 = Localidad()
    gestion_localidad_665.cod_postal = '5291'
    gestion_localidad_665.localidad = 'EL VALLESITO'
    gestion_localidad_665.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_665 = importer.save_or_locate(gestion_localidad_665)

    gestion_localidad_666 = Localidad()
    gestion_localidad_666.cod_postal = '5214'
    gestion_localidad_666.localidad = 'EL VEINTICINCO'
    gestion_localidad_666.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_666 = importer.save_or_locate(gestion_localidad_666)

    gestion_localidad_667 = Localidad()
    gestion_localidad_667.cod_postal = '5231'
    gestion_localidad_667.localidad = 'EL VENCE'
    gestion_localidad_667.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_667 = importer.save_or_locate(gestion_localidad_667)

    gestion_localidad_668 = Localidad()
    gestion_localidad_668.cod_postal = '5155'
    gestion_localidad_668.localidad = 'EL VERGEL'
    gestion_localidad_668.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_668 = importer.save_or_locate(gestion_localidad_668)

    gestion_localidad_669 = Localidad()
    gestion_localidad_669.cod_postal = '5233'
    gestion_localidad_669.localidad = 'EL VISMAL'
    gestion_localidad_669.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_669 = importer.save_or_locate(gestion_localidad_669)

    gestion_localidad_670 = Localidad()
    gestion_localidad_670.cod_postal = '5149'
    gestion_localidad_670.localidad = 'EL ZAINO'
    gestion_localidad_670.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_670 = importer.save_or_locate(gestion_localidad_670)

    gestion_localidad_671 = Localidad()
    gestion_localidad_671.cod_postal = '5233'
    gestion_localidad_671.localidad = 'EL ZAPALLAR'
    gestion_localidad_671.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_671 = importer.save_or_locate(gestion_localidad_671)

    gestion_localidad_672 = Localidad()
    gestion_localidad_672.cod_postal = '5184'
    gestion_localidad_672.localidad = 'EL ZAPATO'
    gestion_localidad_672.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_672 = importer.save_or_locate(gestion_localidad_672)

    gestion_localidad_673 = Localidad()
    gestion_localidad_673.cod_postal = '5856'
    gestion_localidad_673.localidad = 'EMBALSE'
    gestion_localidad_673.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_673 = importer.save_or_locate(gestion_localidad_673)

    gestion_localidad_674 = Localidad()
    gestion_localidad_674.cod_postal = '5231'
    gestion_localidad_674.localidad = 'ENCRUCIJADA'
    gestion_localidad_674.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_674 = importer.save_or_locate(gestion_localidad_674)

    gestion_localidad_675 = Localidad()
    gestion_localidad_675.cod_postal = '2587'
    gestion_localidad_675.localidad = 'ENFERMERA KELLY'
    gestion_localidad_675.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_675 = importer.save_or_locate(gestion_localidad_675)

    gestion_localidad_676 = Localidad()
    gestion_localidad_676.cod_postal = '5282'
    gestion_localidad_676.localidad = 'ESCOBAS'
    gestion_localidad_676.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_676 = importer.save_or_locate(gestion_localidad_676)

    gestion_localidad_677 = Localidad()
    gestion_localidad_677.cod_postal = '5101'
    gestion_localidad_677.localidad = 'ESCUELA DE ARTILLERIA'
    gestion_localidad_677.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_677 = importer.save_or_locate(gestion_localidad_677)

    gestion_localidad_678 = Localidad()
    gestion_localidad_678.cod_postal = '5131'
    gestion_localidad_678.localidad = 'ESPERANZA'
    gestion_localidad_678.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_678 = importer.save_or_locate(gestion_localidad_678)

    gestion_localidad_679 = Localidad()
    gestion_localidad_679.cod_postal = '5129'
    gestion_localidad_679.localidad = 'ESPINILLO'
    gestion_localidad_679.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_679 = importer.save_or_locate(gestion_localidad_679)

    gestion_localidad_680 = Localidad()
    gestion_localidad_680.cod_postal = '5203'
    gestion_localidad_680.localidad = 'ESPINILLO'
    gestion_localidad_680.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_680 = importer.save_or_locate(gestion_localidad_680)

    gestion_localidad_681 = Localidad()
    gestion_localidad_681.cod_postal = '5221'
    gestion_localidad_681.localidad = 'ESPINILLO'
    gestion_localidad_681.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_681 = importer.save_or_locate(gestion_localidad_681)

    gestion_localidad_682 = Localidad()
    gestion_localidad_682.cod_postal = '5811'
    gestion_localidad_682.localidad = 'ESPINILLO'
    gestion_localidad_682.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_682 = importer.save_or_locate(gestion_localidad_682)

    gestion_localidad_683 = Localidad()
    gestion_localidad_683.cod_postal = '5131'
    gestion_localidad_683.localidad = 'ESPINILLO NUÑEZ DEL PRADO'
    gestion_localidad_683.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_683 = importer.save_or_locate(gestion_localidad_683)

    gestion_localidad_684 = Localidad()
    gestion_localidad_684.cod_postal = '5131'
    gestion_localidad_684.localidad = 'ESQUINA'
    gestion_localidad_684.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_684 = importer.save_or_locate(gestion_localidad_684)

    gestion_localidad_685 = Localidad()
    gestion_localidad_685.cod_postal = '5281'
    gestion_localidad_685.localidad = 'ESQUINA DEL ALAMBRE'
    gestion_localidad_685.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_685 = importer.save_or_locate(gestion_localidad_685)

    gestion_localidad_686 = Localidad()
    gestion_localidad_686.cod_postal = '5831'
    gestion_localidad_686.localidad = 'ESTACION ACHIRAS'
    gestion_localidad_686.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_686 = importer.save_or_locate(gestion_localidad_686)

    gestion_localidad_687 = Localidad()
    gestion_localidad_687.cod_postal = '2550'
    gestion_localidad_687.localidad = 'ESTACION BELL VILLE'
    gestion_localidad_687.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_687 = importer.save_or_locate(gestion_localidad_687)

    gestion_localidad_688 = Localidad()
    gestion_localidad_688.cod_postal = '5969'
    gestion_localidad_688.localidad = 'ESTACION CALCHIN'
    gestion_localidad_688.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_688 = importer.save_or_locate(gestion_localidad_688)

    gestion_localidad_689 = Localidad()
    gestion_localidad_689.cod_postal = '5220'
    gestion_localidad_689.localidad = 'ESTACION CAROYA'
    gestion_localidad_689.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_689 = importer.save_or_locate(gestion_localidad_689)

    gestion_localidad_690 = Localidad()
    gestion_localidad_690.cod_postal = '5131'
    gestion_localidad_690.localidad = 'ESTACION COLONIA TIROLESA'
    gestion_localidad_690.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_690 = importer.save_or_locate(gestion_localidad_690)

    gestion_localidad_691 = Localidad()
    gestion_localidad_691.cod_postal = '5145'
    gestion_localidad_691.localidad = 'ESTACION GENERAL PAZ'
    gestion_localidad_691.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_691 = importer.save_or_locate(gestion_localidad_691)

    gestion_localidad_692 = Localidad()
    gestion_localidad_692.cod_postal = '5839'
    gestion_localidad_692.localidad = 'ESTACION PUNTA DE AGUA'
    gestion_localidad_692.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_692 = importer.save_or_locate(gestion_localidad_692)

    gestion_localidad_693 = Localidad()
    gestion_localidad_693.cod_postal = '5284'
    gestion_localidad_693.localidad = 'ESTACION SOTO'
    gestion_localidad_693.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_693 = importer.save_or_locate(gestion_localidad_693)

    gestion_localidad_694 = Localidad()
    gestion_localidad_694.cod_postal = '5229'
    gestion_localidad_694.localidad = 'ESTANCIA BOTTARO'
    gestion_localidad_694.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_694 = importer.save_or_locate(gestion_localidad_694)

    gestion_localidad_695 = Localidad()
    gestion_localidad_695.cod_postal = '5291'
    gestion_localidad_695.localidad = 'ESTANCIA DE GUADALUPE'
    gestion_localidad_695.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_695 = importer.save_or_locate(gestion_localidad_695)

    gestion_localidad_696 = Localidad()
    gestion_localidad_696.cod_postal = '5155'
    gestion_localidad_696.localidad = 'ESTANCIA DOS RIOS'
    gestion_localidad_696.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_696 = importer.save_or_locate(gestion_localidad_696)

    gestion_localidad_697 = Localidad()
    gestion_localidad_697.cod_postal = '5131'
    gestion_localidad_697.localidad = 'ESTANCIA EL CARMEN'
    gestion_localidad_697.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_697 = importer.save_or_locate(gestion_localidad_697)

    gestion_localidad_698 = Localidad()
    gestion_localidad_698.cod_postal = '2428'
    gestion_localidad_698.localidad = 'ESTANCIA EL CHAÑAR'
    gestion_localidad_698.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_698 = importer.save_or_locate(gestion_localidad_698)

    gestion_localidad_699 = Localidad()
    gestion_localidad_699.cod_postal = '5244'
    gestion_localidad_699.localidad = 'ESTANCIA EL NACIONAL'
    gestion_localidad_699.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_699 = importer.save_or_locate(gestion_localidad_699)

    gestion_localidad_700 = Localidad()
    gestion_localidad_700.cod_postal = '5229'
    gestion_localidad_700.localidad = 'ESTANCIA EL TACO'
    gestion_localidad_700.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_700 = importer.save_or_locate(gestion_localidad_700)

    gestion_localidad_701 = Localidad()
    gestion_localidad_701.cod_postal = '5212'
    gestion_localidad_701.localidad = 'ESTANCIA GOROSITO'
    gestion_localidad_701.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_701 = importer.save_or_locate(gestion_localidad_701)

    gestion_localidad_702 = Localidad()
    gestion_localidad_702.cod_postal = '2428'
    gestion_localidad_702.localidad = 'ESTANCIA LA CHIQUITA'
    gestion_localidad_702.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_702 = importer.save_or_locate(gestion_localidad_702)

    gestion_localidad_703 = Localidad()
    gestion_localidad_703.cod_postal = '2428'
    gestion_localidad_703.localidad = 'ESTANCIA LA MOROCHA'
    gestion_localidad_703.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_703 = importer.save_or_locate(gestion_localidad_703)

    gestion_localidad_704 = Localidad()
    gestion_localidad_704.cod_postal = '5187'
    gestion_localidad_704.localidad = 'ESTANCIA LA PUNTA DEL AGUA'
    gestion_localidad_704.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_704 = importer.save_or_locate(gestion_localidad_704)

    gestion_localidad_705 = Localidad()
    gestion_localidad_705.cod_postal = '5131'
    gestion_localidad_705.localidad = 'ESTANCIA LAS CAÑAS'
    gestion_localidad_705.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_705 = importer.save_or_locate(gestion_localidad_705)

    gestion_localidad_706 = Localidad()
    gestion_localidad_706.cod_postal = '2671'
    gestion_localidad_706.localidad = 'ESTANCIA LAS MARGARITAS'
    gestion_localidad_706.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_706 = importer.save_or_locate(gestion_localidad_706)

    gestion_localidad_707 = Localidad()
    gestion_localidad_707.cod_postal = '5229'
    gestion_localidad_707.localidad = 'ESTANCIA LAS MERCEDES'
    gestion_localidad_707.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_707 = importer.save_or_locate(gestion_localidad_707)

    gestion_localidad_708 = Localidad()
    gestion_localidad_708.cod_postal = '5229'
    gestion_localidad_708.localidad = 'ESTANCIA LAS ROSAS'
    gestion_localidad_708.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_708 = importer.save_or_locate(gestion_localidad_708)

    gestion_localidad_709 = Localidad()
    gestion_localidad_709.cod_postal = '5987'
    gestion_localidad_709.localidad = 'ESTANCIA LOS MATORRALES'
    gestion_localidad_709.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_709 = importer.save_or_locate(gestion_localidad_709)

    gestion_localidad_710 = Localidad()
    gestion_localidad_710.cod_postal = '5249'
    gestion_localidad_710.localidad = 'ESTANCIA PATIÑO'
    gestion_localidad_710.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_710 = importer.save_or_locate(gestion_localidad_710)

    gestion_localidad_711 = Localidad()
    gestion_localidad_711.cod_postal = '5152'
    gestion_localidad_711.localidad = 'ESTANCIA VIEJA'
    gestion_localidad_711.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_711 = importer.save_or_locate(gestion_localidad_711)

    gestion_localidad_712 = Localidad()
    gestion_localidad_712.cod_postal = '5235'
    gestion_localidad_712.localidad = 'EST CANDELARIA NORTE'
    gestion_localidad_712.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_712 = importer.save_or_locate(gestion_localidad_712)

    gestion_localidad_713 = Localidad()
    gestion_localidad_713.cod_postal = '5145'
    gestion_localidad_713.localidad = 'EST JUAREZ CELMAN'
    gestion_localidad_713.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_713 = importer.save_or_locate(gestion_localidad_713)

    gestion_localidad_714 = Localidad()
    gestion_localidad_714.cod_postal = '2681'
    gestion_localidad_714.localidad = 'ETRURIA'
    gestion_localidad_714.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_714 = importer.save_or_locate(gestion_localidad_714)

    gestion_localidad_715 = Localidad()
    gestion_localidad_715.cod_postal = '5248'
    gestion_localidad_715.localidad = 'EUFRASIO LOZA'
    gestion_localidad_715.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_715 = importer.save_or_locate(gestion_localidad_715)

    gestion_localidad_716 = Localidad()
    gestion_localidad_716.cod_postal = '5189'
    gestion_localidad_716.localidad = 'FABRICA MILITAR'
    gestion_localidad_716.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_716 = importer.save_or_locate(gestion_localidad_716)

    gestion_localidad_717 = Localidad()
    gestion_localidad_717.cod_postal = '5900'
    gestion_localidad_717.localidad = 'FABRICA MILITAR'
    gestion_localidad_717.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_717 = importer.save_or_locate(gestion_localidad_717)

    gestion_localidad_718 = Localidad()
    gestion_localidad_718.cod_postal = '5850'
    gestion_localidad_718.localidad = 'FABRICA MILITAR RIO TERCERO'
    gestion_localidad_718.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_718 = importer.save_or_locate(gestion_localidad_718)

    gestion_localidad_719 = Localidad()
    gestion_localidad_719.cod_postal = '5186'
    gestion_localidad_719.localidad = 'FALDA DE CAÑETE'
    gestion_localidad_719.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_719 = importer.save_or_locate(gestion_localidad_719)

    gestion_localidad_720 = Localidad()
    gestion_localidad_720.cod_postal = '5187'
    gestion_localidad_720.localidad = 'FALDA DEL CARMEN'
    gestion_localidad_720.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_720 = importer.save_or_locate(gestion_localidad_720)

    gestion_localidad_721 = Localidad()
    gestion_localidad_721.cod_postal = '5189'
    gestion_localidad_721.localidad = 'FALDA DE LOS REARTES'
    gestion_localidad_721.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_721 = importer.save_or_locate(gestion_localidad_721)

    gestion_localidad_722 = Localidad()
    gestion_localidad_722.cod_postal = '5925'
    gestion_localidad_722.localidad = 'FERREYRA'
    gestion_localidad_722.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_722 = importer.save_or_locate(gestion_localidad_722)

    gestion_localidad_723 = Localidad()
    gestion_localidad_723.cod_postal = '2525'
    gestion_localidad_723.localidad = 'FLORA'
    gestion_localidad_723.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_723 = importer.save_or_locate(gestion_localidad_723)

    gestion_localidad_724 = Localidad()
    gestion_localidad_724.cod_postal = '5847'
    gestion_localidad_724.localidad = 'FRAGUEYRO'
    gestion_localidad_724.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_724 = importer.save_or_locate(gestion_localidad_724)

    gestion_localidad_725 = Localidad()
    gestion_localidad_725.cod_postal = '6120'
    gestion_localidad_725.localidad = 'FRAY CAYETANO RODRIGUEZ'
    gestion_localidad_725.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_725 = importer.save_or_locate(gestion_localidad_725)

    gestion_localidad_726 = Localidad()
    gestion_localidad_726.cod_postal = '2413'
    gestion_localidad_726.localidad = 'FREYRE'
    gestion_localidad_726.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_726 = importer.save_or_locate(gestion_localidad_726)

    gestion_localidad_727 = Localidad()
    gestion_localidad_727.cod_postal = '5967'
    gestion_localidad_727.localidad = 'GALPON CHICO'
    gestion_localidad_727.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_727 = importer.save_or_locate(gestion_localidad_727)

    gestion_localidad_728 = Localidad()
    gestion_localidad_728.cod_postal = '6132'
    gestion_localidad_728.localidad = 'GAVILAN'
    gestion_localidad_728.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_728 = importer.save_or_locate(gestion_localidad_728)

    gestion_localidad_729 = Localidad()
    gestion_localidad_729.cod_postal = '2583'
    gestion_localidad_729.localidad = 'GENERAL BALDISSERA'
    gestion_localidad_729.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_729 = importer.save_or_locate(gestion_localidad_729)

    gestion_localidad_730 = Localidad()
    gestion_localidad_730.cod_postal = '5809'
    gestion_localidad_730.localidad = 'GENERAL CABRERA'
    gestion_localidad_730.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_730 = importer.save_or_locate(gestion_localidad_730)

    gestion_localidad_731 = Localidad()
    gestion_localidad_731.cod_postal = '5923'
    gestion_localidad_731.localidad = 'GENERAL DEHEZA'
    gestion_localidad_731.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_731 = importer.save_or_locate(gestion_localidad_731)

    gestion_localidad_732 = Localidad()
    gestion_localidad_732.cod_postal = '5933'
    gestion_localidad_732.localidad = 'GENERAL FOTHERINGHAM'
    gestion_localidad_732.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_732 = importer.save_or_locate(gestion_localidad_732)

    gestion_localidad_733 = Localidad()
    gestion_localidad_733.cod_postal = '5101'
    gestion_localidad_733.localidad = 'GENERAL LAS HERAS'
    gestion_localidad_733.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_733 = importer.save_or_locate(gestion_localidad_733)

    gestion_localidad_734 = Localidad()
    gestion_localidad_734.cod_postal = '6132'
    gestion_localidad_734.localidad = 'GENERAL LEVALLE'
    gestion_localidad_734.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_734 = importer.save_or_locate(gestion_localidad_734)

    gestion_localidad_735 = Localidad()
    gestion_localidad_735.cod_postal = '5151'
    gestion_localidad_735.localidad = 'GENERAL ORTIZ DE OCAMPO'
    gestion_localidad_735.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_735 = importer.save_or_locate(gestion_localidad_735)

    gestion_localidad_736 = Localidad()
    gestion_localidad_736.cod_postal = '6140'
    gestion_localidad_736.localidad = 'GENERAL PUEYRREDON'
    gestion_localidad_736.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_736 = importer.save_or_locate(gestion_localidad_736)

    gestion_localidad_737 = Localidad()
    gestion_localidad_737.cod_postal = '2592'
    gestion_localidad_737.localidad = 'GENERAL ROCA'
    gestion_localidad_737.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_737 = importer.save_or_locate(gestion_localidad_737)

    gestion_localidad_738 = Localidad()
    gestion_localidad_738.cod_postal = '6142'
    gestion_localidad_738.localidad = 'GENERAL SOLER'
    gestion_localidad_738.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_738 = importer.save_or_locate(gestion_localidad_738)

    gestion_localidad_739 = Localidad()
    gestion_localidad_739.cod_postal = '2671'
    gestion_localidad_739.localidad = 'GENERAL VIAMONTE'
    gestion_localidad_739.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_739 = importer.save_or_locate(gestion_localidad_739)

    gestion_localidad_740 = Localidad()
    gestion_localidad_740.cod_postal = '5837'
    gestion_localidad_740.localidad = 'GLORIALDO FERNANDEZ'
    gestion_localidad_740.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_740 = importer.save_or_locate(gestion_localidad_740)

    gestion_localidad_741 = Localidad()
    gestion_localidad_741.cod_postal = '5187'
    gestion_localidad_741.localidad = 'GOLPE DE AGUA'
    gestion_localidad_741.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_741 = importer.save_or_locate(gestion_localidad_741)

    gestion_localidad_742 = Localidad()
    gestion_localidad_742.cod_postal = '5209'
    gestion_localidad_742.localidad = 'GRACIELA'
    gestion_localidad_742.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_742 = importer.save_or_locate(gestion_localidad_742)

    gestion_localidad_743 = Localidad()
    gestion_localidad_743.cod_postal = '5172'
    gestion_localidad_743.localidad = 'GRUTA DE SAN ANTONIO'
    gestion_localidad_743.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_743 = importer.save_or_locate(gestion_localidad_743)

    gestion_localidad_744 = Localidad()
    gestion_localidad_744.cod_postal = '5244'
    gestion_localidad_744.localidad = 'GUALLASCATE'
    gestion_localidad_744.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_744 = importer.save_or_locate(gestion_localidad_744)

    gestion_localidad_745 = Localidad()
    gestion_localidad_745.cod_postal = '5875'
    gestion_localidad_745.localidad = 'GUANACO BOLEADO'
    gestion_localidad_745.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_745 = importer.save_or_locate(gestion_localidad_745)

    gestion_localidad_746 = Localidad()
    gestion_localidad_746.cod_postal = '5281'
    gestion_localidad_746.localidad = 'GUANACO MUERTO'
    gestion_localidad_746.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_746 = importer.save_or_locate(gestion_localidad_746)

    gestion_localidad_747 = Localidad()
    gestion_localidad_747.cod_postal = '6120'
    gestion_localidad_747.localidad = 'GUARDIA VIEJA'
    gestion_localidad_747.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_747 = importer.save_or_locate(gestion_localidad_747)

    gestion_localidad_748 = Localidad()
    gestion_localidad_748.cod_postal = '5285'
    gestion_localidad_748.localidad = 'GUASAPAMPA'
    gestion_localidad_748.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_748 = importer.save_or_locate(gestion_localidad_748)

    gestion_localidad_749 = Localidad()
    gestion_localidad_749.cod_postal = '5155'
    gestion_localidad_749.localidad = 'GUASTA'
    gestion_localidad_749.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_749 = importer.save_or_locate(gestion_localidad_749)

    gestion_localidad_750 = Localidad()
    gestion_localidad_750.cod_postal = '2627'
    gestion_localidad_750.localidad = 'GUATIMOZIN'
    gestion_localidad_750.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_750 = importer.save_or_locate(gestion_localidad_750)

    gestion_localidad_751 = Localidad()
    gestion_localidad_751.cod_postal = '5821'
    gestion_localidad_751.localidad = 'GUINDAS'
    gestion_localidad_751.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_751 = importer.save_or_locate(gestion_localidad_751)

    gestion_localidad_752 = Localidad()
    gestion_localidad_752.cod_postal = '5249'
    gestion_localidad_752.localidad = 'GUTEMBERG'
    gestion_localidad_752.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_752 = importer.save_or_locate(gestion_localidad_752)

    gestion_localidad_753 = Localidad()
    gestion_localidad_753.cod_postal = '5236'
    gestion_localidad_753.localidad = 'HARAS SAN ANTONIO'
    gestion_localidad_753.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_753 = importer.save_or_locate(gestion_localidad_753)

    gestion_localidad_754 = Localidad()
    gestion_localidad_754.cod_postal = '5123'
    gestion_localidad_754.localidad = 'HARAS SANTA MARTHA'
    gestion_localidad_754.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_754 = importer.save_or_locate(gestion_localidad_754)

    gestion_localidad_755 = Localidad()
    gestion_localidad_755.cod_postal = '5929'
    gestion_localidad_755.localidad = 'HERNANDO'
    gestion_localidad_755.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_755 = importer.save_or_locate(gestion_localidad_755)

    gestion_localidad_756 = Localidad()
    gestion_localidad_756.cod_postal = '5131'
    gestion_localidad_756.localidad = 'HIGUERIAS'
    gestion_localidad_756.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_756 = importer.save_or_locate(gestion_localidad_756)

    gestion_localidad_757 = Localidad()
    gestion_localidad_757.cod_postal = '5125'
    gestion_localidad_757.localidad = 'HIGUERILLAS'
    gestion_localidad_757.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_757 = importer.save_or_locate(gestion_localidad_757)

    gestion_localidad_758 = Localidad()
    gestion_localidad_758.cod_postal = '6225'
    gestion_localidad_758.localidad = 'HIPOLITO BOUCHARD'
    gestion_localidad_758.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_758 = importer.save_or_locate(gestion_localidad_758)

    gestion_localidad_759 = Localidad()
    gestion_localidad_759.cod_postal = '5825'
    gestion_localidad_759.localidad = 'HOLMBERG'
    gestion_localidad_759.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_759 = importer.save_or_locate(gestion_localidad_759)

    gestion_localidad_760 = Localidad()
    gestion_localidad_760.cod_postal = '5885'
    gestion_localidad_760.localidad = 'HORNILLOS'
    gestion_localidad_760.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_760 = importer.save_or_locate(gestion_localidad_760)

    gestion_localidad_761 = Localidad()
    gestion_localidad_761.cod_postal = '5165'
    gestion_localidad_761.localidad = 'HOSPITAL FLIA DOMINGO FUNES'
    gestion_localidad_761.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_761 = importer.save_or_locate(gestion_localidad_761)

    gestion_localidad_762 = Localidad()
    gestion_localidad_762.cod_postal = '6121'
    gestion_localidad_762.localidad = 'HUANCHILLA'
    gestion_localidad_762.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_762 = importer.save_or_locate(gestion_localidad_762)

    gestion_localidad_763 = Localidad()
    gestion_localidad_763.cod_postal = '6121'
    gestion_localidad_763.localidad = 'HUANCHILLA SUD'
    gestion_localidad_763.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_763 = importer.save_or_locate(gestion_localidad_763)

    gestion_localidad_764 = Localidad()
    gestion_localidad_764.cod_postal = '5218'
    gestion_localidad_764.localidad = 'HUASCHA'
    gestion_localidad_764.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_764 = importer.save_or_locate(gestion_localidad_764)

    gestion_localidad_765 = Localidad()
    gestion_localidad_765.cod_postal = '5875'
    gestion_localidad_765.localidad = 'HUASTA'
    gestion_localidad_765.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_765 = importer.save_or_locate(gestion_localidad_765)

    gestion_localidad_766 = Localidad()
    gestion_localidad_766.cod_postal = '5887'
    gestion_localidad_766.localidad = 'HUCLE'
    gestion_localidad_766.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_766 = importer.save_or_locate(gestion_localidad_766)

    gestion_localidad_767 = Localidad()
    gestion_localidad_767.cod_postal = '5174'
    gestion_localidad_767.localidad = 'HUERTA GRANDE'
    gestion_localidad_767.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_767 = importer.save_or_locate(gestion_localidad_767)

    gestion_localidad_768 = Localidad()
    gestion_localidad_768.cod_postal = '6270'
    gestion_localidad_768.localidad = 'HUINCA RENANCO'
    gestion_localidad_768.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_768 = importer.save_or_locate(gestion_localidad_768)

    gestion_localidad_769 = Localidad()
    gestion_localidad_769.cod_postal = '2557'
    gestion_localidad_769.localidad = 'IDIAZABAL'
    gestion_localidad_769.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_769 = importer.save_or_locate(gestion_localidad_769)

    gestion_localidad_770 = Localidad()
    gestion_localidad_770.cod_postal = '5270'
    gestion_localidad_770.localidad = 'IGLESIA VIEJA'
    gestion_localidad_770.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_770 = importer.save_or_locate(gestion_localidad_770)

    gestion_localidad_771 = Localidad()
    gestion_localidad_771.cod_postal = '5987'
    gestion_localidad_771.localidad = 'IMPIRA'
    gestion_localidad_771.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_771 = importer.save_or_locate(gestion_localidad_771)

    gestion_localidad_772 = Localidad()
    gestion_localidad_772.cod_postal = '5988'
    gestion_localidad_772.localidad = 'INDEPENDENCIA'
    gestion_localidad_772.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_772 = importer.save_or_locate(gestion_localidad_772)

    gestion_localidad_773 = Localidad()
    gestion_localidad_773.cod_postal = '5909'
    gestion_localidad_773.localidad = 'INDIA MUERTA'
    gestion_localidad_773.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_773 = importer.save_or_locate(gestion_localidad_773)

    gestion_localidad_774 = Localidad()
    gestion_localidad_774.cod_postal = '5200'
    gestion_localidad_774.localidad = 'INGENIERO BERTINI'
    gestion_localidad_774.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_774 = importer.save_or_locate(gestion_localidad_774)

    gestion_localidad_775 = Localidad()
    gestion_localidad_775.cod_postal = '2587'
    gestion_localidad_775.localidad = 'INRIVILLE'
    gestion_localidad_775.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_775 = importer.save_or_locate(gestion_localidad_775)

    gestion_localidad_776 = Localidad()
    gestion_localidad_776.cod_postal = '5209'
    gestion_localidad_776.localidad = 'INVERNADA'
    gestion_localidad_776.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_776 = importer.save_or_locate(gestion_localidad_776)

    gestion_localidad_777 = Localidad()
    gestion_localidad_777.cod_postal = '5168'
    gestion_localidad_777.localidad = 'IRIGOYEN'
    gestion_localidad_777.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_777 = importer.save_or_locate(gestion_localidad_777)

    gestion_localidad_778 = Localidad()
    gestion_localidad_778.cod_postal = '5201'
    gestion_localidad_778.localidad = 'ISCHILIN'
    gestion_localidad_778.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_778 = importer.save_or_locate(gestion_localidad_778)

    gestion_localidad_779 = Localidad()
    gestion_localidad_779.cod_postal = '5129'
    gestion_localidad_779.localidad = 'ISLA DEL CERRO'
    gestion_localidad_779.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_779 = importer.save_or_locate(gestion_localidad_779)

    gestion_localidad_780 = Localidad()
    gestion_localidad_780.cod_postal = '5214'
    gestion_localidad_780.localidad = 'ISLA DE SAN ANTONIO'
    gestion_localidad_780.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_780 = importer.save_or_locate(gestion_localidad_780)

    gestion_localidad_781 = Localidad()
    gestion_localidad_781.cod_postal = '5129'
    gestion_localidad_781.localidad = 'ISLA LARGA'
    gestion_localidad_781.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_781 = importer.save_or_locate(gestion_localidad_781)

    gestion_localidad_782 = Localidad()
    gestion_localidad_782.cod_postal = '5225'
    gestion_localidad_782.localidad = 'ISLA VERDE'
    gestion_localidad_782.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_782 = importer.save_or_locate(gestion_localidad_782)

    gestion_localidad_783 = Localidad()
    gestion_localidad_783.cod_postal = '2661'
    gestion_localidad_783.localidad = 'ISLA VERDE'
    gestion_localidad_783.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_783 = importer.save_or_locate(gestion_localidad_783)

    gestion_localidad_784 = Localidad()
    gestion_localidad_784.cod_postal = '5893'
    gestion_localidad_784.localidad = 'ISLA VERDE'
    gestion_localidad_784.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_784 = importer.save_or_locate(gestion_localidad_784)

    gestion_localidad_785 = Localidad()
    gestion_localidad_785.cod_postal = '2559'
    gestion_localidad_785.localidad = 'ISLETA NEGRA'
    gestion_localidad_785.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_785 = importer.save_or_locate(gestion_localidad_785)

    gestion_localidad_786 = Localidad()
    gestion_localidad_786.cod_postal = '6271'
    gestion_localidad_786.localidad = 'ITALO'
    gestion_localidad_786.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_786 = importer.save_or_locate(gestion_localidad_786)

    gestion_localidad_787 = Localidad()
    gestion_localidad_787.cod_postal = '5203'
    gestion_localidad_787.localidad = 'ITI HUASI'
    gestion_localidad_787.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_787 = importer.save_or_locate(gestion_localidad_787)

    gestion_localidad_788 = Localidad()
    gestion_localidad_788.cod_postal = '5218'
    gestion_localidad_788.localidad = 'JAIME PETER'
    gestion_localidad_788.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_788 = importer.save_or_locate(gestion_localidad_788)

    gestion_localidad_789 = Localidad()
    gestion_localidad_789.cod_postal = '5984'
    gestion_localidad_789.localidad = 'JAMES CRAIK'
    gestion_localidad_789.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_789 = importer.save_or_locate(gestion_localidad_789)

    gestion_localidad_790 = Localidad()
    gestion_localidad_790.cod_postal = '5209'
    gestion_localidad_790.localidad = 'JARILLAS'
    gestion_localidad_790.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_790 = importer.save_or_locate(gestion_localidad_790)

    gestion_localidad_791 = Localidad()
    gestion_localidad_791.cod_postal = '2424'
    gestion_localidad_791.localidad = 'JEANMAIRE'
    gestion_localidad_791.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_791 = importer.save_or_locate(gestion_localidad_791)

    gestion_localidad_792 = Localidad()
    gestion_localidad_792.cod_postal = '5141'
    gestion_localidad_792.localidad = 'JERONIMO CORTES'
    gestion_localidad_792.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_792 = importer.save_or_locate(gestion_localidad_792)

    gestion_localidad_793 = Localidad()
    gestion_localidad_793.cod_postal = '5220'
    gestion_localidad_793.localidad = 'JESUS MARIA'
    gestion_localidad_793.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_793 = importer.save_or_locate(gestion_localidad_793)

    gestion_localidad_794 = Localidad()
    gestion_localidad_794.cod_postal = '5189'
    gestion_localidad_794.localidad = 'JOSE DE LA QUINTANA'
    gestion_localidad_794.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_794 = importer.save_or_locate(gestion_localidad_794)

    gestion_localidad_795 = Localidad()
    gestion_localidad_795.cod_postal = '6127'
    gestion_localidad_795.localidad = 'JOVITA'
    gestion_localidad_795.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_795 = importer.save_or_locate(gestion_localidad_795)

    gestion_localidad_796 = Localidad()
    gestion_localidad_796.cod_postal = '5891'
    gestion_localidad_796.localidad = 'JUAN BAUTISTA ALBERDI'
    gestion_localidad_796.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_796 = importer.save_or_locate(gestion_localidad_796)

    gestion_localidad_797 = Localidad()
    gestion_localidad_797.cod_postal = '5212'
    gestion_localidad_797.localidad = 'JUAN GARCIA'
    gestion_localidad_797.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_797 = importer.save_or_locate(gestion_localidad_797)

    gestion_localidad_798 = Localidad()
    gestion_localidad_798.cod_postal = '5145'
    gestion_localidad_798.localidad = 'JUAREZ CELMAN'
    gestion_localidad_798.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_798 = importer.save_or_locate(gestion_localidad_798)

    gestion_localidad_799 = Localidad()
    gestion_localidad_799.cod_postal = '6134'
    gestion_localidad_799.localidad = 'JULIO ARGENTINO ROCA'
    gestion_localidad_799.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_799 = importer.save_or_locate(gestion_localidad_799)

    gestion_localidad_800 = Localidad()
    gestion_localidad_800.cod_postal = '5209'
    gestion_localidad_800.localidad = 'JUME'
    gestion_localidad_800.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_800 = importer.save_or_locate(gestion_localidad_800)

    gestion_localidad_801 = Localidad()
    gestion_localidad_801.cod_postal = '2553'
    gestion_localidad_801.localidad = 'JUSTINIANO POSSE'
    gestion_localidad_801.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_801 = importer.save_or_locate(gestion_localidad_801)

    gestion_localidad_802 = Localidad()
    gestion_localidad_802.cod_postal = '2625'
    gestion_localidad_802.localidad = 'KILEGRUMAN'
    gestion_localidad_802.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_802 = importer.save_or_locate(gestion_localidad_802)

    gestion_localidad_803 = Localidad()
    gestion_localidad_803.cod_postal = '5107'
    gestion_localidad_803.localidad = 'KILOMETRO 25'
    gestion_localidad_803.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_803 = importer.save_or_locate(gestion_localidad_803)

    gestion_localidad_804 = Localidad()
    gestion_localidad_804.cod_postal = '5123'
    gestion_localidad_804.localidad = 'KILOMETRO 25 LA CARBONADA'
    gestion_localidad_804.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_804 = importer.save_or_locate(gestion_localidad_804)

    gestion_localidad_805 = Localidad()
    gestion_localidad_805.cod_postal = '5901'
    gestion_localidad_805.localidad = 'KILOMETRO 267'
    gestion_localidad_805.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_805 = importer.save_or_locate(gestion_localidad_805)

    gestion_localidad_806 = Localidad()
    gestion_localidad_806.cod_postal = '5139'
    gestion_localidad_806.localidad = 'KILOMETRO 271'
    gestion_localidad_806.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_806 = importer.save_or_locate(gestion_localidad_806)

    gestion_localidad_807 = Localidad()
    gestion_localidad_807.cod_postal = '5137'
    gestion_localidad_807.localidad = 'KILOMETRO 294'
    gestion_localidad_807.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_807 = importer.save_or_locate(gestion_localidad_807)

    gestion_localidad_808 = Localidad()
    gestion_localidad_808.cod_postal = '5137'
    gestion_localidad_808.localidad = 'KILOMETRO 316'
    gestion_localidad_808.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_808 = importer.save_or_locate(gestion_localidad_808)

    gestion_localidad_809 = Localidad()
    gestion_localidad_809.cod_postal = '5229'
    gestion_localidad_809.localidad = 'KILOMETRO 364'
    gestion_localidad_809.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_809 = importer.save_or_locate(gestion_localidad_809)

    gestion_localidad_810 = Localidad()
    gestion_localidad_810.cod_postal = '5238'
    gestion_localidad_810.localidad = 'KILOMETRO 394'
    gestion_localidad_810.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_810 = importer.save_or_locate(gestion_localidad_810)

    gestion_localidad_811 = Localidad()
    gestion_localidad_811.cod_postal = '5200'
    gestion_localidad_811.localidad = 'KILOMETRO 430'
    gestion_localidad_811.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_811 = importer.save_or_locate(gestion_localidad_811)

    gestion_localidad_812 = Localidad()
    gestion_localidad_812.cod_postal = '5218'
    gestion_localidad_812.localidad = 'KILOMETRO 450'
    gestion_localidad_812.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_812 = importer.save_or_locate(gestion_localidad_812)

    gestion_localidad_813 = Localidad()
    gestion_localidad_813.cod_postal = '5280'
    gestion_localidad_813.localidad = 'KILOMETRO 505'
    gestion_localidad_813.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_813 = importer.save_or_locate(gestion_localidad_813)

    gestion_localidad_814 = Localidad()
    gestion_localidad_814.cod_postal = '2424'
    gestion_localidad_814.localidad = 'KILOMETRO 531'
    gestion_localidad_814.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_814 = importer.save_or_locate(gestion_localidad_814)

    gestion_localidad_815 = Localidad()
    gestion_localidad_815.cod_postal = '5284'
    gestion_localidad_815.localidad = 'KILOMETRO 541'
    gestion_localidad_815.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_815 = importer.save_or_locate(gestion_localidad_815)

    gestion_localidad_816 = Localidad()
    gestion_localidad_816.cod_postal = '6142'
    gestion_localidad_816.localidad = 'KILOMETRO 545'
    gestion_localidad_816.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_816 = importer.save_or_locate(gestion_localidad_816)

    gestion_localidad_817 = Localidad()
    gestion_localidad_817.cod_postal = '6121'
    gestion_localidad_817.localidad = 'KILOMETRO 55'
    gestion_localidad_817.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_817 = importer.save_or_locate(gestion_localidad_817)

    gestion_localidad_818 = Localidad()
    gestion_localidad_818.cod_postal = '2619'
    gestion_localidad_818.localidad = 'KILOMETRO 57'
    gestion_localidad_818.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_818 = importer.save_or_locate(gestion_localidad_818)

    gestion_localidad_819 = Localidad()
    gestion_localidad_819.cod_postal = '5168'
    gestion_localidad_819.localidad = 'KILOMETRO 579'
    gestion_localidad_819.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_819 = importer.save_or_locate(gestion_localidad_819)

    gestion_localidad_820 = Localidad()
    gestion_localidad_820.cod_postal = '2428'
    gestion_localidad_820.localidad = 'KILOMETRO 581'
    gestion_localidad_820.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_820 = importer.save_or_locate(gestion_localidad_820)

    gestion_localidad_821 = Localidad()
    gestion_localidad_821.cod_postal = '5166'
    gestion_localidad_821.localidad = 'KILOMETRO 592'
    gestion_localidad_821.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_821 = importer.save_or_locate(gestion_localidad_821)

    gestion_localidad_822 = Localidad()
    gestion_localidad_822.cod_postal = '5149'
    gestion_localidad_822.localidad = 'KILOMETRO 608'
    gestion_localidad_822.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_822 = importer.save_or_locate(gestion_localidad_822)

    gestion_localidad_823 = Localidad()
    gestion_localidad_823.cod_postal = '5125'
    gestion_localidad_823.localidad = 'KILOMETRO 658'
    gestion_localidad_823.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_823 = importer.save_or_locate(gestion_localidad_823)

    gestion_localidad_824 = Localidad()
    gestion_localidad_824.cod_postal = '5123'
    gestion_localidad_824.localidad = 'KILOMETRO 679'
    gestion_localidad_824.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_824 = importer.save_or_locate(gestion_localidad_824)

    gestion_localidad_825 = Localidad()
    gestion_localidad_825.cod_postal = '5123'
    gestion_localidad_825.localidad = 'KILOMETRO 680 RUTA 9'
    gestion_localidad_825.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_825 = importer.save_or_locate(gestion_localidad_825)

    gestion_localidad_826 = Localidad()
    gestion_localidad_826.cod_postal = '5125'
    gestion_localidad_826.localidad = 'KILOMETRO 691'
    gestion_localidad_826.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_826 = importer.save_or_locate(gestion_localidad_826)

    gestion_localidad_827 = Localidad()
    gestion_localidad_827.cod_postal = '5123'
    gestion_localidad_827.localidad = 'KILOMETRO 692'
    gestion_localidad_827.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_827 = importer.save_or_locate(gestion_localidad_827)

    gestion_localidad_828 = Localidad()
    gestion_localidad_828.cod_postal = '5125'
    gestion_localidad_828.localidad = 'KILOMETRO 711'
    gestion_localidad_828.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_828 = importer.save_or_locate(gestion_localidad_828)

    gestion_localidad_829 = Localidad()
    gestion_localidad_829.cod_postal = '5145'
    gestion_localidad_829.localidad = 'KILOMETRO 730'
    gestion_localidad_829.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_829 = importer.save_or_locate(gestion_localidad_829)

    gestion_localidad_830 = Localidad()
    gestion_localidad_830.cod_postal = '5220'
    gestion_localidad_830.localidad = 'KILOMETRO 745'
    gestion_localidad_830.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_830 = importer.save_or_locate(gestion_localidad_830)

    gestion_localidad_831 = Localidad()
    gestion_localidad_831.cod_postal = '5212'
    gestion_localidad_831.localidad = 'KILOMETRO 784'
    gestion_localidad_831.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_831 = importer.save_or_locate(gestion_localidad_831)

    gestion_localidad_832 = Localidad()
    gestion_localidad_832.cod_postal = '5212'
    gestion_localidad_832.localidad = 'KILOMETRO 807'
    gestion_localidad_832.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_832 = importer.save_or_locate(gestion_localidad_832)

    gestion_localidad_833 = Localidad()
    gestion_localidad_833.cod_postal = '5212'
    gestion_localidad_833.localidad = 'KILOMETRO 827'
    gestion_localidad_833.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_833 = importer.save_or_locate(gestion_localidad_833)

    gestion_localidad_834 = Localidad()
    gestion_localidad_834.cod_postal = '5200'
    gestion_localidad_834.localidad = 'KILOMETRO 832'
    gestion_localidad_834.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_834 = importer.save_or_locate(gestion_localidad_834)

    gestion_localidad_835 = Localidad()
    gestion_localidad_835.cod_postal = '5214'
    gestion_localidad_835.localidad = 'KILOMETRO 859'
    gestion_localidad_835.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_835 = importer.save_or_locate(gestion_localidad_835)

    gestion_localidad_836 = Localidad()
    gestion_localidad_836.cod_postal = '5214'
    gestion_localidad_836.localidad = 'KILOMETRO 865'
    gestion_localidad_836.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_836 = importer.save_or_locate(gestion_localidad_836)

    gestion_localidad_837 = Localidad()
    gestion_localidad_837.cod_postal = '5214'
    gestion_localidad_837.localidad = 'KILOMETRO 881'
    gestion_localidad_837.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_837 = importer.save_or_locate(gestion_localidad_837)

    gestion_localidad_838 = Localidad()
    gestion_localidad_838.cod_postal = '5216'
    gestion_localidad_838.localidad = 'KILOMETRO 907'
    gestion_localidad_838.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_838 = importer.save_or_locate(gestion_localidad_838)

    gestion_localidad_839 = Localidad()
    gestion_localidad_839.cod_postal = '5216'
    gestion_localidad_839.localidad = 'KILOMETRO 931'
    gestion_localidad_839.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_839 = importer.save_or_locate(gestion_localidad_839)

    gestion_localidad_840 = Localidad()
    gestion_localidad_840.cod_postal = '5281'
    gestion_localidad_840.localidad = 'LA ABRA'
    gestion_localidad_840.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_840 = importer.save_or_locate(gestion_localidad_840)

    gestion_localidad_841 = Localidad()
    gestion_localidad_841.cod_postal = '5211'
    gestion_localidad_841.localidad = 'LA AGUADA'
    gestion_localidad_841.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_841 = importer.save_or_locate(gestion_localidad_841)

    gestion_localidad_842 = Localidad()
    gestion_localidad_842.cod_postal = '5212'
    gestion_localidad_842.localidad = 'LA AGUADA'
    gestion_localidad_842.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_842 = importer.save_or_locate(gestion_localidad_842)

    gestion_localidad_843 = Localidad()
    gestion_localidad_843.cod_postal = '5285'
    gestion_localidad_843.localidad = 'LA AGUADA'
    gestion_localidad_843.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_843 = importer.save_or_locate(gestion_localidad_843)

    gestion_localidad_844 = Localidad()
    gestion_localidad_844.cod_postal = '5801'
    gestion_localidad_844.localidad = 'LA AGUADA'
    gestion_localidad_844.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_844 = importer.save_or_locate(gestion_localidad_844)

    gestion_localidad_845 = Localidad()
    gestion_localidad_845.cod_postal = '5299'
    gestion_localidad_845.localidad = 'LA AGUADITA'
    gestion_localidad_845.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_845 = importer.save_or_locate(gestion_localidad_845)

    gestion_localidad_846 = Localidad()
    gestion_localidad_846.cod_postal = '5887'
    gestion_localidad_846.localidad = 'LA AGUADITA'
    gestion_localidad_846.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_846 = importer.save_or_locate(gestion_localidad_846)

    gestion_localidad_847 = Localidad()
    gestion_localidad_847.cod_postal = '5293'
    gestion_localidad_847.localidad = 'LA ARGENTINA'
    gestion_localidad_847.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_847 = importer.save_or_locate(gestion_localidad_847)

    gestion_localidad_848 = Localidad()
    gestion_localidad_848.cod_postal = '5218'
    gestion_localidad_848.localidad = 'LA AURA'
    gestion_localidad_848.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_848 = importer.save_or_locate(gestion_localidad_848)

    gestion_localidad_849 = Localidad()
    gestion_localidad_849.cod_postal = '5249'
    gestion_localidad_849.localidad = 'LA BANDA'
    gestion_localidad_849.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_849 = importer.save_or_locate(gestion_localidad_849)

    gestion_localidad_850 = Localidad()
    gestion_localidad_850.cod_postal = '5214'
    gestion_localidad_850.localidad = 'LA BARRANCA'
    gestion_localidad_850.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_850 = importer.save_or_locate(gestion_localidad_850)

    gestion_localidad_851 = Localidad()
    gestion_localidad_851.cod_postal = '5248'
    gestion_localidad_851.localidad = 'LA BARRANCA'
    gestion_localidad_851.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_851 = importer.save_or_locate(gestion_localidad_851)

    gestion_localidad_852 = Localidad()
    gestion_localidad_852.cod_postal = '5833'
    gestion_localidad_852.localidad = 'LA BARRANQUITA'
    gestion_localidad_852.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_852 = importer.save_or_locate(gestion_localidad_852)

    gestion_localidad_853 = Localidad()
    gestion_localidad_853.cod_postal = '5201'
    gestion_localidad_853.localidad = 'LA BATALLA'
    gestion_localidad_853.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_853 = importer.save_or_locate(gestion_localidad_853)

    gestion_localidad_854 = Localidad()
    gestion_localidad_854.cod_postal = '5270'
    gestion_localidad_854.localidad = 'LA BATEA'
    gestion_localidad_854.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_854 = importer.save_or_locate(gestion_localidad_854)

    gestion_localidad_855 = Localidad()
    gestion_localidad_855.cod_postal = '5189'
    gestion_localidad_855.localidad = 'LA BETANIA'
    gestion_localidad_855.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_855 = importer.save_or_locate(gestion_localidad_855)

    gestion_localidad_856 = Localidad()
    gestion_localidad_856.cod_postal = '5291'
    gestion_localidad_856.localidad = 'LA BISMUTINA'
    gestion_localidad_856.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_856 = importer.save_or_locate(gestion_localidad_856)

    gestion_localidad_857 = Localidad()
    gestion_localidad_857.cod_postal = '2657'
    gestion_localidad_857.localidad = 'LABORDE'
    gestion_localidad_857.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_857 = importer.save_or_locate(gestion_localidad_857)

    gestion_localidad_858 = Localidad()
    gestion_localidad_858.cod_postal = '5214'
    gestion_localidad_858.localidad = 'LA BOTIJA'
    gestion_localidad_858.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_858 = importer.save_or_locate(gestion_localidad_858)

    gestion_localidad_859 = Localidad()
    gestion_localidad_859.cod_postal = '6120'
    gestion_localidad_859.localidad = 'LABOULAYE'
    gestion_localidad_859.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_859 = importer.save_or_locate(gestion_localidad_859)

    gestion_localidad_860 = Localidad()
    gestion_localidad_860.cod_postal = '5848'
    gestion_localidad_860.localidad = 'LA BRIANZA'
    gestion_localidad_860.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_860 = importer.save_or_locate(gestion_localidad_860)

    gestion_localidad_861 = Localidad()
    gestion_localidad_861.cod_postal = '5129'
    gestion_localidad_861.localidad = 'LA BUENA PARADA'
    gestion_localidad_861.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_861 = importer.save_or_locate(gestion_localidad_861)

    gestion_localidad_862 = Localidad()
    gestion_localidad_862.cod_postal = '2563'
    gestion_localidad_862.localidad = 'LA CAJUELA'
    gestion_localidad_862.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_862 = importer.save_or_locate(gestion_localidad_862)

    gestion_localidad_863 = Localidad()
    gestion_localidad_863.cod_postal = '5297'
    gestion_localidad_863.localidad = 'LA CALERA'
    gestion_localidad_863.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_863 = importer.save_or_locate(gestion_localidad_863)

    gestion_localidad_864 = Localidad()
    gestion_localidad_864.cod_postal = '5813'
    gestion_localidad_864.localidad = 'LA CALERA'
    gestion_localidad_864.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_864 = importer.save_or_locate(gestion_localidad_864)

    gestion_localidad_865 = Localidad()
    gestion_localidad_865.cod_postal = '5819'
    gestion_localidad_865.localidad = 'LA CALERA'
    gestion_localidad_865.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_865 = importer.save_or_locate(gestion_localidad_865)

    gestion_localidad_866 = Localidad()
    gestion_localidad_866.cod_postal = '5218'
    gestion_localidad_866.localidad = 'LA CALERA'
    gestion_localidad_866.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_866 = importer.save_or_locate(gestion_localidad_866)

    gestion_localidad_867 = Localidad()
    gestion_localidad_867.cod_postal = '5151'
    gestion_localidad_867.localidad = 'LA CALERA'
    gestion_localidad_867.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_867 = importer.save_or_locate(gestion_localidad_867)

    gestion_localidad_868 = Localidad()
    gestion_localidad_868.cod_postal = '5168'
    gestion_localidad_868.localidad = 'LA CANTERA'
    gestion_localidad_868.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_868 = importer.save_or_locate(gestion_localidad_868)

    gestion_localidad_869 = Localidad()
    gestion_localidad_869.cod_postal = '5870'
    gestion_localidad_869.localidad = 'LA CAÑADA'
    gestion_localidad_869.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_869 = importer.save_or_locate(gestion_localidad_869)

    gestion_localidad_870 = Localidad()
    gestion_localidad_870.cod_postal = '5155'
    gestion_localidad_870.localidad = 'LA CAÑADA'
    gestion_localidad_870.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_870 = importer.save_or_locate(gestion_localidad_870)

    gestion_localidad_871 = Localidad()
    gestion_localidad_871.cod_postal = '5101'
    gestion_localidad_871.localidad = 'LA CAÑADA'
    gestion_localidad_871.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_871 = importer.save_or_locate(gestion_localidad_871)

    gestion_localidad_872 = Localidad()
    gestion_localidad_872.cod_postal = '5231'
    gestion_localidad_872.localidad = 'LA CAÑADA'
    gestion_localidad_872.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_872 = importer.save_or_locate(gestion_localidad_872)

    gestion_localidad_873 = Localidad()
    gestion_localidad_873.cod_postal = '5218'
    gestion_localidad_873.localidad = 'LA CAÑADA ANGOSTA'
    gestion_localidad_873.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_873 = importer.save_or_locate(gestion_localidad_873)

    gestion_localidad_874 = Localidad()
    gestion_localidad_874.cod_postal = '5803'
    gestion_localidad_874.localidad = 'LA CAÑADA GRANDE'
    gestion_localidad_874.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_874 = importer.save_or_locate(gestion_localidad_874)

    gestion_localidad_875 = Localidad()
    gestion_localidad_875.cod_postal = '5201'
    gestion_localidad_875.localidad = 'LA CAÑADA SANTA CRUZ'
    gestion_localidad_875.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_875 = importer.save_or_locate(gestion_localidad_875)

    gestion_localidad_876 = Localidad()
    gestion_localidad_876.cod_postal = '5280'
    gestion_localidad_876.localidad = 'LA CARBONERA'
    gestion_localidad_876.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_876 = importer.save_or_locate(gestion_localidad_876)

    gestion_localidad_877 = Localidad()
    gestion_localidad_877.cod_postal = '2670'
    gestion_localidad_877.localidad = 'LA CARLOTA'
    gestion_localidad_877.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_877 = importer.save_or_locate(gestion_localidad_877)

    gestion_localidad_878 = Localidad()
    gestion_localidad_878.cod_postal = '5841'
    gestion_localidad_878.localidad = 'LA CAROLINA'
    gestion_localidad_878.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_878 = importer.save_or_locate(gestion_localidad_878)

    gestion_localidad_879 = Localidad()
    gestion_localidad_879.cod_postal = '5854'
    gestion_localidad_879.localidad = 'LA CASCADA'
    gestion_localidad_879.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_879 = importer.save_or_locate(gestion_localidad_879)

    gestion_localidad_880 = Localidad()
    gestion_localidad_880.cod_postal = '6142'
    gestion_localidad_880.localidad = 'LA CAUTIVA'
    gestion_localidad_880.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_880 = importer.save_or_locate(gestion_localidad_880)

    gestion_localidad_881 = Localidad()
    gestion_localidad_881.cod_postal = '5125'
    gestion_localidad_881.localidad = 'LA CELINA'
    gestion_localidad_881.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_881 = importer.save_or_locate(gestion_localidad_881)

    gestion_localidad_882 = Localidad()
    gestion_localidad_882.cod_postal = '6101'
    gestion_localidad_882.localidad = 'LA CESIRA'
    gestion_localidad_882.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_882 = importer.save_or_locate(gestion_localidad_882)

    gestion_localidad_883 = Localidad()
    gestion_localidad_883.cod_postal = '5212'
    gestion_localidad_883.localidad = 'LA CHACRA'
    gestion_localidad_883.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_883 = importer.save_or_locate(gestion_localidad_883)

    gestion_localidad_884 = Localidad()
    gestion_localidad_884.cod_postal = '5249'
    gestion_localidad_884.localidad = 'LA CHICHARRA'
    gestion_localidad_884.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_884 = importer.save_or_locate(gestion_localidad_884)

    gestion_localidad_885 = Localidad()
    gestion_localidad_885.cod_postal = '5196'
    gestion_localidad_885.localidad = 'LA CHOZA'
    gestion_localidad_885.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_885 = importer.save_or_locate(gestion_localidad_885)

    gestion_localidad_886 = Localidad()
    gestion_localidad_886.cod_postal = '5133'
    gestion_localidad_886.localidad = 'LA CIENAGA'
    gestion_localidad_886.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_886 = importer.save_or_locate(gestion_localidad_886)

    gestion_localidad_887 = Localidad()
    gestion_localidad_887.cod_postal = '5893'
    gestion_localidad_887.localidad = 'LA COCHA'
    gestion_localidad_887.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_887 = importer.save_or_locate(gestion_localidad_887)

    gestion_localidad_888 = Localidad()
    gestion_localidad_888.cod_postal = '5101'
    gestion_localidad_888.localidad = 'LA COCHA'
    gestion_localidad_888.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_888 = importer.save_or_locate(gestion_localidad_888)

    gestion_localidad_889 = Localidad()
    gestion_localidad_889.cod_postal = '5201'
    gestion_localidad_889.localidad = 'LA COLONIA'
    gestion_localidad_889.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_889 = importer.save_or_locate(gestion_localidad_889)

    gestion_localidad_890 = Localidad()
    gestion_localidad_890.cod_postal = '5831'
    gestion_localidad_890.localidad = 'LA COLORADA'
    gestion_localidad_890.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_890 = importer.save_or_locate(gestion_localidad_890)

    gestion_localidad_891 = Localidad()
    gestion_localidad_891.cod_postal = '5871'
    gestion_localidad_891.localidad = 'LA COMPASION'
    gestion_localidad_891.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_891 = importer.save_or_locate(gestion_localidad_891)

    gestion_localidad_892 = Localidad()
    gestion_localidad_892.cod_postal = '5281'
    gestion_localidad_892.localidad = 'LA CONCEPCION'
    gestion_localidad_892.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_892 = importer.save_or_locate(gestion_localidad_892)

    gestion_localidad_893 = Localidad()
    gestion_localidad_893.cod_postal = '5870'
    gestion_localidad_893.localidad = 'LA CONCEPCION'
    gestion_localidad_893.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_893 = importer.save_or_locate(gestion_localidad_893)

    gestion_localidad_894 = Localidad()
    gestion_localidad_894.cod_postal = '2434'
    gestion_localidad_894.localidad = 'LA CORTADERA'
    gestion_localidad_894.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_894 = importer.save_or_locate(gestion_localidad_894)

    gestion_localidad_895 = Localidad()
    gestion_localidad_895.cod_postal = '5871'
    gestion_localidad_895.localidad = 'LA CORTADERA'
    gestion_localidad_895.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_895 = importer.save_or_locate(gestion_localidad_895)

    gestion_localidad_896 = Localidad()
    gestion_localidad_896.cod_postal = '5282'
    gestion_localidad_896.localidad = 'LA COSTA'
    gestion_localidad_896.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_896 = importer.save_or_locate(gestion_localidad_896)

    gestion_localidad_897 = Localidad()
    gestion_localidad_897.cod_postal = '5885'
    gestion_localidad_897.localidad = 'LA COSTA'
    gestion_localidad_897.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_897 = importer.save_or_locate(gestion_localidad_897)

    gestion_localidad_898 = Localidad()
    gestion_localidad_898.cod_postal = '5244'
    gestion_localidad_898.localidad = 'LA COSTA'
    gestion_localidad_898.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_898 = importer.save_or_locate(gestion_localidad_898)

    gestion_localidad_899 = Localidad()
    gestion_localidad_899.cod_postal = '5249'
    gestion_localidad_899.localidad = 'LA COSTA'
    gestion_localidad_899.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_899 = importer.save_or_locate(gestion_localidad_899)

    gestion_localidad_900 = Localidad()
    gestion_localidad_900.cod_postal = '5220'
    gestion_localidad_900.localidad = 'LA COTITA'
    gestion_localidad_900.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_900 = importer.save_or_locate(gestion_localidad_900)

    gestion_localidad_901 = Localidad()
    gestion_localidad_901.cod_postal = '5859'
    gestion_localidad_901.localidad = 'LA CRUZ'
    gestion_localidad_901.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_901 = importer.save_or_locate(gestion_localidad_901)

    gestion_localidad_902 = Localidad()
    gestion_localidad_902.cod_postal = '5249'
    gestion_localidad_902.localidad = 'LA CRUZ'
    gestion_localidad_902.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_902 = importer.save_or_locate(gestion_localidad_902)

    gestion_localidad_903 = Localidad()
    gestion_localidad_903.cod_postal = '5178'
    gestion_localidad_903.localidad = 'LA CUMBRE'
    gestion_localidad_903.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_903 = importer.save_or_locate(gestion_localidad_903)

    gestion_localidad_904 = Localidad()
    gestion_localidad_904.cod_postal = '5801'
    gestion_localidad_904.localidad = 'LA CUMBRE'
    gestion_localidad_904.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_904 = importer.save_or_locate(gestion_localidad_904)

    gestion_localidad_905 = Localidad()
    gestion_localidad_905.cod_postal = '5194'
    gestion_localidad_905.localidad = 'LA CUMBRECITA'
    gestion_localidad_905.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_905 = importer.save_or_locate(gestion_localidad_905)

    gestion_localidad_906 = Localidad()
    gestion_localidad_906.cod_postal = '2434'
    gestion_localidad_906.localidad = 'LA CURVA'
    gestion_localidad_906.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_906 = importer.save_or_locate(gestion_localidad_906)

    gestion_localidad_907 = Localidad()
    gestion_localidad_907.cod_postal = '5246'
    gestion_localidad_907.localidad = 'LADERA YACUS'
    gestion_localidad_907.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_907 = importer.save_or_locate(gestion_localidad_907)

    gestion_localidad_908 = Localidad()
    gestion_localidad_908.cod_postal = '5229'
    gestion_localidad_908.localidad = 'LA DORA'
    gestion_localidad_908.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_908 = importer.save_or_locate(gestion_localidad_908)

    gestion_localidad_909 = Localidad()
    gestion_localidad_909.cod_postal = '5817'
    gestion_localidad_909.localidad = 'LA DORMIDA'
    gestion_localidad_909.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_909 = importer.save_or_locate(gestion_localidad_909)

    gestion_localidad_910 = Localidad()
    gestion_localidad_910.cod_postal = '5209'
    gestion_localidad_910.localidad = 'LA ESPERANZA'
    gestion_localidad_910.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_910 = importer.save_or_locate(gestion_localidad_910)

    gestion_localidad_911 = Localidad()
    gestion_localidad_911.cod_postal = '5231'
    gestion_localidad_911.localidad = 'LA ESPERANZA'
    gestion_localidad_911.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_911 = importer.save_or_locate(gestion_localidad_911)

    gestion_localidad_912 = Localidad()
    gestion_localidad_912.cod_postal = '5295'
    gestion_localidad_912.localidad = 'LA ESQUINA'
    gestion_localidad_912.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_912 = importer.save_or_locate(gestion_localidad_912)

    gestion_localidad_913 = Localidad()
    gestion_localidad_913.cod_postal = '5801'
    gestion_localidad_913.localidad = 'LA ESQUINA'
    gestion_localidad_913.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_913 = importer.save_or_locate(gestion_localidad_913)

    gestion_localidad_914 = Localidad()
    gestion_localidad_914.cod_postal = '5212'
    gestion_localidad_914.localidad = 'LA ESTACADA'
    gestion_localidad_914.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_914 = importer.save_or_locate(gestion_localidad_914)

    gestion_localidad_915 = Localidad()
    gestion_localidad_915.cod_postal = '5291'
    gestion_localidad_915.localidad = 'LA ESTANCIA'
    gestion_localidad_915.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_915 = importer.save_or_locate(gestion_localidad_915)

    gestion_localidad_916 = Localidad()
    gestion_localidad_916.cod_postal = '5249'
    gestion_localidad_916.localidad = 'LA ESTANCIA'
    gestion_localidad_916.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_916 = importer.save_or_locate(gestion_localidad_916)

    gestion_localidad_917 = Localidad()
    gestion_localidad_917.cod_postal = '5111'
    gestion_localidad_917.localidad = 'LA ESTANCITA'
    gestion_localidad_917.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_917 = importer.save_or_locate(gestion_localidad_917)

    gestion_localidad_918 = Localidad()
    gestion_localidad_918.cod_postal = '5129'
    gestion_localidad_918.localidad = 'LA ESTRELLA'
    gestion_localidad_918.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_918 = importer.save_or_locate(gestion_localidad_918)

    gestion_localidad_919 = Localidad()
    gestion_localidad_919.cod_postal = '5172'
    gestion_localidad_919.localidad = 'LA FALDA'
    gestion_localidad_919.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_919 = importer.save_or_locate(gestion_localidad_919)

    gestion_localidad_920 = Localidad()
    gestion_localidad_920.cod_postal = '5214'
    gestion_localidad_920.localidad = 'LA FLORIDA'
    gestion_localidad_920.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_920 = importer.save_or_locate(gestion_localidad_920)

    gestion_localidad_921 = Localidad()
    gestion_localidad_921.cod_postal = '5281'
    gestion_localidad_921.localidad = 'LA FLORIDA'
    gestion_localidad_921.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_921 = importer.save_or_locate(gestion_localidad_921)

    gestion_localidad_922 = Localidad()
    gestion_localidad_922.cod_postal = '2426'
    gestion_localidad_922.localidad = 'LA FRANCIA'
    gestion_localidad_922.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_922 = importer.save_or_locate(gestion_localidad_922)

    gestion_localidad_923 = Localidad()
    gestion_localidad_923.cod_postal = '5282'
    gestion_localidad_923.localidad = 'LA FRONDA'
    gestion_localidad_923.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_923 = importer.save_or_locate(gestion_localidad_923)

    gestion_localidad_924 = Localidad()
    gestion_localidad_924.cod_postal = '2433'
    gestion_localidad_924.localidad = 'LA FRONTERA'
    gestion_localidad_924.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_924 = importer.save_or_locate(gestion_localidad_924)

    gestion_localidad_925 = Localidad()
    gestion_localidad_925.cod_postal = '5879'
    gestion_localidad_925.localidad = 'LA FUENTE'
    gestion_localidad_925.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_925 = importer.save_or_locate(gestion_localidad_925)

    gestion_localidad_926 = Localidad()
    gestion_localidad_926.cod_postal = '5848'
    gestion_localidad_926.localidad = 'LA GILDA'
    gestion_localidad_926.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_926 = importer.save_or_locate(gestion_localidad_926)

    gestion_localidad_927 = Localidad()
    gestion_localidad_927.cod_postal = '5282'
    gestion_localidad_927.localidad = 'LA GRAMILLA'
    gestion_localidad_927.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_927 = importer.save_or_locate(gestion_localidad_927)

    gestion_localidad_928 = Localidad()
    gestion_localidad_928.cod_postal = '5187'
    gestion_localidad_928.localidad = 'LA GRANADILLA'
    gestion_localidad_928.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_928 = importer.save_or_locate(gestion_localidad_928)

    gestion_localidad_929 = Localidad()
    gestion_localidad_929.cod_postal = '5115'
    gestion_localidad_929.localidad = 'LA GRANJA'
    gestion_localidad_929.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_929 = importer.save_or_locate(gestion_localidad_929)

    gestion_localidad_930 = Localidad()
    gestion_localidad_930.cod_postal = '5889'
    gestion_localidad_930.localidad = 'LA GRUTA'
    gestion_localidad_930.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_930 = importer.save_or_locate(gestion_localidad_930)

    gestion_localidad_931 = Localidad()
    gestion_localidad_931.cod_postal = '5891'
    gestion_localidad_931.localidad = 'LA GUARDIA'
    gestion_localidad_931.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_931 = importer.save_or_locate(gestion_localidad_931)

    gestion_localidad_932 = Localidad()
    gestion_localidad_932.cod_postal = '5244'
    gestion_localidad_932.localidad = 'LAGUNA BRAVA'
    gestion_localidad_932.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_932 = importer.save_or_locate(gestion_localidad_932)

    gestion_localidad_933 = Localidad()
    gestion_localidad_933.cod_postal = '5813'
    gestion_localidad_933.localidad = 'LAGUNA CLARA'
    gestion_localidad_933.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_933 = importer.save_or_locate(gestion_localidad_933)

    gestion_localidad_934 = Localidad()
    gestion_localidad_934.cod_postal = '5244'
    gestion_localidad_934.localidad = 'LAGUNA DE GOMEZ'
    gestion_localidad_934.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_934 = importer.save_or_locate(gestion_localidad_934)

    gestion_localidad_935 = Localidad()
    gestion_localidad_935.cod_postal = '5974'
    gestion_localidad_935.localidad = 'LAGUNA LARGA'
    gestion_localidad_935.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_935 = importer.save_or_locate(gestion_localidad_935)

    gestion_localidad_936 = Localidad()
    gestion_localidad_936.cod_postal = '5988'
    gestion_localidad_936.localidad = 'LAGUNA LARGA SUD'
    gestion_localidad_936.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_936 = importer.save_or_locate(gestion_localidad_936)

    gestion_localidad_937 = Localidad()
    gestion_localidad_937.cod_postal = '6144'
    gestion_localidad_937.localidad = 'LAGUNA OSCURA'
    gestion_localidad_937.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_937 = importer.save_or_locate(gestion_localidad_937)

    gestion_localidad_938 = Localidad()
    gestion_localidad_938.cod_postal = '5829'
    gestion_localidad_938.localidad = 'LAGUNA SECA'
    gestion_localidad_938.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_938 = importer.save_or_locate(gestion_localidad_938)

    gestion_localidad_939 = Localidad()
    gestion_localidad_939.cod_postal = '5101'
    gestion_localidad_939.localidad = 'LAGUNILLA'
    gestion_localidad_939.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_939 = importer.save_or_locate(gestion_localidad_939)

    gestion_localidad_940 = Localidad()
    gestion_localidad_940.cod_postal = '5972'
    gestion_localidad_940.localidad = 'LAGUNILLA'
    gestion_localidad_940.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_940 = importer.save_or_locate(gestion_localidad_940)

    gestion_localidad_941 = Localidad()
    gestion_localidad_941.cod_postal = '5807'
    gestion_localidad_941.localidad = 'LAGUNILLAS'
    gestion_localidad_941.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_941 = importer.save_or_locate(gestion_localidad_941)

    gestion_localidad_942 = Localidad()
    gestion_localidad_942.cod_postal = '5900'
    gestion_localidad_942.localidad = 'LA HERRADURA'
    gestion_localidad_942.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_942 = importer.save_or_locate(gestion_localidad_942)

    gestion_localidad_943 = Localidad()
    gestion_localidad_943.cod_postal = '5285'
    gestion_localidad_943.localidad = 'LA HIGUERA'
    gestion_localidad_943.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_943 = importer.save_or_locate(gestion_localidad_943)

    gestion_localidad_944 = Localidad()
    gestion_localidad_944.cod_postal = '5201'
    gestion_localidad_944.localidad = 'LA HIGUERITA'
    gestion_localidad_944.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_944 = importer.save_or_locate(gestion_localidad_944)

    gestion_localidad_945 = Localidad()
    gestion_localidad_945.cod_postal = '5244'
    gestion_localidad_945.localidad = 'LA HIGUERITA'
    gestion_localidad_945.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_945 = importer.save_or_locate(gestion_localidad_945)

    gestion_localidad_946 = Localidad()
    gestion_localidad_946.cod_postal = '5801'
    gestion_localidad_946.localidad = 'LA INVERNADA'
    gestion_localidad_946.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_946 = importer.save_or_locate(gestion_localidad_946)

    gestion_localidad_947 = Localidad()
    gestion_localidad_947.cod_postal = '5200'
    gestion_localidad_947.localidad = 'LA ISABELA'
    gestion_localidad_947.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_947 = importer.save_or_locate(gestion_localidad_947)

    gestion_localidad_948 = Localidad()
    gestion_localidad_948.cod_postal = '5186'
    gestion_localidad_948.localidad = 'LA ISLA'
    gestion_localidad_948.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_948 = importer.save_or_locate(gestion_localidad_948)

    gestion_localidad_949 = Localidad()
    gestion_localidad_949.cod_postal = '5963'
    gestion_localidad_949.localidad = 'LA ISLETA'
    gestion_localidad_949.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_949 = importer.save_or_locate(gestion_localidad_949)

    gestion_localidad_950 = Localidad()
    gestion_localidad_950.cod_postal = '5186'
    gestion_localidad_950.localidad = 'LA ISOLINA'
    gestion_localidad_950.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_950 = importer.save_or_locate(gestion_localidad_950)

    gestion_localidad_951 = Localidad()
    gestion_localidad_951.cod_postal = '2651'
    gestion_localidad_951.localidad = 'LA ITALIANA'
    gestion_localidad_951.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_951 = importer.save_or_locate(gestion_localidad_951)

    gestion_localidad_952 = Localidad()
    gestion_localidad_952.cod_postal = '5871'
    gestion_localidad_952.localidad = 'LA JARILLA'
    gestion_localidad_952.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_952 = importer.save_or_locate(gestion_localidad_952)

    gestion_localidad_953 = Localidad()
    gestion_localidad_953.cod_postal = '5205'
    gestion_localidad_953.localidad = 'LA LAGUNA'
    gestion_localidad_953.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_953 = importer.save_or_locate(gestion_localidad_953)

    gestion_localidad_954 = Localidad()
    gestion_localidad_954.cod_postal = '5284'
    gestion_localidad_954.localidad = 'LA LAGUNA'
    gestion_localidad_954.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_954 = importer.save_or_locate(gestion_localidad_954)

    gestion_localidad_955 = Localidad()
    gestion_localidad_955.cod_postal = '5901'
    gestion_localidad_955.localidad = 'LA LAGUNA'
    gestion_localidad_955.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_955 = importer.save_or_locate(gestion_localidad_955)

    gestion_localidad_956 = Localidad()
    gestion_localidad_956.cod_postal = '5119'
    gestion_localidad_956.localidad = 'LA LAGUNILLA'
    gestion_localidad_956.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_956 = importer.save_or_locate(gestion_localidad_956)

    gestion_localidad_957 = Localidad()
    gestion_localidad_957.cod_postal = '5825'
    gestion_localidad_957.localidad = 'LA LAGUNILLA'
    gestion_localidad_957.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_957 = importer.save_or_locate(gestion_localidad_957)

    gestion_localidad_958 = Localidad()
    gestion_localidad_958.cod_postal = '5281'
    gestion_localidad_958.localidad = 'LA LILIA'
    gestion_localidad_958.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_958 = importer.save_or_locate(gestion_localidad_958)

    gestion_localidad_959 = Localidad()
    gestion_localidad_959.cod_postal = '5871'
    gestion_localidad_959.localidad = 'LA LINEA'
    gestion_localidad_959.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_959 = importer.save_or_locate(gestion_localidad_959)

    gestion_localidad_960 = Localidad()
    gestion_localidad_960.cod_postal = '6271'
    gestion_localidad_960.localidad = 'LA LUZ'
    gestion_localidad_960.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_960 = importer.save_or_locate(gestion_localidad_960)

    gestion_localidad_961 = Localidad()
    gestion_localidad_961.cod_postal = '5887'
    gestion_localidad_961.localidad = 'LA MAJADA'
    gestion_localidad_961.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_961 = importer.save_or_locate(gestion_localidad_961)

    gestion_localidad_962 = Localidad()
    gestion_localidad_962.cod_postal = '5212'
    gestion_localidad_962.localidad = 'LA MAJADA'
    gestion_localidad_962.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_962 = importer.save_or_locate(gestion_localidad_962)

    gestion_localidad_963 = Localidad()
    gestion_localidad_963.cod_postal = '5231'
    gestion_localidad_963.localidad = 'LA MAZA'
    gestion_localidad_963.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_963 = importer.save_or_locate(gestion_localidad_963)

    gestion_localidad_964 = Localidad()
    gestion_localidad_964.cod_postal = '5841'
    gestion_localidad_964.localidad = 'LA MERCANTIL'
    gestion_localidad_964.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_964 = importer.save_or_locate(gestion_localidad_964)

    gestion_localidad_965 = Localidad()
    gestion_localidad_965.cod_postal = '5200'
    gestion_localidad_965.localidad = 'LA MESADA'
    gestion_localidad_965.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_965 = importer.save_or_locate(gestion_localidad_965)

    gestion_localidad_966 = Localidad()
    gestion_localidad_966.cod_postal = '5801'
    gestion_localidad_966.localidad = 'LA MESADA'
    gestion_localidad_966.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_966 = importer.save_or_locate(gestion_localidad_966)

    gestion_localidad_967 = Localidad()
    gestion_localidad_967.cod_postal = '5285'
    gestion_localidad_967.localidad = 'LA MESILLA'
    gestion_localidad_967.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_967 = importer.save_or_locate(gestion_localidad_967)

    gestion_localidad_968 = Localidad()
    gestion_localidad_968.cod_postal = '2400'
    gestion_localidad_968.localidad = 'LA MILKA'
    gestion_localidad_968.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_968 = importer.save_or_locate(gestion_localidad_968)

    gestion_localidad_969 = Localidad()
    gestion_localidad_969.cod_postal = '5137'
    gestion_localidad_969.localidad = 'LA MOSTAZA'
    gestion_localidad_969.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_969 = importer.save_or_locate(gestion_localidad_969)

    gestion_localidad_970 = Localidad()
    gestion_localidad_970.cod_postal = '5299'
    gestion_localidad_970.localidad = 'LA MUDANA'
    gestion_localidad_970.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_970 = importer.save_or_locate(gestion_localidad_970)

    gestion_localidad_971 = Localidad()
    gestion_localidad_971.cod_postal = '6275'
    gestion_localidad_971.localidad = 'LA NACIONAL'
    gestion_localidad_971.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_971 = importer.save_or_locate(gestion_localidad_971)

    gestion_localidad_972 = Localidad()
    gestion_localidad_972.cod_postal = '5255'
    gestion_localidad_972.localidad = 'LA OSCURIDAD'
    gestion_localidad_972.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_972 = importer.save_or_locate(gestion_localidad_972)

    gestion_localidad_973 = Localidad()
    gestion_localidad_973.cod_postal = '5186'
    gestion_localidad_973.localidad = 'LA PAISANITA'
    gestion_localidad_973.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_973 = importer.save_or_locate(gestion_localidad_973)

    gestion_localidad_974 = Localidad()
    gestion_localidad_974.cod_postal = '5925'
    gestion_localidad_974.localidad = 'LA PALESTINA'
    gestion_localidad_974.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_974 = importer.save_or_locate(gestion_localidad_974)

    gestion_localidad_975 = Localidad()
    gestion_localidad_975.cod_postal = '5231'
    gestion_localidad_975.localidad = 'LA PALMA'
    gestion_localidad_975.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_975 = importer.save_or_locate(gestion_localidad_975)

    gestion_localidad_976 = Localidad()
    gestion_localidad_976.cod_postal = '5913'
    gestion_localidad_976.localidad = 'LA PALMERINA'
    gestion_localidad_976.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_976 = importer.save_or_locate(gestion_localidad_976)

    gestion_localidad_977 = Localidad()
    gestion_localidad_977.cod_postal = '5117'
    gestion_localidad_977.localidad = 'LA PAMPA'
    gestion_localidad_977.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_977 = importer.save_or_locate(gestion_localidad_977)

    gestion_localidad_978 = Localidad()
    gestion_localidad_978.cod_postal = '2417'
    gestion_localidad_978.localidad = 'LA PAQUITA'
    gestion_localidad_978.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_978 = importer.save_or_locate(gestion_localidad_978)

    gestion_localidad_979 = Localidad()
    gestion_localidad_979.cod_postal = '5137'
    gestion_localidad_979.localidad = 'LA PARA'
    gestion_localidad_979.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_979 = importer.save_or_locate(gestion_localidad_979)

    gestion_localidad_980 = Localidad()
    gestion_localidad_980.cod_postal = '5871'
    gestion_localidad_980.localidad = 'LA PATRIA'
    gestion_localidad_980.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_980 = importer.save_or_locate(gestion_localidad_980)

    gestion_localidad_981 = Localidad()
    gestion_localidad_981.cod_postal = '5117'
    gestion_localidad_981.localidad = 'LA PAZ'
    gestion_localidad_981.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_981 = importer.save_or_locate(gestion_localidad_981)

    gestion_localidad_982 = Localidad()
    gestion_localidad_982.cod_postal = '5879'
    gestion_localidad_982.localidad = 'LA PAZ'
    gestion_localidad_982.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_982 = importer.save_or_locate(gestion_localidad_982)

    gestion_localidad_983 = Localidad()
    gestion_localidad_983.cod_postal = '5231'
    gestion_localidad_983.localidad = 'LA PENCA'
    gestion_localidad_983.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_983 = importer.save_or_locate(gestion_localidad_983)

    gestion_localidad_984 = Localidad()
    gestion_localidad_984.cod_postal = '6279'
    gestion_localidad_984.localidad = 'LA PENCA'
    gestion_localidad_984.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_984 = importer.save_or_locate(gestion_localidad_984)

    gestion_localidad_985 = Localidad()
    gestion_localidad_985.cod_postal = '6271'
    gestion_localidad_985.localidad = 'LA PERLITA'
    gestion_localidad_985.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_985 = importer.save_or_locate(gestion_localidad_985)

    gestion_localidad_986 = Localidad()
    gestion_localidad_986.cod_postal = '5246'
    gestion_localidad_986.localidad = 'LA PIEDRA BLANCA'
    gestion_localidad_986.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_986 = importer.save_or_locate(gestion_localidad_986)

    gestion_localidad_987 = Localidad()
    gestion_localidad_987.cod_postal = '5184'
    gestion_localidad_987.localidad = 'LA PIEDRA MOVEDIZA'
    gestion_localidad_987.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_987 = importer.save_or_locate(gestion_localidad_987)

    gestion_localidad_988 = Localidad()
    gestion_localidad_988.cod_postal = '5248'
    gestion_localidad_988.localidad = 'LA PINTADA'
    gestion_localidad_988.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_988 = importer.save_or_locate(gestion_localidad_988)

    gestion_localidad_989 = Localidad()
    gestion_localidad_989.cod_postal = '5271'
    gestion_localidad_989.localidad = 'LA PINTADA'
    gestion_localidad_989.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_989 = importer.save_or_locate(gestion_localidad_989)

    gestion_localidad_990 = Localidad()
    gestion_localidad_990.cod_postal = '5285'
    gestion_localidad_990.localidad = 'LA PLAYA'
    gestion_localidad_990.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_990 = importer.save_or_locate(gestion_localidad_990)

    gestion_localidad_991 = Localidad()
    gestion_localidad_991.cod_postal = '5911'
    gestion_localidad_991.localidad = 'LA PLAYOSA'
    gestion_localidad_991.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_991 = importer.save_or_locate(gestion_localidad_991)

    gestion_localidad_992 = Localidad()
    gestion_localidad_992.cod_postal = '5244'
    gestion_localidad_992.localidad = 'LA PLAZA'
    gestion_localidad_992.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_992 = importer.save_or_locate(gestion_localidad_992)

    gestion_localidad_993 = Localidad()
    gestion_localidad_993.cod_postal = '5875'
    gestion_localidad_993.localidad = 'LA POBLACION'
    gestion_localidad_993.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_993 = importer.save_or_locate(gestion_localidad_993)

    gestion_localidad_994 = Localidad()
    gestion_localidad_994.cod_postal = '5945'
    gestion_localidad_994.localidad = 'LA POBLADORA'
    gestion_localidad_994.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_994 = importer.save_or_locate(gestion_localidad_994)

    gestion_localidad_995 = Localidad()
    gestion_localidad_995.cod_postal = '5119'
    gestion_localidad_995.localidad = 'LA PORFIA'
    gestion_localidad_995.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_995 = importer.save_or_locate(gestion_localidad_995)

    gestion_localidad_996 = Localidad()
    gestion_localidad_996.cod_postal = '5221'
    gestion_localidad_996.localidad = 'LA PORTEÑA'
    gestion_localidad_996.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_996 = importer.save_or_locate(gestion_localidad_996)

    gestion_localidad_997 = Localidad()
    gestion_localidad_997.cod_postal = '5227'
    gestion_localidad_997.localidad = 'LA POSTA'
    gestion_localidad_997.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_997 = importer.save_or_locate(gestion_localidad_997)

    gestion_localidad_998 = Localidad()
    gestion_localidad_998.cod_postal = '5201'
    gestion_localidad_998.localidad = 'LA POSTA CHUÑAGUAS'
    gestion_localidad_998.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_998 = importer.save_or_locate(gestion_localidad_998)

    gestion_localidad_999 = Localidad()
    gestion_localidad_999.cod_postal = '5139'
    gestion_localidad_999.localidad = 'LA PRIMAVERA'
    gestion_localidad_999.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_999 = importer.save_or_locate(gestion_localidad_999)

    gestion_localidad_1000 = Localidad()
    gestion_localidad_1000.cod_postal = '5231'
    gestion_localidad_1000.localidad = 'LA PROVIDENCIA'
    gestion_localidad_1000.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1000 = importer.save_or_locate(gestion_localidad_1000)

    gestion_localidad_1001 = Localidad()
    gestion_localidad_1001.cod_postal = '5281'
    gestion_localidad_1001.localidad = 'LA PUERTA'
    gestion_localidad_1001.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1001 = importer.save_or_locate(gestion_localidad_1001)

    gestion_localidad_1002 = Localidad()
    gestion_localidad_1002.cod_postal = '5101'
    gestion_localidad_1002.localidad = 'LA PUERTA'
    gestion_localidad_1002.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1002 = importer.save_or_locate(gestion_localidad_1002)

    gestion_localidad_1003 = Localidad()
    gestion_localidad_1003.cod_postal = '5137'
    gestion_localidad_1003.localidad = 'LA PUERTA'
    gestion_localidad_1003.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1003 = importer.save_or_locate(gestion_localidad_1003)

    gestion_localidad_1004 = Localidad()
    gestion_localidad_1004.cod_postal = '5284'
    gestion_localidad_1004.localidad = 'LA PUERTA VILLA DE SOTO'
    gestion_localidad_1004.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1004 = importer.save_or_locate(gestion_localidad_1004)

    gestion_localidad_1005 = Localidad()
    gestion_localidad_1005.cod_postal = '5107'
    gestion_localidad_1005.localidad = 'LA QUEBRADA'
    gestion_localidad_1005.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1005 = importer.save_or_locate(gestion_localidad_1005)

    gestion_localidad_1006 = Localidad()
    gestion_localidad_1006.cod_postal = '5297'
    gestion_localidad_1006.localidad = 'LA QUEBRADA'
    gestion_localidad_1006.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1006 = importer.save_or_locate(gestion_localidad_1006)

    gestion_localidad_1007 = Localidad()
    gestion_localidad_1007.cod_postal = '5172'
    gestion_localidad_1007.localidad = 'LA QUEBRADA'
    gestion_localidad_1007.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1007 = importer.save_or_locate(gestion_localidad_1007)

    gestion_localidad_1008 = Localidad()
    gestion_localidad_1008.cod_postal = '5135'
    gestion_localidad_1008.localidad = 'LA QUINTA'
    gestion_localidad_1008.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1008 = importer.save_or_locate(gestion_localidad_1008)

    gestion_localidad_1009 = Localidad()
    gestion_localidad_1009.cod_postal = '5887'
    gestion_localidad_1009.localidad = 'LA QUINTA'
    gestion_localidad_1009.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1009 = importer.save_or_locate(gestion_localidad_1009)

    gestion_localidad_1010 = Localidad()
    gestion_localidad_1010.cod_postal = '5209'
    gestion_localidad_1010.localidad = 'LA QUINTA'
    gestion_localidad_1010.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1010 = importer.save_or_locate(gestion_localidad_1010)

    gestion_localidad_1011 = Localidad()
    gestion_localidad_1011.cod_postal = '5249'
    gestion_localidad_1011.localidad = 'LA QUINTANA'
    gestion_localidad_1011.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1011 = importer.save_or_locate(gestion_localidad_1011)

    gestion_localidad_1012 = Localidad()
    gestion_localidad_1012.cod_postal = '6123'
    gestion_localidad_1012.localidad = 'LA RAMADA'
    gestion_localidad_1012.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1012 = importer.save_or_locate(gestion_localidad_1012)

    gestion_localidad_1013 = Localidad()
    gestion_localidad_1013.cod_postal = '5875'
    gestion_localidad_1013.localidad = 'LA RAMADA'
    gestion_localidad_1013.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1013 = importer.save_or_locate(gestion_localidad_1013)

    gestion_localidad_1014 = Localidad()
    gestion_localidad_1014.cod_postal = '5813'
    gestion_localidad_1014.localidad = 'LA RAMONCITA'
    gestion_localidad_1014.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1014 = importer.save_or_locate(gestion_localidad_1014)

    gestion_localidad_1015 = Localidad()
    gestion_localidad_1015.cod_postal = '5105'
    gestion_localidad_1015.localidad = 'LA REDENCION'
    gestion_localidad_1015.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1015 = importer.save_or_locate(gestion_localidad_1015)

    gestion_localidad_1016 = Localidad()
    gestion_localidad_1016.cod_postal = '2594'
    gestion_localidad_1016.localidad = 'LA REDUCCION'
    gestion_localidad_1016.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1016 = importer.save_or_locate(gestion_localidad_1016)

    gestion_localidad_1017 = Localidad()
    gestion_localidad_1017.cod_postal = '5105'
    gestion_localidad_1017.localidad = 'LA REDUCCION'
    gestion_localidad_1017.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1017 = importer.save_or_locate(gestion_localidad_1017)

    gestion_localidad_1018 = Localidad()
    gestion_localidad_1018.cod_postal = '5925'
    gestion_localidad_1018.localidad = 'LA REINA'
    gestion_localidad_1018.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1018 = importer.save_or_locate(gestion_localidad_1018)

    gestion_localidad_1019 = Localidad()
    gestion_localidad_1019.cod_postal = '2436'
    gestion_localidad_1019.localidad = 'LA REPRESA'
    gestion_localidad_1019.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1019 = importer.save_or_locate(gestion_localidad_1019)

    gestion_localidad_1020 = Localidad()
    gestion_localidad_1020.cod_postal = '5233'
    gestion_localidad_1020.localidad = 'LA RINCONADA'
    gestion_localidad_1020.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1020 = importer.save_or_locate(gestion_localidad_1020)

    gestion_localidad_1021 = Localidad()
    gestion_localidad_1021.cod_postal = '5249'
    gestion_localidad_1021.localidad = 'LA RINCONADA CANDELARIA'
    gestion_localidad_1021.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1021 = importer.save_or_locate(gestion_localidad_1021)

    gestion_localidad_1022 = Localidad()
    gestion_localidad_1022.cod_postal = '5951'
    gestion_localidad_1022.localidad = 'LA ROSARINA'
    gestion_localidad_1022.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1022 = importer.save_or_locate(gestion_localidad_1022)

    gestion_localidad_1023 = Localidad()
    gestion_localidad_1023.cod_postal = '6275'
    gestion_localidad_1023.localidad = 'LARSEN'
    gestion_localidad_1023.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1023 = importer.save_or_locate(gestion_localidad_1023)

    gestion_localidad_1024 = Localidad()
    gestion_localidad_1024.cod_postal = '5214'
    gestion_localidad_1024.localidad = 'LA RUDA'
    gestion_localidad_1024.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1024 = importer.save_or_locate(gestion_localidad_1024)

    gestion_localidad_1025 = Localidad()
    gestion_localidad_1025.cod_postal = '5801'
    gestion_localidad_1025.localidad = 'LAS ABAHACAS'
    gestion_localidad_1025.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1025 = importer.save_or_locate(gestion_localidad_1025)

    gestion_localidad_1026 = Localidad()
    gestion_localidad_1026.cod_postal = '5270'
    gestion_localidad_1026.localidad = 'LAS ABRAS'
    gestion_localidad_1026.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1026 = importer.save_or_locate(gestion_localidad_1026)

    gestion_localidad_1027 = Localidad()
    gestion_localidad_1027.cod_postal = '5129'
    gestion_localidad_1027.localidad = 'LAS ACACIAS'
    gestion_localidad_1027.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1027 = importer.save_or_locate(gestion_localidad_1027)

    gestion_localidad_1028 = Localidad()
    gestion_localidad_1028.cod_postal = '5848'
    gestion_localidad_1028.localidad = 'LAS ACEQUIAS'
    gestion_localidad_1028.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1028 = importer.save_or_locate(gestion_localidad_1028)

    gestion_localidad_1029 = Localidad()
    gestion_localidad_1029.cod_postal = '5201'
    gestion_localidad_1029.localidad = 'LAS AGUADITAS'
    gestion_localidad_1029.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1029 = importer.save_or_locate(gestion_localidad_1029)

    gestion_localidad_1030 = Localidad()
    gestion_localidad_1030.cod_postal = '5801'
    gestion_localidad_1030.localidad = 'LAS ALBAHACAS'
    gestion_localidad_1030.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1030 = importer.save_or_locate(gestion_localidad_1030)

    gestion_localidad_1031 = Localidad()
    gestion_localidad_1031.cod_postal = '5270'
    gestion_localidad_1031.localidad = 'LAS ALERAS'
    gestion_localidad_1031.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1031 = importer.save_or_locate(gestion_localidad_1031)

    gestion_localidad_1032 = Localidad()
    gestion_localidad_1032.cod_postal = '5231'
    gestion_localidad_1032.localidad = 'LAS AROMAS'
    gestion_localidad_1032.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1032 = importer.save_or_locate(gestion_localidad_1032)

    gestion_localidad_1033 = Localidad()
    gestion_localidad_1033.cod_postal = '5231'
    gestion_localidad_1033.localidad = 'LAS ARRIAS'
    gestion_localidad_1033.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1033 = importer.save_or_locate(gestion_localidad_1033)

    gestion_localidad_1034 = Localidad()
    gestion_localidad_1034.cod_postal = '5220'
    gestion_localidad_1034.localidad = 'LAS ASTILLAS'
    gestion_localidad_1034.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1034 = importer.save_or_locate(gestion_localidad_1034)

    gestion_localidad_1035 = Localidad()
    gestion_localidad_1035.cod_postal = '5135'
    gestion_localidad_1035.localidad = 'LAS AVERIAS'
    gestion_localidad_1035.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1035 = importer.save_or_locate(gestion_localidad_1035)

    gestion_localidad_1036 = Localidad()
    gestion_localidad_1036.cod_postal = '5851'
    gestion_localidad_1036.localidad = 'LAS BAJADAS'
    gestion_localidad_1036.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1036 = importer.save_or_locate(gestion_localidad_1036)

    gestion_localidad_1037 = Localidad()
    gestion_localidad_1037.cod_postal = '5236'
    gestion_localidad_1037.localidad = 'LAS BANDURRIAS'
    gestion_localidad_1037.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1037 = importer.save_or_locate(gestion_localidad_1037)

    gestion_localidad_1038 = Localidad()
    gestion_localidad_1038.cod_postal = '5225'
    gestion_localidad_1038.localidad = 'LAS BANDURRIAS NORTE'
    gestion_localidad_1038.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1038 = importer.save_or_locate(gestion_localidad_1038)

    gestion_localidad_1039 = Localidad()
    gestion_localidad_1039.cod_postal = '5127'
    gestion_localidad_1039.localidad = 'LAS CABRAS'
    gestion_localidad_1039.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1039 = importer.save_or_locate(gestion_localidad_1039)

    gestion_localidad_1040 = Localidad()
    gestion_localidad_1040.cod_postal = '5801'
    gestion_localidad_1040.localidad = 'LAS CALECITAS'
    gestion_localidad_1040.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1040 = importer.save_or_locate(gestion_localidad_1040)

    gestion_localidad_1041 = Localidad()
    gestion_localidad_1041.cod_postal = '5819'
    gestion_localidad_1041.localidad = 'LAS CALERAS'
    gestion_localidad_1041.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1041 = importer.save_or_locate(gestion_localidad_1041)

    gestion_localidad_1042 = Localidad()
    gestion_localidad_1042.cod_postal = '5885'
    gestion_localidad_1042.localidad = 'LAS CALLES'
    gestion_localidad_1042.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1042 = importer.save_or_locate(gestion_localidad_1042)

    gestion_localidad_1043 = Localidad()
    gestion_localidad_1043.cod_postal = '5218'
    gestion_localidad_1043.localidad = 'LAS CANTERAS'
    gestion_localidad_1043.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1043 = importer.save_or_locate(gestion_localidad_1043)

    gestion_localidad_1044 = Localidad()
    gestion_localidad_1044.cod_postal = '5870'
    gestion_localidad_1044.localidad = 'LAS CAÑADAS'
    gestion_localidad_1044.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1044 = importer.save_or_locate(gestion_localidad_1044)

    gestion_localidad_1045 = Localidad()
    gestion_localidad_1045.cod_postal = '5284'
    gestion_localidad_1045.localidad = 'LAS CAÑADAS'
    gestion_localidad_1045.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1045 = importer.save_or_locate(gestion_localidad_1045)

    gestion_localidad_1046 = Localidad()
    gestion_localidad_1046.cod_postal = '5201'
    gestion_localidad_1046.localidad = 'LAS CAÑAS'
    gestion_localidad_1046.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1046 = importer.save_or_locate(gestion_localidad_1046)

    gestion_localidad_1047 = Localidad()
    gestion_localidad_1047.cod_postal = '5216'
    gestion_localidad_1047.localidad = 'LAS CAÑAS'
    gestion_localidad_1047.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1047 = importer.save_or_locate(gestion_localidad_1047)

    gestion_localidad_1048 = Localidad()
    gestion_localidad_1048.cod_postal = '5246'
    gestion_localidad_1048.localidad = 'LAS CAÑAS'
    gestion_localidad_1048.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1048 = importer.save_or_locate(gestion_localidad_1048)

    gestion_localidad_1049 = Localidad()
    gestion_localidad_1049.cod_postal = '5101'
    gestion_localidad_1049.localidad = 'LAS CAÑAS'
    gestion_localidad_1049.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1049 = importer.save_or_locate(gestion_localidad_1049)

    gestion_localidad_1050 = Localidad()
    gestion_localidad_1050.cod_postal = '2428'
    gestion_localidad_1050.localidad = 'LAS CAÑITAS'
    gestion_localidad_1050.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1050 = importer.save_or_locate(gestion_localidad_1050)

    gestion_localidad_1051 = Localidad()
    gestion_localidad_1051.cod_postal = '5801'
    gestion_localidad_1051.localidad = 'LAS CAÑITAS'
    gestion_localidad_1051.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1051 = importer.save_or_locate(gestion_localidad_1051)

    gestion_localidad_1052 = Localidad()
    gestion_localidad_1052.cod_postal = '5248'
    gestion_localidad_1052.localidad = 'LAS CARDAS'
    gestion_localidad_1052.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1052 = importer.save_or_locate(gestion_localidad_1052)

    gestion_localidad_1053 = Localidad()
    gestion_localidad_1053.cod_postal = '5158'
    gestion_localidad_1053.localidad = 'LAS CASITAS'
    gestion_localidad_1053.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1053 = importer.save_or_locate(gestion_localidad_1053)

    gestion_localidad_1054 = Localidad()
    gestion_localidad_1054.cod_postal = '5885'
    gestion_localidad_1054.localidad = 'LAS CEBOLLAS'
    gestion_localidad_1054.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1054 = importer.save_or_locate(gestion_localidad_1054)

    gestion_localidad_1055 = Localidad()
    gestion_localidad_1055.cod_postal = '5214'
    gestion_localidad_1055.localidad = 'LAS CHACRAS'
    gestion_localidad_1055.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1055 = importer.save_or_locate(gestion_localidad_1055)

    gestion_localidad_1056 = Localidad()
    gestion_localidad_1056.cod_postal = '5249'
    gestion_localidad_1056.localidad = 'LAS CHACRAS'
    gestion_localidad_1056.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1056 = importer.save_or_locate(gestion_localidad_1056)

    gestion_localidad_1057 = Localidad()
    gestion_localidad_1057.cod_postal = '5284'
    gestion_localidad_1057.localidad = 'LAS CHACRAS'
    gestion_localidad_1057.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1057 = importer.save_or_locate(gestion_localidad_1057)

    gestion_localidad_1058 = Localidad()
    gestion_localidad_1058.cod_postal = '5297'
    gestion_localidad_1058.localidad = 'LAS CHACRAS'
    gestion_localidad_1058.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1058 = importer.save_or_locate(gestion_localidad_1058)

    gestion_localidad_1059 = Localidad()
    gestion_localidad_1059.cod_postal = '5875'
    gestion_localidad_1059.localidad = 'LAS CHACRAS'
    gestion_localidad_1059.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1059 = importer.save_or_locate(gestion_localidad_1059)

    gestion_localidad_1060 = Localidad()
    gestion_localidad_1060.cod_postal = '5101'
    gestion_localidad_1060.localidad = 'LAS CHACRAS RUTA 111 KM 14'
    gestion_localidad_1060.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1060 = importer.save_or_locate(gestion_localidad_1060)

    gestion_localidad_1061 = Localidad()
    gestion_localidad_1061.cod_postal = '5841'
    gestion_localidad_1061.localidad = 'LAS CINCO CUADRAS'
    gestion_localidad_1061.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1061 = importer.save_or_locate(gestion_localidad_1061)

    gestion_localidad_1062 = Localidad()
    gestion_localidad_1062.cod_postal = '5885'
    gestion_localidad_1062.localidad = 'LAS CONANITAS'
    gestion_localidad_1062.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1062 = importer.save_or_locate(gestion_localidad_1062)

    gestion_localidad_1063 = Localidad()
    gestion_localidad_1063.cod_postal = '5249'
    gestion_localidad_1063.localidad = 'LAS CORTADERAS'
    gestion_localidad_1063.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1063 = importer.save_or_locate(gestion_localidad_1063)

    gestion_localidad_1064 = Localidad()
    gestion_localidad_1064.cod_postal = '5293'
    gestion_localidad_1064.localidad = 'LAS CORTADERAS'
    gestion_localidad_1064.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1064 = importer.save_or_locate(gestion_localidad_1064)

    gestion_localidad_1065 = Localidad()
    gestion_localidad_1065.cod_postal = '5295'
    gestion_localidad_1065.localidad = 'LAS CORTADERAS'
    gestion_localidad_1065.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1065 = importer.save_or_locate(gestion_localidad_1065)

    gestion_localidad_1066 = Localidad()
    gestion_localidad_1066.cod_postal = '5201'
    gestion_localidad_1066.localidad = 'LAS CRUCECITAS'
    gestion_localidad_1066.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1066 = importer.save_or_locate(gestion_localidad_1066)

    gestion_localidad_1067 = Localidad()
    gestion_localidad_1067.cod_postal = '5900'
    gestion_localidad_1067.localidad = 'LAS CUATRO ESQUINAS'
    gestion_localidad_1067.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1067 = importer.save_or_locate(gestion_localidad_1067)

    gestion_localidad_1068 = Localidad()
    gestion_localidad_1068.cod_postal = '5109'
    gestion_localidad_1068.localidad = 'LAS CUSENADAS'
    gestion_localidad_1068.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1068 = importer.save_or_locate(gestion_localidad_1068)

    gestion_localidad_1069 = Localidad()
    gestion_localidad_1069.cod_postal = '5212'
    gestion_localidad_1069.localidad = 'LAS DELICIAS'
    gestion_localidad_1069.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1069 = importer.save_or_locate(gestion_localidad_1069)

    gestion_localidad_1070 = Localidad()
    gestion_localidad_1070.cod_postal = '2433'
    gestion_localidad_1070.localidad = 'LAS DELICIAS'
    gestion_localidad_1070.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1070 = importer.save_or_locate(gestion_localidad_1070)

    gestion_localidad_1071 = Localidad()
    gestion_localidad_1071.cod_postal = '5212'
    gestion_localidad_1071.localidad = 'LA SELVA'
    gestion_localidad_1071.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1071 = importer.save_or_locate(gestion_localidad_1071)

    gestion_localidad_1072 = Localidad()
    gestion_localidad_1072.cod_postal = '5109'
    gestion_localidad_1072.localidad = 'LAS ENCADENADAS'
    gestion_localidad_1072.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1072 = importer.save_or_locate(gestion_localidad_1072)

    gestion_localidad_1073 = Localidad()
    gestion_localidad_1073.cod_postal = '5871'
    gestion_localidad_1073.localidad = 'LAS ENCRUCIJADAS'
    gestion_localidad_1073.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1073 = importer.save_or_locate(gestion_localidad_1073)

    gestion_localidad_1074 = Localidad()
    gestion_localidad_1074.cod_postal = '5825'
    gestion_localidad_1074.localidad = 'LAS ENSENADAS'
    gestion_localidad_1074.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1074 = importer.save_or_locate(gestion_localidad_1074)

    gestion_localidad_1075 = Localidad()
    gestion_localidad_1075.cod_postal = '5153'
    gestion_localidad_1075.localidad = 'LAS ENSENADAS'
    gestion_localidad_1075.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1075 = importer.save_or_locate(gestion_localidad_1075)

    gestion_localidad_1076 = Localidad()
    gestion_localidad_1076.cod_postal = '5189'
    gestion_localidad_1076.localidad = 'LA SERRANITA'
    gestion_localidad_1076.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1076 = importer.save_or_locate(gestion_localidad_1076)

    gestion_localidad_1077 = Localidad()
    gestion_localidad_1077.cod_postal = '5249'
    gestion_localidad_1077.localidad = 'LAS FLORES'
    gestion_localidad_1077.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1077 = importer.save_or_locate(gestion_localidad_1077)

    gestion_localidad_1078 = Localidad()
    gestion_localidad_1078.cod_postal = '5819'
    gestion_localidad_1078.localidad = 'LAS GAMAS'
    gestion_localidad_1078.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1078 = importer.save_or_locate(gestion_localidad_1078)

    gestion_localidad_1079 = Localidad()
    gestion_localidad_1079.cod_postal = '5184'
    gestion_localidad_1079.localidad = 'LAS GEMELAS'
    gestion_localidad_1079.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1079 = importer.save_or_locate(gestion_localidad_1079)

    gestion_localidad_1080 = Localidad()
    gestion_localidad_1080.cod_postal = '5246'
    gestion_localidad_1080.localidad = 'LAS GRAMILLAS'
    gestion_localidad_1080.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1080 = importer.save_or_locate(gestion_localidad_1080)

    gestion_localidad_1081 = Localidad()
    gestion_localidad_1081.cod_postal = '5135'
    gestion_localidad_1081.localidad = 'LAS GRAMILLAS'
    gestion_localidad_1081.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1081 = importer.save_or_locate(gestion_localidad_1081)

    gestion_localidad_1082 = Localidad()
    gestion_localidad_1082.cod_postal = '5801'
    gestion_localidad_1082.localidad = 'LAS GUINDAS'
    gestion_localidad_1082.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1082 = importer.save_or_locate(gestion_localidad_1082)

    gestion_localidad_1083 = Localidad()
    gestion_localidad_1083.cod_postal = '5101'
    gestion_localidad_1083.localidad = 'LAS HERAS'
    gestion_localidad_1083.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1083 = importer.save_or_locate(gestion_localidad_1083)

    gestion_localidad_1084 = Localidad()
    gestion_localidad_1084.cod_postal = '5805'
    gestion_localidad_1084.localidad = 'LAS HIGUERAS'
    gestion_localidad_1084.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1084 = importer.save_or_locate(gestion_localidad_1084)

    gestion_localidad_1085 = Localidad()
    gestion_localidad_1085.cod_postal = '5131'
    gestion_localidad_1085.localidad = 'LAS HIGUERILLAS'
    gestion_localidad_1085.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1085 = importer.save_or_locate(gestion_localidad_1085)

    gestion_localidad_1086 = Localidad()
    gestion_localidad_1086.cod_postal = '5186'
    gestion_localidad_1086.localidad = 'LAS HIGUERITAS'
    gestion_localidad_1086.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1086 = importer.save_or_locate(gestion_localidad_1086)

    gestion_localidad_1087 = Localidad()
    gestion_localidad_1087.cod_postal = '5199'
    gestion_localidad_1087.localidad = 'LAS HIGUERITAS'
    gestion_localidad_1087.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1087 = importer.save_or_locate(gestion_localidad_1087)

    gestion_localidad_1088 = Localidad()
    gestion_localidad_1088.cod_postal = '5137'
    gestion_localidad_1088.localidad = 'LAS HILERAS'
    gestion_localidad_1088.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1088 = importer.save_or_locate(gestion_localidad_1088)

    gestion_localidad_1089 = Localidad()
    gestion_localidad_1089.cod_postal = '5244'
    gestion_localidad_1089.localidad = 'LAS HORQUETAS'
    gestion_localidad_1089.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1089 = importer.save_or_locate(gestion_localidad_1089)

    gestion_localidad_1090 = Localidad()
    gestion_localidad_1090.cod_postal = '5875'
    gestion_localidad_1090.localidad = 'LA SIENA'
    gestion_localidad_1090.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1090 = importer.save_or_locate(gestion_localidad_1090)

    gestion_localidad_1091 = Localidad()
    gestion_localidad_1091.cod_postal = '5297'
    gestion_localidad_1091.localidad = 'LA SIERRITA'
    gestion_localidad_1091.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1091 = importer.save_or_locate(gestion_localidad_1091)

    gestion_localidad_1092 = Localidad()
    gestion_localidad_1092.cod_postal = '5813'
    gestion_localidad_1092.localidad = 'LA SIERRITA'
    gestion_localidad_1092.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1092 = importer.save_or_locate(gestion_localidad_1092)

    gestion_localidad_1093 = Localidad()
    gestion_localidad_1093.cod_postal = '5931'
    gestion_localidad_1093.localidad = 'LAS ISLETILLAS'
    gestion_localidad_1093.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1093 = importer.save_or_locate(gestion_localidad_1093)

    gestion_localidad_1094 = Localidad()
    gestion_localidad_1094.cod_postal = '5209'
    gestion_localidad_1094.localidad = 'LAS JARILLAS'
    gestion_localidad_1094.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1094 = importer.save_or_locate(gestion_localidad_1094)

    gestion_localidad_1095 = Localidad()
    gestion_localidad_1095.cod_postal = '5871'
    gestion_localidad_1095.localidad = 'LAS JARILLAS'
    gestion_localidad_1095.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1095 = importer.save_or_locate(gestion_localidad_1095)

    gestion_localidad_1096 = Localidad()
    gestion_localidad_1096.cod_postal = '5203'
    gestion_localidad_1096.localidad = 'LAS JUNTAS'
    gestion_localidad_1096.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1096 = importer.save_or_locate(gestion_localidad_1096)

    gestion_localidad_1097 = Localidad()
    gestion_localidad_1097.cod_postal = '5965'
    gestion_localidad_1097.localidad = 'LAS JUNTURAS'
    gestion_localidad_1097.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1097 = importer.save_or_locate(gestion_localidad_1097)

    gestion_localidad_1098 = Localidad()
    gestion_localidad_1098.cod_postal = '2568'
    gestion_localidad_1098.localidad = 'LAS LAGUNITAS'
    gestion_localidad_1098.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1098 = importer.save_or_locate(gestion_localidad_1098)

    gestion_localidad_1099 = Localidad()
    gestion_localidad_1099.cod_postal = '5272'
    gestion_localidad_1099.localidad = 'LAS LATAS'
    gestion_localidad_1099.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1099 = importer.save_or_locate(gestion_localidad_1099)

    gestion_localidad_1100 = Localidad()
    gestion_localidad_1100.cod_postal = '5284'
    gestion_localidad_1100.localidad = 'LAS LOMAS'
    gestion_localidad_1100.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1100 = importer.save_or_locate(gestion_localidad_1100)

    gestion_localidad_1101 = Localidad()
    gestion_localidad_1101.cod_postal = '5244'
    gestion_localidad_1101.localidad = 'LAS LOMITAS'
    gestion_localidad_1101.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1101 = importer.save_or_locate(gestion_localidad_1101)

    gestion_localidad_1102 = Localidad()
    gestion_localidad_1102.cod_postal = '5212'
    gestion_localidad_1102.localidad = 'LAS LOMITAS'
    gestion_localidad_1102.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1102 = importer.save_or_locate(gestion_localidad_1102)

    gestion_localidad_1103 = Localidad()
    gestion_localidad_1103.cod_postal = '5212'
    gestion_localidad_1103.localidad = 'LAS MANZANAS'
    gestion_localidad_1103.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1103 = importer.save_or_locate(gestion_localidad_1103)

    gestion_localidad_1104 = Localidad()
    gestion_localidad_1104.cod_postal = '5231'
    gestion_localidad_1104.localidad = 'LAS MASITAS'
    gestion_localidad_1104.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1104 = importer.save_or_locate(gestion_localidad_1104)

    gestion_localidad_1105 = Localidad()
    gestion_localidad_1105.cod_postal = '5249'
    gestion_localidad_1105.localidad = 'LAS MERCEDES'
    gestion_localidad_1105.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1105 = importer.save_or_locate(gestion_localidad_1105)

    gestion_localidad_1106 = Localidad()
    gestion_localidad_1106.cod_postal = '2572'
    gestion_localidad_1106.localidad = 'LAS MERCEDITAS'
    gestion_localidad_1106.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1106 = importer.save_or_locate(gestion_localidad_1106)

    gestion_localidad_1107 = Localidad()
    gestion_localidad_1107.cod_postal = '5909'
    gestion_localidad_1107.localidad = 'LAS MOJARRAS'
    gestion_localidad_1107.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1107 = importer.save_or_locate(gestion_localidad_1107)

    gestion_localidad_1108 = Localidad()
    gestion_localidad_1108.cod_postal = '5801'
    gestion_localidad_1108.localidad = 'LAS MORAS'
    gestion_localidad_1108.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1108 = importer.save_or_locate(gestion_localidad_1108)

    gestion_localidad_1109 = Localidad()
    gestion_localidad_1109.cod_postal = '5249'
    gestion_localidad_1109.localidad = 'LA SOLEDAD'
    gestion_localidad_1109.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1109 = importer.save_or_locate(gestion_localidad_1109)

    gestion_localidad_1110 = Localidad()
    gestion_localidad_1110.cod_postal = '5871'
    gestion_localidad_1110.localidad = 'LAS OSCURAS'
    gestion_localidad_1110.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1110 = importer.save_or_locate(gestion_localidad_1110)

    gestion_localidad_1111 = Localidad()
    gestion_localidad_1111.cod_postal = '2559'
    gestion_localidad_1111.localidad = 'LAS OVERIAS'
    gestion_localidad_1111.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1111 = importer.save_or_locate(gestion_localidad_1111)

    gestion_localidad_1112 = Localidad()
    gestion_localidad_1112.cod_postal = '5231'
    gestion_localidad_1112.localidad = 'LAS PALMAS'
    gestion_localidad_1112.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1112 = importer.save_or_locate(gestion_localidad_1112)

    gestion_localidad_1113 = Localidad()
    gestion_localidad_1113.cod_postal = '5201'
    gestion_localidad_1113.localidad = 'LAS PALMAS'
    gestion_localidad_1113.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1113 = importer.save_or_locate(gestion_localidad_1113)

    gestion_localidad_1114 = Localidad()
    gestion_localidad_1114.cod_postal = '5299'
    gestion_localidad_1114.localidad = 'LAS PALMAS'
    gestion_localidad_1114.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1114 = importer.save_or_locate(gestion_localidad_1114)

    gestion_localidad_1115 = Localidad()
    gestion_localidad_1115.cod_postal = '2559'
    gestion_localidad_1115.localidad = 'LAS PALMERAS'
    gestion_localidad_1115.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1115 = importer.save_or_locate(gestion_localidad_1115)

    gestion_localidad_1116 = Localidad()
    gestion_localidad_1116.cod_postal = '5889'
    gestion_localidad_1116.localidad = 'LAS PALMITAS'
    gestion_localidad_1116.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1116 = importer.save_or_locate(gestion_localidad_1116)

    gestion_localidad_1117 = Localidad()
    gestion_localidad_1117.cod_postal = '5227'
    gestion_localidad_1117.localidad = 'LAS PALMITAS'
    gestion_localidad_1117.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1117 = importer.save_or_locate(gestion_localidad_1117)

    gestion_localidad_1118 = Localidad()
    gestion_localidad_1118.cod_postal = '5221'
    gestion_localidad_1118.localidad = 'LAS PALMITAS'
    gestion_localidad_1118.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1118 = importer.save_or_locate(gestion_localidad_1118)

    gestion_localidad_1119 = Localidad()
    gestion_localidad_1119.cod_postal = '5870'
    gestion_localidad_1119.localidad = 'LAS PALOMAS'
    gestion_localidad_1119.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1119 = importer.save_or_locate(gestion_localidad_1119)

    gestion_localidad_1120 = Localidad()
    gestion_localidad_1120.cod_postal = '5201'
    gestion_localidad_1120.localidad = 'LAS PALOMITAS'
    gestion_localidad_1120.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1120 = importer.save_or_locate(gestion_localidad_1120)

    gestion_localidad_1121 = Localidad()
    gestion_localidad_1121.cod_postal = '5182'
    gestion_localidad_1121.localidad = 'LAS PAMPILLAS'
    gestion_localidad_1121.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1121 = importer.save_or_locate(gestion_localidad_1121)

    gestion_localidad_1122 = Localidad()
    gestion_localidad_1122.cod_postal = '5200'
    gestion_localidad_1122.localidad = 'LAS PENCAS'
    gestion_localidad_1122.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1122 = importer.save_or_locate(gestion_localidad_1122)

    gestion_localidad_1123 = Localidad()
    gestion_localidad_1123.cod_postal = '5238'
    gestion_localidad_1123.localidad = 'LAS PEÑAS'
    gestion_localidad_1123.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1123 = importer.save_or_locate(gestion_localidad_1123)

    gestion_localidad_1124 = Localidad()
    gestion_localidad_1124.cod_postal = '5817'
    gestion_localidad_1124.localidad = 'LAS PEÑAS'
    gestion_localidad_1124.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1124 = importer.save_or_locate(gestion_localidad_1124)

    gestion_localidad_1125 = Localidad()
    gestion_localidad_1125.cod_postal = '5823'
    gestion_localidad_1125.localidad = 'LAS PEÑAS NORTE'
    gestion_localidad_1125.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1125 = importer.save_or_locate(gestion_localidad_1125)

    gestion_localidad_1126 = Localidad()
    gestion_localidad_1126.cod_postal = '5819'
    gestion_localidad_1126.localidad = 'LAS PEÑAS SUD'
    gestion_localidad_1126.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1126 = importer.save_or_locate(gestion_localidad_1126)

    gestion_localidad_1127 = Localidad()
    gestion_localidad_1127.cod_postal = '5921'
    gestion_localidad_1127.localidad = 'LAS PERDICES'
    gestion_localidad_1127.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1127 = importer.save_or_locate(gestion_localidad_1127)

    gestion_localidad_1128 = Localidad()
    gestion_localidad_1128.cod_postal = '5900'
    gestion_localidad_1128.localidad = 'LAS PICHANAS'
    gestion_localidad_1128.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1128 = importer.save_or_locate(gestion_localidad_1128)

    gestion_localidad_1129 = Localidad()
    gestion_localidad_1129.cod_postal = '5212'
    gestion_localidad_1129.localidad = 'LAS PIEDRAS ANCHAS'
    gestion_localidad_1129.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1129 = importer.save_or_locate(gestion_localidad_1129)

    gestion_localidad_1130 = Localidad()
    gestion_localidad_1130.cod_postal = '5281'
    gestion_localidad_1130.localidad = 'LAS PIEDRITAS'
    gestion_localidad_1130.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1130 = importer.save_or_locate(gestion_localidad_1130)

    gestion_localidad_1131 = Localidad()
    gestion_localidad_1131.cod_postal = '5129'
    gestion_localidad_1131.localidad = 'LAS PIGUAS'
    gestion_localidad_1131.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1131 = importer.save_or_locate(gestion_localidad_1131)

    gestion_localidad_1132 = Localidad()
    gestion_localidad_1132.cod_postal = '5285'
    gestion_localidad_1132.localidad = 'LAS PLAYAS'
    gestion_localidad_1132.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1132 = importer.save_or_locate(gestion_localidad_1132)

    gestion_localidad_1133 = Localidad()
    gestion_localidad_1133.cod_postal = '5172'
    gestion_localidad_1133.localidad = 'LAS PLAYAS'
    gestion_localidad_1133.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1133 = importer.save_or_locate(gestion_localidad_1133)

    gestion_localidad_1134 = Localidad()
    gestion_localidad_1134.cod_postal = '5101'
    gestion_localidad_1134.localidad = 'LAS PLAYAS LOZADA'
    gestion_localidad_1134.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1134 = importer.save_or_locate(gestion_localidad_1134)

    gestion_localidad_1135 = Localidad()
    gestion_localidad_1135.cod_postal = '5244'
    gestion_localidad_1135.localidad = 'LAS QUINTAS'
    gestion_localidad_1135.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1135 = importer.save_or_locate(gestion_localidad_1135)

    gestion_localidad_1136 = Localidad()
    gestion_localidad_1136.cod_postal = '5885'
    gestion_localidad_1136.localidad = 'LAS RABONAS'
    gestion_localidad_1136.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1136 = importer.save_or_locate(gestion_localidad_1136)

    gestion_localidad_1137 = Localidad()
    gestion_localidad_1137.cod_postal = '5295'
    gestion_localidad_1137.localidad = 'LAS ROSAS'
    gestion_localidad_1137.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1137 = importer.save_or_locate(gestion_localidad_1137)

    gestion_localidad_1138 = Localidad()
    gestion_localidad_1138.cod_postal = '5137'
    gestion_localidad_1138.localidad = 'LAS SALADAS'
    gestion_localidad_1138.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1138 = importer.save_or_locate(gestion_localidad_1138)

    gestion_localidad_1139 = Localidad()
    gestion_localidad_1139.cod_postal = '5212'
    gestion_localidad_1139.localidad = 'LAS SIERRAS'
    gestion_localidad_1139.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1139 = importer.save_or_locate(gestion_localidad_1139)

    gestion_localidad_1140 = Localidad()
    gestion_localidad_1140.cod_postal = '5199'
    gestion_localidad_1140.localidad = 'LAS SIERRITAS'
    gestion_localidad_1140.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1140 = importer.save_or_locate(gestion_localidad_1140)

    gestion_localidad_1141 = Localidad()
    gestion_localidad_1141.cod_postal = '5885'
    gestion_localidad_1141.localidad = 'LAS TAPIAS'
    gestion_localidad_1141.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1141 = importer.save_or_locate(gestion_localidad_1141)

    gestion_localidad_1142 = Localidad()
    gestion_localidad_1142.cod_postal = '5281'
    gestion_localidad_1142.localidad = 'LAS TAPIAS'
    gestion_localidad_1142.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1142 = importer.save_or_locate(gestion_localidad_1142)

    gestion_localidad_1143 = Localidad()
    gestion_localidad_1143.cod_postal = '5801'
    gestion_localidad_1143.localidad = 'LAS TAPIAS'
    gestion_localidad_1143.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1143 = importer.save_or_locate(gestion_localidad_1143)

    gestion_localidad_1144 = Localidad()
    gestion_localidad_1144.cod_postal = '5284'
    gestion_localidad_1144.localidad = 'LAS TINAJERAS'
    gestion_localidad_1144.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1144 = importer.save_or_locate(gestion_localidad_1144)

    gestion_localidad_1145 = Localidad()
    gestion_localidad_1145.cod_postal = '5214'
    gestion_localidad_1145.localidad = 'LAS TOSCAS'
    gestion_localidad_1145.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1145 = importer.save_or_locate(gestion_localidad_1145)

    gestion_localidad_1146 = Localidad()
    gestion_localidad_1146.cod_postal = '5871'
    gestion_localidad_1146.localidad = 'LAS TOSCAS'
    gestion_localidad_1146.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1146 = importer.save_or_locate(gestion_localidad_1146)

    gestion_localidad_1147 = Localidad()
    gestion_localidad_1147.cod_postal = '5285'
    gestion_localidad_1147.localidad = 'LAS TOTORITAS'
    gestion_localidad_1147.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1147 = importer.save_or_locate(gestion_localidad_1147)

    gestion_localidad_1148 = Localidad()
    gestion_localidad_1148.cod_postal = '5246'
    gestion_localidad_1148.localidad = 'LAS TRANCAS'
    gestion_localidad_1148.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1148 = importer.save_or_locate(gestion_localidad_1148)

    gestion_localidad_1149 = Localidad()
    gestion_localidad_1149.cod_postal = '5879'
    gestion_localidad_1149.localidad = 'LAS TRES PIEDRAS'
    gestion_localidad_1149.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1149 = importer.save_or_locate(gestion_localidad_1149)

    gestion_localidad_1150 = Localidad()
    gestion_localidad_1150.cod_postal = '5218'
    gestion_localidad_1150.localidad = 'LAS TUSCAS'
    gestion_localidad_1150.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1150 = importer.save_or_locate(gestion_localidad_1150)

    gestion_localidad_1151 = Localidad()
    gestion_localidad_1151.cod_postal = '5184'
    gestion_localidad_1151.localidad = 'LAS VAQUERIAS'
    gestion_localidad_1151.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1151 = importer.save_or_locate(gestion_localidad_1151)

    gestion_localidad_1152 = Localidad()
    gestion_localidad_1152.cod_postal = '5941'
    gestion_localidad_1152.localidad = 'LAS VARAS'
    gestion_localidad_1152.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1152 = importer.save_or_locate(gestion_localidad_1152)

    gestion_localidad_1153 = Localidad()
    gestion_localidad_1153.cod_postal = '5940'
    gestion_localidad_1153.localidad = 'LAS VARILLAS'
    gestion_localidad_1153.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1153 = importer.save_or_locate(gestion_localidad_1153)

    gestion_localidad_1154 = Localidad()
    gestion_localidad_1154.cod_postal = '5839'
    gestion_localidad_1154.localidad = 'LAS VERTIENTES'
    gestion_localidad_1154.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1154 = importer.save_or_locate(gestion_localidad_1154)

    gestion_localidad_1155 = Localidad()
    gestion_localidad_1155.cod_postal = '5107'
    gestion_localidad_1155.localidad = 'LAS VERTIENTES DE LA GRANJA'
    gestion_localidad_1155.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1155 = importer.save_or_locate(gestion_localidad_1155)

    gestion_localidad_1156 = Localidad()
    gestion_localidad_1156.cod_postal = '5299'
    gestion_localidad_1156.localidad = 'LA TABLADA'
    gestion_localidad_1156.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1156 = importer.save_or_locate(gestion_localidad_1156)

    gestion_localidad_1157 = Localidad()
    gestion_localidad_1157.cod_postal = '2625'
    gestion_localidad_1157.localidad = 'LATAN HALL'
    gestion_localidad_1157.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1157 = importer.save_or_locate(gestion_localidad_1157)

    gestion_localidad_1158 = Localidad()
    gestion_localidad_1158.cod_postal = '5949'
    gestion_localidad_1158.localidad = 'LA TIGRA'
    gestion_localidad_1158.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1158 = importer.save_or_locate(gestion_localidad_1158)

    gestion_localidad_1159 = Localidad()
    gestion_localidad_1159.cod_postal = '5280'
    gestion_localidad_1159.localidad = 'LA TOMA'
    gestion_localidad_1159.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1159 = importer.save_or_locate(gestion_localidad_1159)

    gestion_localidad_1160 = Localidad()
    gestion_localidad_1160.cod_postal = '5889'
    gestion_localidad_1160.localidad = 'LA TOMA'
    gestion_localidad_1160.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1160 = importer.save_or_locate(gestion_localidad_1160)

    gestion_localidad_1161 = Localidad()
    gestion_localidad_1161.cod_postal = '5244'
    gestion_localidad_1161.localidad = 'LA TOMA'
    gestion_localidad_1161.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1161 = importer.save_or_locate(gestion_localidad_1161)

    gestion_localidad_1162 = Localidad()
    gestion_localidad_1162.cod_postal = '5209'
    gestion_localidad_1162.localidad = 'LA TOTORILLA'
    gestion_localidad_1162.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1162 = importer.save_or_locate(gestion_localidad_1162)

    gestion_localidad_1163 = Localidad()
    gestion_localidad_1163.cod_postal = '5871'
    gestion_localidad_1163.localidad = 'LA TRAMPA'
    gestion_localidad_1163.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1163 = importer.save_or_locate(gestion_localidad_1163)

    gestion_localidad_1164 = Localidad()
    gestion_localidad_1164.cod_postal = '5875'
    gestion_localidad_1164.localidad = 'LA TRAVESIA'
    gestion_localidad_1164.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1164 = importer.save_or_locate(gestion_localidad_1164)

    gestion_localidad_1165 = Localidad()
    gestion_localidad_1165.cod_postal = '2417'
    gestion_localidad_1165.localidad = 'LA TRINCHERA'
    gestion_localidad_1165.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1165 = importer.save_or_locate(gestion_localidad_1165)

    gestion_localidad_1166 = Localidad()
    gestion_localidad_1166.cod_postal = '5212'
    gestion_localidad_1166.localidad = 'LA TUNA'
    gestion_localidad_1166.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1166 = importer.save_or_locate(gestion_localidad_1166)

    gestion_localidad_1167 = Localidad()
    gestion_localidad_1167.cod_postal = '5131'
    gestion_localidad_1167.localidad = 'LA TUNA TINOCO'
    gestion_localidad_1167.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1167 = importer.save_or_locate(gestion_localidad_1167)

    gestion_localidad_1168 = Localidad()
    gestion_localidad_1168.cod_postal = '2413'
    gestion_localidad_1168.localidad = 'LA UDINE'
    gestion_localidad_1168.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1168 = importer.save_or_locate(gestion_localidad_1168)

    gestion_localidad_1169 = Localidad()
    gestion_localidad_1169.cod_postal = '5168'
    gestion_localidad_1169.localidad = 'LA USINA'
    gestion_localidad_1169.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1169 = importer.save_or_locate(gestion_localidad_1169)

    gestion_localidad_1170 = Localidad()
    gestion_localidad_1170.cod_postal = '5870'
    gestion_localidad_1170.localidad = 'LA VENTANA'
    gestion_localidad_1170.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1170 = importer.save_or_locate(gestion_localidad_1170)

    gestion_localidad_1171 = Localidad()
    gestion_localidad_1171.cod_postal = '5801'
    gestion_localidad_1171.localidad = 'LA VERONICA'
    gestion_localidad_1171.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1171 = importer.save_or_locate(gestion_localidad_1171)

    gestion_localidad_1172 = Localidad()
    gestion_localidad_1172.cod_postal = '2417'
    gestion_localidad_1172.localidad = 'LA VICENTA'
    gestion_localidad_1172.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1172 = importer.save_or_locate(gestion_localidad_1172)

    gestion_localidad_1173 = Localidad()
    gestion_localidad_1173.cod_postal = '5231'
    gestion_localidad_1173.localidad = 'LA VICTORIA'
    gestion_localidad_1173.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1173 = importer.save_or_locate(gestion_localidad_1173)

    gestion_localidad_1174 = Localidad()
    gestion_localidad_1174.cod_postal = '5220'
    gestion_localidad_1174.localidad = 'LA VIRGINIA'
    gestion_localidad_1174.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1174 = importer.save_or_locate(gestion_localidad_1174)

    gestion_localidad_1175 = Localidad()
    gestion_localidad_1175.cod_postal = '5281'
    gestion_localidad_1175.localidad = 'LA VIRGINIA'
    gestion_localidad_1175.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1175 = importer.save_or_locate(gestion_localidad_1175)

    gestion_localidad_1176 = Localidad()
    gestion_localidad_1176.cod_postal = '5201'
    gestion_localidad_1176.localidad = 'LA ZANJA'
    gestion_localidad_1176.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1176 = importer.save_or_locate(gestion_localidad_1176)

    gestion_localidad_1177 = Localidad()
    gestion_localidad_1177.cod_postal = '5913'
    gestion_localidad_1177.localidad = 'LA ZARA'
    gestion_localidad_1177.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1177 = importer.save_or_locate(gestion_localidad_1177)

    gestion_localidad_1178 = Localidad()
    gestion_localidad_1178.cod_postal = '5913'
    gestion_localidad_1178.localidad = 'LA ZARITA'
    gestion_localidad_1178.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1178 = importer.save_or_locate(gestion_localidad_1178)

    gestion_localidad_1179 = Localidad()
    gestion_localidad_1179.cod_postal = '6273'
    gestion_localidad_1179.localidad = 'LECUEDER'
    gestion_localidad_1179.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1179 = importer.save_or_locate(gestion_localidad_1179)

    gestion_localidad_1180 = Localidad()
    gestion_localidad_1180.cod_postal = '6128'
    gestion_localidad_1180.localidad = 'LEGUIZAMON'
    gestion_localidad_1180.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1180 = importer.save_or_locate(gestion_localidad_1180)

    gestion_localidad_1181 = Localidad()
    gestion_localidad_1181.cod_postal = '2594'
    gestion_localidad_1181.localidad = 'LEONES'
    gestion_localidad_1181.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1181 = importer.save_or_locate(gestion_localidad_1181)

    gestion_localidad_1182 = Localidad()
    gestion_localidad_1182.cod_postal = '5201'
    gestion_localidad_1182.localidad = 'LOBERA'
    gestion_localidad_1182.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1182 = importer.save_or_locate(gestion_localidad_1182)

    gestion_localidad_1183 = Localidad()
    gestion_localidad_1183.cod_postal = '5209'
    gestion_localidad_1183.localidad = 'LOMA BLANCA'
    gestion_localidad_1183.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1183 = importer.save_or_locate(gestion_localidad_1183)

    gestion_localidad_1184 = Localidad()
    gestion_localidad_1184.cod_postal = '5879'
    gestion_localidad_1184.localidad = 'LOMA BOLA'
    gestion_localidad_1184.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1184 = importer.save_or_locate(gestion_localidad_1184)

    gestion_localidad_1185 = Localidad()
    gestion_localidad_1185.cod_postal = '5246'
    gestion_localidad_1185.localidad = 'LO MACHADO'
    gestion_localidad_1185.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1185 = importer.save_or_locate(gestion_localidad_1185)

    gestion_localidad_1186 = Localidad()
    gestion_localidad_1186.cod_postal = '5244'
    gestion_localidad_1186.localidad = 'LOMA DE PIEDRA'
    gestion_localidad_1186.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1186 = importer.save_or_locate(gestion_localidad_1186)

    gestion_localidad_1187 = Localidad()
    gestion_localidad_1187.cod_postal = '5299'
    gestion_localidad_1187.localidad = 'LOMA REDONDA'
    gestion_localidad_1187.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1187 = importer.save_or_locate(gestion_localidad_1187)

    gestion_localidad_1188 = Localidad()
    gestion_localidad_1188.cod_postal = '5137'
    gestion_localidad_1188.localidad = 'LOMAS DEL TROZO'
    gestion_localidad_1188.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1188 = importer.save_or_locate(gestion_localidad_1188)

    gestion_localidad_1189 = Localidad()
    gestion_localidad_1189.cod_postal = '5209'
    gestion_localidad_1189.localidad = 'LOMITAS'
    gestion_localidad_1189.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1189 = importer.save_or_locate(gestion_localidad_1189)

    gestion_localidad_1190 = Localidad()
    gestion_localidad_1190.cod_postal = '5875'
    gestion_localidad_1190.localidad = 'LOMITAS'
    gestion_localidad_1190.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1190 = importer.save_or_locate(gestion_localidad_1190)

    gestion_localidad_1191 = Localidad()
    gestion_localidad_1191.cod_postal = '5244'
    gestion_localidad_1191.localidad = 'LOS ALAMOS'
    gestion_localidad_1191.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1191 = importer.save_or_locate(gestion_localidad_1191)

    gestion_localidad_1192 = Localidad()
    gestion_localidad_1192.cod_postal = '6275'
    gestion_localidad_1192.localidad = 'LOS ALFALFARES'
    gestion_localidad_1192.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1192 = importer.save_or_locate(gestion_localidad_1192)

    gestion_localidad_1193 = Localidad()
    gestion_localidad_1193.cod_postal = '5225'
    gestion_localidad_1193.localidad = 'LOS ALGARROBITOS'
    gestion_localidad_1193.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1193 = importer.save_or_locate(gestion_localidad_1193)

    gestion_localidad_1194 = Localidad()
    gestion_localidad_1194.cod_postal = '2432'
    gestion_localidad_1194.localidad = 'LOS ALGARROBITOS'
    gestion_localidad_1194.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1194 = importer.save_or_locate(gestion_localidad_1194)

    gestion_localidad_1195 = Localidad()
    gestion_localidad_1195.cod_postal = '5281'
    gestion_localidad_1195.localidad = 'LOS ALGARROBITOS'
    gestion_localidad_1195.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1195 = importer.save_or_locate(gestion_localidad_1195)

    gestion_localidad_1196 = Localidad()
    gestion_localidad_1196.cod_postal = '5189'
    gestion_localidad_1196.localidad = 'LOS ALGARROBOS'
    gestion_localidad_1196.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1196 = importer.save_or_locate(gestion_localidad_1196)

    gestion_localidad_1197 = Localidad()
    gestion_localidad_1197.cod_postal = '5887'
    gestion_localidad_1197.localidad = 'LOS ALGARROBOS'
    gestion_localidad_1197.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1197 = importer.save_or_locate(gestion_localidad_1197)

    gestion_localidad_1198 = Localidad()
    gestion_localidad_1198.cod_postal = '5133'
    gestion_localidad_1198.localidad = 'LOS ALVAREZ'
    gestion_localidad_1198.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1198 = importer.save_or_locate(gestion_localidad_1198)

    gestion_localidad_1199 = Localidad()
    gestion_localidad_1199.cod_postal = '5137'
    gestion_localidad_1199.localidad = 'LOS AVILES'
    gestion_localidad_1199.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1199 = importer.save_or_locate(gestion_localidad_1199)

    gestion_localidad_1200 = Localidad()
    gestion_localidad_1200.cod_postal = '5291'
    gestion_localidad_1200.localidad = 'LOS BARRIALES'
    gestion_localidad_1200.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1200 = importer.save_or_locate(gestion_localidad_1200)

    gestion_localidad_1201 = Localidad()
    gestion_localidad_1201.cod_postal = '5209'
    gestion_localidad_1201.localidad = 'LOS BORDOS'
    gestion_localidad_1201.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1201 = importer.save_or_locate(gestion_localidad_1201)

    gestion_localidad_1202 = Localidad()
    gestion_localidad_1202.cod_postal = '5201'
    gestion_localidad_1202.localidad = 'LOS BRINZES'
    gestion_localidad_1202.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1202 = importer.save_or_locate(gestion_localidad_1202)

    gestion_localidad_1203 = Localidad()
    gestion_localidad_1203.cod_postal = '5214'
    gestion_localidad_1203.localidad = 'LOS CADILLOS'
    gestion_localidad_1203.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1203 = importer.save_or_locate(gestion_localidad_1203)

    gestion_localidad_1204 = Localidad()
    gestion_localidad_1204.cod_postal = '5246'
    gestion_localidad_1204.localidad = 'LOS CAJONES'
    gestion_localidad_1204.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1204 = importer.save_or_locate(gestion_localidad_1204)

    gestion_localidad_1205 = Localidad()
    gestion_localidad_1205.cod_postal = '5871'
    gestion_localidad_1205.localidad = 'LOS CALLEJONES'
    gestion_localidad_1205.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1205 = importer.save_or_locate(gestion_localidad_1205)

    gestion_localidad_1206 = Localidad()
    gestion_localidad_1206.cod_postal = '5220'
    gestion_localidad_1206.localidad = 'LOS CALLEJONES'
    gestion_localidad_1206.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1206 = importer.save_or_locate(gestion_localidad_1206)

    gestion_localidad_1207 = Localidad()
    gestion_localidad_1207.cod_postal = '5137'
    gestion_localidad_1207.localidad = 'LOS CASTAÑOS'
    gestion_localidad_1207.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1207 = importer.save_or_locate(gestion_localidad_1207)

    gestion_localidad_1208 = Localidad()
    gestion_localidad_1208.cod_postal = '5101'
    gestion_localidad_1208.localidad = 'LOS CEDROS'
    gestion_localidad_1208.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1208 = importer.save_or_locate(gestion_localidad_1208)

    gestion_localidad_1209 = Localidad()
    gestion_localidad_1209.cod_postal = '5201'
    gestion_localidad_1209.localidad = 'LOS CEJAS'
    gestion_localidad_1209.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1209 = importer.save_or_locate(gestion_localidad_1209)

    gestion_localidad_1210 = Localidad()
    gestion_localidad_1210.cod_postal = '5101'
    gestion_localidad_1210.localidad = 'LOS CERRILLOS'
    gestion_localidad_1210.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1210 = importer.save_or_locate(gestion_localidad_1210)

    gestion_localidad_1211 = Localidad()
    gestion_localidad_1211.cod_postal = '5209'
    gestion_localidad_1211.localidad = 'LOS CERRILLOS'
    gestion_localidad_1211.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1211 = importer.save_or_locate(gestion_localidad_1211)

    gestion_localidad_1212 = Localidad()
    gestion_localidad_1212.cod_postal = '5246'
    gestion_localidad_1212.localidad = 'LOS CERRILLOS'
    gestion_localidad_1212.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1212 = importer.save_or_locate(gestion_localidad_1212)

    gestion_localidad_1213 = Localidad()
    gestion_localidad_1213.cod_postal = '5871'
    gestion_localidad_1213.localidad = 'LOS CERRILLOS'
    gestion_localidad_1213.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1213 = importer.save_or_locate(gestion_localidad_1213)

    gestion_localidad_1214 = Localidad()
    gestion_localidad_1214.cod_postal = '5137'
    gestion_localidad_1214.localidad = 'LOS CERROS'
    gestion_localidad_1214.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1214 = importer.save_or_locate(gestion_localidad_1214)

    gestion_localidad_1215 = Localidad()
    gestion_localidad_1215.cod_postal = '5821'
    gestion_localidad_1215.localidad = 'LOS CERROS NEGROS'
    gestion_localidad_1215.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1215 = importer.save_or_locate(gestion_localidad_1215)

    gestion_localidad_1216 = Localidad()
    gestion_localidad_1216.cod_postal = '5133'
    gestion_localidad_1216.localidad = 'LOS CHAÑARES'
    gestion_localidad_1216.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1216 = importer.save_or_locate(gestion_localidad_1216)

    gestion_localidad_1217 = Localidad()
    gestion_localidad_1217.cod_postal = '5212'
    gestion_localidad_1217.localidad = 'LOS CHAÑARES'
    gestion_localidad_1217.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1217 = importer.save_or_locate(gestion_localidad_1217)

    gestion_localidad_1218 = Localidad()
    gestion_localidad_1218.cod_postal = '5220'
    gestion_localidad_1218.localidad = 'LOS CHAÑARES'
    gestion_localidad_1218.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1218 = importer.save_or_locate(gestion_localidad_1218)

    gestion_localidad_1219 = Localidad()
    gestion_localidad_1219.cod_postal = '5873'
    gestion_localidad_1219.localidad = 'LOS CHAÑARES'
    gestion_localidad_1219.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1219 = importer.save_or_locate(gestion_localidad_1219)

    gestion_localidad_1220 = Localidad()
    gestion_localidad_1220.cod_postal = '5125'
    gestion_localidad_1220.localidad = 'LOS CHAÑARITOS'
    gestion_localidad_1220.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1220 = importer.save_or_locate(gestion_localidad_1220)

    gestion_localidad_1221 = Localidad()
    gestion_localidad_1221.cod_postal = '5281'
    gestion_localidad_1221.localidad = 'LOS CHAÑARITOS'
    gestion_localidad_1221.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1221 = importer.save_or_locate(gestion_localidad_1221)

    gestion_localidad_1222 = Localidad()
    gestion_localidad_1222.cod_postal = '5873'
    gestion_localidad_1222.localidad = 'LOS CHAÑARITOS'
    gestion_localidad_1222.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1222 = importer.save_or_locate(gestion_localidad_1222)

    gestion_localidad_1223 = Localidad()
    gestion_localidad_1223.cod_postal = '5107'
    gestion_localidad_1223.localidad = 'LOS CIGARRALES'
    gestion_localidad_1223.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1223 = importer.save_or_locate(gestion_localidad_1223)

    gestion_localidad_1224 = Localidad()
    gestion_localidad_1224.cod_postal = '2684'
    gestion_localidad_1224.localidad = 'LOS CISNES'
    gestion_localidad_1224.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1224 = importer.save_or_locate(gestion_localidad_1224)

    gestion_localidad_1225 = Localidad()
    gestion_localidad_1225.cod_postal = '5182'
    gestion_localidad_1225.localidad = 'LOS COCOS'
    gestion_localidad_1225.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1225 = importer.save_or_locate(gestion_localidad_1225)

    gestion_localidad_1226 = Localidad()
    gestion_localidad_1226.cod_postal = '5246'
    gestion_localidad_1226.localidad = 'LOS COCOS'
    gestion_localidad_1226.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1226 = importer.save_or_locate(gestion_localidad_1226)

    gestion_localidad_1227 = Localidad()
    gestion_localidad_1227.cod_postal = '5821'
    gestion_localidad_1227.localidad = 'LOS COCOS'
    gestion_localidad_1227.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1227 = importer.save_or_locate(gestion_localidad_1227)

    gestion_localidad_1228 = Localidad()
    gestion_localidad_1228.cod_postal = '5221'
    gestion_localidad_1228.localidad = 'LOS COMETIERRA'
    gestion_localidad_1228.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1228 = importer.save_or_locate(gestion_localidad_1228)

    gestion_localidad_1229 = Localidad()
    gestion_localidad_1229.cod_postal = '5823'
    gestion_localidad_1229.localidad = 'LOS CONDORES'
    gestion_localidad_1229.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1229 = importer.save_or_locate(gestion_localidad_1229)

    gestion_localidad_1230 = Localidad()
    gestion_localidad_1230.cod_postal = '5201'
    gestion_localidad_1230.localidad = 'LOS COQUITOS'
    gestion_localidad_1230.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1230 = importer.save_or_locate(gestion_localidad_1230)

    gestion_localidad_1231 = Localidad()
    gestion_localidad_1231.cod_postal = '2421'
    gestion_localidad_1231.localidad = 'LOS DESAGUES'
    gestion_localidad_1231.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1231 = importer.save_or_locate(gestion_localidad_1231)

    gestion_localidad_1232 = Localidad()
    gestion_localidad_1232.cod_postal = '5871'
    gestion_localidad_1232.localidad = 'LOS DOS POZOS'
    gestion_localidad_1232.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1232 = importer.save_or_locate(gestion_localidad_1232)

    gestion_localidad_1233 = Localidad()
    gestion_localidad_1233.cod_postal = '5220'
    gestion_localidad_1233.localidad = 'LOS DOS RIOS'
    gestion_localidad_1233.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1233 = importer.save_or_locate(gestion_localidad_1233)

    gestion_localidad_1234 = Localidad()
    gestion_localidad_1234.cod_postal = '5220'
    gestion_localidad_1234.localidad = 'LOS DURAZNOS'
    gestion_localidad_1234.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1234 = importer.save_or_locate(gestion_localidad_1234)

    gestion_localidad_1235 = Localidad()
    gestion_localidad_1235.cod_postal = '5270'
    gestion_localidad_1235.localidad = 'LOS ESLABONES'
    gestion_localidad_1235.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1235 = importer.save_or_locate(gestion_localidad_1235)

    gestion_localidad_1236 = Localidad()
    gestion_localidad_1236.cod_postal = '6127'
    gestion_localidad_1236.localidad = 'LOS GAUCHOS DE GUEMES'
    gestion_localidad_1236.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1236 = importer.save_or_locate(gestion_localidad_1236)

    gestion_localidad_1237 = Localidad()
    gestion_localidad_1237.cod_postal = '5155'
    gestion_localidad_1237.localidad = 'LOS GIGANTES'
    gestion_localidad_1237.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1237 = importer.save_or_locate(gestion_localidad_1237)

    gestion_localidad_1238 = Localidad()
    gestion_localidad_1238.cod_postal = '5282'
    gestion_localidad_1238.localidad = 'LOS GUEVARA'
    gestion_localidad_1238.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1238 = importer.save_or_locate(gestion_localidad_1238)

    gestion_localidad_1239 = Localidad()
    gestion_localidad_1239.cod_postal = '5127'
    gestion_localidad_1239.localidad = 'LOS GUINDOS'
    gestion_localidad_1239.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1239 = importer.save_or_locate(gestion_localidad_1239)

    gestion_localidad_1240 = Localidad()
    gestion_localidad_1240.cod_postal = '5168'
    gestion_localidad_1240.localidad = 'LOS HELECHOS'
    gestion_localidad_1240.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1240 = importer.save_or_locate(gestion_localidad_1240)

    gestion_localidad_1241 = Localidad()
    gestion_localidad_1241.cod_postal = '5281'
    gestion_localidad_1241.localidad = 'LOS HORMIGUEROS'
    gestion_localidad_1241.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1241 = importer.save_or_locate(gestion_localidad_1241)

    gestion_localidad_1242 = Localidad()
    gestion_localidad_1242.cod_postal = '5885'
    gestion_localidad_1242.localidad = 'LOS HORNILLOS'
    gestion_localidad_1242.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1242 = importer.save_or_locate(gestion_localidad_1242)

    gestion_localidad_1243 = Localidad()
    gestion_localidad_1243.cod_postal = '5249'
    gestion_localidad_1243.localidad = 'LOS HOYOS'
    gestion_localidad_1243.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1243 = importer.save_or_locate(gestion_localidad_1243)

    gestion_localidad_1244 = Localidad()
    gestion_localidad_1244.cod_postal = '5153'
    gestion_localidad_1244.localidad = 'LOS HUESOS'
    gestion_localidad_1244.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1244 = importer.save_or_locate(gestion_localidad_1244)

    gestion_localidad_1245 = Localidad()
    gestion_localidad_1245.cod_postal = '5839'
    gestion_localidad_1245.localidad = 'LOS JAGUELES'
    gestion_localidad_1245.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1245 = importer.save_or_locate(gestion_localidad_1245)

    gestion_localidad_1246 = Localidad()
    gestion_localidad_1246.cod_postal = '5249'
    gestion_localidad_1246.localidad = 'LOS JUSTES'
    gestion_localidad_1246.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1246 = importer.save_or_locate(gestion_localidad_1246)

    gestion_localidad_1247 = Localidad()
    gestion_localidad_1247.cod_postal = '5873'
    gestion_localidad_1247.localidad = 'LOS MANGUITOS'
    gestion_localidad_1247.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1247 = importer.save_or_locate(gestion_localidad_1247)

    gestion_localidad_1248 = Localidad()
    gestion_localidad_1248.cod_postal = '5127'
    gestion_localidad_1248.localidad = 'LOS MANSILLAS'
    gestion_localidad_1248.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1248 = importer.save_or_locate(gestion_localidad_1248)

    gestion_localidad_1249 = Localidad()
    gestion_localidad_1249.cod_postal = '5871'
    gestion_localidad_1249.localidad = 'LOS MEDANITOS'
    gestion_localidad_1249.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1249 = importer.save_or_locate(gestion_localidad_1249)

    gestion_localidad_1250 = Localidad()
    gestion_localidad_1250.cod_postal = '5815'
    gestion_localidad_1250.localidad = 'LOS MEDANOS'
    gestion_localidad_1250.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1250 = importer.save_or_locate(gestion_localidad_1250)

    gestion_localidad_1251 = Localidad()
    gestion_localidad_1251.cod_postal = '5137'
    gestion_localidad_1251.localidad = 'LOS MIGUELITOS'
    gestion_localidad_1251.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1251 = importer.save_or_locate(gestion_localidad_1251)

    gestion_localidad_1252 = Localidad()
    gestion_localidad_1252.cod_postal = '5221'
    gestion_localidad_1252.localidad = 'LOS MIQUILES'
    gestion_localidad_1252.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1252 = importer.save_or_locate(gestion_localidad_1252)

    gestion_localidad_1253 = Localidad()
    gestion_localidad_1253.cod_postal = '5229'
    gestion_localidad_1253.localidad = 'LOS MISTOLES'
    gestion_localidad_1253.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1253 = importer.save_or_locate(gestion_localidad_1253)

    gestion_localidad_1254 = Localidad()
    gestion_localidad_1254.cod_postal = '5281'
    gestion_localidad_1254.localidad = 'LOS MISTOLES'
    gestion_localidad_1254.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1254 = importer.save_or_locate(gestion_localidad_1254)

    gestion_localidad_1255 = Localidad()
    gestion_localidad_1255.cod_postal = '5182'
    gestion_localidad_1255.localidad = 'LOS MOGOTES'
    gestion_localidad_1255.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1255 = importer.save_or_locate(gestion_localidad_1255)

    gestion_localidad_1256 = Localidad()
    gestion_localidad_1256.cod_postal = '5189'
    gestion_localidad_1256.localidad = 'LOS MOLINOS'
    gestion_localidad_1256.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1256 = importer.save_or_locate(gestion_localidad_1256)

    gestion_localidad_1257 = Localidad()
    gestion_localidad_1257.cod_postal = '2561'
    gestion_localidad_1257.localidad = 'LOS MOLLES'
    gestion_localidad_1257.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1257 = importer.save_or_locate(gestion_localidad_1257)

    gestion_localidad_1258 = Localidad()
    gestion_localidad_1258.cod_postal = '5885'
    gestion_localidad_1258.localidad = 'LOS MOLLES'
    gestion_localidad_1258.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1258 = importer.save_or_locate(gestion_localidad_1258)

    gestion_localidad_1259 = Localidad()
    gestion_localidad_1259.cod_postal = '5887'
    gestion_localidad_1259.localidad = 'LOS MOLLES'
    gestion_localidad_1259.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1259 = importer.save_or_locate(gestion_localidad_1259)

    gestion_localidad_1260 = Localidad()
    gestion_localidad_1260.cod_postal = '5214'
    gestion_localidad_1260.localidad = 'LOS MORTEROS'
    gestion_localidad_1260.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1260 = importer.save_or_locate(gestion_localidad_1260)

    gestion_localidad_1261 = Localidad()
    gestion_localidad_1261.cod_postal = '5101'
    gestion_localidad_1261.localidad = 'LOS OLIVARES'
    gestion_localidad_1261.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1261 = importer.save_or_locate(gestion_localidad_1261)

    gestion_localidad_1262 = Localidad()
    gestion_localidad_1262.cod_postal = '5284'
    gestion_localidad_1262.localidad = 'LOS PANTALLES'
    gestion_localidad_1262.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1262 = importer.save_or_locate(gestion_localidad_1262)

    gestion_localidad_1263 = Localidad()
    gestion_localidad_1263.cod_postal = '5125'
    gestion_localidad_1263.localidad = 'LOS PANTANILLOS'
    gestion_localidad_1263.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1263 = importer.save_or_locate(gestion_localidad_1263)

    gestion_localidad_1264 = Localidad()
    gestion_localidad_1264.cod_postal = '5187'
    gestion_localidad_1264.localidad = 'LOS PARAISOS'
    gestion_localidad_1264.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1264 = importer.save_or_locate(gestion_localidad_1264)

    gestion_localidad_1265 = Localidad()
    gestion_localidad_1265.cod_postal = '5282'
    gestion_localidad_1265.localidad = 'LOS PAREDONES'
    gestion_localidad_1265.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1265 = importer.save_or_locate(gestion_localidad_1265)

    gestion_localidad_1266 = Localidad()
    gestion_localidad_1266.cod_postal = '5212'
    gestion_localidad_1266.localidad = 'LOS PEDERNALES'
    gestion_localidad_1266.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1266 = importer.save_or_locate(gestion_localidad_1266)

    gestion_localidad_1267 = Localidad()
    gestion_localidad_1267.cod_postal = '5201'
    gestion_localidad_1267.localidad = 'LOS PIQUILLINES'
    gestion_localidad_1267.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1267 = importer.save_or_locate(gestion_localidad_1267)

    gestion_localidad_1268 = Localidad()
    gestion_localidad_1268.cod_postal = '5145'
    gestion_localidad_1268.localidad = 'LOS POCITOS'
    gestion_localidad_1268.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1268 = importer.save_or_locate(gestion_localidad_1268)

    gestion_localidad_1269 = Localidad()
    gestion_localidad_1269.cod_postal = '5249'
    gestion_localidad_1269.localidad = 'LOS POCITOS'
    gestion_localidad_1269.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1269 = importer.save_or_locate(gestion_localidad_1269)

    gestion_localidad_1270 = Localidad()
    gestion_localidad_1270.cod_postal = '5850'
    gestion_localidad_1270.localidad = 'LOS POTREROS'
    gestion_localidad_1270.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1270 = importer.save_or_locate(gestion_localidad_1270)

    gestion_localidad_1271 = Localidad()
    gestion_localidad_1271.cod_postal = '5212'
    gestion_localidad_1271.localidad = 'LOS POZOS'
    gestion_localidad_1271.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1271 = importer.save_or_locate(gestion_localidad_1271)

    gestion_localidad_1272 = Localidad()
    gestion_localidad_1272.cod_postal = '5225'
    gestion_localidad_1272.localidad = 'LOS POZOS'
    gestion_localidad_1272.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1272 = importer.save_or_locate(gestion_localidad_1272)

    gestion_localidad_1273 = Localidad()
    gestion_localidad_1273.cod_postal = '5244'
    gestion_localidad_1273.localidad = 'LOS POZOS'
    gestion_localidad_1273.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1273 = importer.save_or_locate(gestion_localidad_1273)

    gestion_localidad_1274 = Localidad()
    gestion_localidad_1274.cod_postal = '5249'
    gestion_localidad_1274.localidad = 'LOS POZOS'
    gestion_localidad_1274.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1274 = importer.save_or_locate(gestion_localidad_1274)

    gestion_localidad_1275 = Localidad()
    gestion_localidad_1275.cod_postal = '5870'
    gestion_localidad_1275.localidad = 'LOS POZOS'
    gestion_localidad_1275.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1275 = importer.save_or_locate(gestion_localidad_1275)

    gestion_localidad_1276 = Localidad()
    gestion_localidad_1276.cod_postal = '5158'
    gestion_localidad_1276.localidad = 'LOS PUENTES'
    gestion_localidad_1276.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1276 = importer.save_or_locate(gestion_localidad_1276)

    gestion_localidad_1277 = Localidad()
    gestion_localidad_1277.cod_postal = '5200'
    gestion_localidad_1277.localidad = 'LOS PUESTITOS'
    gestion_localidad_1277.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1277 = importer.save_or_locate(gestion_localidad_1277)

    gestion_localidad_1278 = Localidad()
    gestion_localidad_1278.cod_postal = '5221'
    gestion_localidad_1278.localidad = 'LOS QUEBRACHITOS'
    gestion_localidad_1278.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1278 = importer.save_or_locate(gestion_localidad_1278)

    gestion_localidad_1279 = Localidad()
    gestion_localidad_1279.cod_postal = '5246'
    gestion_localidad_1279.localidad = 'LOS QUEBRACHOS'
    gestion_localidad_1279.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1279 = importer.save_or_locate(gestion_localidad_1279)

    gestion_localidad_1280 = Localidad()
    gestion_localidad_1280.cod_postal = '5194'
    gestion_localidad_1280.localidad = 'LOS REARTES'
    gestion_localidad_1280.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1280 = importer.save_or_locate(gestion_localidad_1280)

    gestion_localidad_1281 = Localidad()
    gestion_localidad_1281.cod_postal = '5925'
    gestion_localidad_1281.localidad = 'LOS REYUNOS'
    gestion_localidad_1281.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1281 = importer.save_or_locate(gestion_localidad_1281)

    gestion_localidad_1282 = Localidad()
    gestion_localidad_1282.cod_postal = '5201'
    gestion_localidad_1282.localidad = 'LOS RUICES'
    gestion_localidad_1282.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1282 = importer.save_or_locate(gestion_localidad_1282)

    gestion_localidad_1283 = Localidad()
    gestion_localidad_1283.cod_postal = '5282'
    gestion_localidad_1283.localidad = 'LOS SAUCES'
    gestion_localidad_1283.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1283 = importer.save_or_locate(gestion_localidad_1283)

    gestion_localidad_1284 = Localidad()
    gestion_localidad_1284.cod_postal = '5214'
    gestion_localidad_1284.localidad = 'LOS SOCABONES'
    gestion_localidad_1284.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1284 = importer.save_or_locate(gestion_localidad_1284)

    gestion_localidad_1285 = Localidad()
    gestion_localidad_1285.cod_postal = '2581'
    gestion_localidad_1285.localidad = 'LOS SURGENTES'
    gestion_localidad_1285.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1285 = importer.save_or_locate(gestion_localidad_1285)

    gestion_localidad_1286 = Localidad()
    gestion_localidad_1286.cod_postal = '5233'
    gestion_localidad_1286.localidad = 'LOS TAJAMARES'
    gestion_localidad_1286.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1286 = importer.save_or_locate(gestion_localidad_1286)

    gestion_localidad_1287 = Localidad()
    gestion_localidad_1287.cod_postal = '5299'
    gestion_localidad_1287.localidad = 'LOS TALARES'
    gestion_localidad_1287.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1287 = importer.save_or_locate(gestion_localidad_1287)

    gestion_localidad_1288 = Localidad()
    gestion_localidad_1288.cod_postal = '5218'
    gestion_localidad_1288.localidad = 'LOS TARTAGOS'
    gestion_localidad_1288.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1288 = importer.save_or_locate(gestion_localidad_1288)

    gestion_localidad_1289 = Localidad()
    gestion_localidad_1289.cod_postal = '2559'
    gestion_localidad_1289.localidad = 'LOS TASIS'
    gestion_localidad_1289.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1289 = importer.save_or_locate(gestion_localidad_1289)

    gestion_localidad_1290 = Localidad()
    gestion_localidad_1290.cod_postal = '5184'
    gestion_localidad_1290.localidad = 'LOS TERRONES'
    gestion_localidad_1290.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1290 = importer.save_or_locate(gestion_localidad_1290)

    gestion_localidad_1291 = Localidad()
    gestion_localidad_1291.cod_postal = '5851'
    gestion_localidad_1291.localidad = 'LOS TRES POZOS'
    gestion_localidad_1291.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1291 = importer.save_or_locate(gestion_localidad_1291)

    gestion_localidad_1292 = Localidad()
    gestion_localidad_1292.cod_postal = '5246'
    gestion_localidad_1292.localidad = 'LOS TRONCOS'
    gestion_localidad_1292.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1292 = importer.save_or_locate(gestion_localidad_1292)

    gestion_localidad_1293 = Localidad()
    gestion_localidad_1293.cod_postal = '2559'
    gestion_localidad_1293.localidad = 'LOS UCLES'
    gestion_localidad_1293.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1293 = importer.save_or_locate(gestion_localidad_1293)

    gestion_localidad_1294 = Localidad()
    gestion_localidad_1294.cod_postal = '5270'
    gestion_localidad_1294.localidad = 'LOS VALDES'
    gestion_localidad_1294.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1294 = importer.save_or_locate(gestion_localidad_1294)

    gestion_localidad_1295 = Localidad()
    gestion_localidad_1295.cod_postal = '5125'
    gestion_localidad_1295.localidad = 'LOS VAZQUEZ'
    gestion_localidad_1295.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1295 = importer.save_or_locate(gestion_localidad_1295)

    gestion_localidad_1296 = Localidad()
    gestion_localidad_1296.cod_postal = '5901'
    gestion_localidad_1296.localidad = 'LOS ZORROS'
    gestion_localidad_1296.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1296 = importer.save_or_locate(gestion_localidad_1296)

    gestion_localidad_1297 = Localidad()
    gestion_localidad_1297.cod_postal = '5101'
    gestion_localidad_1297.localidad = 'LOZADA'
    gestion_localidad_1297.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1297 = importer.save_or_locate(gestion_localidad_1297)

    gestion_localidad_1298 = Localidad()
    gestion_localidad_1298.cod_postal = '5917'
    gestion_localidad_1298.localidad = 'LUCA'
    gestion_localidad_1298.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1298 = importer.save_or_locate(gestion_localidad_1298)

    gestion_localidad_1299 = Localidad()
    gestion_localidad_1299.cod_postal = '5216'
    gestion_localidad_1299.localidad = 'LUCIO V MANSILLA'
    gestion_localidad_1299.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1299 = importer.save_or_locate(gestion_localidad_1299)

    gestion_localidad_1300 = Localidad()
    gestion_localidad_1300.cod_postal = '2423'
    gestion_localidad_1300.localidad = 'LUIS SAUZE'
    gestion_localidad_1300.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1300 = importer.save_or_locate(gestion_localidad_1300)

    gestion_localidad_1301 = Localidad()
    gestion_localidad_1301.cod_postal = '5967'
    gestion_localidad_1301.localidad = 'LUQUE'
    gestion_localidad_1301.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1301 = importer.save_or_locate(gestion_localidad_1301)

    gestion_localidad_1302 = Localidad()
    gestion_localidad_1302.cod_postal = '5859'
    gestion_localidad_1302.localidad = 'LUTTI'
    gestion_localidad_1302.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1302 = importer.save_or_locate(gestion_localidad_1302)

    gestion_localidad_1303 = Localidad()
    gestion_localidad_1303.cod_postal = '2411'
    gestion_localidad_1303.localidad = 'LUXARDO'
    gestion_localidad_1303.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1303 = importer.save_or_locate(gestion_localidad_1303)

    gestion_localidad_1304 = Localidad()
    gestion_localidad_1304.cod_postal = '5875'
    gestion_localidad_1304.localidad = 'LUYABA'
    gestion_localidad_1304.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1304 = importer.save_or_locate(gestion_localidad_1304)

    gestion_localidad_1305 = Localidad()
    gestion_localidad_1305.cod_postal = '5211'
    gestion_localidad_1305.localidad = 'MACHA'
    gestion_localidad_1305.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1305 = importer.save_or_locate(gestion_localidad_1305)

    gestion_localidad_1306 = Localidad()
    gestion_localidad_1306.cod_postal = '5287'
    gestion_localidad_1306.localidad = 'MAJADA DE SANTIAGO'
    gestion_localidad_1306.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1306 = importer.save_or_locate(gestion_localidad_1306)

    gestion_localidad_1307 = Localidad()
    gestion_localidad_1307.cod_postal = '5203'
    gestion_localidad_1307.localidad = 'MAJADILLA'
    gestion_localidad_1307.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1307 = importer.save_or_locate(gestion_localidad_1307)

    gestion_localidad_1308 = Localidad()
    gestion_localidad_1308.cod_postal = '5209'
    gestion_localidad_1308.localidad = 'MAJADILLA'
    gestion_localidad_1308.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1308 = importer.save_or_locate(gestion_localidad_1308)

    gestion_localidad_1309 = Localidad()
    gestion_localidad_1309.cod_postal = '5101'
    gestion_localidad_1309.localidad = 'MALAGUEÑO'
    gestion_localidad_1309.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1309 = importer.save_or_locate(gestion_localidad_1309)

    gestion_localidad_1310 = Localidad()
    gestion_localidad_1310.cod_postal = '5839'
    gestion_localidad_1310.localidad = 'MALENA'
    gestion_localidad_1310.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1310 = importer.save_or_locate(gestion_localidad_1310)

    gestion_localidad_1311 = Localidad()
    gestion_localidad_1311.cod_postal = '5155'
    gestion_localidad_1311.localidad = 'MALLIN'
    gestion_localidad_1311.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1311 = importer.save_or_locate(gestion_localidad_1311)

    gestion_localidad_1312 = Localidad()
    gestion_localidad_1312.cod_postal = '5125'
    gestion_localidad_1312.localidad = 'MALVINAS ARGENTINAS'
    gestion_localidad_1312.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1312 = importer.save_or_locate(gestion_localidad_1312)

    gestion_localidad_1313 = Localidad()
    gestion_localidad_1313.cod_postal = '2671'
    gestion_localidad_1313.localidad = 'MANANTIALES'
    gestion_localidad_1313.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1313 = importer.save_or_locate(gestion_localidad_1313)

    gestion_localidad_1314 = Localidad()
    gestion_localidad_1314.cod_postal = '5209'
    gestion_localidad_1314.localidad = 'MANANTIALES'
    gestion_localidad_1314.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1314 = importer.save_or_locate(gestion_localidad_1314)

    gestion_localidad_1315 = Localidad()
    gestion_localidad_1315.cod_postal = '5284'
    gestion_localidad_1315.localidad = 'MANDALA'
    gestion_localidad_1315.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1315 = importer.save_or_locate(gestion_localidad_1315)

    gestion_localidad_1316 = Localidad()
    gestion_localidad_1316.cod_postal = '5988'
    gestion_localidad_1316.localidad = 'MANFREDI'
    gestion_localidad_1316.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1316 = importer.save_or_locate(gestion_localidad_1316)

    gestion_localidad_1317 = Localidad()
    gestion_localidad_1317.cod_postal = '5873'
    gestion_localidad_1317.localidad = 'MANGUITAS'
    gestion_localidad_1317.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1317 = importer.save_or_locate(gestion_localidad_1317)

    gestion_localidad_1318 = Localidad()
    gestion_localidad_1318.cod_postal = '5227'
    gestion_localidad_1318.localidad = 'MAQUINISTA GALLINI'
    gestion_localidad_1318.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1318 = importer.save_or_locate(gestion_localidad_1318)

    gestion_localidad_1319 = Localidad()
    gestion_localidad_1319.cod_postal = '5199'
    gestion_localidad_1319.localidad = 'MAR AZUL'
    gestion_localidad_1319.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1319 = importer.save_or_locate(gestion_localidad_1319)

    gestion_localidad_1320 = Localidad()
    gestion_localidad_1320.cod_postal = '2580'
    gestion_localidad_1320.localidad = 'MARCOS JUAREZ'
    gestion_localidad_1320.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1320 = importer.save_or_locate(gestion_localidad_1320)

    gestion_localidad_1321 = Localidad()
    gestion_localidad_1321.cod_postal = '5925'
    gestion_localidad_1321.localidad = 'MARIA'
    gestion_localidad_1321.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1321 = importer.save_or_locate(gestion_localidad_1321)

    gestion_localidad_1322 = Localidad()
    gestion_localidad_1322.cod_postal = '5139'
    gestion_localidad_1322.localidad = 'MARULL'
    gestion_localidad_1322.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1322 = importer.save_or_locate(gestion_localidad_1322)

    gestion_localidad_1323 = Localidad()
    gestion_localidad_1323.cod_postal = '2659'
    gestion_localidad_1323.localidad = 'MATACOS'
    gestion_localidad_1323.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1323 = importer.save_or_locate(gestion_localidad_1323)

    gestion_localidad_1324 = Localidad()
    gestion_localidad_1324.cod_postal = '5965'
    gestion_localidad_1324.localidad = 'MATORRALES'
    gestion_localidad_1324.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1324 = importer.save_or_locate(gestion_localidad_1324)

    gestion_localidad_1325 = Localidad()
    gestion_localidad_1325.cod_postal = '6271'
    gestion_localidad_1325.localidad = 'MATTALDI'
    gestion_localidad_1325.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1325 = importer.save_or_locate(gestion_localidad_1325)

    gestion_localidad_1326 = Localidad()
    gestion_localidad_1326.cod_postal = '2421'
    gestion_localidad_1326.localidad = 'MAUNIER'
    gestion_localidad_1326.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1326 = importer.save_or_locate(gestion_localidad_1326)

    gestion_localidad_1327 = Localidad()
    gestion_localidad_1327.cod_postal = '5153'
    gestion_localidad_1327.localidad = 'MAYU SUMAJ'
    gestion_localidad_1327.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1327 = importer.save_or_locate(gestion_localidad_1327)

    gestion_localidad_1328 = Localidad()
    gestion_localidad_1328.cod_postal = '5125'
    gestion_localidad_1328.localidad = 'MEDIA LUNA'
    gestion_localidad_1328.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1328 = importer.save_or_locate(gestion_localidad_1328)

    gestion_localidad_1329 = Localidad()
    gestion_localidad_1329.cod_postal = '5281'
    gestion_localidad_1329.localidad = 'MEDIA NARANJA'
    gestion_localidad_1329.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1329 = importer.save_or_locate(gestion_localidad_1329)

    gestion_localidad_1330 = Localidad()
    gestion_localidad_1330.cod_postal = '6270'
    gestion_localidad_1330.localidad = 'MELIDEO'
    gestion_localidad_1330.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1330 = importer.save_or_locate(gestion_localidad_1330)

    gestion_localidad_1331 = Localidad()
    gestion_localidad_1331.cod_postal = '6123'
    gestion_localidad_1331.localidad = 'MELO'
    gestion_localidad_1331.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1331 = importer.save_or_locate(gestion_localidad_1331)

    gestion_localidad_1332 = Localidad()
    gestion_localidad_1332.cod_postal = '5107'
    gestion_localidad_1332.localidad = 'MENDIOLAZA'
    gestion_localidad_1332.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1332 = importer.save_or_locate(gestion_localidad_1332)

    gestion_localidad_1333 = Localidad()
    gestion_localidad_1333.cod_postal = '5285'
    gestion_localidad_1333.localidad = 'MESA DE MARIANO'
    gestion_localidad_1333.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1333 = importer.save_or_locate(gestion_localidad_1333)

    gestion_localidad_1334 = Localidad()
    gestion_localidad_1334.cod_postal = '5153'
    gestion_localidad_1334.localidad = 'MESILLAS'
    gestion_localidad_1334.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1334 = importer.save_or_locate(gestion_localidad_1334)

    gestion_localidad_1335 = Localidad()
    gestion_localidad_1335.cod_postal = '5125'
    gestion_localidad_1335.localidad = 'MI GRANJA'
    gestion_localidad_1335.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1335 = importer.save_or_locate(gestion_localidad_1335)

    gestion_localidad_1336 = Localidad()
    gestion_localidad_1336.cod_postal = '5225'
    gestion_localidad_1336.localidad = 'MIGUELITO'
    gestion_localidad_1336.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1336 = importer.save_or_locate(gestion_localidad_1336)

    gestion_localidad_1337 = Localidad()
    gestion_localidad_1337.cod_postal = '6128'
    gestion_localidad_1337.localidad = 'MIGUEL SALAS'
    gestion_localidad_1337.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1337 = importer.save_or_locate(gestion_localidad_1337)

    gestion_localidad_1338 = Localidad()
    gestion_localidad_1338.cod_postal = '5297'
    gestion_localidad_1338.localidad = 'MINA ARAUJO'
    gestion_localidad_1338.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1338 = importer.save_or_locate(gestion_localidad_1338)

    gestion_localidad_1339 = Localidad()
    gestion_localidad_1339.cod_postal = '5889'
    gestion_localidad_1339.localidad = 'MINA CLAVERO'
    gestion_localidad_1339.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1339 = importer.save_or_locate(gestion_localidad_1339)

    gestion_localidad_1340 = Localidad()
    gestion_localidad_1340.cod_postal = '5291'
    gestion_localidad_1340.localidad = 'MINA LA BISMUTINA'
    gestion_localidad_1340.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1340 = importer.save_or_locate(gestion_localidad_1340)

    gestion_localidad_1341 = Localidad()
    gestion_localidad_1341.cod_postal = '5221'
    gestion_localidad_1341.localidad = 'MIQUILOS'
    gestion_localidad_1341.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1341 = importer.save_or_locate(gestion_localidad_1341)

    gestion_localidad_1342 = Localidad()
    gestion_localidad_1342.cod_postal = '5244'
    gestion_localidad_1342.localidad = 'MIRAFLORES'
    gestion_localidad_1342.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1342 = importer.save_or_locate(gestion_localidad_1342)

    gestion_localidad_1343 = Localidad()
    gestion_localidad_1343.cod_postal = '5272'
    gestion_localidad_1343.localidad = 'MIRAFLORES'
    gestion_localidad_1343.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1343 = importer.save_or_locate(gestion_localidad_1343)

    gestion_localidad_1344 = Localidad()
    gestion_localidad_1344.cod_postal = '5143'
    gestion_localidad_1344.localidad = 'MIRAMAR'
    gestion_localidad_1344.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1344 = importer.save_or_locate(gestion_localidad_1344)

    gestion_localidad_1345 = Localidad()
    gestion_localidad_1345.cod_postal = '5101'
    gestion_localidad_1345.localidad = 'MI VALLE'
    gestion_localidad_1345.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1345 = importer.save_or_locate(gestion_localidad_1345)

    gestion_localidad_1346 = Localidad()
    gestion_localidad_1346.cod_postal = '6273'
    gestion_localidad_1346.localidad = 'MODESTINO PIZARRO'
    gestion_localidad_1346.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1346 = importer.save_or_locate(gestion_localidad_1346)

    gestion_localidad_1347 = Localidad()
    gestion_localidad_1347.cod_postal = '5823'
    gestion_localidad_1347.localidad = 'MODESTO ACUÑA'
    gestion_localidad_1347.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1347 = importer.save_or_locate(gestion_localidad_1347)

    gestion_localidad_1348 = Localidad()
    gestion_localidad_1348.cod_postal = '5891'
    gestion_localidad_1348.localidad = 'MOGIGASTA'
    gestion_localidad_1348.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1348 = importer.save_or_locate(gestion_localidad_1348)

    gestion_localidad_1349 = Localidad()
    gestion_localidad_1349.cod_postal = '5291'
    gestion_localidad_1349.localidad = 'MOGOTE VERDE'
    gestion_localidad_1349.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1349 = importer.save_or_locate(gestion_localidad_1349)

    gestion_localidad_1350 = Localidad()
    gestion_localidad_1350.cod_postal = '5166'
    gestion_localidad_1350.localidad = 'MOLINARI'
    gestion_localidad_1350.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1350 = importer.save_or_locate(gestion_localidad_1350)

    gestion_localidad_1351 = Localidad()
    gestion_localidad_1351.cod_postal = '5212'
    gestion_localidad_1351.localidad = 'MOLINOS'
    gestion_localidad_1351.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1351 = importer.save_or_locate(gestion_localidad_1351)

    gestion_localidad_1352 = Localidad()
    gestion_localidad_1352.cod_postal = '5851'
    gestion_localidad_1352.localidad = 'MONSALVO'
    gestion_localidad_1352.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1352 = importer.save_or_locate(gestion_localidad_1352)

    gestion_localidad_1353 = Localidad()
    gestion_localidad_1353.cod_postal = '2589'
    gestion_localidad_1353.localidad = 'MONTE BUEY'
    gestion_localidad_1353.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1353 = importer.save_or_locate(gestion_localidad_1353)

    gestion_localidad_1354 = Localidad()
    gestion_localidad_1354.cod_postal = '2563'
    gestion_localidad_1354.localidad = 'MONTE CASTILLO'
    gestion_localidad_1354.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1354 = importer.save_or_locate(gestion_localidad_1354)

    gestion_localidad_1355 = Localidad()
    gestion_localidad_1355.cod_postal = '5125'
    gestion_localidad_1355.localidad = 'MONTE CRISTO'
    gestion_localidad_1355.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1355 = importer.save_or_locate(gestion_localidad_1355)

    gestion_localidad_1356 = Localidad()
    gestion_localidad_1356.cod_postal = '5931'
    gestion_localidad_1356.localidad = 'MONTE DEL FRAYLE'
    gestion_localidad_1356.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1356 = importer.save_or_locate(gestion_localidad_1356)

    gestion_localidad_1357 = Localidad()
    gestion_localidad_1357.cod_postal = '5831'
    gestion_localidad_1357.localidad = 'MONTE DE LOS GAUCHOS'
    gestion_localidad_1357.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1357 = importer.save_or_locate(gestion_localidad_1357)

    gestion_localidad_1358 = Localidad()
    gestion_localidad_1358.cod_postal = '5900'
    gestion_localidad_1358.localidad = 'MONTE DE LOS LAZOS'
    gestion_localidad_1358.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1358 = importer.save_or_locate(gestion_localidad_1358)

    gestion_localidad_1359 = Localidad()
    gestion_localidad_1359.cod_postal = '5129'
    gestion_localidad_1359.localidad = 'MONTE DEL ROSARIO'
    gestion_localidad_1359.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1359 = importer.save_or_locate(gestion_localidad_1359)

    gestion_localidad_1360 = Localidad()
    gestion_localidad_1360.cod_postal = '5135'
    gestion_localidad_1360.localidad = 'MONTE DE TORO PUJIO'
    gestion_localidad_1360.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1360 = importer.save_or_locate(gestion_localidad_1360)

    gestion_localidad_1361 = Localidad()
    gestion_localidad_1361.cod_postal = '2417'
    gestion_localidad_1361.localidad = 'MONTE GRANDE'
    gestion_localidad_1361.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1361 = importer.save_or_locate(gestion_localidad_1361)

    gestion_localidad_1362 = Localidad()
    gestion_localidad_1362.cod_postal = '5119'
    gestion_localidad_1362.localidad = 'MONTE GRANDE RAFAEL GARCIA'
    gestion_localidad_1362.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1362 = importer.save_or_locate(gestion_localidad_1362)

    gestion_localidad_1363 = Localidad()
    gestion_localidad_1363.cod_postal = '5801'
    gestion_localidad_1363.localidad = 'MONTE LA INVERNADA'
    gestion_localidad_1363.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1363 = importer.save_or_locate(gestion_localidad_1363)

    gestion_localidad_1364 = Localidad()
    gestion_localidad_1364.cod_postal = '2564'
    gestion_localidad_1364.localidad = 'MONTE LEÑA'
    gestion_localidad_1364.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1364 = importer.save_or_locate(gestion_localidad_1364)

    gestion_localidad_1365 = Localidad()
    gestion_localidad_1365.cod_postal = '2659'
    gestion_localidad_1365.localidad = 'MONTE MAIZ'
    gestion_localidad_1365.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1365 = importer.save_or_locate(gestion_localidad_1365)

    gestion_localidad_1366 = Localidad()
    gestion_localidad_1366.cod_postal = '5119'
    gestion_localidad_1366.localidad = 'MONTE RALO'
    gestion_localidad_1366.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1366 = importer.save_or_locate(gestion_localidad_1366)

    gestion_localidad_1367 = Localidad()
    gestion_localidad_1367.cod_postal = '2423'
    gestion_localidad_1367.localidad = 'MONTE REDONDO'
    gestion_localidad_1367.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1367 = importer.save_or_locate(gestion_localidad_1367)

    gestion_localidad_1368 = Localidad()
    gestion_localidad_1368.cod_postal = '5889'
    gestion_localidad_1368.localidad = 'MONTE REDONDO'
    gestion_localidad_1368.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1368 = importer.save_or_locate(gestion_localidad_1368)

    gestion_localidad_1369 = Localidad()
    gestion_localidad_1369.cod_postal = '5963'
    gestion_localidad_1369.localidad = 'MONTE REDONDO'
    gestion_localidad_1369.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1369 = importer.save_or_locate(gestion_localidad_1369)

    gestion_localidad_1370 = Localidad()
    gestion_localidad_1370.cod_postal = '2568'
    gestion_localidad_1370.localidad = 'MORRISON'
    gestion_localidad_1370.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1370 = importer.save_or_locate(gestion_localidad_1370)

    gestion_localidad_1371 = Localidad()
    gestion_localidad_1371.cod_postal = '2421'
    gestion_localidad_1371.localidad = 'MORTEROS'
    gestion_localidad_1371.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1371 = importer.save_or_locate(gestion_localidad_1371)

    gestion_localidad_1372 = Localidad()
    gestion_localidad_1372.cod_postal = '5209'
    gestion_localidad_1372.localidad = 'MOVADO'
    gestion_localidad_1372.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1372 = importer.save_or_locate(gestion_localidad_1372)

    gestion_localidad_1373 = Localidad()
    gestion_localidad_1373.cod_postal = '5221'
    gestion_localidad_1373.localidad = 'MULA MUERTA'
    gestion_localidad_1373.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1373 = importer.save_or_locate(gestion_localidad_1373)

    gestion_localidad_1374 = Localidad()
    gestion_localidad_1374.cod_postal = '5299'
    gestion_localidad_1374.localidad = 'MUSSI'
    gestion_localidad_1374.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1374 = importer.save_or_locate(gestion_localidad_1374)

    gestion_localidad_1375 = Localidad()
    gestion_localidad_1375.cod_postal = '5209'
    gestion_localidad_1375.localidad = 'NAVARRO'
    gestion_localidad_1375.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1375 = importer.save_or_locate(gestion_localidad_1375)

    gestion_localidad_1376 = Localidad()
    gestion_localidad_1376.cod_postal = '6270'
    gestion_localidad_1376.localidad = 'NAZCA'
    gestion_localidad_1376.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1376 = importer.save_or_locate(gestion_localidad_1376)

    gestion_localidad_1377 = Localidad()
    gestion_localidad_1377.cod_postal = '5280'
    gestion_localidad_1377.localidad = 'NEGRO HUASI'
    gestion_localidad_1377.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1377 = importer.save_or_locate(gestion_localidad_1377)

    gestion_localidad_1378 = Localidad()
    gestion_localidad_1378.cod_postal = '5870'
    gestion_localidad_1378.localidad = 'NICHO'
    gestion_localidad_1378.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1378 = importer.save_or_locate(gestion_localidad_1378)

    gestion_localidad_1379 = Localidad()
    gestion_localidad_1379.cod_postal = '6271'
    gestion_localidad_1379.localidad = 'NICOLAS BRUZONE'
    gestion_localidad_1379.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1379 = importer.save_or_locate(gestion_localidad_1379)

    gestion_localidad_1380 = Localidad()
    gestion_localidad_1380.cod_postal = '5889'
    gestion_localidad_1380.localidad = 'NIDO DEL AGUILA'
    gestion_localidad_1380.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1380 = importer.save_or_locate(gestion_localidad_1380)

    gestion_localidad_1381 = Localidad()
    gestion_localidad_1381.cod_postal = '5291'
    gestion_localidad_1381.localidad = 'NINALQUIN'
    gestion_localidad_1381.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1381 = importer.save_or_locate(gestion_localidad_1381)

    gestion_localidad_1382 = Localidad()
    gestion_localidad_1382.cod_postal = '5220'
    gestion_localidad_1382.localidad = 'NINTES'
    gestion_localidad_1382.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1382 = importer.save_or_locate(gestion_localidad_1382)

    gestion_localidad_1383 = Localidad()
    gestion_localidad_1383.cod_postal = '5889'
    gestion_localidad_1383.localidad = 'NIÑA PAULA'
    gestion_localidad_1383.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1383 = importer.save_or_locate(gestion_localidad_1383)

    gestion_localidad_1384 = Localidad()
    gestion_localidad_1384.cod_postal = '2563'
    gestion_localidad_1384.localidad = 'NOETINGER'
    gestion_localidad_1384.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1384 = importer.save_or_locate(gestion_localidad_1384)

    gestion_localidad_1385 = Localidad()
    gestion_localidad_1385.cod_postal = '5887'
    gestion_localidad_1385.localidad = 'NONO'
    gestion_localidad_1385.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1385 = importer.save_or_locate(gestion_localidad_1385)

    gestion_localidad_1386 = Localidad()
    gestion_localidad_1386.cod_postal = '5101'
    gestion_localidad_1386.localidad = 'NUEVA ANDALUCIA'
    gestion_localidad_1386.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1386 = importer.save_or_locate(gestion_localidad_1386)

    gestion_localidad_1387 = Localidad()
    gestion_localidad_1387.cod_postal = '5280'
    gestion_localidad_1387.localidad = 'NUEVA ESPERANZA'
    gestion_localidad_1387.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1387 = importer.save_or_locate(gestion_localidad_1387)

    gestion_localidad_1388 = Localidad()
    gestion_localidad_1388.cod_postal = '5131'
    gestion_localidad_1388.localidad = 'NUÑEZ DEL PRADO'
    gestion_localidad_1388.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1388 = importer.save_or_locate(gestion_localidad_1388)

    gestion_localidad_1389 = Localidad()
    gestion_localidad_1389.cod_postal = '5111'
    gestion_localidad_1389.localidad = 'ÑU PORA'
    gestion_localidad_1389.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1389 = importer.save_or_locate(gestion_localidad_1389)

    gestion_localidad_1390 = Localidad()
    gestion_localidad_1390.cod_postal = '5225'
    gestion_localidad_1390.localidad = 'OBISPO TREJO'
    gestion_localidad_1390.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1390 = importer.save_or_locate(gestion_localidad_1390)

    gestion_localidad_1391 = Localidad()
    gestion_localidad_1391.cod_postal = '5189'
    gestion_localidad_1391.localidad = 'OBREGON'
    gestion_localidad_1391.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1391 = importer.save_or_locate(gestion_localidad_1391)

    gestion_localidad_1392 = Localidad()
    gestion_localidad_1392.cod_postal = '5220'
    gestion_localidad_1392.localidad = 'OJO DE AGUA'
    gestion_localidad_1392.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1392 = importer.save_or_locate(gestion_localidad_1392)

    gestion_localidad_1393 = Localidad()
    gestion_localidad_1393.cod_postal = '5293'
    gestion_localidad_1393.localidad = 'OJO DE AGUA'
    gestion_localidad_1393.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1393 = importer.save_or_locate(gestion_localidad_1393)

    gestion_localidad_1394 = Localidad()
    gestion_localidad_1394.cod_postal = '5887'
    gestion_localidad_1394.localidad = 'OJO DE AGUA'
    gestion_localidad_1394.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1394 = importer.save_or_locate(gestion_localidad_1394)

    gestion_localidad_1395 = Localidad()
    gestion_localidad_1395.cod_postal = '5293'
    gestion_localidad_1395.localidad = 'OJO DE AGUA DE TOTOX'
    gestion_localidad_1395.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1395 = importer.save_or_locate(gestion_localidad_1395)

    gestion_localidad_1396 = Localidad()
    gestion_localidad_1396.cod_postal = '5807'
    gestion_localidad_1396.localidad = 'OLAETA'
    gestion_localidad_1396.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1396 = importer.save_or_locate(gestion_localidad_1396)

    gestion_localidad_1397 = Localidad()
    gestion_localidad_1397.cod_postal = '5980'
    gestion_localidad_1397.localidad = 'OLIVA'
    gestion_localidad_1397.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1397 = importer.save_or_locate(gestion_localidad_1397)

    gestion_localidad_1398 = Localidad()
    gestion_localidad_1398.cod_postal = '5280'
    gestion_localidad_1398.localidad = 'OLIVARES SAN NICOLAS'
    gestion_localidad_1398.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1398 = importer.save_or_locate(gestion_localidad_1398)

    gestion_localidad_1399 = Localidad()
    gestion_localidad_1399.cod_postal = '2684'
    gestion_localidad_1399.localidad = 'OLMOS'
    gestion_localidad_1399.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1399 = importer.save_or_locate(gestion_localidad_1399)

    gestion_localidad_1400 = Localidad()
    gestion_localidad_1400.cod_postal = '6227'
    gestion_localidad_1400.localidad = 'ONAGOITY'
    gestion_localidad_1400.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1400 = importer.save_or_locate(gestion_localidad_1400)

    gestion_localidad_1401 = Localidad()
    gestion_localidad_1401.cod_postal = '5986'
    gestion_localidad_1401.localidad = 'ONCATIVO'
    gestion_localidad_1401.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1401 = importer.save_or_locate(gestion_localidad_1401)

    gestion_localidad_1402 = Localidad()
    gestion_localidad_1402.cod_postal = '5184'
    gestion_localidad_1402.localidad = 'ONGAMIRA'
    gestion_localidad_1402.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1402 = importer.save_or_locate(gestion_localidad_1402)

    gestion_localidad_1403 = Localidad()
    gestion_localidad_1403.cod_postal = '5125'
    gestion_localidad_1403.localidad = 'ORATORIO DE PERALTA'
    gestion_localidad_1403.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1403 = importer.save_or_locate(gestion_localidad_1403)

    gestion_localidad_1404 = Localidad()
    gestion_localidad_1404.cod_postal = '5214'
    gestion_localidad_1404.localidad = 'ORCOSUNI'
    gestion_localidad_1404.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1404 = importer.save_or_locate(gestion_localidad_1404)

    gestion_localidad_1405 = Localidad()
    gestion_localidad_1405.cod_postal = '2555'
    gestion_localidad_1405.localidad = 'ORDOÑEZ'
    gestion_localidad_1405.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1405 = importer.save_or_locate(gestion_localidad_1405)

    gestion_localidad_1406 = Localidad()
    gestion_localidad_1406.cod_postal = '5287'
    gestion_localidad_1406.localidad = 'ORO GRUESO'
    gestion_localidad_1406.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1406 = importer.save_or_locate(gestion_localidad_1406)

    gestion_localidad_1407 = Localidad()
    gestion_localidad_1407.cod_postal = '5951'
    gestion_localidad_1407.localidad = 'OVERA NEGRA'
    gestion_localidad_1407.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1407 = importer.save_or_locate(gestion_localidad_1407)

    gestion_localidad_1408 = Localidad()
    gestion_localidad_1408.cod_postal = '5893'
    gestion_localidad_1408.localidad = 'PACHANGO'
    gestion_localidad_1408.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1408 = importer.save_or_locate(gestion_localidad_1408)

    gestion_localidad_1409 = Localidad()
    gestion_localidad_1409.cod_postal = '6121'
    gestion_localidad_1409.localidad = 'PACHECO DE MELO'
    gestion_localidad_1409.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1409 = importer.save_or_locate(gestion_localidad_1409)

    gestion_localidad_1410 = Localidad()
    gestion_localidad_1410.cod_postal = '5111'
    gestion_localidad_1410.localidad = 'PAJAS BLANCAS'
    gestion_localidad_1410.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1410 = importer.save_or_locate(gestion_localidad_1410)

    gestion_localidad_1411 = Localidad()
    gestion_localidad_1411.cod_postal = '5291'
    gestion_localidad_1411.localidad = 'PAJONAL'
    gestion_localidad_1411.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1411 = importer.save_or_locate(gestion_localidad_1411)

    gestion_localidad_1412 = Localidad()
    gestion_localidad_1412.cod_postal = '5280'
    gestion_localidad_1412.localidad = 'PALO CORTADO'
    gestion_localidad_1412.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1412 = importer.save_or_locate(gestion_localidad_1412)

    gestion_localidad_1413 = Localidad()
    gestion_localidad_1413.cod_postal = '5281'
    gestion_localidad_1413.localidad = 'PALO LABRADO'
    gestion_localidad_1413.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1413 = importer.save_or_locate(gestion_localidad_1413)

    gestion_localidad_1414 = Localidad()
    gestion_localidad_1414.cod_postal = '5284'
    gestion_localidad_1414.localidad = 'PALOMA POZO'
    gestion_localidad_1414.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1414 = importer.save_or_locate(gestion_localidad_1414)

    gestion_localidad_1415 = Localidad()
    gestion_localidad_1415.cod_postal = '5961'
    gestion_localidad_1415.localidad = 'PALO NEGRO'
    gestion_localidad_1415.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1415 = importer.save_or_locate(gestion_localidad_1415)

    gestion_localidad_1416 = Localidad()
    gestion_localidad_1416.cod_postal = '5281'
    gestion_localidad_1416.localidad = 'PALO PARADO'
    gestion_localidad_1416.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1416 = importer.save_or_locate(gestion_localidad_1416)

    gestion_localidad_1417 = Localidad()
    gestion_localidad_1417.cod_postal = '5284'
    gestion_localidad_1417.localidad = 'PALO QUEMADO'
    gestion_localidad_1417.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1417 = importer.save_or_locate(gestion_localidad_1417)

    gestion_localidad_1418 = Localidad()
    gestion_localidad_1418.cod_postal = '5153'
    gestion_localidad_1418.localidad = 'PAMPA DE ACHALA'
    gestion_localidad_1418.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1418 = importer.save_or_locate(gestion_localidad_1418)

    gestion_localidad_1419 = Localidad()
    gestion_localidad_1419.cod_postal = '5166'
    gestion_localidad_1419.localidad = 'PAMPA DE OLAEN'
    gestion_localidad_1419.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1419 = importer.save_or_locate(gestion_localidad_1419)

    gestion_localidad_1420 = Localidad()
    gestion_localidad_1420.cod_postal = '5931'
    gestion_localidad_1420.localidad = 'PAMPAYASTA NORTE'
    gestion_localidad_1420.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1420 = importer.save_or_locate(gestion_localidad_1420)

    gestion_localidad_1421 = Localidad()
    gestion_localidad_1421.cod_postal = '5931'
    gestion_localidad_1421.localidad = 'PAMPAYASTA SUR'
    gestion_localidad_1421.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1421 = importer.save_or_locate(gestion_localidad_1421)

    gestion_localidad_1422 = Localidad()
    gestion_localidad_1422.cod_postal = '5893'
    gestion_localidad_1422.localidad = 'PANAHOLMA'
    gestion_localidad_1422.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1422 = importer.save_or_locate(gestion_localidad_1422)

    gestion_localidad_1423 = Localidad()
    gestion_localidad_1423.cod_postal = '5158'
    gestion_localidad_1423.localidad = 'PARQUE SIQUIMAN'
    gestion_localidad_1423.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1423 = importer.save_or_locate(gestion_localidad_1423)

    gestion_localidad_1424 = Localidad()
    gestion_localidad_1424.cod_postal = '2679'
    gestion_localidad_1424.localidad = 'PASCANAS'
    gestion_localidad_1424.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1424 = importer.save_or_locate(gestion_localidad_1424)

    gestion_localidad_1425 = Localidad()
    gestion_localidad_1425.cod_postal = '5925'
    gestion_localidad_1425.localidad = 'PASCO'
    gestion_localidad_1425.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1425 = importer.save_or_locate(gestion_localidad_1425)

    gestion_localidad_1426 = Localidad()
    gestion_localidad_1426.cod_postal = '5817'
    gestion_localidad_1426.localidad = 'PASO CABRAL'
    gestion_localidad_1426.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1426 = importer.save_or_locate(gestion_localidad_1426)

    gestion_localidad_1427 = Localidad()
    gestion_localidad_1427.cod_postal = '5145'
    gestion_localidad_1427.localidad = 'PASO CASTELLANOS'
    gestion_localidad_1427.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1427 = importer.save_or_locate(gestion_localidad_1427)

    gestion_localidad_1428 = Localidad()
    gestion_localidad_1428.cod_postal = '5803'
    gestion_localidad_1428.localidad = 'PASO DEL DURAZNO'
    gestion_localidad_1428.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1428 = importer.save_or_locate(gestion_localidad_1428)

    gestion_localidad_1429 = Localidad()
    gestion_localidad_1429.cod_postal = '2433'
    gestion_localidad_1429.localidad = 'PASO DE LOS GALLEGOS'
    gestion_localidad_1429.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1429 = importer.save_or_locate(gestion_localidad_1429)

    gestion_localidad_1430 = Localidad()
    gestion_localidad_1430.cod_postal = '5101'
    gestion_localidad_1430.localidad = 'PASO DEL SAUCE'
    gestion_localidad_1430.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1430 = importer.save_or_locate(gestion_localidad_1430)

    gestion_localidad_1431 = Localidad()
    gestion_localidad_1431.cod_postal = '5246'
    gestion_localidad_1431.localidad = 'PASO DEL SILVERIO'
    gestion_localidad_1431.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1431 = importer.save_or_locate(gestion_localidad_1431)

    gestion_localidad_1432 = Localidad()
    gestion_localidad_1432.cod_postal = '5284'
    gestion_localidad_1432.localidad = 'PASO DE MONTOYA'
    gestion_localidad_1432.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1432 = importer.save_or_locate(gestion_localidad_1432)

    gestion_localidad_1433 = Localidad()
    gestion_localidad_1433.cod_postal = '5972'
    gestion_localidad_1433.localidad = 'PASO DE VELEZ'
    gestion_localidad_1433.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1433 = importer.save_or_locate(gestion_localidad_1433)

    gestion_localidad_1434 = Localidad()
    gestion_localidad_1434.cod_postal = '5291'
    gestion_localidad_1434.localidad = 'PASO GRANDE'
    gestion_localidad_1434.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1434 = importer.save_or_locate(gestion_localidad_1434)

    gestion_localidad_1435 = Localidad()
    gestion_localidad_1435.cod_postal = '5887'
    gestion_localidad_1435.localidad = 'PASO LAS TROPAS'
    gestion_localidad_1435.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1435 = importer.save_or_locate(gestion_localidad_1435)

    gestion_localidad_1436 = Localidad()
    gestion_localidad_1436.cod_postal = '5819'
    gestion_localidad_1436.localidad = 'PASO SANDIALITO'
    gestion_localidad_1436.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1436 = importer.save_or_locate(gestion_localidad_1436)

    gestion_localidad_1437 = Localidad()
    gestion_localidad_1437.cod_postal = '5284'
    gestion_localidad_1437.localidad = 'PASO VIEJO'
    gestion_localidad_1437.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1437 = importer.save_or_locate(gestion_localidad_1437)

    gestion_localidad_1438 = Localidad()
    gestion_localidad_1438.cod_postal = '5807'
    gestion_localidad_1438.localidad = 'PASTOS ALTOS'
    gestion_localidad_1438.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1438 = importer.save_or_locate(gestion_localidad_1438)

    gestion_localidad_1439 = Localidad()
    gestion_localidad_1439.cod_postal = '5738'
    gestion_localidad_1439.localidad = 'PAUNERO'
    gestion_localidad_1439.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1439 = importer.save_or_locate(gestion_localidad_1439)

    gestion_localidad_1440 = Localidad()
    gestion_localidad_1440.cod_postal = '6121'
    gestion_localidad_1440.localidad = 'PAVIN'
    gestion_localidad_1440.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1440 = importer.save_or_locate(gestion_localidad_1440)

    gestion_localidad_1441 = Localidad()
    gestion_localidad_1441.cod_postal = '5233'
    gestion_localidad_1441.localidad = 'PEDANIA CANDELARIA SUD'
    gestion_localidad_1441.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1441 = importer.save_or_locate(gestion_localidad_1441)

    gestion_localidad_1442 = Localidad()
    gestion_localidad_1442.cod_postal = '2671'
    gestion_localidad_1442.localidad = 'PEDRO E FUNES'
    gestion_localidad_1442.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1442 = importer.save_or_locate(gestion_localidad_1442)

    gestion_localidad_1443 = Localidad()
    gestion_localidad_1443.cod_postal = '5127'
    gestion_localidad_1443.localidad = 'PEDRO E VIVAS'
    gestion_localidad_1443.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1443 = importer.save_or_locate(gestion_localidad_1443)

    gestion_localidad_1444 = Localidad()
    gestion_localidad_1444.cod_postal = '5801'
    gestion_localidad_1444.localidad = 'PERMANENTES'
    gestion_localidad_1444.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1444 = importer.save_or_locate(gestion_localidad_1444)

    gestion_localidad_1445 = Localidad()
    gestion_localidad_1445.cod_postal = '5821'
    gestion_localidad_1445.localidad = 'PERMANENTES'
    gestion_localidad_1445.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1445 = importer.save_or_locate(gestion_localidad_1445)

    gestion_localidad_1446 = Localidad()
    gestion_localidad_1446.cod_postal = '5284'
    gestion_localidad_1446.localidad = 'PICHANAS'
    gestion_localidad_1446.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1446 = importer.save_or_locate(gestion_localidad_1446)

    gestion_localidad_1447 = Localidad()
    gestion_localidad_1447.cod_postal = '5285'
    gestion_localidad_1447.localidad = 'PIEDRA BLANCA'
    gestion_localidad_1447.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1447 = importer.save_or_locate(gestion_localidad_1447)

    gestion_localidad_1448 = Localidad()
    gestion_localidad_1448.cod_postal = '5801'
    gestion_localidad_1448.localidad = 'PIEDRA BLANCA'
    gestion_localidad_1448.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1448 = importer.save_or_locate(gestion_localidad_1448)

    gestion_localidad_1449 = Localidad()
    gestion_localidad_1449.cod_postal = '5887'
    gestion_localidad_1449.localidad = 'PIEDRA BLANCA'
    gestion_localidad_1449.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1449 = importer.save_or_locate(gestion_localidad_1449)

    gestion_localidad_1450 = Localidad()
    gestion_localidad_1450.cod_postal = '5168'
    gestion_localidad_1450.localidad = 'PIEDRA GRANDE'
    gestion_localidad_1450.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1450 = importer.save_or_locate(gestion_localidad_1450)

    gestion_localidad_1451 = Localidad()
    gestion_localidad_1451.cod_postal = '5174'
    gestion_localidad_1451.localidad = 'PIEDRA MOVEDIZA'
    gestion_localidad_1451.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1451 = importer.save_or_locate(gestion_localidad_1451)

    gestion_localidad_1452 = Localidad()
    gestion_localidad_1452.cod_postal = '5871'
    gestion_localidad_1452.localidad = 'PIEDRA PINTADA'
    gestion_localidad_1452.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1452 = importer.save_or_locate(gestion_localidad_1452)

    gestion_localidad_1453 = Localidad()
    gestion_localidad_1453.cod_postal = '5284'
    gestion_localidad_1453.localidad = 'PIEDRAS AMONTONADAS'
    gestion_localidad_1453.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1453 = importer.save_or_locate(gestion_localidad_1453)

    gestion_localidad_1454 = Localidad()
    gestion_localidad_1454.cod_postal = '2645'
    gestion_localidad_1454.localidad = 'PIEDRAS ANCHAS'
    gestion_localidad_1454.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1454 = importer.save_or_locate(gestion_localidad_1454)

    gestion_localidad_1455 = Localidad()
    gestion_localidad_1455.cod_postal = '5284'
    gestion_localidad_1455.localidad = 'PIEDRAS ANCHAS'
    gestion_localidad_1455.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1455 = importer.save_or_locate(gestion_localidad_1455)

    gestion_localidad_1456 = Localidad()
    gestion_localidad_1456.cod_postal = '5291'
    gestion_localidad_1456.localidad = 'PIEDRAS ANCHAS'
    gestion_localidad_1456.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1456 = importer.save_or_locate(gestion_localidad_1456)

    gestion_localidad_1457 = Localidad()
    gestion_localidad_1457.cod_postal = '5174'
    gestion_localidad_1457.localidad = 'PIEDRAS BLANCAS'
    gestion_localidad_1457.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1457 = importer.save_or_locate(gestion_localidad_1457)

    gestion_localidad_1458 = Localidad()
    gestion_localidad_1458.cod_postal = '5172'
    gestion_localidad_1458.localidad = 'PIEDRAS GRANDES'
    gestion_localidad_1458.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1458 = importer.save_or_locate(gestion_localidad_1458)

    gestion_localidad_1459 = Localidad()
    gestion_localidad_1459.cod_postal = '5271'
    gestion_localidad_1459.localidad = 'PIEDRITA BLANCA'
    gestion_localidad_1459.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1459 = importer.save_or_locate(gestion_localidad_1459)

    gestion_localidad_1460 = Localidad()
    gestion_localidad_1460.cod_postal = '5295'
    gestion_localidad_1460.localidad = 'PIEDRITAS ROSADAS'
    gestion_localidad_1460.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1460 = importer.save_or_locate(gestion_localidad_1460)

    gestion_localidad_1461 = Localidad()
    gestion_localidad_1461.cod_postal = '5972'
    gestion_localidad_1461.localidad = 'PILAR'
    gestion_localidad_1461.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1461 = importer.save_or_locate(gestion_localidad_1461)

    gestion_localidad_1462 = Localidad()
    gestion_localidad_1462.cod_postal = '2572'
    gestion_localidad_1462.localidad = 'PINAS'
    gestion_localidad_1462.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1462 = importer.save_or_locate(gestion_localidad_1462)

    gestion_localidad_1463 = Localidad()
    gestion_localidad_1463.cod_postal = '6271'
    gestion_localidad_1463.localidad = 'PINCEN'
    gestion_localidad_1463.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1463 = importer.save_or_locate(gestion_localidad_1463)

    gestion_localidad_1464 = Localidad()
    gestion_localidad_1464.cod_postal = '5125'
    gestion_localidad_1464.localidad = 'PIQUILLIN'
    gestion_localidad_1464.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1464 = importer.save_or_locate(gestion_localidad_1464)

    gestion_localidad_1465 = Localidad()
    gestion_localidad_1465.cod_postal = '5244'
    gestion_localidad_1465.localidad = 'PISCO HUASI'
    gestion_localidad_1465.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1465 = importer.save_or_locate(gestion_localidad_1465)

    gestion_localidad_1466 = Localidad()
    gestion_localidad_1466.cod_postal = '5295'
    gestion_localidad_1466.localidad = 'PITOA'
    gestion_localidad_1466.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1466 = importer.save_or_locate(gestion_localidad_1466)

    gestion_localidad_1467 = Localidad()
    gestion_localidad_1467.cod_postal = '5139'
    gestion_localidad_1467.localidad = 'PLAYA GRANDE'
    gestion_localidad_1467.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1467 = importer.save_or_locate(gestion_localidad_1467)

    gestion_localidad_1468 = Localidad()
    gestion_localidad_1468.cod_postal = '2436'
    gestion_localidad_1468.localidad = 'PLAZA BRUNO'
    gestion_localidad_1468.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1468 = importer.save_or_locate(gestion_localidad_1468)

    gestion_localidad_1469 = Localidad()
    gestion_localidad_1469.cod_postal = '5137'
    gestion_localidad_1469.localidad = 'PLAZA DE MERCEDES'
    gestion_localidad_1469.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1469 = importer.save_or_locate(gestion_localidad_1469)

    gestion_localidad_1470 = Localidad()
    gestion_localidad_1470.cod_postal = '5967'
    gestion_localidad_1470.localidad = 'PLAZA MINETTI'
    gestion_localidad_1470.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1470 = importer.save_or_locate(gestion_localidad_1470)

    gestion_localidad_1471 = Localidad()
    gestion_localidad_1471.cod_postal = '5987'
    gestion_localidad_1471.localidad = 'PLAZA RODRIGUEZ'
    gestion_localidad_1471.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1471 = importer.save_or_locate(gestion_localidad_1471)

    gestion_localidad_1472 = Localidad()
    gestion_localidad_1472.cod_postal = '2401'
    gestion_localidad_1472.localidad = 'PLAZA SAN FRANCISCO'
    gestion_localidad_1472.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1472 = importer.save_or_locate(gestion_localidad_1472)

    gestion_localidad_1473 = Localidad()
    gestion_localidad_1473.cod_postal = '5141'
    gestion_localidad_1473.localidad = 'PLUJUNTA'
    gestion_localidad_1473.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1473 = importer.save_or_locate(gestion_localidad_1473)

    gestion_localidad_1474 = Localidad()
    gestion_localidad_1474.cod_postal = '5299'
    gestion_localidad_1474.localidad = 'POCHO'
    gestion_localidad_1474.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1474 = importer.save_or_locate(gestion_localidad_1474)

    gestion_localidad_1475 = Localidad()
    gestion_localidad_1475.cod_postal = '5248'
    gestion_localidad_1475.localidad = 'POCITO DEL CAMPO'
    gestion_localidad_1475.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1475 = importer.save_or_locate(gestion_localidad_1475)

    gestion_localidad_1476 = Localidad()
    gestion_localidad_1476.cod_postal = '2415'
    gestion_localidad_1476.localidad = 'PORTEÑA'
    gestion_localidad_1476.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1476 = importer.save_or_locate(gestion_localidad_1476)

    gestion_localidad_1477 = Localidad()
    gestion_localidad_1477.cod_postal = '5189'
    gestion_localidad_1477.localidad = 'POTRERO DE FUNES'
    gestion_localidad_1477.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1477 = importer.save_or_locate(gestion_localidad_1477)

    gestion_localidad_1478 = Localidad()
    gestion_localidad_1478.cod_postal = '5189'
    gestion_localidad_1478.localidad = 'POTRERO DE GARAY'
    gestion_localidad_1478.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1478 = importer.save_or_locate(gestion_localidad_1478)

    gestion_localidad_1479 = Localidad()
    gestion_localidad_1479.cod_postal = '5191'
    gestion_localidad_1479.localidad = 'POTRERO DE LUJAN'
    gestion_localidad_1479.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1479 = importer.save_or_locate(gestion_localidad_1479)

    gestion_localidad_1480 = Localidad()
    gestion_localidad_1480.cod_postal = '5297'
    gestion_localidad_1480.localidad = 'POTRERO DE MARQUES'
    gestion_localidad_1480.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1480 = importer.save_or_locate(gestion_localidad_1480)

    gestion_localidad_1481 = Localidad()
    gestion_localidad_1481.cod_postal = '5186'
    gestion_localidad_1481.localidad = 'POTRERO DE TUTZER'
    gestion_localidad_1481.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1481 = importer.save_or_locate(gestion_localidad_1481)

    gestion_localidad_1482 = Localidad()
    gestion_localidad_1482.cod_postal = '5221'
    gestion_localidad_1482.localidad = 'POZO CONCA'
    gestion_localidad_1482.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1482 = importer.save_or_locate(gestion_localidad_1482)

    gestion_localidad_1483 = Localidad()
    gestion_localidad_1483.cod_postal = '5221'
    gestion_localidad_1483.localidad = 'POZO CORREA'
    gestion_localidad_1483.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1483 = importer.save_or_locate(gestion_localidad_1483)

    gestion_localidad_1484 = Localidad()
    gestion_localidad_1484.cod_postal = '5246'
    gestion_localidad_1484.localidad = 'POZO DE JUANCHO'
    gestion_localidad_1484.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1484 = importer.save_or_locate(gestion_localidad_1484)

    gestion_localidad_1485 = Localidad()
    gestion_localidad_1485.cod_postal = '5133'
    gestion_localidad_1485.localidad = 'POZO DE LA ESQUINA'
    gestion_localidad_1485.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1485 = importer.save_or_locate(gestion_localidad_1485)

    gestion_localidad_1486 = Localidad()
    gestion_localidad_1486.cod_postal = '5125'
    gestion_localidad_1486.localidad = 'POZO DE LA LOMA'
    gestion_localidad_1486.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1486 = importer.save_or_locate(gestion_localidad_1486)

    gestion_localidad_1487 = Localidad()
    gestion_localidad_1487.cod_postal = '5871'
    gestion_localidad_1487.localidad = 'POZO DE LA PAMPA'
    gestion_localidad_1487.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1487 = importer.save_or_locate(gestion_localidad_1487)

    gestion_localidad_1488 = Localidad()
    gestion_localidad_1488.cod_postal = '5249'
    gestion_localidad_1488.localidad = 'POZO DE LAS OLLAS'
    gestion_localidad_1488.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1488 = importer.save_or_locate(gestion_localidad_1488)

    gestion_localidad_1489 = Localidad()
    gestion_localidad_1489.cod_postal = '5125'
    gestion_localidad_1489.localidad = 'POZO DE LAS YEGUAS'
    gestion_localidad_1489.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1489 = importer.save_or_locate(gestion_localidad_1489)

    gestion_localidad_1490 = Localidad()
    gestion_localidad_1490.cod_postal = '5947'
    gestion_localidad_1490.localidad = 'POZO DEL AVESTRUZ'
    gestion_localidad_1490.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1490 = importer.save_or_locate(gestion_localidad_1490)

    gestion_localidad_1491 = Localidad()
    gestion_localidad_1491.cod_postal = '5272'
    gestion_localidad_1491.localidad = 'POZO DEL BARRIAL'
    gestion_localidad_1491.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1491 = importer.save_or_locate(gestion_localidad_1491)

    gestion_localidad_1492 = Localidad()
    gestion_localidad_1492.cod_postal = '2433'
    gestion_localidad_1492.localidad = 'POZO DEL CHAJA'
    gestion_localidad_1492.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1492 = importer.save_or_locate(gestion_localidad_1492)

    gestion_localidad_1493 = Localidad()
    gestion_localidad_1493.cod_postal = '5873'
    gestion_localidad_1493.localidad = 'POZO DEL CHAÑAR'
    gestion_localidad_1493.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1493 = importer.save_or_locate(gestion_localidad_1493)

    gestion_localidad_1494 = Localidad()
    gestion_localidad_1494.cod_postal = '2435'
    gestion_localidad_1494.localidad = 'POZO DEL CHAÑAR'
    gestion_localidad_1494.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1494 = importer.save_or_locate(gestion_localidad_1494)

    gestion_localidad_1495 = Localidad()
    gestion_localidad_1495.cod_postal = '5873'
    gestion_localidad_1495.localidad = 'POZO DEL MOLLE'
    gestion_localidad_1495.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1495 = importer.save_or_locate(gestion_localidad_1495)

    gestion_localidad_1496 = Localidad()
    gestion_localidad_1496.cod_postal = '5913'
    gestion_localidad_1496.localidad = 'POZO DEL MOLLE'
    gestion_localidad_1496.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1496 = importer.save_or_locate(gestion_localidad_1496)

    gestion_localidad_1497 = Localidad()
    gestion_localidad_1497.cod_postal = '5225'
    gestion_localidad_1497.localidad = 'POZO DEL MORO'
    gestion_localidad_1497.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1497 = importer.save_or_locate(gestion_localidad_1497)

    gestion_localidad_1498 = Localidad()
    gestion_localidad_1498.cod_postal = '5249'
    gestion_localidad_1498.localidad = 'POZO DE LOS ARBOLES'
    gestion_localidad_1498.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1498 = importer.save_or_locate(gestion_localidad_1498)

    gestion_localidad_1499 = Localidad()
    gestion_localidad_1499.cod_postal = '5137'
    gestion_localidad_1499.localidad = 'POZO DE LOS TRONCOS'
    gestion_localidad_1499.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1499 = importer.save_or_locate(gestion_localidad_1499)

    gestion_localidad_1500 = Localidad()
    gestion_localidad_1500.cod_postal = '5281'
    gestion_localidad_1500.localidad = 'POZO DEL SIMBOL'
    gestion_localidad_1500.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1500 = importer.save_or_locate(gestion_localidad_1500)

    gestion_localidad_1501 = Localidad()
    gestion_localidad_1501.cod_postal = '5249'
    gestion_localidad_1501.localidad = 'POZO DEL SIMBOL'
    gestion_localidad_1501.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1501 = importer.save_or_locate(gestion_localidad_1501)

    gestion_localidad_1502 = Localidad()
    gestion_localidad_1502.cod_postal = '5145'
    gestion_localidad_1502.localidad = 'POZO DEL TIGRE'
    gestion_localidad_1502.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1502 = importer.save_or_locate(gestion_localidad_1502)

    gestion_localidad_1503 = Localidad()
    gestion_localidad_1503.cod_postal = '5209'
    gestion_localidad_1503.localidad = 'POZO DEL TIGRE'
    gestion_localidad_1503.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1503 = importer.save_or_locate(gestion_localidad_1503)

    gestion_localidad_1504 = Localidad()
    gestion_localidad_1504.cod_postal = '5249'
    gestion_localidad_1504.localidad = 'POZO DE MOLINA'
    gestion_localidad_1504.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1504 = importer.save_or_locate(gestion_localidad_1504)

    gestion_localidad_1505 = Localidad()
    gestion_localidad_1505.cod_postal = '5135'
    gestion_localidad_1505.localidad = 'POZO LA PIEDRA'
    gestion_localidad_1505.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1505 = importer.save_or_locate(gestion_localidad_1505)

    gestion_localidad_1506 = Localidad()
    gestion_localidad_1506.cod_postal = '5209'
    gestion_localidad_1506.localidad = 'POZO NUEVO'
    gestion_localidad_1506.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1506 = importer.save_or_locate(gestion_localidad_1506)

    gestion_localidad_1507 = Localidad()
    gestion_localidad_1507.cod_postal = '5285'
    gestion_localidad_1507.localidad = 'POZO SECO'
    gestion_localidad_1507.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1507 = importer.save_or_locate(gestion_localidad_1507)

    gestion_localidad_1508 = Localidad()
    gestion_localidad_1508.cod_postal = '5244'
    gestion_localidad_1508.localidad = 'POZO SOLO'
    gestion_localidad_1508.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1508 = importer.save_or_locate(gestion_localidad_1508)

    gestion_localidad_1509 = Localidad()
    gestion_localidad_1509.cod_postal = '6140'
    gestion_localidad_1509.localidad = 'PRETOT FREYRE'
    gestion_localidad_1509.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1509 = importer.save_or_locate(gestion_localidad_1509)

    gestion_localidad_1510 = Localidad()
    gestion_localidad_1510.cod_postal = '5139'
    gestion_localidad_1510.localidad = 'PRIMAVERA'
    gestion_localidad_1510.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1510 = importer.save_or_locate(gestion_localidad_1510)

    gestion_localidad_1511 = Localidad()
    gestion_localidad_1511.cod_postal = '5231'
    gestion_localidad_1511.localidad = 'PROVIDENCIA'
    gestion_localidad_1511.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1511 = importer.save_or_locate(gestion_localidad_1511)

    gestion_localidad_1512 = Localidad()
    gestion_localidad_1512.cod_postal = '5800'
    gestion_localidad_1512.localidad = 'PUEBLO ALBERDI'
    gestion_localidad_1512.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1512 = importer.save_or_locate(gestion_localidad_1512)

    gestion_localidad_1513 = Localidad()
    gestion_localidad_1513.cod_postal = '2580'
    gestion_localidad_1513.localidad = 'PUEBLO ARGENTINO'
    gestion_localidad_1513.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1513 = importer.save_or_locate(gestion_localidad_1513)

    gestion_localidad_1514 = Localidad()
    gestion_localidad_1514.cod_postal = '2581'
    gestion_localidad_1514.localidad = 'PUEBLO CARLOS SAUVERAN'
    gestion_localidad_1514.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1514 = importer.save_or_locate(gestion_localidad_1514)

    gestion_localidad_1515 = Localidad()
    gestion_localidad_1515.cod_postal = '2627'
    gestion_localidad_1515.localidad = 'PUEBLO GAMBANDE'
    gestion_localidad_1515.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1515 = importer.save_or_locate(gestion_localidad_1515)

    gestion_localidad_1516 = Localidad()
    gestion_localidad_1516.cod_postal = '2651'
    gestion_localidad_1516.localidad = 'PUEBLO ITALIANO'
    gestion_localidad_1516.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1516 = importer.save_or_locate(gestion_localidad_1516)

    gestion_localidad_1517 = Localidad()
    gestion_localidad_1517.cod_postal = '5131'
    gestion_localidad_1517.localidad = 'PUEBLO PIANELLI'
    gestion_localidad_1517.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1517 = importer.save_or_locate(gestion_localidad_1517)

    gestion_localidad_1518 = Localidad()
    gestion_localidad_1518.cod_postal = '2581'
    gestion_localidad_1518.localidad = 'PUEBLO RIO TERCERO'
    gestion_localidad_1518.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1518 = importer.save_or_locate(gestion_localidad_1518)

    gestion_localidad_1519 = Localidad()
    gestion_localidad_1519.cod_postal = '2555'
    gestion_localidad_1519.localidad = 'PUEBLO VIEJO'
    gestion_localidad_1519.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1519 = importer.save_or_locate(gestion_localidad_1519)

    gestion_localidad_1520 = Localidad()
    gestion_localidad_1520.cod_postal = '5891'
    gestion_localidad_1520.localidad = 'PUENTE DEL CURA'
    gestion_localidad_1520.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1520 = importer.save_or_locate(gestion_localidad_1520)

    gestion_localidad_1521 = Localidad()
    gestion_localidad_1521.cod_postal = '5809'
    gestion_localidad_1521.localidad = 'PUENTE LOS MOLLES'
    gestion_localidad_1521.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1521 = importer.save_or_locate(gestion_localidad_1521)

    gestion_localidad_1522 = Localidad()
    gestion_localidad_1522.cod_postal = '5139'
    gestion_localidad_1522.localidad = 'PUENTE RIO PLUJUNTA'
    gestion_localidad_1522.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1522 = importer.save_or_locate(gestion_localidad_1522)

    gestion_localidad_1523 = Localidad()
    gestion_localidad_1523.cod_postal = '5817'
    gestion_localidad_1523.localidad = 'PUERTA COLORADA'
    gestion_localidad_1523.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1523 = importer.save_or_locate(gestion_localidad_1523)

    gestion_localidad_1524 = Localidad()
    gestion_localidad_1524.cod_postal = '5297'
    gestion_localidad_1524.localidad = 'PUERTA DE LA QUEBRADA'
    gestion_localidad_1524.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1524 = importer.save_or_locate(gestion_localidad_1524)

    gestion_localidad_1525 = Localidad()
    gestion_localidad_1525.cod_postal = '5131'
    gestion_localidad_1525.localidad = 'PUESTO DE AFUERA'
    gestion_localidad_1525.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1525 = importer.save_or_locate(gestion_localidad_1525)

    gestion_localidad_1526 = Localidad()
    gestion_localidad_1526.cod_postal = '5214'
    gestion_localidad_1526.localidad = 'PUESTO DE ARRIBA'
    gestion_localidad_1526.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1526 = importer.save_or_locate(gestion_localidad_1526)

    gestion_localidad_1527 = Localidad()
    gestion_localidad_1527.cod_postal = '5218'
    gestion_localidad_1527.localidad = 'PUESTO DE BATALLA'
    gestion_localidad_1527.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1527 = importer.save_or_locate(gestion_localidad_1527)

    gestion_localidad_1528 = Localidad()
    gestion_localidad_1528.cod_postal = '5233'
    gestion_localidad_1528.localidad = 'PUESTO DE CASTRO'
    gestion_localidad_1528.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1528 = importer.save_or_locate(gestion_localidad_1528)

    gestion_localidad_1529 = Localidad()
    gestion_localidad_1529.cod_postal = '5200'
    gestion_localidad_1529.localidad = 'PUESTO DE CERRO'
    gestion_localidad_1529.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1529 = importer.save_or_locate(gestion_localidad_1529)

    gestion_localidad_1530 = Localidad()
    gestion_localidad_1530.cod_postal = '5227'
    gestion_localidad_1530.localidad = 'PUESTO DE FIERRO'
    gestion_localidad_1530.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1530 = importer.save_or_locate(gestion_localidad_1530)

    gestion_localidad_1531 = Localidad()
    gestion_localidad_1531.cod_postal = '5131'
    gestion_localidad_1531.localidad = 'PUESTO DE LA OVEJA'
    gestion_localidad_1531.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1531 = importer.save_or_locate(gestion_localidad_1531)

    gestion_localidad_1532 = Localidad()
    gestion_localidad_1532.cod_postal = '5281'
    gestion_localidad_1532.localidad = 'PUESTO DEL GALLO'
    gestion_localidad_1532.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1532 = importer.save_or_locate(gestion_localidad_1532)

    gestion_localidad_1533 = Localidad()
    gestion_localidad_1533.cod_postal = '5117'
    gestion_localidad_1533.localidad = 'PUESTO DEL MEDIO'
    gestion_localidad_1533.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1533 = importer.save_or_locate(gestion_localidad_1533)

    gestion_localidad_1534 = Localidad()
    gestion_localidad_1534.cod_postal = '5249'
    gestion_localidad_1534.localidad = 'PUESTO DE LOS ALAMOS'
    gestion_localidad_1534.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1534 = importer.save_or_locate(gestion_localidad_1534)

    gestion_localidad_1535 = Localidad()
    gestion_localidad_1535.cod_postal = '5200'
    gestion_localidad_1535.localidad = 'PUESTO DE LOS RODRIGUEZ'
    gestion_localidad_1535.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1535 = importer.save_or_locate(gestion_localidad_1535)

    gestion_localidad_1536 = Localidad()
    gestion_localidad_1536.cod_postal = '5236'
    gestion_localidad_1536.localidad = 'PUESTO DEL ROSARIO'
    gestion_localidad_1536.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1536 = importer.save_or_locate(gestion_localidad_1536)

    gestion_localidad_1537 = Localidad()
    gestion_localidad_1537.cod_postal = '5233'
    gestion_localidad_1537.localidad = 'PUESTO DE LUNA'
    gestion_localidad_1537.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1537 = importer.save_or_locate(gestion_localidad_1537)

    gestion_localidad_1538 = Localidad()
    gestion_localidad_1538.cod_postal = '5225'
    gestion_localidad_1538.localidad = 'PUESTO DE PUCHETA'
    gestion_localidad_1538.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1538 = importer.save_or_locate(gestion_localidad_1538)

    gestion_localidad_1539 = Localidad()
    gestion_localidad_1539.cod_postal = '5271'
    gestion_localidad_1539.localidad = 'PUESTO DE VERA'
    gestion_localidad_1539.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1539 = importer.save_or_locate(gestion_localidad_1539)

    gestion_localidad_1540 = Localidad()
    gestion_localidad_1540.cod_postal = '5284'
    gestion_localidad_1540.localidad = 'PUESTO EL ABRA'
    gestion_localidad_1540.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1540 = importer.save_or_locate(gestion_localidad_1540)

    gestion_localidad_1541 = Localidad()
    gestion_localidad_1541.cod_postal = '5153'
    gestion_localidad_1541.localidad = 'PUESTO GUZMAN'
    gestion_localidad_1541.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1541 = importer.save_or_locate(gestion_localidad_1541)

    gestion_localidad_1542 = Localidad()
    gestion_localidad_1542.cod_postal = '5189'
    gestion_localidad_1542.localidad = 'PUESTO MULITA'
    gestion_localidad_1542.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1542 = importer.save_or_locate(gestion_localidad_1542)

    gestion_localidad_1543 = Localidad()
    gestion_localidad_1543.cod_postal = '5209'
    gestion_localidad_1543.localidad = 'PUESTO NUEVO'
    gestion_localidad_1543.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1543 = importer.save_or_locate(gestion_localidad_1543)

    gestion_localidad_1544 = Localidad()
    gestion_localidad_1544.cod_postal = '5242'
    gestion_localidad_1544.localidad = 'PUESTO SAN JOSE'
    gestion_localidad_1544.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1544 = importer.save_or_locate(gestion_localidad_1544)

    gestion_localidad_1545 = Localidad()
    gestion_localidad_1545.cod_postal = '5244'
    gestion_localidad_1545.localidad = 'PUESTO VIEJO'
    gestion_localidad_1545.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1545 = importer.save_or_locate(gestion_localidad_1545)

    gestion_localidad_1546 = Localidad()
    gestion_localidad_1546.cod_postal = '5184'
    gestion_localidad_1546.localidad = 'PUNILLA'
    gestion_localidad_1546.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1546 = importer.save_or_locate(gestion_localidad_1546)

    gestion_localidad_1547 = Localidad()
    gestion_localidad_1547.cod_postal = '5129'
    gestion_localidad_1547.localidad = 'PUNTA DEL AGUA'
    gestion_localidad_1547.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1547 = importer.save_or_locate(gestion_localidad_1547)

    gestion_localidad_1548 = Localidad()
    gestion_localidad_1548.cod_postal = '5839'
    gestion_localidad_1548.localidad = 'PUNTA DEL AGUA'
    gestion_localidad_1548.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1548 = importer.save_or_locate(gestion_localidad_1548)

    gestion_localidad_1549 = Localidad()
    gestion_localidad_1549.cod_postal = '5931'
    gestion_localidad_1549.localidad = 'PUNTA DEL AGUA'
    gestion_localidad_1549.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1549 = importer.save_or_locate(gestion_localidad_1549)

    gestion_localidad_1550 = Localidad()
    gestion_localidad_1550.cod_postal = '5249'
    gestion_localidad_1550.localidad = 'PUNTA DEL MONTE'
    gestion_localidad_1550.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1550 = importer.save_or_locate(gestion_localidad_1550)

    gestion_localidad_1551 = Localidad()
    gestion_localidad_1551.cod_postal = '5299'
    gestion_localidad_1551.localidad = 'PUSISUNA'
    gestion_localidad_1551.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1551 = importer.save_or_locate(gestion_localidad_1551)

    gestion_localidad_1552 = Localidad()
    gestion_localidad_1552.cod_postal = '2436'
    gestion_localidad_1552.localidad = 'QUEBRACHITOS'
    gestion_localidad_1552.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1552 = importer.save_or_locate(gestion_localidad_1552)

    gestion_localidad_1553 = Localidad()
    gestion_localidad_1553.cod_postal = '2423'
    gestion_localidad_1553.localidad = 'QUEBRACHO HERRADO'
    gestion_localidad_1553.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1553 = importer.save_or_locate(gestion_localidad_1553)

    gestion_localidad_1554 = Localidad()
    gestion_localidad_1554.cod_postal = '5875'
    gestion_localidad_1554.localidad = 'QUEBRACHO LADEADO'
    gestion_localidad_1554.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1554 = importer.save_or_locate(gestion_localidad_1554)

    gestion_localidad_1555 = Localidad()
    gestion_localidad_1555.cod_postal = '5131'
    gestion_localidad_1555.localidad = 'QUEBRACHOS'
    gestion_localidad_1555.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1555 = importer.save_or_locate(gestion_localidad_1555)

    gestion_localidad_1556 = Localidad()
    gestion_localidad_1556.cod_postal = '5871'
    gestion_localidad_1556.localidad = 'QUEBRACHO SOLO'
    gestion_localidad_1556.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1556 = importer.save_or_locate(gestion_localidad_1556)

    gestion_localidad_1557 = Localidad()
    gestion_localidad_1557.cod_postal = '5889'
    gestion_localidad_1557.localidad = 'QUEBRADA DEL HORNO'
    gestion_localidad_1557.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1557 = importer.save_or_locate(gestion_localidad_1557)

    gestion_localidad_1558 = Localidad()
    gestion_localidad_1558.cod_postal = '5885'
    gestion_localidad_1558.localidad = 'QUEBRADA DE LOS POZOS'
    gestion_localidad_1558.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1558 = importer.save_or_locate(gestion_localidad_1558)

    gestion_localidad_1559 = Localidad()
    gestion_localidad_1559.cod_postal = '5282'
    gestion_localidad_1559.localidad = 'QUEBRADA DE LUNA'
    gestion_localidad_1559.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1559 = importer.save_or_locate(gestion_localidad_1559)

    gestion_localidad_1560 = Localidad()
    gestion_localidad_1560.cod_postal = '5184'
    gestion_localidad_1560.localidad = 'QUEBRADA DE NONA'
    gestion_localidad_1560.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1560 = importer.save_or_locate(gestion_localidad_1560)

    gestion_localidad_1561 = Localidad()
    gestion_localidad_1561.cod_postal = '5214'
    gestion_localidad_1561.localidad = 'QUILINO'
    gestion_localidad_1561.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1561 = importer.save_or_locate(gestion_localidad_1561)

    gestion_localidad_1562 = Localidad()
    gestion_localidad_1562.cod_postal = '5270'
    gestion_localidad_1562.localidad = 'QUILMES'
    gestion_localidad_1562.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1562 = importer.save_or_locate(gestion_localidad_1562)

    gestion_localidad_1563 = Localidad()
    gestion_localidad_1563.cod_postal = '5221'
    gestion_localidad_1563.localidad = 'QUISCASACATE'
    gestion_localidad_1563.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1563 = importer.save_or_locate(gestion_localidad_1563)

    gestion_localidad_1564 = Localidad()
    gestion_localidad_1564.cod_postal = '5249'
    gestion_localidad_1564.localidad = 'RACEDO'
    gestion_localidad_1564.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1564 = importer.save_or_locate(gestion_localidad_1564)

    gestion_localidad_1565 = Localidad()
    gestion_localidad_1565.cod_postal = '5119'
    gestion_localidad_1565.localidad = 'RAFAEL GARCIA'
    gestion_localidad_1565.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1565 = importer.save_or_locate(gestion_localidad_1565)

    gestion_localidad_1566 = Localidad()
    gestion_localidad_1566.cod_postal = '5225'
    gestion_localidad_1566.localidad = 'RAMALLO'
    gestion_localidad_1566.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1566 = importer.save_or_locate(gestion_localidad_1566)

    gestion_localidad_1567 = Localidad()
    gestion_localidad_1567.cod_postal = '5284'
    gestion_localidad_1567.localidad = 'RAMBLON'
    gestion_localidad_1567.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1567 = importer.save_or_locate(gestion_localidad_1567)

    gestion_localidad_1568 = Localidad()
    gestion_localidad_1568.cod_postal = '5289'
    gestion_localidad_1568.localidad = 'RAMIREZ'
    gestion_localidad_1568.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1568 = importer.save_or_locate(gestion_localidad_1568)

    gestion_localidad_1569 = Localidad()
    gestion_localidad_1569.cod_postal = '5900'
    gestion_localidad_1569.localidad = 'RAMON J CARCANO'
    gestion_localidad_1569.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1569 = importer.save_or_locate(gestion_localidad_1569)

    gestion_localidad_1570 = Localidad()
    gestion_localidad_1570.cod_postal = '5131'
    gestion_localidad_1570.localidad = 'RANGEL'
    gestion_localidad_1570.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1570 = importer.save_or_locate(gestion_localidad_1570)

    gestion_localidad_1571 = Localidad()
    gestion_localidad_1571.cod_postal = '6271'
    gestion_localidad_1571.localidad = 'RANQUELES'
    gestion_localidad_1571.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1571 = importer.save_or_locate(gestion_localidad_1571)

    gestion_localidad_1572 = Localidad()
    gestion_localidad_1572.cod_postal = '5287'
    gestion_localidad_1572.localidad = 'RARA FORTUNA'
    gestion_localidad_1572.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1572 = importer.save_or_locate(gestion_localidad_1572)

    gestion_localidad_1573 = Localidad()
    gestion_localidad_1573.cod_postal = '5246'
    gestion_localidad_1573.localidad = 'RAYO CORTADO'
    gestion_localidad_1573.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1573 = importer.save_or_locate(gestion_localidad_1573)

    gestion_localidad_1574 = Localidad()
    gestion_localidad_1574.cod_postal = '5144'
    gestion_localidad_1574.localidad = 'RECREO VICTORIA'
    gestion_localidad_1574.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1574 = importer.save_or_locate(gestion_localidad_1574)

    gestion_localidad_1575 = Localidad()
    gestion_localidad_1575.cod_postal = '5803'
    gestion_localidad_1575.localidad = 'REDUCCION'
    gestion_localidad_1575.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1575 = importer.save_or_locate(gestion_localidad_1575)

    gestion_localidad_1576 = Localidad()
    gestion_localidad_1576.cod_postal = '5285'
    gestion_localidad_1576.localidad = 'REPRESA DE MORALES'
    gestion_localidad_1576.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1576 = importer.save_or_locate(gestion_localidad_1576)

    gestion_localidad_1577 = Localidad()
    gestion_localidad_1577.cod_postal = '5961'
    gestion_localidad_1577.localidad = 'RINCON'
    gestion_localidad_1577.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1577 = importer.save_or_locate(gestion_localidad_1577)

    gestion_localidad_1578 = Localidad()
    gestion_localidad_1578.cod_postal = '5162'
    gestion_localidad_1578.localidad = 'RINCON CASA GRANDE'
    gestion_localidad_1578.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1578 = importer.save_or_locate(gestion_localidad_1578)

    gestion_localidad_1579 = Localidad()
    gestion_localidad_1579.cod_postal = '5197'
    gestion_localidad_1579.localidad = 'RINCON DE LUNA'
    gestion_localidad_1579.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1579 = importer.save_or_locate(gestion_localidad_1579)

    gestion_localidad_1580 = Localidad()
    gestion_localidad_1580.cod_postal = '5887'
    gestion_localidad_1580.localidad = 'RIO ARRIBA'
    gestion_localidad_1580.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1580 = importer.save_or_locate(gestion_localidad_1580)

    gestion_localidad_1581 = Localidad()
    gestion_localidad_1581.cod_postal = '6134'
    gestion_localidad_1581.localidad = 'RIO BAMBA'
    gestion_localidad_1581.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1581 = importer.save_or_locate(gestion_localidad_1581)

    gestion_localidad_1582 = Localidad()
    gestion_localidad_1582.cod_postal = '5111'
    gestion_localidad_1582.localidad = 'RIO CEBALLOS'
    gestion_localidad_1582.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1582 = importer.save_or_locate(gestion_localidad_1582)

    gestion_localidad_1583 = Localidad()
    gestion_localidad_1583.cod_postal = '5221'
    gestion_localidad_1583.localidad = 'RIO CHICO'
    gestion_localidad_1583.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1583 = importer.save_or_locate(gestion_localidad_1583)

    gestion_localidad_1584 = Localidad()
    gestion_localidad_1584.cod_postal = '5800'
    gestion_localidad_1584.localidad = 'RIO CUARTO'
    gestion_localidad_1584.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1584 = importer.save_or_locate(gestion_localidad_1584)

    gestion_localidad_1585 = Localidad()
    gestion_localidad_1585.cod_postal = '5875'
    gestion_localidad_1585.localidad = 'RIO DE JAIME'
    gestion_localidad_1585.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1585 = importer.save_or_locate(gestion_localidad_1585)

    gestion_localidad_1586 = Localidad()
    gestion_localidad_1586.cod_postal = '5280'
    gestion_localidad_1586.localidad = 'RIO DE LA POBLACION'
    gestion_localidad_1586.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1586 = importer.save_or_locate(gestion_localidad_1586)

    gestion_localidad_1587 = Localidad()
    gestion_localidad_1587.cod_postal = '5212'
    gestion_localidad_1587.localidad = 'RIO DE LAS MANZANAS'
    gestion_localidad_1587.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1587 = importer.save_or_locate(gestion_localidad_1587)

    gestion_localidad_1588 = Localidad()
    gestion_localidad_1588.cod_postal = '5197'
    gestion_localidad_1588.localidad = 'RIO DEL DURAZNO'
    gestion_localidad_1588.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1588 = importer.save_or_locate(gestion_localidad_1588)

    gestion_localidad_1589 = Localidad()
    gestion_localidad_1589.cod_postal = '5221'
    gestion_localidad_1589.localidad = 'RIO DE LOS SAUCES'
    gestion_localidad_1589.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1589 = importer.save_or_locate(gestion_localidad_1589)

    gestion_localidad_1590 = Localidad()
    gestion_localidad_1590.cod_postal = '5821'
    gestion_localidad_1590.localidad = 'RIO DE LOS SAUCES'
    gestion_localidad_1590.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1590 = importer.save_or_locate(gestion_localidad_1590)

    gestion_localidad_1591 = Localidad()
    gestion_localidad_1591.cod_postal = '5221'
    gestion_localidad_1591.localidad = 'RIO DE LOS TALAS'
    gestion_localidad_1591.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1591 = importer.save_or_locate(gestion_localidad_1591)

    gestion_localidad_1592 = Localidad()
    gestion_localidad_1592.cod_postal = '5249'
    gestion_localidad_1592.localidad = 'RIO DULCE'
    gestion_localidad_1592.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1592 = importer.save_or_locate(gestion_localidad_1592)

    gestion_localidad_1593 = Localidad()
    gestion_localidad_1593.cod_postal = '5172'
    gestion_localidad_1593.localidad = 'RIO GRANDE'
    gestion_localidad_1593.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1593 = importer.save_or_locate(gestion_localidad_1593)

    gestion_localidad_1594 = Localidad()
    gestion_localidad_1594.cod_postal = '5199'
    gestion_localidad_1594.localidad = 'RIO GRANDE AMBOY'
    gestion_localidad_1594.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1594 = importer.save_or_locate(gestion_localidad_1594)

    gestion_localidad_1595 = Localidad()
    gestion_localidad_1595.cod_postal = '5297'
    gestion_localidad_1595.localidad = 'RIO HONDO'
    gestion_localidad_1595.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1595 = importer.save_or_locate(gestion_localidad_1595)

    gestion_localidad_1596 = Localidad()
    gestion_localidad_1596.cod_postal = '5875'
    gestion_localidad_1596.localidad = 'RIO HONDO'
    gestion_localidad_1596.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1596 = importer.save_or_locate(gestion_localidad_1596)

    gestion_localidad_1597 = Localidad()
    gestion_localidad_1597.cod_postal = '5891'
    gestion_localidad_1597.localidad = 'RIO HONDO'
    gestion_localidad_1597.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1597 = importer.save_or_locate(gestion_localidad_1597)

    gestion_localidad_1598 = Localidad()
    gestion_localidad_1598.cod_postal = '5189'
    gestion_localidad_1598.localidad = 'RIO LOS MOLINOS'
    gestion_localidad_1598.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1598 = importer.save_or_locate(gestion_localidad_1598)

    gestion_localidad_1599 = Localidad()
    gestion_localidad_1599.cod_postal = '5246'
    gestion_localidad_1599.localidad = 'RIO PEDRO'
    gestion_localidad_1599.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1599 = importer.save_or_locate(gestion_localidad_1599)

    gestion_localidad_1600 = Localidad()
    gestion_localidad_1600.cod_postal = '5221'
    gestion_localidad_1600.localidad = 'RIO PINTO'
    gestion_localidad_1600.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1600 = importer.save_or_locate(gestion_localidad_1600)

    gestion_localidad_1601 = Localidad()
    gestion_localidad_1601.cod_postal = '5127'
    gestion_localidad_1601.localidad = 'RIO PRIMERO'
    gestion_localidad_1601.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1601 = importer.save_or_locate(gestion_localidad_1601)

    gestion_localidad_1602 = Localidad()
    gestion_localidad_1602.cod_postal = '5249'
    gestion_localidad_1602.localidad = 'RIO SAN MIGUEL'
    gestion_localidad_1602.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1602 = importer.save_or_locate(gestion_localidad_1602)

    gestion_localidad_1603 = Localidad()
    gestion_localidad_1603.cod_postal = '5284'
    gestion_localidad_1603.localidad = 'RIO SECO'
    gestion_localidad_1603.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1603 = importer.save_or_locate(gestion_localidad_1603)

    gestion_localidad_1604 = Localidad()
    gestion_localidad_1604.cod_postal = '5801'
    gestion_localidad_1604.localidad = 'RIO SECO'
    gestion_localidad_1604.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1604 = importer.save_or_locate(gestion_localidad_1604)

    gestion_localidad_1605 = Localidad()
    gestion_localidad_1605.cod_postal = '5960'
    gestion_localidad_1605.localidad = 'RIO SEGUNDO'
    gestion_localidad_1605.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1605 = importer.save_or_locate(gestion_localidad_1605)

    gestion_localidad_1606 = Localidad()
    gestion_localidad_1606.cod_postal = '5850'
    gestion_localidad_1606.localidad = 'RIO TERCERO'
    gestion_localidad_1606.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1606 = importer.save_or_locate(gestion_localidad_1606)

    gestion_localidad_1607 = Localidad()
    gestion_localidad_1607.cod_postal = '5249'
    gestion_localidad_1607.localidad = 'RIO VIEJO'
    gestion_localidad_1607.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1607 = importer.save_or_locate(gestion_localidad_1607)

    gestion_localidad_1608 = Localidad()
    gestion_localidad_1608.cod_postal = '5209'
    gestion_localidad_1608.localidad = 'RODEITO'
    gestion_localidad_1608.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1608 = importer.save_or_locate(gestion_localidad_1608)

    gestion_localidad_1609 = Localidad()
    gestion_localidad_1609.cod_postal = '5821'
    gestion_localidad_1609.localidad = 'RODEO DE LOS CABALLOS'
    gestion_localidad_1609.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1609 = importer.save_or_locate(gestion_localidad_1609)

    gestion_localidad_1610 = Localidad()
    gestion_localidad_1610.cod_postal = '5875'
    gestion_localidad_1610.localidad = 'RODEO DE PIEDRA'
    gestion_localidad_1610.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1610 = importer.save_or_locate(gestion_localidad_1610)

    gestion_localidad_1611 = Localidad()
    gestion_localidad_1611.cod_postal = '5821'
    gestion_localidad_1611.localidad = 'RODEO LAS YEGUAS'
    gestion_localidad_1611.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1611 = importer.save_or_locate(gestion_localidad_1611)

    gestion_localidad_1612 = Localidad()
    gestion_localidad_1612.cod_postal = '5801'
    gestion_localidad_1612.localidad = 'RODEO VIEJO'
    gestion_localidad_1612.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1612 = importer.save_or_locate(gestion_localidad_1612)

    gestion_localidad_1613 = Localidad()
    gestion_localidad_1613.cod_postal = '5246'
    gestion_localidad_1613.localidad = 'ROJAS'
    gestion_localidad_1613.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1613 = importer.save_or_locate(gestion_localidad_1613)

    gestion_localidad_1614 = Localidad()
    gestion_localidad_1614.cod_postal = '6128'
    gestion_localidad_1614.localidad = 'ROSALES'
    gestion_localidad_1614.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1614 = importer.save_or_locate(gestion_localidad_1614)

    gestion_localidad_1615 = Localidad()
    gestion_localidad_1615.cod_postal = '6120'
    gestion_localidad_1615.localidad = 'RUIZ DIAZ DE GUZMAN'
    gestion_localidad_1615.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1615 = importer.save_or_locate(gestion_localidad_1615)

    gestion_localidad_1616 = Localidad()
    gestion_localidad_1616.cod_postal = '5289'
    gestion_localidad_1616.localidad = 'RUMIACO'
    gestion_localidad_1616.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1616 = importer.save_or_locate(gestion_localidad_1616)

    gestion_localidad_1617 = Localidad()
    gestion_localidad_1617.cod_postal = '5285'
    gestion_localidad_1617.localidad = 'RUMIHUASI'
    gestion_localidad_1617.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1617 = importer.save_or_locate(gestion_localidad_1617)

    gestion_localidad_1618 = Localidad()
    gestion_localidad_1618.cod_postal = '5101'
    gestion_localidad_1618.localidad = 'RUTA 111 KILOMETRO 14'
    gestion_localidad_1618.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1618 = importer.save_or_locate(gestion_localidad_1618)

    gestion_localidad_1619 = Localidad()
    gestion_localidad_1619.cod_postal = '5125'
    gestion_localidad_1619.localidad = 'RUTA 19 KILOMETRO 317'
    gestion_localidad_1619.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1619 = importer.save_or_locate(gestion_localidad_1619)

    gestion_localidad_1620 = Localidad()
    gestion_localidad_1620.cod_postal = '5945'
    gestion_localidad_1620.localidad = 'SACANTA'
    gestion_localidad_1620.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1620 = importer.save_or_locate(gestion_localidad_1620)

    gestion_localidad_1621 = Localidad()
    gestion_localidad_1621.cod_postal = '5875'
    gestion_localidad_1621.localidad = 'SAGRADA FAMILIA'
    gestion_localidad_1621.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1621 = importer.save_or_locate(gestion_localidad_1621)

    gestion_localidad_1622 = Localidad()
    gestion_localidad_1622.cod_postal = '5297'
    gestion_localidad_1622.localidad = 'SAGRADA FAMILIA'
    gestion_localidad_1622.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1622 = importer.save_or_locate(gestion_localidad_1622)

    gestion_localidad_1623 = Localidad()
    gestion_localidad_1623.cod_postal = '2525'
    gestion_localidad_1623.localidad = 'SAIRA'
    gestion_localidad_1623.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1623 = importer.save_or_locate(gestion_localidad_1623)

    gestion_localidad_1624 = Localidad()
    gestion_localidad_1624.cod_postal = '5200'
    gestion_localidad_1624.localidad = 'SAJON'
    gestion_localidad_1624.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1624 = importer.save_or_locate(gestion_localidad_1624)

    gestion_localidad_1625 = Localidad()
    gestion_localidad_1625.cod_postal = '2587'
    gestion_localidad_1625.localidad = 'SALADILLO'
    gestion_localidad_1625.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1625 = importer.save_or_locate(gestion_localidad_1625)

    gestion_localidad_1626 = Localidad()
    gestion_localidad_1626.cod_postal = '5149'
    gestion_localidad_1626.localidad = 'SALDAN'
    gestion_localidad_1626.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1626 = importer.save_or_locate(gestion_localidad_1626)

    gestion_localidad_1627 = Localidad()
    gestion_localidad_1627.cod_postal = '6120'
    gestion_localidad_1627.localidad = 'SALGUERO'
    gestion_localidad_1627.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1627 = importer.save_or_locate(gestion_localidad_1627)

    gestion_localidad_1628 = Localidad()
    gestion_localidad_1628.cod_postal = '5295'
    gestion_localidad_1628.localidad = 'SALSACATE'
    gestion_localidad_1628.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1628 = importer.save_or_locate(gestion_localidad_1628)

    gestion_localidad_1629 = Localidad()
    gestion_localidad_1629.cod_postal = '5113'
    gestion_localidad_1629.localidad = 'SALSIPUEDES'
    gestion_localidad_1629.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1629 = importer.save_or_locate(gestion_localidad_1629)

    gestion_localidad_1630 = Localidad()
    gestion_localidad_1630.cod_postal = '5873'
    gestion_localidad_1630.localidad = 'SALTO'
    gestion_localidad_1630.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1630 = importer.save_or_locate(gestion_localidad_1630)

    gestion_localidad_1631 = Localidad()
    gestion_localidad_1631.cod_postal = '5829'
    gestion_localidad_1631.localidad = 'SAMPACHO'
    gestion_localidad_1631.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1631 = importer.save_or_locate(gestion_localidad_1631)

    gestion_localidad_1632 = Localidad()
    gestion_localidad_1632.cod_postal = '5901'
    gestion_localidad_1632.localidad = 'SANABRIA'
    gestion_localidad_1632.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1632 = importer.save_or_locate(gestion_localidad_1632)

    gestion_localidad_1633 = Localidad()
    gestion_localidad_1633.cod_postal = '5191'
    gestion_localidad_1633.localidad = 'SAN AGUSTIN'
    gestion_localidad_1633.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1633 = importer.save_or_locate(gestion_localidad_1633)

    gestion_localidad_1634 = Localidad()
    gestion_localidad_1634.cod_postal = '5848'
    gestion_localidad_1634.localidad = 'SAN AMBROSIO'
    gestion_localidad_1634.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1634 = importer.save_or_locate(gestion_localidad_1634)

    gestion_localidad_1635 = Localidad()
    gestion_localidad_1635.cod_postal = '5281'
    gestion_localidad_1635.localidad = 'SAN ANTONIO'
    gestion_localidad_1635.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1635 = importer.save_or_locate(gestion_localidad_1635)

    gestion_localidad_1636 = Localidad()
    gestion_localidad_1636.cod_postal = '5870'
    gestion_localidad_1636.localidad = 'SAN ANTONIO'
    gestion_localidad_1636.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1636 = importer.save_or_locate(gestion_localidad_1636)

    gestion_localidad_1637 = Localidad()
    gestion_localidad_1637.cod_postal = '5121'
    gestion_localidad_1637.localidad = 'SAN ANTONIO'
    gestion_localidad_1637.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1637 = importer.save_or_locate(gestion_localidad_1637)

    gestion_localidad_1638 = Localidad()
    gestion_localidad_1638.cod_postal = '5153'
    gestion_localidad_1638.localidad = 'SAN ANTONIO DE ARREDONDO'
    gestion_localidad_1638.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1638 = importer.save_or_locate(gestion_localidad_1638)

    gestion_localidad_1639 = Localidad()
    gestion_localidad_1639.cod_postal = '5236'
    gestion_localidad_1639.localidad = 'SAN ANTONIO DE BELLA VISTA'
    gestion_localidad_1639.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1639 = importer.save_or_locate(gestion_localidad_1639)

    gestion_localidad_1640 = Localidad()
    gestion_localidad_1640.cod_postal = '2559'
    gestion_localidad_1640.localidad = 'SAN ANTONIO DE LITIN'
    gestion_localidad_1640.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1640 = importer.save_or_locate(gestion_localidad_1640)

    gestion_localidad_1641 = Localidad()
    gestion_localidad_1641.cod_postal = '5936'
    gestion_localidad_1641.localidad = 'SAN ANTONIO DE YUCAT'
    gestion_localidad_1641.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1641 = importer.save_or_locate(gestion_localidad_1641)

    gestion_localidad_1642 = Localidad()
    gestion_localidad_1642.cod_postal = '5119'
    gestion_localidad_1642.localidad = 'SAN ANTONIO NORTE'
    gestion_localidad_1642.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1642 = importer.save_or_locate(gestion_localidad_1642)

    gestion_localidad_1643 = Localidad()
    gestion_localidad_1643.cod_postal = '5249'
    gestion_localidad_1643.localidad = 'SAN BARTOLO'
    gestion_localidad_1643.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1643 = importer.save_or_locate(gestion_localidad_1643)

    gestion_localidad_1644 = Localidad()
    gestion_localidad_1644.cod_postal = '5801'
    gestion_localidad_1644.localidad = 'SAN BARTOLOME'
    gestion_localidad_1644.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1644 = importer.save_or_locate(gestion_localidad_1644)

    gestion_localidad_1645 = Localidad()
    gestion_localidad_1645.cod_postal = '5841'
    gestion_localidad_1645.localidad = 'SAN BASILIO'
    gestion_localidad_1645.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1645 = importer.save_or_locate(gestion_localidad_1645)

    gestion_localidad_1646 = Localidad()
    gestion_localidad_1646.cod_postal = '5848'
    gestion_localidad_1646.localidad = 'SAN BERNARDO'
    gestion_localidad_1646.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1646 = importer.save_or_locate(gestion_localidad_1646)

    gestion_localidad_1647 = Localidad()
    gestion_localidad_1647.cod_postal = '5201'
    gestion_localidad_1647.localidad = 'SAN BERNARDO'
    gestion_localidad_1647.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1647 = importer.save_or_locate(gestion_localidad_1647)

    gestion_localidad_1648 = Localidad()
    gestion_localidad_1648.cod_postal = '5164'
    gestion_localidad_1648.localidad = 'SAN BUENAVENTURA'
    gestion_localidad_1648.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1648 = importer.save_or_locate(gestion_localidad_1648)

    gestion_localidad_1649 = Localidad()
    gestion_localidad_1649.cod_postal = '5212'
    gestion_localidad_1649.localidad = 'SAN CARLOS'
    gestion_localidad_1649.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1649 = importer.save_or_locate(gestion_localidad_1649)

    gestion_localidad_1650 = Localidad()
    gestion_localidad_1650.cod_postal = '5291'
    gestion_localidad_1650.localidad = 'SAN CARLOS'
    gestion_localidad_1650.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1650 = importer.save_or_locate(gestion_localidad_1650)

    gestion_localidad_1651 = Localidad()
    gestion_localidad_1651.cod_postal = '2572'
    gestion_localidad_1651.localidad = 'SAN CARLOS'
    gestion_localidad_1651.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1651 = importer.save_or_locate(gestion_localidad_1651)

    gestion_localidad_1652 = Localidad()
    gestion_localidad_1652.cod_postal = '5187'
    gestion_localidad_1652.localidad = 'SAN CLEMENTE'
    gestion_localidad_1652.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1652 = importer.save_or_locate(gestion_localidad_1652)

    gestion_localidad_1653 = Localidad()
    gestion_localidad_1653.cod_postal = '5107'
    gestion_localidad_1653.localidad = 'SAN CRISTOBAL'
    gestion_localidad_1653.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1653 = importer.save_or_locate(gestion_localidad_1653)

    gestion_localidad_1654 = Localidad()
    gestion_localidad_1654.cod_postal = '5182'
    gestion_localidad_1654.localidad = 'SAN ESTEBAN'
    gestion_localidad_1654.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1654 = importer.save_or_locate(gestion_localidad_1654)

    gestion_localidad_1655 = Localidad()
    gestion_localidad_1655.cod_postal = '2561'
    gestion_localidad_1655.localidad = 'SAN EUSEBIO'
    gestion_localidad_1655.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1655 = importer.save_or_locate(gestion_localidad_1655)

    gestion_localidad_1656 = Localidad()
    gestion_localidad_1656.cod_postal = '2400'
    gestion_localidad_1656.localidad = 'SAN FRANCISCO'
    gestion_localidad_1656.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1656 = importer.save_or_locate(gestion_localidad_1656)

    gestion_localidad_1657 = Localidad()
    gestion_localidad_1657.cod_postal = '5209'
    gestion_localidad_1657.localidad = 'SAN FRANCISCO DEL CHAÑAR'
    gestion_localidad_1657.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1657 = importer.save_or_locate(gestion_localidad_1657)

    gestion_localidad_1658 = Localidad()
    gestion_localidad_1658.cod_postal = '5244'
    gestion_localidad_1658.localidad = 'SAN GABRIEL'
    gestion_localidad_1658.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1658 = importer.save_or_locate(gestion_localidad_1658)

    gestion_localidad_1659 = Localidad()
    gestion_localidad_1659.cod_postal = '5297'
    gestion_localidad_1659.localidad = 'SAN GERONIMO'
    gestion_localidad_1659.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1659 = importer.save_or_locate(gestion_localidad_1659)

    gestion_localidad_1660 = Localidad()
    gestion_localidad_1660.cod_postal = '5199'
    gestion_localidad_1660.localidad = 'SAN IGNACIO'
    gestion_localidad_1660.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1660 = importer.save_or_locate(gestion_localidad_1660)

    gestion_localidad_1661 = Localidad()
    gestion_localidad_1661.cod_postal = '5248'
    gestion_localidad_1661.localidad = 'SAN IGNACIO'
    gestion_localidad_1661.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1661 = importer.save_or_locate(gestion_localidad_1661)

    gestion_localidad_1662 = Localidad()
    gestion_localidad_1662.cod_postal = '5182'
    gestion_localidad_1662.localidad = 'SAN IGNACIO'
    gestion_localidad_1662.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1662 = importer.save_or_locate(gestion_localidad_1662)

    gestion_localidad_1663 = Localidad()
    gestion_localidad_1663.cod_postal = '5281'
    gestion_localidad_1663.localidad = 'SAN ISIDRO'
    gestion_localidad_1663.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1663 = importer.save_or_locate(gestion_localidad_1663)

    gestion_localidad_1664 = Localidad()
    gestion_localidad_1664.cod_postal = '5875'
    gestion_localidad_1664.localidad = 'SAN ISIDRO'
    gestion_localidad_1664.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1664 = importer.save_or_locate(gestion_localidad_1664)

    gestion_localidad_1665 = Localidad()
    gestion_localidad_1665.cod_postal = '5220'
    gestion_localidad_1665.localidad = 'SAN ISIDRO'
    gestion_localidad_1665.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1665 = importer.save_or_locate(gestion_localidad_1665)

    gestion_localidad_1666 = Localidad()
    gestion_localidad_1666.cod_postal = '5875'
    gestion_localidad_1666.localidad = 'SAN JAVIER'
    gestion_localidad_1666.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1666 = importer.save_or_locate(gestion_localidad_1666)

    gestion_localidad_1667 = Localidad()
    gestion_localidad_1667.cod_postal = '5297'
    gestion_localidad_1667.localidad = 'SAN JERONIMO'
    gestion_localidad_1667.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1667 = importer.save_or_locate(gestion_localidad_1667)

    gestion_localidad_1668 = Localidad()
    gestion_localidad_1668.cod_postal = '5963'
    gestion_localidad_1668.localidad = 'SAN JERONIMO'
    gestion_localidad_1668.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1668 = importer.save_or_locate(gestion_localidad_1668)

    gestion_localidad_1669 = Localidad()
    gestion_localidad_1669.cod_postal = '6123'
    gestion_localidad_1669.localidad = 'SAN JOAQUIN'
    gestion_localidad_1669.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1669 = importer.save_or_locate(gestion_localidad_1669)

    gestion_localidad_1670 = Localidad()
    gestion_localidad_1670.cod_postal = '5117'
    gestion_localidad_1670.localidad = 'SAN JORGE'
    gestion_localidad_1670.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1670 = importer.save_or_locate(gestion_localidad_1670)

    gestion_localidad_1671 = Localidad()
    gestion_localidad_1671.cod_postal = '5961'
    gestion_localidad_1671.localidad = 'SAN JOSE'
    gestion_localidad_1671.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1671 = importer.save_or_locate(gestion_localidad_1671)

    gestion_localidad_1672 = Localidad()
    gestion_localidad_1672.cod_postal = '2563'
    gestion_localidad_1672.localidad = 'SAN JOSE'
    gestion_localidad_1672.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1672 = importer.save_or_locate(gestion_localidad_1672)

    gestion_localidad_1673 = Localidad()
    gestion_localidad_1673.cod_postal = '5166'
    gestion_localidad_1673.localidad = 'SAN JOSE'
    gestion_localidad_1673.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1673 = importer.save_or_locate(gestion_localidad_1673)

    gestion_localidad_1674 = Localidad()
    gestion_localidad_1674.cod_postal = '5216'
    gestion_localidad_1674.localidad = 'SAN JOSE'
    gestion_localidad_1674.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1674 = importer.save_or_locate(gestion_localidad_1674)

    gestion_localidad_1675 = Localidad()
    gestion_localidad_1675.cod_postal = '5242'
    gestion_localidad_1675.localidad = 'SAN JOSE'
    gestion_localidad_1675.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1675 = importer.save_or_locate(gestion_localidad_1675)

    gestion_localidad_1676 = Localidad()
    gestion_localidad_1676.cod_postal = '5281'
    gestion_localidad_1676.localidad = 'SAN JOSE'
    gestion_localidad_1676.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1676 = importer.save_or_locate(gestion_localidad_1676)

    gestion_localidad_1677 = Localidad()
    gestion_localidad_1677.cod_postal = '5871'
    gestion_localidad_1677.localidad = 'SAN JOSE'
    gestion_localidad_1677.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1677 = importer.save_or_locate(gestion_localidad_1677)

    gestion_localidad_1678 = Localidad()
    gestion_localidad_1678.cod_postal = '5244'
    gestion_localidad_1678.localidad = 'SAN JOSE DE LA DORMIDA'
    gestion_localidad_1678.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1678 = importer.save_or_locate(gestion_localidad_1678)

    gestion_localidad_1679 = Localidad()
    gestion_localidad_1679.cod_postal = '5216'
    gestion_localidad_1679.localidad = 'SAN JOSE DE LAS SALINAS'
    gestion_localidad_1679.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1679 = importer.save_or_locate(gestion_localidad_1679)

    gestion_localidad_1680 = Localidad()
    gestion_localidad_1680.cod_postal = '2563'
    gestion_localidad_1680.localidad = 'SAN JOSE DEL SALTEÑO'
    gestion_localidad_1680.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1680 = importer.save_or_locate(gestion_localidad_1680)

    gestion_localidad_1681 = Localidad()
    gestion_localidad_1681.cod_postal = '5249'
    gestion_localidad_1681.localidad = 'SAN JUANCITO'
    gestion_localidad_1681.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1681 = importer.save_or_locate(gestion_localidad_1681)

    gestion_localidad_1682 = Localidad()
    gestion_localidad_1682.cod_postal = '5893'
    gestion_localidad_1682.localidad = 'SAN LORENZO'
    gestion_localidad_1682.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1682 = importer.save_or_locate(gestion_localidad_1682)

    gestion_localidad_1683 = Localidad()
    gestion_localidad_1683.cod_postal = '5221'
    gestion_localidad_1683.localidad = 'SAN LORENZO'
    gestion_localidad_1683.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1683 = importer.save_or_locate(gestion_localidad_1683)

    gestion_localidad_1684 = Localidad()
    gestion_localidad_1684.cod_postal = '5837'
    gestion_localidad_1684.localidad = 'SAN LUCAS NORTE'
    gestion_localidad_1684.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1684 = importer.save_or_locate(gestion_localidad_1684)

    gestion_localidad_1685 = Localidad()
    gestion_localidad_1685.cod_postal = '5209'
    gestion_localidad_1685.localidad = 'SAN LUIS'
    gestion_localidad_1685.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1685 = importer.save_or_locate(gestion_localidad_1685)

    gestion_localidad_1686 = Localidad()
    gestion_localidad_1686.cod_postal = '5282'
    gestion_localidad_1686.localidad = 'SAN MARCOS SIERRAS'
    gestion_localidad_1686.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1686 = importer.save_or_locate(gestion_localidad_1686)

    gestion_localidad_1687 = Localidad()
    gestion_localidad_1687.cod_postal = '2566'
    gestion_localidad_1687.localidad = 'SAN MARCOS SUD'
    gestion_localidad_1687.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1687 = importer.save_or_locate(gestion_localidad_1687)

    gestion_localidad_1688 = Localidad()
    gestion_localidad_1688.cod_postal = '5249'
    gestion_localidad_1688.localidad = 'SAN MARTIN'
    gestion_localidad_1688.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1688 = importer.save_or_locate(gestion_localidad_1688)

    gestion_localidad_1689 = Localidad()
    gestion_localidad_1689.cod_postal = '2664'
    gestion_localidad_1689.localidad = 'SAN MELITON'
    gestion_localidad_1689.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1689 = importer.save_or_locate(gestion_localidad_1689)

    gestion_localidad_1690 = Localidad()
    gestion_localidad_1690.cod_postal = '5212'
    gestion_localidad_1690.localidad = 'SAN MIGUEL'
    gestion_localidad_1690.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1690 = importer.save_or_locate(gestion_localidad_1690)

    gestion_localidad_1691 = Localidad()
    gestion_localidad_1691.cod_postal = '5117'
    gestion_localidad_1691.localidad = 'SAN MIGUEL'
    gestion_localidad_1691.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1691 = importer.save_or_locate(gestion_localidad_1691)

    gestion_localidad_1692 = Localidad()
    gestion_localidad_1692.cod_postal = '5871'
    gestion_localidad_1692.localidad = 'SAN MIGUEL SAN VICENTE'
    gestion_localidad_1692.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1692 = importer.save_or_locate(gestion_localidad_1692)

    gestion_localidad_1693 = Localidad()
    gestion_localidad_1693.cod_postal = '5281'
    gestion_localidad_1693.localidad = 'SAN NICOLAS'
    gestion_localidad_1693.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1693 = importer.save_or_locate(gestion_localidad_1693)

    gestion_localidad_1694 = Localidad()
    gestion_localidad_1694.cod_postal = '5871'
    gestion_localidad_1694.localidad = 'SAN NICOLAS'
    gestion_localidad_1694.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1694 = importer.save_or_locate(gestion_localidad_1694)

    gestion_localidad_1695 = Localidad()
    gestion_localidad_1695.cod_postal = '5187'
    gestion_localidad_1695.localidad = 'SAN NICOLAS'
    gestion_localidad_1695.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1695 = importer.save_or_locate(gestion_localidad_1695)

    gestion_localidad_1696 = Localidad()
    gestion_localidad_1696.cod_postal = '5220'
    gestion_localidad_1696.localidad = 'SAN PABLO'
    gestion_localidad_1696.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1696 = importer.save_or_locate(gestion_localidad_1696)

    gestion_localidad_1697 = Localidad()
    gestion_localidad_1697.cod_postal = '5209'
    gestion_localidad_1697.localidad = 'SAN PABLO'
    gestion_localidad_1697.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1697 = importer.save_or_locate(gestion_localidad_1697)

    gestion_localidad_1698 = Localidad()
    gestion_localidad_1698.cod_postal = '2559'
    gestion_localidad_1698.localidad = 'SAN PEDRO'
    gestion_localidad_1698.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1698 = importer.save_or_locate(gestion_localidad_1698)

    gestion_localidad_1699 = Localidad()
    gestion_localidad_1699.cod_postal = '5871'
    gestion_localidad_1699.localidad = 'SAN PEDRO'
    gestion_localidad_1699.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1699 = importer.save_or_locate(gestion_localidad_1699)

    gestion_localidad_1700 = Localidad()
    gestion_localidad_1700.cod_postal = '5249'
    gestion_localidad_1700.localidad = 'SAN PEDRO'
    gestion_localidad_1700.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1700 = importer.save_or_locate(gestion_localidad_1700)

    gestion_localidad_1701 = Localidad()
    gestion_localidad_1701.cod_postal = '5871'
    gestion_localidad_1701.localidad = 'SAN PEDRO DE SAN ALBERTO'
    gestion_localidad_1701.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1701 = importer.save_or_locate(gestion_localidad_1701)

    gestion_localidad_1702 = Localidad()
    gestion_localidad_1702.cod_postal = '5201'
    gestion_localidad_1702.localidad = 'SAN PEDRO DE TOYOS'
    gestion_localidad_1702.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1702 = importer.save_or_locate(gestion_localidad_1702)

    gestion_localidad_1703 = Localidad()
    gestion_localidad_1703.cod_postal = '5205'
    gestion_localidad_1703.localidad = 'SAN PEDRO NORTE'
    gestion_localidad_1703.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1703 = importer.save_or_locate(gestion_localidad_1703)

    gestion_localidad_1704 = Localidad()
    gestion_localidad_1704.cod_postal = '5221'
    gestion_localidad_1704.localidad = 'SAN PELLEGRINO'
    gestion_localidad_1704.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1704 = importer.save_or_locate(gestion_localidad_1704)

    gestion_localidad_1705 = Localidad()
    gestion_localidad_1705.cod_postal = '5960'
    gestion_localidad_1705.localidad = 'SAN RAFAEL'
    gestion_localidad_1705.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1705 = importer.save_or_locate(gestion_localidad_1705)

    gestion_localidad_1706 = Localidad()
    gestion_localidad_1706.cod_postal = '5139'
    gestion_localidad_1706.localidad = 'SAN RAFAEL'
    gestion_localidad_1706.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1706 = importer.save_or_locate(gestion_localidad_1706)

    gestion_localidad_1707 = Localidad()
    gestion_localidad_1707.cod_postal = '5871'
    gestion_localidad_1707.localidad = 'SAN RAFAEL'
    gestion_localidad_1707.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1707 = importer.save_or_locate(gestion_localidad_1707)

    gestion_localidad_1708 = Localidad()
    gestion_localidad_1708.cod_postal = '5137'
    gestion_localidad_1708.localidad = 'SAN RAMON'
    gestion_localidad_1708.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1708 = importer.save_or_locate(gestion_localidad_1708)

    gestion_localidad_1709 = Localidad()
    gestion_localidad_1709.cod_postal = '5249'
    gestion_localidad_1709.localidad = 'SAN RAMON'
    gestion_localidad_1709.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1709 = importer.save_or_locate(gestion_localidad_1709)

    gestion_localidad_1710 = Localidad()
    gestion_localidad_1710.cod_postal = '5199'
    gestion_localidad_1710.localidad = 'SAN ROQUE'
    gestion_localidad_1710.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1710 = importer.save_or_locate(gestion_localidad_1710)

    gestion_localidad_1711 = Localidad()
    gestion_localidad_1711.cod_postal = '5227'
    gestion_localidad_1711.localidad = 'SAN ROQUE'
    gestion_localidad_1711.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1711 = importer.save_or_locate(gestion_localidad_1711)

    gestion_localidad_1712 = Localidad()
    gestion_localidad_1712.cod_postal = '5870'
    gestion_localidad_1712.localidad = 'SAN ROQUE'
    gestion_localidad_1712.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1712 = importer.save_or_locate(gestion_localidad_1712)

    gestion_localidad_1713 = Localidad()
    gestion_localidad_1713.cod_postal = '5149'
    gestion_localidad_1713.localidad = 'SAN ROQUE'
    gestion_localidad_1713.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1713 = importer.save_or_locate(gestion_localidad_1713)

    gestion_localidad_1714 = Localidad()
    gestion_localidad_1714.cod_postal = '5231'
    gestion_localidad_1714.localidad = 'SAN ROQUE LAS ARRIAS'
    gestion_localidad_1714.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1714 = importer.save_or_locate(gestion_localidad_1714)

    gestion_localidad_1715 = Localidad()
    gestion_localidad_1715.cod_postal = '5227'
    gestion_localidad_1715.localidad = 'SAN SALVADOR'
    gestion_localidad_1715.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1715 = importer.save_or_locate(gestion_localidad_1715)

    gestion_localidad_1716 = Localidad()
    gestion_localidad_1716.cod_postal = '5282'
    gestion_localidad_1716.localidad = 'SAN SALVADOR'
    gestion_localidad_1716.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1716 = importer.save_or_locate(gestion_localidad_1716)

    gestion_localidad_1717 = Localidad()
    gestion_localidad_1717.cod_postal = '5889'
    gestion_localidad_1717.localidad = 'SAN SEBASTIAN'
    gestion_localidad_1717.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1717 = importer.save_or_locate(gestion_localidad_1717)

    gestion_localidad_1718 = Localidad()
    gestion_localidad_1718.cod_postal = '5209'
    gestion_localidad_1718.localidad = 'SANTA ANA'
    gestion_localidad_1718.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1718 = importer.save_or_locate(gestion_localidad_1718)

    gestion_localidad_1719 = Localidad()
    gestion_localidad_1719.cod_postal = '5284'
    gestion_localidad_1719.localidad = 'SANTA ANA'
    gestion_localidad_1719.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1719 = importer.save_or_locate(gestion_localidad_1719)

    gestion_localidad_1720 = Localidad()
    gestion_localidad_1720.cod_postal = '5221'
    gestion_localidad_1720.localidad = 'SANTA CATALINA'
    gestion_localidad_1720.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1720 = importer.save_or_locate(gestion_localidad_1720)

    gestion_localidad_1721 = Localidad()
    gestion_localidad_1721.cod_postal = '5248'
    gestion_localidad_1721.localidad = 'SANTA CATALINA'
    gestion_localidad_1721.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1721 = importer.save_or_locate(gestion_localidad_1721)

    gestion_localidad_1722 = Localidad()
    gestion_localidad_1722.cod_postal = '5825'
    gestion_localidad_1722.localidad = 'SANTA CATALINA'
    gestion_localidad_1722.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1722 = importer.save_or_locate(gestion_localidad_1722)

    gestion_localidad_1723 = Localidad()
    gestion_localidad_1723.cod_postal = '2561'
    gestion_localidad_1723.localidad = 'SANTA CECILIA'
    gestion_localidad_1723.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1723 = importer.save_or_locate(gestion_localidad_1723)

    gestion_localidad_1724 = Localidad()
    gestion_localidad_1724.cod_postal = '6123'
    gestion_localidad_1724.localidad = 'SANTA CLARA'
    gestion_localidad_1724.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1724 = importer.save_or_locate(gestion_localidad_1724)

    gestion_localidad_1725 = Localidad()
    gestion_localidad_1725.cod_postal = '6134'
    gestion_localidad_1725.localidad = 'SANTA CRISTINA'
    gestion_localidad_1725.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1725 = importer.save_or_locate(gestion_localidad_1725)

    gestion_localidad_1726 = Localidad()
    gestion_localidad_1726.cod_postal = '5201'
    gestion_localidad_1726.localidad = 'SANTA CRUZ'
    gestion_localidad_1726.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1726 = importer.save_or_locate(gestion_localidad_1726)

    gestion_localidad_1727 = Localidad()
    gestion_localidad_1727.cod_postal = '5246'
    gestion_localidad_1727.localidad = 'SANTA ELENA'
    gestion_localidad_1727.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1727 = importer.save_or_locate(gestion_localidad_1727)

    gestion_localidad_1728 = Localidad()
    gestion_localidad_1728.cod_postal = '5131'
    gestion_localidad_1728.localidad = 'SANTA ELENA'
    gestion_localidad_1728.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1728 = importer.save_or_locate(gestion_localidad_1728)

    gestion_localidad_1729 = Localidad()
    gestion_localidad_1729.cod_postal = '2671'
    gestion_localidad_1729.localidad = 'SANTA EUFEMIA'
    gestion_localidad_1729.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1729 = importer.save_or_locate(gestion_localidad_1729)

    gestion_localidad_1730 = Localidad()
    gestion_localidad_1730.cod_postal = '5282'
    gestion_localidad_1730.localidad = 'SANTA ISABEL'
    gestion_localidad_1730.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1730 = importer.save_or_locate(gestion_localidad_1730)

    gestion_localidad_1731 = Localidad()
    gestion_localidad_1731.cod_postal = '5249'
    gestion_localidad_1731.localidad = 'SANTA ISABEL'
    gestion_localidad_1731.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1731 = importer.save_or_locate(gestion_localidad_1731)

    gestion_localidad_1732 = Localidad()
    gestion_localidad_1732.cod_postal = '5229'
    gestion_localidad_1732.localidad = 'SANTA LUCIA'
    gestion_localidad_1732.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1732 = importer.save_or_locate(gestion_localidad_1732)

    gestion_localidad_1733 = Localidad()
    gestion_localidad_1733.cod_postal = '6127'
    gestion_localidad_1733.localidad = 'SANTA MAGDALENA'
    gestion_localidad_1733.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1733 = importer.save_or_locate(gestion_localidad_1733)

    gestion_localidad_1734 = Localidad()
    gestion_localidad_1734.cod_postal = '5889'
    gestion_localidad_1734.localidad = 'SANTA MARIA'
    gestion_localidad_1734.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1734 = importer.save_or_locate(gestion_localidad_1734)

    gestion_localidad_1735 = Localidad()
    gestion_localidad_1735.cod_postal = '2651'
    gestion_localidad_1735.localidad = 'SANTA MARIA'
    gestion_localidad_1735.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1735 = importer.save_or_locate(gestion_localidad_1735)

    gestion_localidad_1736 = Localidad()
    gestion_localidad_1736.cod_postal = '5236'
    gestion_localidad_1736.localidad = 'SANTA MARIA'
    gestion_localidad_1736.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1736 = importer.save_or_locate(gestion_localidad_1736)

    gestion_localidad_1737 = Localidad()
    gestion_localidad_1737.cod_postal = '5164'
    gestion_localidad_1737.localidad = 'SANTA MARIA DE PUNILLA'
    gestion_localidad_1737.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1737 = importer.save_or_locate(gestion_localidad_1737)

    gestion_localidad_1738 = Localidad()
    gestion_localidad_1738.cod_postal = '5209'
    gestion_localidad_1738.localidad = 'SANTA MARIA DE SOBREMONTE'
    gestion_localidad_1738.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1738 = importer.save_or_locate(gestion_localidad_1738)

    gestion_localidad_1739 = Localidad()
    gestion_localidad_1739.cod_postal = '5197'
    gestion_localidad_1739.localidad = 'SANTA MONICA'
    gestion_localidad_1739.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1739 = importer.save_or_locate(gestion_localidad_1739)

    gestion_localidad_1740 = Localidad()
    gestion_localidad_1740.cod_postal = '5248'
    gestion_localidad_1740.localidad = 'SANTANILLA'
    gestion_localidad_1740.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1740 = importer.save_or_locate(gestion_localidad_1740)

    gestion_localidad_1741 = Localidad()
    gestion_localidad_1741.cod_postal = '5189'
    gestion_localidad_1741.localidad = 'SANTA RITA'
    gestion_localidad_1741.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1741 = importer.save_or_locate(gestion_localidad_1741)

    gestion_localidad_1742 = Localidad()
    gestion_localidad_1742.cod_postal = '5893'
    gestion_localidad_1742.localidad = 'SANTA RITA'
    gestion_localidad_1742.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1742 = importer.save_or_locate(gestion_localidad_1742)

    gestion_localidad_1743 = Localidad()
    gestion_localidad_1743.cod_postal = '2413'
    gestion_localidad_1743.localidad = 'SANTA RITA'
    gestion_localidad_1743.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1743 = importer.save_or_locate(gestion_localidad_1743)

    gestion_localidad_1744 = Localidad()
    gestion_localidad_1744.cod_postal = '5200'
    gestion_localidad_1744.localidad = 'SANTA RITA'
    gestion_localidad_1744.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1744 = importer.save_or_locate(gestion_localidad_1744)

    gestion_localidad_1745 = Localidad()
    gestion_localidad_1745.cod_postal = '5166'
    gestion_localidad_1745.localidad = 'SANTA ROSA'
    gestion_localidad_1745.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1745 = importer.save_or_locate(gestion_localidad_1745)

    gestion_localidad_1746 = Localidad()
    gestion_localidad_1746.cod_postal = '5913'
    gestion_localidad_1746.localidad = 'SANTA ROSA'
    gestion_localidad_1746.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1746 = importer.save_or_locate(gestion_localidad_1746)

    gestion_localidad_1747 = Localidad()
    gestion_localidad_1747.cod_postal = '5909'
    gestion_localidad_1747.localidad = 'SANTA ROSA'
    gestion_localidad_1747.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1747 = importer.save_or_locate(gestion_localidad_1747)

    gestion_localidad_1748 = Localidad()
    gestion_localidad_1748.cod_postal = '5196'
    gestion_localidad_1748.localidad = 'SANTA ROSA DE CALAMUCHITA'
    gestion_localidad_1748.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1748 = importer.save_or_locate(gestion_localidad_1748)

    gestion_localidad_1749 = Localidad()
    gestion_localidad_1749.cod_postal = '5133'
    gestion_localidad_1749.localidad = 'SANTA ROSA DE RIO PRIMERO'
    gestion_localidad_1749.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1749 = importer.save_or_locate(gestion_localidad_1749)

    gestion_localidad_1750 = Localidad()
    gestion_localidad_1750.cod_postal = '5174'
    gestion_localidad_1750.localidad = 'SANTA ROSA HUERTA GRANDE'
    gestion_localidad_1750.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1750 = importer.save_or_locate(gestion_localidad_1750)

    gestion_localidad_1751 = Localidad()
    gestion_localidad_1751.cod_postal = '5221'
    gestion_localidad_1751.localidad = 'SANTA SABINA'
    gestion_localidad_1751.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1751 = importer.save_or_locate(gestion_localidad_1751)

    gestion_localidad_1752 = Localidad()
    gestion_localidad_1752.cod_postal = '5221'
    gestion_localidad_1752.localidad = 'SANTA TERESA'
    gestion_localidad_1752.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1752 = importer.save_or_locate(gestion_localidad_1752)

    gestion_localidad_1753 = Localidad()
    gestion_localidad_1753.cod_postal = '2675'
    gestion_localidad_1753.localidad = 'SANTA VICTORIA'
    gestion_localidad_1753.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1753 = importer.save_or_locate(gestion_localidad_1753)

    gestion_localidad_1754 = Localidad()
    gestion_localidad_1754.cod_postal = '5125'
    gestion_localidad_1754.localidad = 'SANTIAGO TEMPLE'
    gestion_localidad_1754.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1754 = importer.save_or_locate(gestion_localidad_1754)

    gestion_localidad_1755 = Localidad()
    gestion_localidad_1755.cod_postal = '5871'
    gestion_localidad_1755.localidad = 'SANTO DOMINGO'
    gestion_localidad_1755.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1755 = importer.save_or_locate(gestion_localidad_1755)

    gestion_localidad_1756 = Localidad()
    gestion_localidad_1756.cod_postal = '5209'
    gestion_localidad_1756.localidad = 'SANTO DOMINGO'
    gestion_localidad_1756.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1756 = importer.save_or_locate(gestion_localidad_1756)

    gestion_localidad_1757 = Localidad()
    gestion_localidad_1757.cod_postal = '5220'
    gestion_localidad_1757.localidad = 'SANTO TOMAS'
    gestion_localidad_1757.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1757 = importer.save_or_locate(gestion_localidad_1757)

    gestion_localidad_1758 = Localidad()
    gestion_localidad_1758.cod_postal = '5200'
    gestion_localidad_1758.localidad = 'SAN VICENTE'
    gestion_localidad_1758.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1758 = importer.save_or_locate(gestion_localidad_1758)

    gestion_localidad_1759 = Localidad()
    gestion_localidad_1759.cod_postal = '5871'
    gestion_localidad_1759.localidad = 'SAN VICENTE'
    gestion_localidad_1759.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1759 = importer.save_or_locate(gestion_localidad_1759)

    gestion_localidad_1760 = Localidad()
    gestion_localidad_1760.cod_postal = '2550'
    gestion_localidad_1760.localidad = 'SAN VICENTE'
    gestion_localidad_1760.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1760 = importer.save_or_locate(gestion_localidad_1760)

    gestion_localidad_1761 = Localidad()
    gestion_localidad_1761.cod_postal = '5291'
    gestion_localidad_1761.localidad = 'SAPANSOTO'
    gestion_localidad_1761.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1761 = importer.save_or_locate(gestion_localidad_1761)

    gestion_localidad_1762 = Localidad()
    gestion_localidad_1762.cod_postal = '5196'
    gestion_localidad_1762.localidad = 'SARLACO'
    gestion_localidad_1762.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1762 = importer.save_or_locate(gestion_localidad_1762)

    gestion_localidad_1763 = Localidad()
    gestion_localidad_1763.cod_postal = '5925'
    gestion_localidad_1763.localidad = 'SARMICA'
    gestion_localidad_1763.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1763 = importer.save_or_locate(gestion_localidad_1763)

    gestion_localidad_1764 = Localidad()
    gestion_localidad_1764.cod_postal = '5212'
    gestion_localidad_1764.localidad = 'SARMIENTO'
    gestion_localidad_1764.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1764 = importer.save_or_locate(gestion_localidad_1764)

    gestion_localidad_1765 = Localidad()
    gestion_localidad_1765.cod_postal = '5943'
    gestion_localidad_1765.localidad = 'SATURNINO M LASPIUR'
    gestion_localidad_1765.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1765 = importer.save_or_locate(gestion_localidad_1765)

    gestion_localidad_1766 = Localidad()
    gestion_localidad_1766.cod_postal = '5871'
    gestion_localidad_1766.localidad = 'SAUCE ARRIBA'
    gestion_localidad_1766.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1766 = importer.save_or_locate(gestion_localidad_1766)

    gestion_localidad_1767 = Localidad()
    gestion_localidad_1767.cod_postal = '5182'
    gestion_localidad_1767.localidad = 'SAUCE ARRIBA'
    gestion_localidad_1767.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1767 = importer.save_or_locate(gestion_localidad_1767)

    gestion_localidad_1768 = Localidad()
    gestion_localidad_1768.cod_postal = '5200'
    gestion_localidad_1768.localidad = 'SAUCE CHIQUITO'
    gestion_localidad_1768.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1768 = importer.save_or_locate(gestion_localidad_1768)

    gestion_localidad_1769 = Localidad()
    gestion_localidad_1769.cod_postal = '5297'
    gestion_localidad_1769.localidad = 'SAUCE DE LOS QUEVEDOS'
    gestion_localidad_1769.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1769 = importer.save_or_locate(gestion_localidad_1769)

    gestion_localidad_1770 = Localidad()
    gestion_localidad_1770.cod_postal = '5200'
    gestion_localidad_1770.localidad = 'SAUCE PUNCO'
    gestion_localidad_1770.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1770 = importer.save_or_locate(gestion_localidad_1770)

    gestion_localidad_1771 = Localidad()
    gestion_localidad_1771.cod_postal = '5231'
    gestion_localidad_1771.localidad = 'SEBASTIAN ELCANO'
    gestion_localidad_1771.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1771 = importer.save_or_locate(gestion_localidad_1771)

    gestion_localidad_1772 = Localidad()
    gestion_localidad_1772.cod_postal = '2419'
    gestion_localidad_1772.localidad = 'SEEBER'
    gestion_localidad_1772.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1772 = importer.save_or_locate(gestion_localidad_1772)

    gestion_localidad_1773 = Localidad()
    gestion_localidad_1773.cod_postal = '5857'
    gestion_localidad_1773.localidad = 'SEGUNDA USINA'
    gestion_localidad_1773.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1773 = importer.save_or_locate(gestion_localidad_1773)

    gestion_localidad_1774 = Localidad()
    gestion_localidad_1774.cod_postal = '5284'
    gestion_localidad_1774.localidad = 'SENDAS GRANDES'
    gestion_localidad_1774.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1774 = importer.save_or_locate(gestion_localidad_1774)

    gestion_localidad_1775 = Localidad()
    gestion_localidad_1775.cod_postal = '6125'
    gestion_localidad_1775.localidad = 'SERRANO'
    gestion_localidad_1775.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1775 = importer.save_or_locate(gestion_localidad_1775)

    gestion_localidad_1776 = Localidad()
    gestion_localidad_1776.cod_postal = '5270'
    gestion_localidad_1776.localidad = 'SERREZUELA'
    gestion_localidad_1776.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1776 = importer.save_or_locate(gestion_localidad_1776)

    gestion_localidad_1777 = Localidad()
    gestion_localidad_1777.cod_postal = '5205'
    gestion_localidad_1777.localidad = 'SEVILLA'
    gestion_localidad_1777.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1777 = importer.save_or_locate(gestion_localidad_1777)

    gestion_localidad_1778 = Localidad()
    gestion_localidad_1778.cod_postal = '5819'
    gestion_localidad_1778.localidad = 'SIERRA BLANCA'
    gestion_localidad_1778.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1778 = importer.save_or_locate(gestion_localidad_1778)

    gestion_localidad_1779 = Localidad()
    gestion_localidad_1779.cod_postal = '5291'
    gestion_localidad_1779.localidad = 'SIERRA DE ABREGU'
    gestion_localidad_1779.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1779 = importer.save_or_locate(gestion_localidad_1779)

    gestion_localidad_1780 = Localidad()
    gestion_localidad_1780.cod_postal = '5291'
    gestion_localidad_1780.localidad = 'SIERRA DE LAS PAREDES'
    gestion_localidad_1780.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1780 = importer.save_or_locate(gestion_localidad_1780)

    gestion_localidad_1781 = Localidad()
    gestion_localidad_1781.cod_postal = '5189'
    gestion_localidad_1781.localidad = 'SIERRAS MORENAS'
    gestion_localidad_1781.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1781 = importer.save_or_locate(gestion_localidad_1781)

    gestion_localidad_1782 = Localidad()
    gestion_localidad_1782.cod_postal = '5242'
    gestion_localidad_1782.localidad = 'SIMBOLAR'
    gestion_localidad_1782.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1782 = importer.save_or_locate(gestion_localidad_1782)

    gestion_localidad_1783 = Localidad()
    gestion_localidad_1783.cod_postal = '5281'
    gestion_localidad_1783.localidad = 'SIMBOLAR'
    gestion_localidad_1783.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1783 = importer.save_or_locate(gestion_localidad_1783)

    gestion_localidad_1784 = Localidad()
    gestion_localidad_1784.cod_postal = '5220'
    gestion_localidad_1784.localidad = 'SINSACATE'
    gestion_localidad_1784.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1784 = importer.save_or_locate(gestion_localidad_1784)

    gestion_localidad_1785 = Localidad()
    gestion_localidad_1785.cod_postal = '5191'
    gestion_localidad_1785.localidad = 'SOCONCHO'
    gestion_localidad_1785.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1785 = importer.save_or_locate(gestion_localidad_1785)

    gestion_localidad_1786 = Localidad()
    gestion_localidad_1786.cod_postal = '5209'
    gestion_localidad_1786.localidad = 'SOCORRO'
    gestion_localidad_1786.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1786 = importer.save_or_locate(gestion_localidad_1786)

    gestion_localidad_1787 = Localidad()
    gestion_localidad_1787.cod_postal = '5153'
    gestion_localidad_1787.localidad = 'SOLARES DE YCHO CRUZ'
    gestion_localidad_1787.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1787 = importer.save_or_locate(gestion_localidad_1787)

    gestion_localidad_1788 = Localidad()
    gestion_localidad_1788.cod_postal = '5189'
    gestion_localidad_1788.localidad = 'SOLAR LOS MOLINOS'
    gestion_localidad_1788.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1788 = importer.save_or_locate(gestion_localidad_1788)

    gestion_localidad_1789 = Localidad()
    gestion_localidad_1789.cod_postal = '5137'
    gestion_localidad_1789.localidad = 'SOLEDAD'
    gestion_localidad_1789.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1789 = importer.save_or_locate(gestion_localidad_1789)

    gestion_localidad_1790 = Localidad()
    gestion_localidad_1790.cod_postal = '5829'
    gestion_localidad_1790.localidad = 'SORIA'
    gestion_localidad_1790.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1790 = importer.save_or_locate(gestion_localidad_1790)

    gestion_localidad_1791 = Localidad()
    gestion_localidad_1791.cod_postal = '5837'
    gestion_localidad_1791.localidad = 'SUCO'
    gestion_localidad_1791.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1791 = importer.save_or_locate(gestion_localidad_1791)

    gestion_localidad_1792 = Localidad()
    gestion_localidad_1792.cod_postal = '5291'
    gestion_localidad_1792.localidad = 'SUNCHAL'
    gestion_localidad_1792.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1792 = importer.save_or_locate(gestion_localidad_1792)

    gestion_localidad_1793 = Localidad()
    gestion_localidad_1793.cod_postal = '5184'
    gestion_localidad_1793.localidad = 'SUNCHO HUICO'
    gestion_localidad_1793.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1793 = importer.save_or_locate(gestion_localidad_1793)

    gestion_localidad_1794 = Localidad()
    gestion_localidad_1794.cod_postal = '5870'
    gestion_localidad_1794.localidad = 'TABANILLO'
    gestion_localidad_1794.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1794 = importer.save_or_locate(gestion_localidad_1794)

    gestion_localidad_1795 = Localidad()
    gestion_localidad_1795.cod_postal = '5281'
    gestion_localidad_1795.localidad = 'TABAQUILLO'
    gestion_localidad_1795.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1795 = importer.save_or_locate(gestion_localidad_1795)

    gestion_localidad_1796 = Localidad()
    gestion_localidad_1796.cod_postal = '5249'
    gestion_localidad_1796.localidad = 'TACO POZO'
    gestion_localidad_1796.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1796 = importer.save_or_locate(gestion_localidad_1796)

    gestion_localidad_1797 = Localidad()
    gestion_localidad_1797.cod_postal = '6123'
    gestion_localidad_1797.localidad = 'TACUREL'
    gestion_localidad_1797.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1797 = importer.save_or_locate(gestion_localidad_1797)

    gestion_localidad_1798 = Localidad()
    gestion_localidad_1798.cod_postal = '5233'
    gestion_localidad_1798.localidad = 'TAJAMARES'
    gestion_localidad_1798.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1798 = importer.save_or_locate(gestion_localidad_1798)

    gestion_localidad_1799 = Localidad()
    gestion_localidad_1799.cod_postal = '5297'
    gestion_localidad_1799.localidad = 'TALA CAÑADA'
    gestion_localidad_1799.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1799 = importer.save_or_locate(gestion_localidad_1799)

    gestion_localidad_1800 = Localidad()
    gestion_localidad_1800.cod_postal = '5859'
    gestion_localidad_1800.localidad = 'TALA CRUZ'
    gestion_localidad_1800.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1800 = importer.save_or_locate(gestion_localidad_1800)

    gestion_localidad_1801 = Localidad()
    gestion_localidad_1801.cod_postal = '5284'
    gestion_localidad_1801.localidad = 'TALA DEL RIO SECO'
    gestion_localidad_1801.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1801 = importer.save_or_locate(gestion_localidad_1801)

    gestion_localidad_1802 = Localidad()
    gestion_localidad_1802.cod_postal = '5153'
    gestion_localidad_1802.localidad = 'TALA HUASI'
    gestion_localidad_1802.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1802 = importer.save_or_locate(gestion_localidad_1802)

    gestion_localidad_1803 = Localidad()
    gestion_localidad_1803.cod_postal = '5291'
    gestion_localidad_1803.localidad = 'TALAINI'
    gestion_localidad_1803.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1803 = importer.save_or_locate(gestion_localidad_1803)

    gestion_localidad_1804 = Localidad()
    gestion_localidad_1804.cod_postal = '5131'
    gestion_localidad_1804.localidad = 'TALA NORTE'
    gestion_localidad_1804.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1804 = importer.save_or_locate(gestion_localidad_1804)

    gestion_localidad_1805 = Localidad()
    gestion_localidad_1805.cod_postal = '5127'
    gestion_localidad_1805.localidad = 'TALA SUD'
    gestion_localidad_1805.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1805 = importer.save_or_locate(gestion_localidad_1805)

    gestion_localidad_1806 = Localidad()
    gestion_localidad_1806.cod_postal = '5933'
    gestion_localidad_1806.localidad = 'TANCACHA'
    gestion_localidad_1806.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1806 = importer.save_or_locate(gestion_localidad_1806)

    gestion_localidad_1807 = Localidad()
    gestion_localidad_1807.cod_postal = '5155'
    gestion_localidad_1807.localidad = 'TANTI'
    gestion_localidad_1807.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1807 = importer.save_or_locate(gestion_localidad_1807)

    gestion_localidad_1808 = Localidad()
    gestion_localidad_1808.cod_postal = '5155'
    gestion_localidad_1808.localidad = 'TANTI LOMAS'
    gestion_localidad_1808.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1808 = importer.save_or_locate(gestion_localidad_1808)

    gestion_localidad_1809 = Localidad()
    gestion_localidad_1809.cod_postal = '5155'
    gestion_localidad_1809.localidad = 'TANTI NUEVO'
    gestion_localidad_1809.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1809 = importer.save_or_locate(gestion_localidad_1809)

    gestion_localidad_1810 = Localidad()
    gestion_localidad_1810.cod_postal = '5299'
    gestion_localidad_1810.localidad = 'TARUCA PAMPA'
    gestion_localidad_1810.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1810 = importer.save_or_locate(gestion_localidad_1810)

    gestion_localidad_1811 = Localidad()
    gestion_localidad_1811.cod_postal = '5284'
    gestion_localidad_1811.localidad = 'TASACUNA'
    gestion_localidad_1811.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1811 = importer.save_or_locate(gestion_localidad_1811)

    gestion_localidad_1812 = Localidad()
    gestion_localidad_1812.cod_postal = '5893'
    gestion_localidad_1812.localidad = 'TASMA'
    gestion_localidad_1812.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1812 = importer.save_or_locate(gestion_localidad_1812)

    gestion_localidad_1813 = Localidad()
    gestion_localidad_1813.cod_postal = '5813'
    gestion_localidad_1813.localidad = 'TEGUA'
    gestion_localidad_1813.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1813 = importer.save_or_locate(gestion_localidad_1813)

    gestion_localidad_1814 = Localidad()
    gestion_localidad_1814.cod_postal = '5125'
    gestion_localidad_1814.localidad = 'TEJEDA'
    gestion_localidad_1814.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1814 = importer.save_or_locate(gestion_localidad_1814)

    gestion_localidad_1815 = Localidad()
    gestion_localidad_1815.cod_postal = '5189'
    gestion_localidad_1815.localidad = 'TERCERA'
    gestion_localidad_1815.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1815 = importer.save_or_locate(gestion_localidad_1815)

    gestion_localidad_1816 = Localidad()
    gestion_localidad_1816.cod_postal = '5101'
    gestion_localidad_1816.localidad = 'TERCER CUERPO DEL EJERCITO'
    gestion_localidad_1816.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1816 = importer.save_or_locate(gestion_localidad_1816)

    gestion_localidad_1817 = Localidad()
    gestion_localidad_1817.cod_postal = '5927'
    gestion_localidad_1817.localidad = 'TICINO'
    gestion_localidad_1817.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1817 = importer.save_or_locate(gestion_localidad_1817)

    gestion_localidad_1818 = Localidad()
    gestion_localidad_1818.cod_postal = '5859'
    gestion_localidad_1818.localidad = 'TIGRE MUERTO'
    gestion_localidad_1818.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1818 = importer.save_or_locate(gestion_localidad_1818)

    gestion_localidad_1819 = Localidad()
    gestion_localidad_1819.cod_postal = '5873'
    gestion_localidad_1819.localidad = 'TILQUICHO'
    gestion_localidad_1819.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1819 = importer.save_or_locate(gestion_localidad_1819)

    gestion_localidad_1820 = Localidad()
    gestion_localidad_1820.cod_postal = '5129'
    gestion_localidad_1820.localidad = 'TIMON CRUZ'
    gestion_localidad_1820.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1820 = importer.save_or_locate(gestion_localidad_1820)

    gestion_localidad_1821 = Localidad()
    gestion_localidad_1821.cod_postal = '5131'
    gestion_localidad_1821.localidad = 'TINOCO'
    gestion_localidad_1821.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1821 = importer.save_or_locate(gestion_localidad_1821)

    gestion_localidad_1822 = Localidad()
    gestion_localidad_1822.cod_postal = '5229'
    gestion_localidad_1822.localidad = 'TINTIZACO'
    gestion_localidad_1822.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1822 = importer.save_or_locate(gestion_localidad_1822)

    gestion_localidad_1823 = Localidad()
    gestion_localidad_1823.cod_postal = '5936'
    gestion_localidad_1823.localidad = 'TIO PUJIO'
    gestion_localidad_1823.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1823 = importer.save_or_locate(gestion_localidad_1823)

    gestion_localidad_1824 = Localidad()
    gestion_localidad_1824.cod_postal = '5201'
    gestion_localidad_1824.localidad = 'TODOS LOS SANTOS'
    gestion_localidad_1824.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1824 = importer.save_or_locate(gestion_localidad_1824)

    gestion_localidad_1825 = Localidad()
    gestion_localidad_1825.cod_postal = '5123'
    gestion_localidad_1825.localidad = 'TOLEDO'
    gestion_localidad_1825.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1825 = importer.save_or_locate(gestion_localidad_1825)

    gestion_localidad_1826 = Localidad()
    gestion_localidad_1826.cod_postal = '6271'
    gestion_localidad_1826.localidad = 'TOMAS ECHENIQUE'
    gestion_localidad_1826.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1826 = importer.save_or_locate(gestion_localidad_1826)

    gestion_localidad_1827 = Localidad()
    gestion_localidad_1827.cod_postal = '5135'
    gestion_localidad_1827.localidad = 'TORDILLA NORTE'
    gestion_localidad_1827.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1827 = importer.save_or_locate(gestion_localidad_1827)

    gestion_localidad_1828 = Localidad()
    gestion_localidad_1828.cod_postal = '2435'
    gestion_localidad_1828.localidad = 'TORDILLA NORTE'
    gestion_localidad_1828.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1828 = importer.save_or_locate(gestion_localidad_1828)

    gestion_localidad_1829 = Localidad()
    gestion_localidad_1829.cod_postal = '5200'
    gestion_localidad_1829.localidad = 'TORO MUERTO'
    gestion_localidad_1829.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1829 = importer.save_or_locate(gestion_localidad_1829)

    gestion_localidad_1830 = Localidad()
    gestion_localidad_1830.cod_postal = '5295'
    gestion_localidad_1830.localidad = 'TORO MUERTO'
    gestion_localidad_1830.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1830 = importer.save_or_locate(gestion_localidad_1830)

    gestion_localidad_1831 = Localidad()
    gestion_localidad_1831.cod_postal = '5139'
    gestion_localidad_1831.localidad = 'TORO PUJIO'
    gestion_localidad_1831.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1831 = importer.save_or_locate(gestion_localidad_1831)

    gestion_localidad_1832 = Localidad()
    gestion_localidad_1832.cod_postal = '5289'
    gestion_localidad_1832.localidad = 'TOSNO'
    gestion_localidad_1832.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1832 = importer.save_or_locate(gestion_localidad_1832)

    gestion_localidad_1833 = Localidad()
    gestion_localidad_1833.cod_postal = '6141'
    gestion_localidad_1833.localidad = 'TOSQUITA'
    gestion_localidad_1833.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1833 = importer.save_or_locate(gestion_localidad_1833)

    gestion_localidad_1834 = Localidad()
    gestion_localidad_1834.cod_postal = '5284'
    gestion_localidad_1834.localidad = 'TOTORA GUASI'
    gestion_localidad_1834.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1834 = importer.save_or_locate(gestion_localidad_1834)

    gestion_localidad_1835 = Localidad()
    gestion_localidad_1835.cod_postal = '5229'
    gestion_localidad_1835.localidad = 'TOTORAL'
    gestion_localidad_1835.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1835 = importer.save_or_locate(gestion_localidad_1835)

    gestion_localidad_1836 = Localidad()
    gestion_localidad_1836.cod_postal = '5216'
    gestion_localidad_1836.localidad = 'TOTORALEJOS'
    gestion_localidad_1836.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1836 = importer.save_or_locate(gestion_localidad_1836)

    gestion_localidad_1837 = Localidad()
    gestion_localidad_1837.cod_postal = '5291'
    gestion_localidad_1837.localidad = 'TOTORITAS'
    gestion_localidad_1837.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1837 = importer.save_or_locate(gestion_localidad_1837)

    gestion_localidad_1838 = Localidad()
    gestion_localidad_1838.cod_postal = '5201'
    gestion_localidad_1838.localidad = 'TOTRILLA'
    gestion_localidad_1838.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1838 = importer.save_or_locate(gestion_localidad_1838)

    gestion_localidad_1839 = Localidad()
    gestion_localidad_1839.cod_postal = '2436'
    gestion_localidad_1839.localidad = 'TRANSITO'
    gestion_localidad_1839.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1839 = importer.save_or_locate(gestion_localidad_1839)

    gestion_localidad_1840 = Localidad()
    gestion_localidad_1840.cod_postal = '5285'
    gestion_localidad_1840.localidad = 'TRES ARBOLES'
    gestion_localidad_1840.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1840 = importer.save_or_locate(gestion_localidad_1840)

    gestion_localidad_1841 = Localidad()
    gestion_localidad_1841.cod_postal = '5295'
    gestion_localidad_1841.localidad = 'TRES CHAÑARES'
    gestion_localidad_1841.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1841 = importer.save_or_locate(gestion_localidad_1841)

    gestion_localidad_1842 = Localidad()
    gestion_localidad_1842.cod_postal = '5291'
    gestion_localidad_1842.localidad = 'TRES ESQUINAS'
    gestion_localidad_1842.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1842 = importer.save_or_locate(gestion_localidad_1842)

    gestion_localidad_1843 = Localidad()
    gestion_localidad_1843.cod_postal = '5291'
    gestion_localidad_1843.localidad = 'TRES LOMAS'
    gestion_localidad_1843.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1843 = importer.save_or_locate(gestion_localidad_1843)

    gestion_localidad_1844 = Localidad()
    gestion_localidad_1844.cod_postal = '5972'
    gestion_localidad_1844.localidad = 'TRES POZOS'
    gestion_localidad_1844.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1844 = importer.save_or_locate(gestion_localidad_1844)

    gestion_localidad_1845 = Localidad()
    gestion_localidad_1845.cod_postal = '5909'
    gestion_localidad_1845.localidad = 'TRINCHERA'
    gestion_localidad_1845.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1845 = importer.save_or_locate(gestion_localidad_1845)

    gestion_localidad_1846 = Localidad()
    gestion_localidad_1846.cod_postal = '5149'
    gestion_localidad_1846.localidad = 'TRISTAN NARVAJA'
    gestion_localidad_1846.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1846 = importer.save_or_locate(gestion_localidad_1846)

    gestion_localidad_1847 = Localidad()
    gestion_localidad_1847.cod_postal = '5223'
    gestion_localidad_1847.localidad = 'TRONCO POZO'
    gestion_localidad_1847.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1847 = importer.save_or_locate(gestion_localidad_1847)

    gestion_localidad_1848 = Localidad()
    gestion_localidad_1848.cod_postal = '5284'
    gestion_localidad_1848.localidad = 'TUCLAME'
    gestion_localidad_1848.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1848 = importer.save_or_locate(gestion_localidad_1848)

    gestion_localidad_1849 = Localidad()
    gestion_localidad_1849.cod_postal = '5203'
    gestion_localidad_1849.localidad = 'TULUMBA'
    gestion_localidad_1849.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1849 = importer.save_or_locate(gestion_localidad_1849)

    gestion_localidad_1850 = Localidad()
    gestion_localidad_1850.cod_postal = '5216'
    gestion_localidad_1850.localidad = 'TUSCAL'
    gestion_localidad_1850.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1850 = importer.save_or_locate(gestion_localidad_1850)

    gestion_localidad_1851 = Localidad()
    gestion_localidad_1851.cod_postal = '2677'
    gestion_localidad_1851.localidad = 'UCACHA'
    gestion_localidad_1851.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1851 = importer.save_or_locate(gestion_localidad_1851)

    gestion_localidad_1852 = Localidad()
    gestion_localidad_1852.cod_postal = '5857'
    gestion_localidad_1852.localidad = 'UNIDAD TURISTICA EMBALSE'
    gestion_localidad_1852.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1852 = importer.save_or_locate(gestion_localidad_1852)

    gestion_localidad_1853 = Localidad()
    gestion_localidad_1853.cod_postal = '5109'
    gestion_localidad_1853.localidad = 'UNQUILLO'
    gestion_localidad_1853.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1853 = importer.save_or_locate(gestion_localidad_1853)

    gestion_localidad_1854 = Localidad()
    gestion_localidad_1854.cod_postal = '5184'
    gestion_localidad_1854.localidad = 'URITORCO'
    gestion_localidad_1854.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1854 = importer.save_or_locate(gestion_localidad_1854)

    gestion_localidad_1855 = Localidad()
    gestion_localidad_1855.cod_postal = '5859'
    gestion_localidad_1855.localidad = 'USINA NUCLEAR EMBALSE'
    gestion_localidad_1855.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1855 = importer.save_or_locate(gestion_localidad_1855)

    gestion_localidad_1856 = Localidad()
    gestion_localidad_1856.cod_postal = '5143'
    gestion_localidad_1856.localidad = 'VACAS BLANCAS'
    gestion_localidad_1856.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1856 = importer.save_or_locate(gestion_localidad_1856)

    gestion_localidad_1857 = Localidad()
    gestion_localidad_1857.cod_postal = '5107'
    gestion_localidad_1857.localidad = 'VALLE DEL SOL'
    gestion_localidad_1857.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1857 = importer.save_or_locate(gestion_localidad_1857)

    gestion_localidad_1858 = Localidad()
    gestion_localidad_1858.cod_postal = '5864'
    gestion_localidad_1858.localidad = 'VALLE DORADO'
    gestion_localidad_1858.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1858 = importer.save_or_locate(gestion_localidad_1858)

    gestion_localidad_1859 = Localidad()
    gestion_localidad_1859.cod_postal = '5168'
    gestion_localidad_1859.localidad = 'VALLE HERMOSO'
    gestion_localidad_1859.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1859 = importer.save_or_locate(gestion_localidad_1859)

    gestion_localidad_1860 = Localidad()
    gestion_localidad_1860.cod_postal = '5115'
    gestion_localidad_1860.localidad = 'VALLE VERDE'
    gestion_localidad_1860.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1860 = importer.save_or_locate(gestion_localidad_1860)

    gestion_localidad_1861 = Localidad()
    gestion_localidad_1861.cod_postal = '5246'
    gestion_localidad_1861.localidad = 'VANGUARDIA'
    gestion_localidad_1861.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1861 = importer.save_or_locate(gestion_localidad_1861)

    gestion_localidad_1862 = Localidad()
    gestion_localidad_1862.cod_postal = '2671'
    gestion_localidad_1862.localidad = 'VIAMONTE'
    gestion_localidad_1862.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1862 = importer.save_or_locate(gestion_localidad_1862)

    gestion_localidad_1863 = Localidad()
    gestion_localidad_1863.cod_postal = '6140'
    gestion_localidad_1863.localidad = 'VICUÑA MACKENNA'
    gestion_localidad_1863.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1863 = importer.save_or_locate(gestion_localidad_1863)

    gestion_localidad_1864 = Localidad()
    gestion_localidad_1864.cod_postal = '5857'
    gestion_localidad_1864.localidad = 'VILLA AGUADA DE LOS REYES'
    gestion_localidad_1864.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1864 = importer.save_or_locate(gestion_localidad_1864)

    gestion_localidad_1865 = Localidad()
    gestion_localidad_1865.cod_postal = '5166'
    gestion_localidad_1865.localidad = 'VILLA AHORA'
    gestion_localidad_1865.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1865 = importer.save_or_locate(gestion_localidad_1865)

    gestion_localidad_1866 = Localidad()
    gestion_localidad_1866.cod_postal = '5221'
    gestion_localidad_1866.localidad = 'VILLA ALBERTINA'
    gestion_localidad_1866.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1866 = importer.save_or_locate(gestion_localidad_1866)

    gestion_localidad_1867 = Localidad()
    gestion_localidad_1867.cod_postal = '5105'
    gestion_localidad_1867.localidad = 'VILLA ALLENDE'
    gestion_localidad_1867.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1867 = importer.save_or_locate(gestion_localidad_1867)

    gestion_localidad_1868 = Localidad()
    gestion_localidad_1868.cod_postal = '5194'
    gestion_localidad_1868.localidad = 'VILLA ALPINA'
    gestion_localidad_1868.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1868 = importer.save_or_locate(gestion_localidad_1868)

    gestion_localidad_1869 = Localidad()
    gestion_localidad_1869.cod_postal = '5199'
    gestion_localidad_1869.localidad = 'VILLA AMANCAY'
    gestion_localidad_1869.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1869 = importer.save_or_locate(gestion_localidad_1869)

    gestion_localidad_1870 = Localidad()
    gestion_localidad_1870.cod_postal = '5885'
    gestion_localidad_1870.localidad = 'VILLA ANGELICA'
    gestion_localidad_1870.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1870 = importer.save_or_locate(gestion_localidad_1870)

    gestion_localidad_1871 = Localidad()
    gestion_localidad_1871.cod_postal = '5189'
    gestion_localidad_1871.localidad = 'VILLA ANISACATE'
    gestion_localidad_1871.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1871 = importer.save_or_locate(gestion_localidad_1871)

    gestion_localidad_1872 = Localidad()
    gestion_localidad_1872.cod_postal = '5935'
    gestion_localidad_1872.localidad = 'VILLA ASCASUBI'
    gestion_localidad_1872.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1872 = importer.save_or_locate(gestion_localidad_1872)

    gestion_localidad_1873 = Localidad()
    gestion_localidad_1873.cod_postal = '5900'
    gestion_localidad_1873.localidad = 'VILLA AURORA'
    gestion_localidad_1873.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1873 = importer.save_or_locate(gestion_localidad_1873)

    gestion_localidad_1874 = Localidad()
    gestion_localidad_1874.cod_postal = '5194'
    gestion_localidad_1874.localidad = 'VILLA BERNA'
    gestion_localidad_1874.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1874 = importer.save_or_locate(gestion_localidad_1874)

    gestion_localidad_1875 = Localidad()
    gestion_localidad_1875.cod_postal = '5164'
    gestion_localidad_1875.localidad = 'VILLA BUSTOS'
    gestion_localidad_1875.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1875 = importer.save_or_locate(gestion_localidad_1875)

    gestion_localidad_1876 = Localidad()
    gestion_localidad_1876.cod_postal = '5164'
    gestion_localidad_1876.localidad = 'VILLA CAEIRO'
    gestion_localidad_1876.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1876 = importer.save_or_locate(gestion_localidad_1876)

    gestion_localidad_1877 = Localidad()
    gestion_localidad_1877.cod_postal = '5249'
    gestion_localidad_1877.localidad = 'VILLA CANDELARIA NORTE'
    gestion_localidad_1877.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1877 = importer.save_or_locate(gestion_localidad_1877)

    gestion_localidad_1878 = Localidad()
    gestion_localidad_1878.cod_postal = '5152'
    gestion_localidad_1878.localidad = 'VILLA CARLOS PAZ'
    gestion_localidad_1878.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1878 = importer.save_or_locate(gestion_localidad_1878)

    gestion_localidad_1879 = Localidad()
    gestion_localidad_1879.cod_postal = '5186'
    gestion_localidad_1879.localidad = 'VILLA CARLOS PELLEGRINI'
    gestion_localidad_1879.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1879 = importer.save_or_locate(gestion_localidad_1879)

    gestion_localidad_1880 = Localidad()
    gestion_localidad_1880.cod_postal = '5107'
    gestion_localidad_1880.localidad = 'VILLA CERRO AZUL'
    gestion_localidad_1880.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1880 = importer.save_or_locate(gestion_localidad_1880)

    gestion_localidad_1881 = Localidad()
    gestion_localidad_1881.cod_postal = '5221'
    gestion_localidad_1881.localidad = 'VILLA CERRO NEGRO'
    gestion_localidad_1881.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1881 = importer.save_or_locate(gestion_localidad_1881)

    gestion_localidad_1882 = Localidad()
    gestion_localidad_1882.cod_postal = '5189'
    gestion_localidad_1882.localidad = 'VILLA CIUDAD DE AMERICA'
    gestion_localidad_1882.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1882 = importer.save_or_locate(gestion_localidad_1882)

    gestion_localidad_1883 = Localidad()
    gestion_localidad_1883.cod_postal = '5189'
    gestion_localidad_1883.localidad = 'VILLA CIUDAD PQUE LOS REARTES'
    gestion_localidad_1883.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1883 = importer.save_or_locate(gestion_localidad_1883)

    gestion_localidad_1884 = Localidad()
    gestion_localidad_1884.cod_postal = '5885'
    gestion_localidad_1884.localidad = 'VILLA CLODOMIRA'
    gestion_localidad_1884.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1884 = importer.save_or_locate(gestion_localidad_1884)

    gestion_localidad_1885 = Localidad()
    gestion_localidad_1885.cod_postal = '5201'
    gestion_localidad_1885.localidad = 'VILLA COLIMBA'
    gestion_localidad_1885.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1885 = importer.save_or_locate(gestion_localidad_1885)

    gestion_localidad_1886 = Localidad()
    gestion_localidad_1886.cod_postal = '2433'
    gestion_localidad_1886.localidad = 'VILLA CONCEPCION DEL TIO'
    gestion_localidad_1886.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1886 = importer.save_or_locate(gestion_localidad_1886)

    gestion_localidad_1887 = Localidad()
    gestion_localidad_1887.cod_postal = '5101'
    gestion_localidad_1887.localidad = 'VILLA CORAZON DE MARIA'
    gestion_localidad_1887.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1887 = importer.save_or_locate(gestion_localidad_1887)

    gestion_localidad_1888 = Localidad()
    gestion_localidad_1888.cod_postal = '5153'
    gestion_localidad_1888.localidad = 'VILLA COSTA AZUL'
    gestion_localidad_1888.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1888 = importer.save_or_locate(gestion_localidad_1888)

    gestion_localidad_1889 = Localidad()
    gestion_localidad_1889.cod_postal = '5153'
    gestion_localidad_1889.localidad = 'VILLA CUESTA BLANCA'
    gestion_localidad_1889.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1889 = importer.save_or_locate(gestion_localidad_1889)

    gestion_localidad_1890 = Localidad()
    gestion_localidad_1890.cod_postal = '5891'
    gestion_localidad_1890.localidad = 'VILLA CURA BROCHERO'
    gestion_localidad_1890.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1890 = importer.save_or_locate(gestion_localidad_1890)

    gestion_localidad_1891 = Localidad()
    gestion_localidad_1891.cod_postal = '5885'
    gestion_localidad_1891.localidad = 'VILLA DE LAS ROSAS'
    gestion_localidad_1891.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1891 = importer.save_or_locate(gestion_localidad_1891)

    gestion_localidad_1892 = Localidad()
    gestion_localidad_1892.cod_postal = '5862'
    gestion_localidad_1892.localidad = 'VILLA DEL DIQUE'
    gestion_localidad_1892.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1892 = importer.save_or_locate(gestion_localidad_1892)

    gestion_localidad_1893 = Localidad()
    gestion_localidad_1893.cod_postal = '5152'
    gestion_localidad_1893.localidad = 'VILLA DEL LAGO'
    gestion_localidad_1893.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1893 = importer.save_or_locate(gestion_localidad_1893)

    gestion_localidad_1894 = Localidad()
    gestion_localidad_1894.cod_postal = '5903'
    gestion_localidad_1894.localidad = 'VILLA DEL PARQUE'
    gestion_localidad_1894.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1894 = importer.save_or_locate(gestion_localidad_1894)

    gestion_localidad_1895 = Localidad()
    gestion_localidad_1895.cod_postal = '5864'
    gestion_localidad_1895.localidad = 'VILLA DEL PARQUE'
    gestion_localidad_1895.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1895 = importer.save_or_locate(gestion_localidad_1895)

    gestion_localidad_1896 = Localidad()
    gestion_localidad_1896.cod_postal = '5186'
    gestion_localidad_1896.localidad = 'VILLA DEL PRADO'
    gestion_localidad_1896.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1896 = importer.save_or_locate(gestion_localidad_1896)

    gestion_localidad_1897 = Localidad()
    gestion_localidad_1897.cod_postal = '5963'
    gestion_localidad_1897.localidad = 'VILLA DEL ROSARIO'
    gestion_localidad_1897.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1897 = importer.save_or_locate(gestion_localidad_1897)

    gestion_localidad_1898 = Localidad()
    gestion_localidad_1898.cod_postal = '5859'
    gestion_localidad_1898.localidad = 'VILLA DEL TALA'
    gestion_localidad_1898.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1898 = importer.save_or_locate(gestion_localidad_1898)

    gestion_localidad_1899 = Localidad()
    gestion_localidad_1899.cod_postal = '5236'
    gestion_localidad_1899.localidad = 'VILLA DEL TOTORAL'
    gestion_localidad_1899.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1899 = importer.save_or_locate(gestion_localidad_1899)

    gestion_localidad_1900 = Localidad()
    gestion_localidad_1900.cod_postal = '5248'
    gestion_localidad_1900.localidad = 'VILLA DE MARIA'
    gestion_localidad_1900.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1900 = importer.save_or_locate(gestion_localidad_1900)

    gestion_localidad_1901 = Localidad()
    gestion_localidad_1901.cod_postal = '5284'
    gestion_localidad_1901.localidad = 'VILLA DE SOTO'
    gestion_localidad_1901.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1901 = importer.save_or_locate(gestion_localidad_1901)

    gestion_localidad_1902 = Localidad()
    gestion_localidad_1902.cod_postal = '5109'
    gestion_localidad_1902.localidad = 'VILLA DIAZ'
    gestion_localidad_1902.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1902 = importer.save_or_locate(gestion_localidad_1902)

    gestion_localidad_1903 = Localidad()
    gestion_localidad_1903.cod_postal = '5870'
    gestion_localidad_1903.localidad = 'VILLA DOLORES'
    gestion_localidad_1903.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1903 = importer.save_or_locate(gestion_localidad_1903)

    gestion_localidad_1904 = Localidad()
    gestion_localidad_1904.cod_postal = '5801'
    gestion_localidad_1904.localidad = 'VILLA EL CHACAY'
    gestion_localidad_1904.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1904 = importer.save_or_locate(gestion_localidad_1904)

    gestion_localidad_1905 = Localidad()
    gestion_localidad_1905.cod_postal = '5199'
    gestion_localidad_1905.localidad = 'VILLA EL CORCOVADO'
    gestion_localidad_1905.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1905 = importer.save_or_locate(gestion_localidad_1905)

    gestion_localidad_1906 = Localidad()
    gestion_localidad_1906.cod_postal = '5189'
    gestion_localidad_1906.localidad = 'VILLA EL DESCANSO'
    gestion_localidad_1906.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1906 = importer.save_or_locate(gestion_localidad_1906)

    gestion_localidad_1907 = Localidad()
    gestion_localidad_1907.cod_postal = '2594'
    gestion_localidad_1907.localidad = 'VILLA ELISA'
    gestion_localidad_1907.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1907 = importer.save_or_locate(gestion_localidad_1907)

    gestion_localidad_1908 = Localidad()
    gestion_localidad_1908.cod_postal = '5199'
    gestion_localidad_1908.localidad = 'VILLA EL TORREON'
    gestion_localidad_1908.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1908 = importer.save_or_locate(gestion_localidad_1908)

    gestion_localidad_1909 = Localidad()
    gestion_localidad_1909.cod_postal = '5900'
    gestion_localidad_1909.localidad = 'VILLA EMILIA'
    gestion_localidad_1909.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1909 = importer.save_or_locate(gestion_localidad_1909)

    gestion_localidad_1910 = Localidad()
    gestion_localidad_1910.cod_postal = '5101'
    gestion_localidad_1910.localidad = 'VILLA ESQUIU'
    gestion_localidad_1910.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1910 = importer.save_or_locate(gestion_localidad_1910)

    gestion_localidad_1911 = Localidad()
    gestion_localidad_1911.cod_postal = '5155'
    gestion_localidad_1911.localidad = 'VILLA FLOR SERRANA'
    gestion_localidad_1911.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1911 = importer.save_or_locate(gestion_localidad_1911)

    gestion_localidad_1912 = Localidad()
    gestion_localidad_1912.cod_postal = '5137'
    gestion_localidad_1912.localidad = 'VILLA FONTANA'
    gestion_localidad_1912.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1912 = importer.save_or_locate(gestion_localidad_1912)

    gestion_localidad_1913 = Localidad()
    gestion_localidad_1913.cod_postal = '5194'
    gestion_localidad_1913.localidad = 'VILLA GENERAL BELGRANO'
    gestion_localidad_1913.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1913 = importer.save_or_locate(gestion_localidad_1913)

    gestion_localidad_1914 = Localidad()
    gestion_localidad_1914.cod_postal = '5236'
    gestion_localidad_1914.localidad = 'VILLA GENERAL MITRE'
    gestion_localidad_1914.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1914 = importer.save_or_locate(gestion_localidad_1914)

    gestion_localidad_1915 = Localidad()
    gestion_localidad_1915.cod_postal = '5176'
    gestion_localidad_1915.localidad = 'VILLA GIARDINO'
    gestion_localidad_1915.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1915 = importer.save_or_locate(gestion_localidad_1915)

    gestion_localidad_1916 = Localidad()
    gestion_localidad_1916.cod_postal = '5153'
    gestion_localidad_1916.localidad = 'VILLA GRACIA'
    gestion_localidad_1916.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1916 = importer.save_or_locate(gestion_localidad_1916)

    gestion_localidad_1917 = Localidad()
    gestion_localidad_1917.cod_postal = '5212'
    gestion_localidad_1917.localidad = 'VILLA GUTIERREZ'
    gestion_localidad_1917.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1917 = importer.save_or_locate(gestion_localidad_1917)

    gestion_localidad_1918 = Localidad()
    gestion_localidad_1918.cod_postal = '6275'
    gestion_localidad_1918.localidad = 'VILLA HUIDOBRO'
    gestion_localidad_1918.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1918 = importer.save_or_locate(gestion_localidad_1918)

    gestion_localidad_1919 = Localidad()
    gestion_localidad_1919.cod_postal = '5153'
    gestion_localidad_1919.localidad = 'VILLA INDEPENDENCIA'
    gestion_localidad_1919.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1919 = importer.save_or_locate(gestion_localidad_1919)

    gestion_localidad_1920 = Localidad()
    gestion_localidad_1920.cod_postal = '5189'
    gestion_localidad_1920.localidad = 'VILLA LA BOLSA'
    gestion_localidad_1920.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1920 = importer.save_or_locate(gestion_localidad_1920)

    gestion_localidad_1921 = Localidad()
    gestion_localidad_1921.cod_postal = '5819'
    gestion_localidad_1921.localidad = 'VILLA LA COBA'
    gestion_localidad_1921.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1921 = importer.save_or_locate(gestion_localidad_1921)

    gestion_localidad_1922 = Localidad()
    gestion_localidad_1922.cod_postal = '5199'
    gestion_localidad_1922.localidad = 'VILLA LAGO AZUL'
    gestion_localidad_1922.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1922 = importer.save_or_locate(gestion_localidad_1922)

    gestion_localidad_1923 = Localidad()
    gestion_localidad_1923.cod_postal = '5189'
    gestion_localidad_1923.localidad = 'VILLA LA RANCHERITA'
    gestion_localidad_1923.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1923 = importer.save_or_locate(gestion_localidad_1923)

    gestion_localidad_1924 = Localidad()
    gestion_localidad_1924.cod_postal = '5107'
    gestion_localidad_1924.localidad = 'VILLA LAS MERCEDES'
    gestion_localidad_1924.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1924 = importer.save_or_locate(gestion_localidad_1924)

    gestion_localidad_1925 = Localidad()
    gestion_localidad_1925.cod_postal = '5109'
    gestion_localidad_1925.localidad = 'VILLA LEONOR'
    gestion_localidad_1925.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1925 = importer.save_or_locate(gestion_localidad_1925)

    gestion_localidad_1926 = Localidad()
    gestion_localidad_1926.cod_postal = '5111'
    gestion_localidad_1926.localidad = 'VILLA LOS ALTOS'
    gestion_localidad_1926.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1926 = importer.save_or_locate(gestion_localidad_1926)

    gestion_localidad_1927 = Localidad()
    gestion_localidad_1927.cod_postal = '5186'
    gestion_localidad_1927.localidad = 'VILLA LOS AROMOS'
    gestion_localidad_1927.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1927 = importer.save_or_locate(gestion_localidad_1927)

    gestion_localidad_1928 = Localidad()
    gestion_localidad_1928.cod_postal = '5281'
    gestion_localidad_1928.localidad = 'VILLA LOS LEONES'
    gestion_localidad_1928.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1928 = importer.save_or_locate(gestion_localidad_1928)

    gestion_localidad_1929 = Localidad()
    gestion_localidad_1929.cod_postal = '2551'
    gestion_localidad_1929.localidad = 'VILLA LOS PATOS'
    gestion_localidad_1929.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1929 = importer.save_or_locate(gestion_localidad_1929)

    gestion_localidad_1930 = Localidad()
    gestion_localidad_1930.cod_postal = '5137'
    gestion_localidad_1930.localidad = 'VILLA MAR CHIQUITA'
    gestion_localidad_1930.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1930 = importer.save_or_locate(gestion_localidad_1930)

    gestion_localidad_1931 = Localidad()
    gestion_localidad_1931.cod_postal = '5220'
    gestion_localidad_1931.localidad = 'VILLA MARIA'
    gestion_localidad_1931.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1931 = importer.save_or_locate(gestion_localidad_1931)

    gestion_localidad_1932 = Localidad()
    gestion_localidad_1932.cod_postal = '5900'
    gestion_localidad_1932.localidad = 'VILLA MARIA'
    gestion_localidad_1932.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1932 = importer.save_or_locate(gestion_localidad_1932)

    gestion_localidad_1933 = Localidad()
    gestion_localidad_1933.cod_postal = '5123'
    gestion_localidad_1933.localidad = 'VILLA MIREA'
    gestion_localidad_1933.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1933 = importer.save_or_locate(gestion_localidad_1933)

    gestion_localidad_1934 = Localidad()
    gestion_localidad_1934.cod_postal = '6275'
    gestion_localidad_1934.localidad = 'VILLA MODERNA'
    gestion_localidad_1934.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1934 = importer.save_or_locate(gestion_localidad_1934)

    gestion_localidad_1935 = Localidad()
    gestion_localidad_1935.cod_postal = '5864'
    gestion_localidad_1935.localidad = 'VILLA NATURALEZA'
    gestion_localidad_1935.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1935 = importer.save_or_locate(gestion_localidad_1935)

    gestion_localidad_1936 = Localidad()
    gestion_localidad_1936.cod_postal = '5903'
    gestion_localidad_1936.localidad = 'VILLA NUEVA'
    gestion_localidad_1936.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1936 = importer.save_or_locate(gestion_localidad_1936)

    gestion_localidad_1937 = Localidad()
    gestion_localidad_1937.cod_postal = '5101'
    gestion_localidad_1937.localidad = 'VILLA PARQUE SANTA ANA'
    gestion_localidad_1937.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1937 = importer.save_or_locate(gestion_localidad_1937)

    gestion_localidad_1938 = Localidad()
    gestion_localidad_1938.cod_postal = '5152'
    gestion_localidad_1938.localidad = 'VILLA PARQUE SIQUIMAN'
    gestion_localidad_1938.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1938 = importer.save_or_locate(gestion_localidad_1938)

    gestion_localidad_1939 = Localidad()
    gestion_localidad_1939.cod_postal = '5123'
    gestion_localidad_1939.localidad = 'VILLA POSSE'
    gestion_localidad_1939.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1939 = importer.save_or_locate(gestion_localidad_1939)

    gestion_localidad_1940 = Localidad()
    gestion_localidad_1940.cod_postal = '5214'
    gestion_localidad_1940.localidad = 'VILLA QUILINO'
    gestion_localidad_1940.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1940 = importer.save_or_locate(gestion_localidad_1940)

    gestion_localidad_1941 = Localidad()
    gestion_localidad_1941.cod_postal = '5859'
    gestion_localidad_1941.localidad = 'VILLA QUILLINZO'
    gestion_localidad_1941.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1941 = importer.save_or_locate(gestion_localidad_1941)

    gestion_localidad_1942 = Localidad()
    gestion_localidad_1942.cod_postal = '5885'
    gestion_localidad_1942.localidad = 'VILLA RAFAEL BENEGAS'
    gestion_localidad_1942.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1942 = importer.save_or_locate(gestion_localidad_1942)

    gestion_localidad_1943 = Localidad()
    gestion_localidad_1943.cod_postal = '5153'
    gestion_localidad_1943.localidad = 'VILLA RIO ICHO CRUZ'
    gestion_localidad_1943.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1943 = importer.save_or_locate(gestion_localidad_1943)

    gestion_localidad_1944 = Localidad()
    gestion_localidad_1944.cod_postal = '5233'
    gestion_localidad_1944.localidad = 'VILLA ROSARIO DEL SALADILLO'
    gestion_localidad_1944.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1944 = importer.save_or_locate(gestion_localidad_1944)

    gestion_localidad_1945 = Localidad()
    gestion_localidad_1945.cod_postal = '6128'
    gestion_localidad_1945.localidad = 'VILLA ROSSI'
    gestion_localidad_1945.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1945 = importer.save_or_locate(gestion_localidad_1945)

    gestion_localidad_1946 = Localidad()
    gestion_localidad_1946.cod_postal = '5864'
    gestion_localidad_1946.localidad = 'VILLA RUMIPAL'
    gestion_localidad_1946.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1946 = importer.save_or_locate(gestion_localidad_1946)

    gestion_localidad_1947 = Localidad()
    gestion_localidad_1947.cod_postal = '5947'
    gestion_localidad_1947.localidad = 'VILLA SAN ESTEBAN'
    gestion_localidad_1947.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1947 = importer.save_or_locate(gestion_localidad_1947)

    gestion_localidad_1948 = Localidad()
    gestion_localidad_1948.cod_postal = '5199'
    gestion_localidad_1948.localidad = 'VILLA SAN JAVIER'
    gestion_localidad_1948.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1948 = importer.save_or_locate(gestion_localidad_1948)

    gestion_localidad_1949 = Localidad()
    gestion_localidad_1949.cod_postal = '5111'
    gestion_localidad_1949.localidad = 'VILLA SAN MIGUEL'
    gestion_localidad_1949.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1949 = importer.save_or_locate(gestion_localidad_1949)

    gestion_localidad_1950 = Localidad()
    gestion_localidad_1950.cod_postal = '5152'
    gestion_localidad_1950.localidad = 'VILLA SANTA CRUZ DEL LAGO'
    gestion_localidad_1950.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1950 = importer.save_or_locate(gestion_localidad_1950)

    gestion_localidad_1951 = Localidad()
    gestion_localidad_1951.cod_postal = '5186'
    gestion_localidad_1951.localidad = 'VILLA SANTA MARIA'
    gestion_localidad_1951.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1951 = importer.save_or_locate(gestion_localidad_1951)

    gestion_localidad_1952 = Localidad()
    gestion_localidad_1952.cod_postal = '5801'
    gestion_localidad_1952.localidad = 'VILLA SANTA RITA'
    gestion_localidad_1952.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1952 = importer.save_or_locate(gestion_localidad_1952)

    gestion_localidad_1953 = Localidad()
    gestion_localidad_1953.cod_postal = '5133'
    gestion_localidad_1953.localidad = 'VILLA SANTA ROSA'
    gestion_localidad_1953.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1953 = importer.save_or_locate(gestion_localidad_1953)

    gestion_localidad_1954 = Localidad()
    gestion_localidad_1954.cod_postal = '5871'
    gestion_localidad_1954.localidad = 'VILLA SARMIENTO'
    gestion_localidad_1954.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1954 = importer.save_or_locate(gestion_localidad_1954)

    gestion_localidad_1955 = Localidad()
    gestion_localidad_1955.cod_postal = '6273'
    gestion_localidad_1955.localidad = 'VILLA SARMIENTO'
    gestion_localidad_1955.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1955 = importer.save_or_locate(gestion_localidad_1955)

    gestion_localidad_1956 = Localidad()
    gestion_localidad_1956.cod_postal = '5189'
    gestion_localidad_1956.localidad = 'VILLA SATYTA'
    gestion_localidad_1956.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1956 = importer.save_or_locate(gestion_localidad_1956)

    gestion_localidad_1957 = Localidad()
    gestion_localidad_1957.cod_postal = '5857'
    gestion_localidad_1957.localidad = 'VILLA SIERRAS DEL LAGO'
    gestion_localidad_1957.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1957 = importer.save_or_locate(gestion_localidad_1957)

    gestion_localidad_1958 = Localidad()
    gestion_localidad_1958.cod_postal = '5156'
    gestion_localidad_1958.localidad = 'VILLA SUIZA ARGENTINA'
    gestion_localidad_1958.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1958 = importer.save_or_locate(gestion_localidad_1958)

    gestion_localidad_1959 = Localidad()
    gestion_localidad_1959.cod_postal = '5295'
    gestion_localidad_1959.localidad = 'VILLA TANINGA'
    gestion_localidad_1959.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1959 = importer.save_or_locate(gestion_localidad_1959)

    gestion_localidad_1960 = Localidad()
    gestion_localidad_1960.cod_postal = '5109'
    gestion_localidad_1960.localidad = 'VILLA TORTOSA'
    gestion_localidad_1960.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1960 = importer.save_or_locate(gestion_localidad_1960)

    gestion_localidad_1961 = Localidad()
    gestion_localidad_1961.cod_postal = '6273'
    gestion_localidad_1961.localidad = 'VILLA VALERIA'
    gestion_localidad_1961.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1961 = importer.save_or_locate(gestion_localidad_1961)

    gestion_localidad_1962 = Localidad()
    gestion_localidad_1962.cod_postal = '2435'
    gestion_localidad_1962.localidad = 'VILLA VAUDAGNA'
    gestion_localidad_1962.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1962 = importer.save_or_locate(gestion_localidad_1962)

    gestion_localidad_1963 = Localidad()
    gestion_localidad_1963.cod_postal = '2426'
    gestion_localidad_1963.localidad = 'VILLA VIEJA'
    gestion_localidad_1963.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1963 = importer.save_or_locate(gestion_localidad_1963)

    gestion_localidad_1964 = Localidad()
    gestion_localidad_1964.cod_postal = '5197'
    gestion_localidad_1964.localidad = 'VILLA YACANTO'
    gestion_localidad_1964.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1964 = importer.save_or_locate(gestion_localidad_1964)

    gestion_localidad_1965 = Localidad()
    gestion_localidad_1965.cod_postal = '5295'
    gestion_localidad_1965.localidad = 'VISO'
    gestion_localidad_1965.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1965 = importer.save_or_locate(gestion_localidad_1965)

    gestion_localidad_1966 = Localidad()
    gestion_localidad_1966.cod_postal = '5197'
    gestion_localidad_1966.localidad = 'VISTA ALEGRE'
    gestion_localidad_1966.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1966 = importer.save_or_locate(gestion_localidad_1966)

    gestion_localidad_1967 = Localidad()
    gestion_localidad_1967.cod_postal = '6128'
    gestion_localidad_1967.localidad = 'VIVERO'
    gestion_localidad_1967.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1967 = importer.save_or_locate(gestion_localidad_1967)

    gestion_localidad_1968 = Localidad()
    gestion_localidad_1968.cod_postal = '6144'
    gestion_localidad_1968.localidad = 'WASHINGTON'
    gestion_localidad_1968.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1968 = importer.save_or_locate(gestion_localidad_1968)

    gestion_localidad_1969 = Localidad()
    gestion_localidad_1969.cod_postal = '6270'
    gestion_localidad_1969.localidad = 'WATT'
    gestion_localidad_1969.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1969 = importer.save_or_locate(gestion_localidad_1969)

    gestion_localidad_1970 = Localidad()
    gestion_localidad_1970.cod_postal = '2655'
    gestion_localidad_1970.localidad = 'WENCESLAO ESCALANTE'
    gestion_localidad_1970.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1970 = importer.save_or_locate(gestion_localidad_1970)

    gestion_localidad_1971 = Localidad()
    gestion_localidad_1971.cod_postal = '5877'
    gestion_localidad_1971.localidad = 'YACANTO'
    gestion_localidad_1971.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1971 = importer.save_or_locate(gestion_localidad_1971)

    gestion_localidad_1972 = Localidad()
    gestion_localidad_1972.cod_postal = '5248'
    gestion_localidad_1972.localidad = 'YANACATO'
    gestion_localidad_1972.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1972 = importer.save_or_locate(gestion_localidad_1972)

    gestion_localidad_1973 = Localidad()
    gestion_localidad_1973.cod_postal = '5841'
    gestion_localidad_1973.localidad = 'YATAY'
    gestion_localidad_1973.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1973 = importer.save_or_locate(gestion_localidad_1973)

    gestion_localidad_1974 = Localidad()
    gestion_localidad_1974.cod_postal = '5153'
    gestion_localidad_1974.localidad = 'YCHO CRUZ SIERRAS'
    gestion_localidad_1974.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1974 = importer.save_or_locate(gestion_localidad_1974)

    gestion_localidad_1975 = Localidad()
    gestion_localidad_1975.cod_postal = '5200'
    gestion_localidad_1975.localidad = 'YERBA BUENA'
    gestion_localidad_1975.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1975 = importer.save_or_locate(gestion_localidad_1975)

    gestion_localidad_1976 = Localidad()
    gestion_localidad_1976.cod_postal = '5101'
    gestion_localidad_1976.localidad = 'YOCSINA'
    gestion_localidad_1976.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1976 = importer.save_or_locate(gestion_localidad_1976)

    gestion_localidad_1977 = Localidad()
    gestion_localidad_1977.cod_postal = '5873'
    gestion_localidad_1977.localidad = 'ZAPATA'
    gestion_localidad_1977.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1977 = importer.save_or_locate(gestion_localidad_1977)

    gestion_localidad_1978 = Localidad()
    gestion_localidad_1978.cod_postal = '5839'
    gestion_localidad_1978.localidad = 'ZAPOLOCO'
    gestion_localidad_1978.provincia =  importer.locate_object(Provincia, "id", Provincia, "id", 6, {'id': 6, 'cod_provincia': 'AR-X', 'provincia': ' Córdoba'} ) 
    gestion_localidad_1978 = importer.save_or_locate(gestion_localidad_1978)

