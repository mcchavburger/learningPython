from employee import Employee, SalaryEmployee, ContractorEmployee, CommissionEmployee


class Company:
    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []
    
    def add_employees(self, new_employee):
        self.employees.append(new_employee)

    def display_employs(self):
        print("------------------------------------")
        for i in self.employees:
            print("Employee:", i.first_name, i.last_name)
            print(f"earns ${i.pay_check():,.2f} a month")
            print("------------------------------------")

def main():
    my_company = Company("Right Cloud IT Limited")

    employee_1 = ContractorEmployee("Dan", "Johnson", 220, 1200)
    employee_2 = SalaryEmployee("Deb", "Valvona Johnson", 12500)
    employee_3 = CommissionEmployee("Gavin", "Stephens", 12000, 20, 1200)

    my_company.add_employees(employee_1)
    my_company.add_employees(employee_2)
    my_company.add_employees(employee_3)

    my_company.display_employs()

main()