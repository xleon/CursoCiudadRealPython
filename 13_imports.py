"""
Ejemplos de cómo importar módulos y funciones en python
"""

import utils

utils.sumar(6, 8)
utils.restar(10, 4)

from utils import sumar

sumar(2, 2)

from libs import bombing
bombing.where_are_the_bombs()
bombing.explosion()

from libs.bombing import *
explosion()