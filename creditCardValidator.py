sum_odd_digits = 0
sum_even_digits = 0
total = 0

# Step 1

card_number = input("Enter a credit card number: ")
card_number = card_number.replace("-", "")
card_number = card_number.replace(" ", "")
card_number = card_number[::-1]

# Step 2

for x in card_number[::2]:
    sum_odd_digits += int(x)

# Step 3

for x in card_number[1::2]:
    double = int(x) * 2
    if double >= 10:
        sum_even_digits += 1 + (double % 10)
    else:
        sum_even_digits += double

# Step 4

total = sum_even_digits + sum_odd_digits

# Step 5

if total % 10 == 0:
    print("VALID")
else:
    print("INVALID")
