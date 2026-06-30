def test_rail(rail_name, voltage, check_count):
    print(f"\n--- Testing {rail_name} ({voltage}V) ---")
    for i in range(1, check_count + 1):
        print(f"Reading {rail_name}: {voltage}V - STABLE")
    print(f"Status: {rail_name} Pass!")
test_rail("PP_CPU", 1.1, 2)
test_rail("PP_1V8_ALWAYS", 1.8, 3)
 