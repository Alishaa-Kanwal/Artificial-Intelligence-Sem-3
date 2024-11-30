import random
class fizz_buzz:
    def __init__(self):
        self.initiate =random.randint(1, 120)
        print("Initial Number: ", self.initiate)
        self.curr_nmber = self.initiate
    def check(self, nmber):
        if nmber% 3 == 0:
            return "Fizz"
        elif nmber%5 == 0:
            return "Buzz"
        elif nmber% 3 == 0 and nmber%5 == 0:
            return "Fizz Buzz"
        else:
            return "___"
    def game(self):
        lst_nmber = self.initiate
        while True:
            choice = input("Enter 'no' to continue or 'yes' to exit. ")
            if choice == 'no':
                new_nmber = random.randint(1,120)
                print("New Generated Number: ", new_nmber)

                result= lst_nmber + new_nmber
                print(f"{lst_nmber} + {new_nmber} = {result}")
                result1= self.check(result)
                print("Result:", result1)
                lst_nmber= new_nmber
            elif choice == 'no':
                print("Exited")
                break
            else:
                print("Invalid Input.\nPlease Enter'yes' or 'no'.")
play= fizz_buzz()
play.game()
