import random
class fizz_buzz:
    def __init__(self):
        self.ini=random.randint(1, 120)
        print("Initial Number is: ", self.ini)
        self.curr= self.ini
    def check_condition(self, num):
        if num% 3 ==0:
            return "Fizz"
        elif num %5 ==0:
            return "Buzz"
        elif num % 3 ==0 and num %5 ==0:
            return "Fizz Buzz"
        else:
            return "___"
    def game_play(self):
        lst_num = self.ini
        while True:
            choice = input("Enter 'no' to continue or 'yes' to exit. ")
            if choice =='no':
                new_num = random.randint(1,120)
                print("New Generated Number is: ", new_num)

                final= lst_num + new_num
                print(f"{lst_num} + {new_num} = {final}")
                result1= self.check_condition(final)
                print("Result is:", result1)
                lst_num= new_num
            elif choice =='no':
                print("Exit the Game.")
                break
            else:
                print("Invalid Input.\nEnter 'yes' or 'no'.")
play= fizz_buzz()
play.game_play()
