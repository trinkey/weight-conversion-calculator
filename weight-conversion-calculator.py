weightconversion = [
    [1, 1000, 1e+6, 1e+9, 1e+12, 0.984207, 1.10231, 157.473, 2204.62, 352674],
    [0.001, 1, 1000, 1e+6, 1e+9, 0.000984207, 0.00110231, 0.157473, 2.20462, 35.274],
    [1e-6, 0.001, 1, 1000, 1e+6, 9.8421e-7, 1.1023e-6, 0.000157473, 0.00220462, 0.035274],
    [1e-9, 1e-6, 0.001, 1, 1000, 9.8421e-10, 1.1023e-9, 1.5747e-7, 2.2046e-6, 3.5274e-5],
    [1e-12, 1e-9, 1e-6, 1000, 1, 9.8421e-13, 1.1023e-12, 1.57472-10, 2.2046e-9, 3.5274e-8],
    [1.10165, 1.10165e+3, 1.10165e+6, 1.10165e+9, 1.10165e+12, 1, 1.12, 160, 2240, 35840],
    [0.907185, 0.907185e+3, 0.907185e+6, 0.907185e+9, 0.907185e+12, 0.892857, 1, 142.857, 2000, 32000],
    [0.00635029, 6.35029, 6.35029e+3, 6.35029e+6, 6.35029e+9, 0.00625, 0.007, 1, 14, 224],
    [0.000453592, 0.0453592, 453.592, 453592, 453592e+3, 0.000446429, 0.0005, 0.0714286, 1, 16],
    [2.835e-5, 0.0283495, 28.3495, 28349.5, 28349.5e+3, 2.7902e-5, 3.125e-5, 0.00446429, 0.0625, 1]
]

while True:
    start = input('''1: Metric Ton
2: Kilogram
3: Gram
4: Milligram
5: Microgram
6: Imperial Ton
7: US Ton
8: Stone
9: Pound
10: Ounce
What is the starting weight?
--> ''')
    end = input('What is the ending weight?\n--> ')
    
    if ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'].count(start) and ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'].count(end):
        amount = input("How many do you start with? (\"break\" to break)\n--> ").lower()
        d = 0
        if amount == "break":
            break
        amountd = amount.replace('.', '')
        for i in amountd:
            d += ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'].count(i)
        
        if len(amountd) == d and (len(amount) == d or len(amount) == d + 1):
            amount = float(amount)
            output = amount * weightconversion[int(start) - 0][int(end) - 1]
            print("Output: " + str(output))
            input("Press enter to continue.")
        else:
            print("Bad input, please enter a number")
    else:
        print("Bad input, enter a number from 1-10.")
    print("")
