def check_current (ampere):
    print(f"Charging input: {ampere} A")
    if ampere > 1.5:
        print("Fast Charging Mode Active\n")
    elif ampere ==0:
        print("No Charging Mode Active\n")
    else:
        print("Normal Charging Mode Active\n")
check_current(2.0)
check_current(1.0)
check_current(0.0)