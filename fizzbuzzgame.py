
input_number= int(input("Select a number between 1 and 100: "))

for number in range(1, input_number+1):
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
    if number % 3 == 0:
        print("fizz")
        continue
    if number % 5 == 0:
        print("buzz")
        continue
    else:
        print(number)