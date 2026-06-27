line_name = input("Enter Power Line Name: \n")
voltage = float(input("Enter Measured Voltage: \n"))
print(f"\nLine: {line_name}")
print("Voltage:", voltage,"v")
if voltage == 0:
    print("Result: Short Circuit or Dead Line!")
elif voltage > 4.2:
    print("Result: High Voltage! Risk of Component Damage!")
else:
    print("Result: Normal Operating Voltage.")