class Employee:
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname


class SalaryEmployee(Employee):
    def __init__(self, fname, lname, salary):
        super().__init__(fname,lname)
        self.salary = salary

    def pay_check(self):
        return self.salary/12

class ContractorEmployee(Employee):
    def __init__(self, fname, lname, days_worked, day_rate):
        super().__init__(fname,lname)
        self.day_rate = day_rate
        self.days_worked = days_worked

    def pay_check(self):
        return self.days_worked * self.day_rate /12

class CommissionEmployee(SalaryEmployee):
    def __init__(self, fname, lname, salary, sales_numbers, com_rate):
        super().__init__(fname,lname,salary)
        self.sales_num = sales_numbers
        self.com_rate = com_rate

    def pay_check(self):
        salary = super().pay_check()
        total_commision = self.sales_num * self.com_rate
        return salary + total_commision /12