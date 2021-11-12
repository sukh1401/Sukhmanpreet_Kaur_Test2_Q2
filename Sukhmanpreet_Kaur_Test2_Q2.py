

class LargestValue:

    def maxValue(self):
        first = float(input("Enter first number: "))
        second = float(input("Enter second number: "))
        third = float(input("Enter third number: "))         
        maximumNumber=0

        if(first >= second and first >= third):
            maximumNumber = first
        if (second >= first and second >= third):
            maximumNumber=second
        if (third >= first and third >= second):
            maximumNumber=third
        print("The maximum number is ",maximumNumber)  

app = LargestValue()
app.maxValue()