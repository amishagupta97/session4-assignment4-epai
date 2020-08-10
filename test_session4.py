import pytest
import random
import string
import session4
import os
import inspect
import re
import math
import decimal
from decimal import Decimal
import cmath

decimal.getcontext().prec = 12

README_CONTENT_CHECK_FOR = [
    'Qualean',
    'Bankers',
    'rounding',
    'precision',
    '__init__',
    '__and__',
    '__or__',
    '__repr__',
    '__str__',
    '__add__',
    '__eq__',
    '__float__',
    '__gt__',
    '__ge__',
    '__invertsign__',
    '__le__',
    '__lt__',
    '__mul__',
    '__sqrt__',
    '__bool__'
]

CHECK_FOR_FUNCT_IMPL = [
    '__and__',
    '__or__',
    '__repr__',
    '__str__',
    '__add__',
    '__eq__',
    '__float__',
    '__invertsign__',
    '__le__',
    '__lt__',
    '__mul__',
    '__sqrt__',
    '__bool__',
    '__gt__',
    '__ge__',
]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r", encoding="utf-8")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            print(c)
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session4)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session4, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_all_functions_implemented():
    code_lines = inspect.getsource(session4)
    FUNCS_IMPL = True
    for c in CHECK_FOR_FUNCT_IMPL:
        if c not in code_lines:
            print(c)
            FUNCS_IMPL = False
            pass
    assert FUNCS_IMPL == True, 'You forgot to implement all functions! Try again!'

def test_decimal_used():
    code_lines = inspect.getsource(session4)
    assert 'decimal' in code_lines, 'Decimal is not used!'
    assert 'import' in code_lines, 'You have not imported decimal!'

def test_qualean_num_precision():
    a = random.choice([1, -1, 1.0, 1.000, -1.0000])
    q = session4.Qualean(a)
    assert len(str(q).split('.')[1]) == 10, 'Well! you always have to be precise in your answer'

def test_user_input():
    with pytest.raises(ValueError):
        session4.Qualean(1.1), 'Looks like you missed to check user inputs!'

def test_function_for_equality():
    a = random.choice([1,0,-1, 1.0, 1.000, 0.0, -1.0000])
    q1 = session4.Qualean(a)
    assert q1.__eq__(q1) == math.isclose(q1, q1, rel_tol = 1e-10, abs_tol=0.0), 'The numbers you are trying to check right now are not equal, please try again later'
    sum = Decimal('0')
    for i in range(1000000):
        any = random.choice([1,0,-1, 1.0, 1.000, 0.0, -1.0000])
        q = session4.Qualean(any)
        sum = sum + q.qual
    assert sum.__eq__(0) == math.isclose(sum, 0), 'The sum of million different q should be equal to zero, think why?'

def test_function_for_add():
    a = random.choice([1,0,-1, 1.0, 1.000, 0.0, -1.0000])
    q1 = session4.Qualean(a)
    sum = Decimal('0')
    for i in range(50):
        sum = sum + q1.__add__(q1)
    assert math.isclose(sum, 100 * q1.qual, rel_tol = 1e-10, abs_tol=0.0), 'Guess your sum of q 100 times is not coming equal to 100 multiply by q, questioning arithmetic here'
    assert round(sum,8) == round(100 * q1.qual,8), 'Looks like your equal is not equal'

def test_function_for_gt():
    a = random.choice([1,0,-1, 1.0, 1.000, 0.0, -1.0000])
    b = random.choice([1,0,-1, 1.0, 1.000, 0.0, -1.0000])
    q1 = session4.Qualean(a)
    q2 = session4.Qualean(b)
    assert (q1.__gt__(q2)) == (q1.qual > q2.qual), 'Something which is not lesser must be greater, simple.'

def test_function_for_ge():
    a = random.choice([1,0,-1, 1.0, 1.000, 0.0, -1.0000])
    b = random.choice([1,0,-1, 1.0, 1.000, 0.0, -1.0000])
    q1 = session4.Qualean(a)
    q2 = session4.Qualean(b)
    assert (q1.__ge__(q1)) == (q1.qual >= q1.qual), 'Greater is fine, but can you also check for equal?'
    assert (q1.__ge__(q2)) == (q1.qual >= q2.qual), 'Difficult to figure out what is greater?'

def test_function_for_lt():
    a = random.choice([1,0,-1, 1.0, 1.000, 0.0, -1.0000])
    b = random.choice([1,0,-1, 1.0, 1.000, 0.0, -1.0000])
    q1 = session4.Qualean(a)
    q2 = session4.Qualean(b)
    assert (q1.__lt__(q2)) == (q1.qual < q2.qual), 'Something which is not greater must be lesser, simple.'

