"""
Parameters
----------
value : String
    A string representing either a male or female gender


Returns
-------
'male' or ' 'female'
    Method, formats valid values and provides the output
"""


def Gender(value):
    if value == 'female' or value == 'Female' or value == 'f' or value == 'F':
        return 'female'
    elif value == 'male' or value == 'Male' or value == 'm' or value == 'M':
        return 'male'
    else:
        raise ValueError(
            'Error: Please enter a valid gender, i.e. Male or Female')
