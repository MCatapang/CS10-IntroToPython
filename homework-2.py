num1 = int(input("Enter an integer: "))
num2 = int(input("Enter another integer: "))

product = num1 * num2
float_div = float(format((num1 / num2), '.2f'))
int_div = num1 // num2
remainder = num1 % num2
sum = num1 + num2
diff = num1 - num2

print(
    f"{num1} * {num2} = {product}",
    f"\n{num1} / {num2} = {float_div}", 
    f"\n{num1} // {num2} = {int_div}",
    f"\n{num1} % {num2} = {remainder}",
    f"\n{num1} + {num2} = {sum}",
    f"\n{num1} - {num2} = {diff}",
)