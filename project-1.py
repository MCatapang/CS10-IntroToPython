full_name = input("Enter a name: ")
hrs = float(input("Enter hours worked: "))
hr_rate = float(input("Enter hourly rate: "))
actual_rate = hr_rate if (hrs <= 40) else (hr_rate * 1.5)
comp = format((hrs * actual_rate), ',.2f')

print(
    f"{full_name} should be paid ${comp}"
)