def test_function_for_le():
    a = random.choice([1,0,-1, 1.0, 1.000, 0.0, -1.0000])
    b = random.choice([1,0,-1, 1.0, 1.000, 0.0, -1.0000])
    q1 = session4.Qualean(a)
    q2 = session4.Qualean(b)
    assert (q1.__le__(q1)) == (q1.qual <= q1.qual), 'Lesser is fine, but can you also check for equal?'
    assert (q1.__le__(q2)) == (q1.qual <= q2.qual), 'Difficult to figure out what is lesser?'

def test_function_for_bool():
    a = random.choice([1,0,-1, 1.0, 1.000, 0.0, -1.0000])
    q1 = session4.Qualean(a)
    assert q1.__bool__() == bool(q1.qual), 'Boolean can always capture your truth or false'

def test_function_for_invertsign():
    a = random.choice([1,0,-1, 1.0, 1.000, 0.0, -1.0000])
    q1 = session4.Qualean(a)
    assert q1.__invertsign__() == (-1 * q1.qual), 'Look from the other side of coin'

def test_function_for_sqrt():
    a = random.choice([1,0,-1, 1.0, 1.000, 0.0, -1.0000])
    q = session4.Qualean(a)
    sqrt = q.__sqrt__()
    if q > session4.Qualean(0):
        assert (type(sqrt) == complex) and math.isclose(Decimal(q.__sqrt__().real), round(Decimal.sqrt(q.qual),10)), 'Postive square roots seem to differ from Decimal.sqrt()'
    else:
        num_sqrt = cmath.sqrt(q.qual)
        assert (type(sqrt) == complex) and (cmath.isclose(sqrt, num_sqrt, rel_tol=1e-7, abs_tol=0.0)), 'Negatives get even difficult to match with cmath.sqrt()'

def test_function_for_mul():
    a = random.choice([1,0,-1, 1.0, 1.000, 0.0, -1.0000])
    b = random.choice([1,0,-1, 1.0, 1.000, 0.0, -1.0000])
    q1 = session4.Qualean(a)
    q2 = session4.Qualean(b)
    assert q1.__mul__(q2) == (q1.qual * q2.qual), 'What else can multiplication of qualean numbers result in? I wonder!'

def test_function_for_and():
    a = random.choice([1,0,-1, 1.0, 1.000, 0.0, -1.0000])
    b = random.choice([1,0,-1, 1.0, 1.000, 0.0, -1.0000])
    q1 = session4.Qualean(a)
    q2 = session4.Qualean(b)
    assert q1.__and__(q2) == bool(q1.qual and q2.qual), 'There goes typical behaviour of and, can you match it?'

def test_function_for_or():
    a = random.choice([1,0,-1, 1.0, 1.000, 0.0, -1.0000])
    b = random.choice([1,0,-1, 1.0, 1.000, 0.0, -1.0000])
    q1 = session4.Qualean(a)
    q2 = session4.Qualean(b)
    assert q1.__or__(q2) == bool(q1.qual or q2.qual), 'Well or is always ready to give right answer, still not getting it right?'

def test_function_for_float():
    a = random.choice([1,0,-1, 1.0, 1.000, 0.0, -1.0000])
    q1 = session4.Qualean(a)
    assert q1.__float__() == float(q1.qual), 'Floating only works the way it wants, can you figure out how?'

def test_function_for_repr():
    a = random.choice([1,0,-1, 1.0, 1.000, 0.0, -1.0000])
    q1 = session4.Qualean(a)
    assert q1.__repr__() == f'Qualean number in decimal representation is {q1.qual}', 'The representation of the Qualean object is not correct'

def test_function_for_str():
    a = random.choice([1,0,-1, 1.0, 1.000, 0.0, -1.0000])
    q1 = session4.Qualean(a)
    assert q1.__str__() == f'Qualean number is {q1.qual}', 'The print of the Qualean object does not meet expectations'

def test_functions_for_non_qualean_values():
    a = random.choice([1,0,-1, 1.0, 1.000, 0.0, -1.0000])
    q1 = session4.Qualean(a)
    q2 = 2
    with pytest.raises(NotImplementedError):
        q1.__add__(q2) # Well, some rules are must follow
    with pytest.raises(NotImplementedError):
        q1.__mul__(q2) # You seem to be a rule breaker, are you?
    with pytest.raises(NotImplementedError):
        q1.__eq__(q2) # Everything looks equal to you?
    with pytest.raises(NotImplementedError):
        q1.__gt__(q2) # Comparing with no rules defined?
    with pytest.raises(NotImplementedError):
        q1.__ge__(q2) # Yeah right, as if you can compare a rat and a balloon! Makes no sense right?
    with pytest.raises(NotImplementedError):
        q1.__lt__(q2) # Your ability to compare a rat and a balloon amazes me!
    with pytest.raises(NotImplementedError):
        q1.__le__(q2) # Everything seems less if expectations are too high, set your criteria right!
