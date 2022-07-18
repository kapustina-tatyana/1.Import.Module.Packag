from application.salary import *
from application.db.people import *
from datetime import *

def calculate_salary():
    print('dirty calculate_salary')

today = datetime.today()
print(today)
calculate_salary()
get_employees()
