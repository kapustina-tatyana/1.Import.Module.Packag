from application.salary import calculate_salary as cal_sal
from application.db.people import get_employees as get_empl
from datetime import datetime

if __name__ == '__main__':
    today = datetime.today()
    print(today)
    cal_sal()
    get_empl()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
