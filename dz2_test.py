#from dz1_1 import list_
from dz1_2 import mounth
from dz1_3 import fib
#from dz1_4 import copy_
from dz1_5 import sred_
from dz1_6 import number
#from dz1_7 import text_

assert mounth(1) == "Winter"
assert mounth(9) == "Autumn"
assert mounth(6) == "Summer"
assert mounth(15) == "Нет такого месяца"
assert mounth(-2) == "Нет такого месяца"
assert mounth(0) == "Нет такого месяца"
assert mounth("1") == "Нет такого месяца"

assert fib(2) == [0, 1]
assert fib(3) == [0, 1, 1]
assert fib(15) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]

assert sred_([6, 6, 6, 6, 6, 6]) == 6
assert sred_([7, 7, 7, 7, 7, 7, 7]) == 7
assert sred_([10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 10
assert sred_([5, 7, 3, 8, 2]) == 5

assert number(53) == True
assert number(55) == False
assert number(2) == True
assert number(3) == True
assert number(1) == False