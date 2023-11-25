class Bill:
    """
    Object that contains data about amount.
    """

    def __init__(self,amount):
        self.amount = amount


class Flatmate:
    """
    Object contains data about the flatmate names, the period that the flatmates
    stayed in the house and pays a share of the bill """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate):
        weight = self.days_in_house/(self.days_in_house+flatmate.days_in_house)
        to_pay = weight*bill.amount
        return to_pay


while True:
    try:
        amount = int(input("Enter the bill amount: "))
        break  # Break out of the loop if the input is valid
    except ValueError:
        print("Please enter a valid integer for the bill amount.")

while True:
    try:
        days_flatmate1 = int(input("Enter the number of days Flatmate 1 stayed: "))
        break  # Break out of the loop if the input is valid
    except ValueError:
        print("Please enter a valid integer for the number of days.")

while True:
    try:
        days_flatmate2 = int(input("Enter the number of days Flatmate 2 stayed: "))
        break  # Break out of the loop if the input is valid
    except ValueError:
        print("Please enter a valid integer for the number of days.")

try:
    The_bill = Bill(amount)
    Flatmate1 = Flatmate(name=input("Name of Flatmate 1: "), days_in_house=days_flatmate1)
    Flatmate2 = Flatmate(name=input("Name of Flatmate 2: "), days_in_house=days_flatmate2)
except ValueError:
    print("Invalid input. Please enter valid values for the bill and days.")

print(Flatmate1.name, "pays", Flatmate1.pays(The_bill, Flatmate2))
print(Flatmate2.name, "pays", Flatmate2.pays(The_bill, Flatmate1))
