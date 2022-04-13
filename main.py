class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

def add(num1, num2):
    return num1+num2

cal1 = Calculator()

print(cal1.add(2))
print(cal1.add(3))
print(add(2,5))

