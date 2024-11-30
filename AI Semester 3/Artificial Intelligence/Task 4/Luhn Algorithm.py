class LUHN:
    def __init__(self,card_nmber):
        self.card_nmber =[int(digit) for digit in card_nmber]
    def validation(self):
        if len(self.card_nmber) != 16:
            print("Please enter a valid 16-digit card number.")
            return
        digit =self.card_nmber.pop()
        self.card_nmber.reverse()
        for dgt in range(0,len(self.card_nmber), 2):
            self.card_nmber[dgt]*= 2
            if self.card_nmber[dgt]> 9:
                self.card_nmber[dgt]-= 9
        t_sum = sum(self.card_nmber)
        t_sum +=digit
        if t_sum % 10 ==0:
            print("Congratulations! Card is valid!")
        else:
            print("Card number is invalid.")
card_nmber = input("Enter a 16-digit card number: ")
card1 =LUHN(card_nmber)
card1.validation()
