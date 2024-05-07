"""
Blackjack
"""
# Provide your solution here
def calculate_score(inta: int, intb: int, intc: int) -> int or str:
    if (inta and intb and intc) > 0 and (inta and intb and intc) < 12:
        sum = inta + intb + intc
        if sum <= 21:
            return sum
        elif sum > 21 and (inta or intb or intc) == 11:
            sum = sum - 10
            if sum > 21:
                return "BUST"
        else:
            sum = sum -10
            return sum
    else:
        print("Invalid input, please enter three integers between 1 and 11!")

print(calculate_score(3, 8, 11))

"""
Even Numbers
"""
# Provide your solution here

def even_positive_numbers(my_list: list) -> list:
    even_numbers = [num for num in my_list if num % 2 == 0]
    even_pos_numbers = [num for num in even_numbers if num >= 0]
    print(even_pos_numbers)


var1 = even_positive_numbers(my_list=[3, -5, 2, -6, 4])
var2 = even_positive_numbers(my_list=[567, 243, -456, 234, 235])
var3 = even_positive_numbers(my_list=[243,-345, 246, 564, 239])

print(var1, var2, var3)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    even_positive_numbers(my_list=[3, -5, 2, -6, 4])
    even_positive_numbers(my_list=[567, 243, -456, 234, 235])
    even_positive_numbers(my_list=[243, -345, 246, 564, 239])
    print("Test your functions by calling them here. Use different parameter values to test them with different scenarios.")

