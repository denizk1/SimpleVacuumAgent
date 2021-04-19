import random

class Environment(object):

    def __init__(self):
        # whether the locations are clean or dirty in the first location were determined randomly
        self.locationConditional = {"A": random.choice(["dirty", "clean"]), "B": random.choice(["dirty", "clean"])}


class SimpleVacuumAgent(Environment):

    def __init__(self, location):
        super().__init__()
        self.location = location.upper()  # location of the room where the vacuum initially stopped

    def VacumWorld(self):
        if (self.location == "A"):  # the first location being "A"
            if (self.locationConditional["A"] == "dirty"):  # if location A is dirty, room A is cleaned
                print("Location A is Dirty.")
                print("The dirt in A is getting sucked")
                print("CLEANING A.... ")
                self.locationConditional["A"] = "clean"
                print("Location A has been Cleaned.")
                print("Moving right to the Location B. ")
                if (self.locationConditional["B"] == "dirty"):
                    print("Location B is Dirty.")
                    print("The dirt in B is getting sucked")
                    print("CLEANING B.... ")
                    self.locationConditional["B"] = "clean"
                    print("Location B has been Cleaned. ")
                else:
                    print("No action")
                    print("Location B is already clean.")
            else:
                print("No action")  # if location A is clear, no action will be taken
                print("Location A is already clean.")
                if (self.locationConditional["B"] == "dirty"):  # The vacuum freezes to the right and controls the B location. If location B is dirty, it is cleared.
                    print("Location B is Dirty.")
                    print("The dirty in B is getting sucked")
                    print("CLEANING B.... ")
                    self.locationConditional["B"] = "clean"
                    print("Location B has been Cleaned. ")
                else:
                    print("No action")  # No action if location B is not dirty
                    print("Location B is already clean.")
        if (self.location == "B"):  # ilk lokasyonun B olma durumu
            if (self.locationConditional["B"] == "dirty"):  # clear if location B is dirty
                print("Location B is Dirty.")
                print("The dirt in B is getting sucked")
                print("CLEANING B.... ")
                self.locationConditional["B"] = "clean"
                print("Location B has been Cleaned.")
                print("Moving left to the Location A. ")
                if (self.locationConditional["A"] == "dirty"):
                    print("Location A is Dirty.")
                    print("The dirt in A is getting sucked")
                    print("CLEANING A.... ")
                    self.locationConditional["A"] = "clean"
                    print("Location A has been Cleaned. ")
                else:  # No action is taken if location A is clean
                    print("No action")
                    print("Location A is already clean.")
            else:
                print("No action")  # If location B is clear, no action will be taken
                print("Location B is already clean.")
                if (self.locationConditional["A"] == "dirty"):  # The vacuum turns to the left and is cleaned if location A is dirty
                    print("Location A is Dirty.")
                    print("The dirt in A is getting sucked")
                    print("CLEANING A.... ")
                    self.locationConditional["A"] = "clean"
                    print("Location A has been Cleaned. ")
                else:  # No action is taken if location A is clean
                    print("No action")
                    print("Location A is already clean.")


if __name__ == "__main__":

    try:

        Location_input = str(input("Please write the first room to be entered as string (A or B): "))
        enver = SimpleVacuumAgent(Location_input)
        enver.VacumWorld()

    except TypeError:

        print("Please enter The correct location")