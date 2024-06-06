# -*- coding: utf-8 -*-

# test_cities.py

import city_function

def test_city_country_population():
    assert city_function.city_country('Santiago', 'Chile', population=5000000) == 'Santiago, Chile - population 5000000'
    
