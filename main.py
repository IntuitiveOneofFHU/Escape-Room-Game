#TODO: troubleshoot problems with locks and bad inputs (like letters when asking for digits), also let user give up on entering code instead of looping forever until correct
class NumberLock:
    def __init__(self, answer):
        self.answer = answer
        #copies answer from initial input
        self.cur_code = []
        for space in self.answer:
            self.cur_code.append(0)
        #creates an empty space for each digit of the answer
    def enter_code(self):
        finish = False
        while finish == False:
            print(f'Current code: {self.cur_code}')
            sub_or_not = input('Submit code? Y/N')
            if sub_or_not == 'Y':
                if self.cur_code == self.answer:
                    print("Correct!")
                    finish = True
                else:
                    print("Incorrect")
            elif sub_or_not == 'N':
                digit = int(input(f'Select digit 1-{len(self.cur_code)}'))
                if digit > 0 and digit <= len(self.cur_code):
                    input_num = int(input(f'Select digit 0-9'))
                    if input_num >= 0 and input_num <= 9:
                        self.cur_code[digit-1] = input_num
                    else:
                        print('Invalid Input')
                else:
                    print('Invalid Input')
            else:
                print('Invalid Input')

test_lock = NumberLock([9, 3, 5, 2])
test_lock.enter_code()