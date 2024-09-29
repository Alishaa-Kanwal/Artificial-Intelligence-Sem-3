class LUHN:
    def __init__(self,card_num):
        self.card_num =[int(digit) for digit in card_num]
    def validation(self):
        if len(self.card_num) != 16:
            print("Please enter a valid 16-digit card number.")
            return
        digit =self.card_num.pop()
        self.card_num.reverse()
        for dgt in range(0,len(self.card_num), 2):
            self.card_num[dgt]*= 2
            if self.card_num[dgt]> 9:
                self.card_num[dgt]-= 9
        t_sum = sum(self.card_num)
        t_sum =t_sum + digit
        if t_sum % 10 ==0:
            print("Congratulations! Card is valid!")
        else:
            print("Card number is invalid.")
card_num = input("Enter a 16-digit card number: ")
card =LUHN(card_num)
card.validation()
