print("customer details")
print("------------------")
brand = input("Enter brand\n")
model = input("Enter model\n")
complaint = input("Enter complaint\n")
imei = input("Enter IMEI number\n")
repair_cost = float(input("Enter repair cost\n"))
discount = repair_cost * 10 / 100
final_bill = repair_cost - discount
print ("::::Brite Shoppe::::")
print("Brand: ", brand)
print("Model: ", model)
print("Repair Cost: ", repair_cost)
print("Discount 10%: ", discount)
print("Final Bill Amount: ", final_bill)
if final_bill >= 2000:
    print("status: Premium Customer 1 month warrenty extended")
else:
    print("status: Normal Customer regular warrenty")