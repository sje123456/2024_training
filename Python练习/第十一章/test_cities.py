# -*- coding: utf-8 -*-

# test_cities.py

import city_function

def test_city_country():
    assert city_function.city_country('Santiago', 'Chile') == 'Santiago, Chile'
    #return "Test passed!"

#print(test_city_country())
