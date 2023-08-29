def pronunciation(a):
    b = ['', "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    c = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    d = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    if 11 <= a <= 19:
        print(d[a % 10])
    elif a == 0:
        print("zero")
    else:
        print(c[a // 10], b[a % 10])
    return

while True:
    print("press 'y' to exit")
    w = input("Enter the number:")
    if w == "y":
        print("Exciting the system...")
        break
    else:
        w = int(w)
        pronunciation(w)
