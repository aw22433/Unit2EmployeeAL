#create an Employee class
#booked list is protected. 
class Employee:
    """Represents an Employee
    attributes: Employee name, Employee number, A/L remaining"""
    Leave_remaining = 30
    __booked= []

#define the leave booking method which checks the leave remaining. If the request is valid, it will:
# deduct days from the remaining leave
# store a record of approved leave requests
# and print a confirmation 
    def book_leave(self, number_of_days, start_date):
        Leave_left = self.Leave_remaining - number_of_days
        if Leave_left >= 0:
            self.Leave_remaining -= number_of_days
            print("Annual leave approved. Remaining days: " + str(self.Leave_remaining))
            self.__booked.append(self.name + " has booked off " + str(number_of_days) + " days of A/L beginning " + start_date)
            print(self.__booked)
#if there isnt sufficient days remaining to fulfil the request the leave will be refused and a confirmation message printed
        else:
            print("Leave request rejected due to insufficient days remaining")

#Create 4 employee objects from our class and name them
E1 = Employee()
E1.name = "A"
E2 = Employee()
E2.name = "B"
E3 = Employee()
E3.name = "C"
E4 = Employee()
E4.name = "D"

#create a dictionary to match the user input to the applicable employee object
Employee_list = {'E1':E1,'E2':E2,'E3':E3,'E4':E4}

#create main function so the program will restart following each request
#this will take in the user input for the leave request details then call the method on the applicablope object.
def main():
    employee_number = input("Which employee? ")
    emp = Employee_list[employee_number]

    start_date = input("Date of first day of A/L? ")
    number_of_days = int(input("Number of days requested? "))
    emp.book_leave(number_of_days, start_date)

    main()

main()