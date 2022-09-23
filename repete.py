#!/usr/bin/env python3

numbers = range(1, 11)

for number in numbers:
    par = number % 2 == 0
    if par:
        print(number)
    else:
        continue

    print(f"mais codigo com {number}")