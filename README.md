# Assignment 4 Submission

This assignment was a whole new experience for me!!! Credits to you guys for giving us this opportunity. It was slightly confusing at first but after going through the assignment multiple times, I am hoping that I have understood it right. So here's what I have to share with you :

### Qualean
So as we have discovered now, Qualean class is inspired by Boolean and Quantum concepts. It only accepts 3 possible real states as follows : True, False, and Maybe represented as (1, 0, -1). Then, it internally picks an imaginary state for itself, how? Lets' see -- The moment you assign it a real number, it immediately finds an imaginary number using random.uniform(-1, 1) and multiplies with it. This number is stored internally after using Bankers rounding and precision is maintained upto 10 decimal places.

### Bankers rounding
Also known as 'ROUND_HALF_EVEN' or Rounding to even is an algorithm to round the given number to its nearest value, checks the fractional component of the number, if it is given halfway between two numbers, also called (Ties), it rounds the value to the nearest value with an even least significant digit.

### __and__
This functions works internally as bool(a and b) for qualean numbers, so a.__and__(b) will work as follows : if a is False, it returns False and doesn't evaluate further so it doesn't check for b value defined or not. In case, value of a is not zero and b is not defined, it throws error that b is not defined, if both are defined, it checks if value of both a and b is greater than zero, returns True else returns False.

### __or__
OR functions works internally as bool(a or b) for qualean numbers, so a.__or__(b) will work as follows : if a is True, it returns True and doesn't evaluate further so it doesn't check for b value defined or not. In case, value of a is not zero and b is not defined, it throws error that b is not defined, if both are defined, it checks if value of either a or b is greater than zero, returns True else returns False.

### __repr__
Repr method is used to display the object, it's representation. So we are defining representation of Qualean number in this method.

### __init__
Init method is used to initialize the object's state, we use this function to assign and store the qualean number value.

### __str__
The str method returns a string object, which is considered as an informal representation of the given object.

### __add__
This add method is used to add two qualean numbers and returns the sum. It accepts user input and checks if the value given is of type Qualean. If it is true, it adds given qualean number to stored qualean number and returns result else raises 'NotImplementedError'.

### __eq__
Eq (Equality) method tests for equality, this method takes input for two qualean numbers and checks if they are equal or not.

### __float__
Float method converts given qualean number to its equivalent float type and returns the float value.

### __gt__
Gt (Greather than) method is used to check if stored qualean number is greater than given qualean number and returns result as True or False.

### __ge__
Ge (Greather than equal to) method is used to check if stored qualean number is greater than or equal to given qualean number and returns result as True or False.

### __invertsign__
This function inverts the sign (+,-) of stored qualean number and returns the output as its negated value.

### __le__
Le (Less than equal to) method is used to check if stored qualean number is less than or equal to given qualean number and returns result as True or False.

### __lt__
Lt (Less than) method is used to check if stored qualean number is less than given qualean number and returns result as True or False.

### __mul__
This function multiplies given qualean number with stored qualean number and returns result if given qualean number is of type Qualean else raises 'NotImplementedError'

### __sqrt__
Sqrt (square root) function is used to return the square root value of stored qualean number. It returns result as a complex number since the qualean number can be a negative number as well so it calculates square root for postive value using Decimal.sqrt() method else converts negative number to positive by multiplying by -1 and then evaluates its square root, finally it returns the value of complex number accordingly based on positive/negative input.

### __bool__
This boolean function only returns true if the value of qualean number is not zero otherwise returns false.

## Test Cases Explanation

### test_readme_exists 
Checks if readme file exists.

### test_readme_contents
Checks if readme file has atleast 500 words.

### test_readme_proper_description
Checks if all functions implemented have been defined in readme

### test_readme_file_for_formatting
Checks if file is formatted properly using "#"

### test_indentations
Checks if four spaces multiple only have been used throughout the code

### test_function_name_had_cap_letter
Checks if no function name starts with capital letter

### test_all_functions_implemented
Checks if all functions have been implemented in code

### test_decimal_used
Checks if decimal has been used or not in code

### test_qualean_num_precision
Checks if non zero qualean numbers stored have precision of 10 decimal places

### test_user_input
Checks if real value entered by user is equivalent to either 0, 1 or -1 only.

### test_function_for_equality  (__eq__)
Checks if two qualean numbers are equal using isclose method. 
Checks sum of million different qualean number is equal to zero using isclose method.

### test_function_for_add (__add__)
Checks sum of a qualean number added to itself 100 times equals 100 * itself using both isclose and == method.

### test_function_for_gt (__gt__)
Checks if stores qualean number is greater than given qualean number.

### test_function_for_ge (__ge__)
Checks if stores qualean number is greater than or equal to given qualean number.

### test_function_for_lt (__lt__)
Checks if stores qualean number is lesser than given qualean number.

### test_function_for_le (__le__)
Checks if stores qualean number is lesser than or equal to given qualean number.

### test_function_for_bool (__bool__)
Checks if bool function returns true for non zero qualean numbers only.

### test_function_for_invertsign (__invertsign__)
Checks if given qualean number is negated in the output when invertsign method is called, i.e positive number given changes to its negative value and vice versa.

### test_function_for_sqrt (__sqrt__)
Checks for positive qualean number square root using Decimal.sqrt and negative qualean number square root using cmath.sqrt().

### test_function_for_mul (__mul__)
Checks if two qualean numbers when multiplied gives correct result or not.

### test_function_for_and (__and__)
Checks if 'and' works like bool(a and b) i.e if b in undefined and a is false, return false, else return true or false based on both values are true or false.

### test_function_for_or (__or__)
Checks if 'or' works like bool(a or b) i.e if b in undefined and a is true, return true, else return true or false based on if either value is true, return true else false.

### test_function_for_float (__float__)
Checks if float function returns value of type float.

### test_function_for_repr (__repr__)
Checks if repr method returns representation of object as expected.

### test_function_for_str (__str__)
Checks if str method returns string for defining object as expected.

### test_functions_for_non_qualean_values
Checks if all functions only operate on qualean values and raise error if input to specified methods is not a Qualean number.


