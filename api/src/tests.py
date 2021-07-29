import random
from django.test import TestCase
# Create your tests here.

def test_case(length: int = 10000):
    lst1 = [random.randint(-10**9, 10**9) for i in range(length)]
    lst2 = [random.randint(-10**9, 10**9) for i in range(length)]
    return lst1, lst2