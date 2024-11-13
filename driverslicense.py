# Drivers license 
import time
import sys

class information:
    def __init__(self, typeoflicense, state, age=0) -> None:
        self.age = age 
        self.typeoflicense = typeoflicense 
        self.state = state

    def license(self):
        print(f"You are from the state of {self.state} and are {self.age} years old and you are looking for a class {self.typeoflicense}")
        print("Processing information")
        time.sleep(5)

    def license_approve(self):
        print("Based off your information you are approved!")
        time.sleep(5)
        sys.exit()

    def license_denied(self):
        print("Based off your information you do not meet our criteria")
        time.sleep(5)
        sys.exit()

typeoflicense = input("What license type are you looking for?")
state = input("What state are you from?")
age = int(input("How old are you?"))
user_info = information(typeoflicense, state, age)
user_info.license()


if age < 16:
    user_info.license_denied()
else:
    user_info.license_approve()