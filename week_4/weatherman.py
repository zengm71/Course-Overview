# Saved in file weatherman.py

# imports the code that is found in report.py, called a module
from random import choice

# we now access the get_description function in the report module
def get_report():
    possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows']
    return choice(possibilities)