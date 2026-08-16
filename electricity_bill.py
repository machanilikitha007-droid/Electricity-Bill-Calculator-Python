print("===== ELECTRICITY BILL CALCULATOR =====")

name = input("Enter customer name: ")
units = float(input("Enter electricity units: "))

if units <= 100:
    bill = units * 1.5
elif units <= 200:
    bill = (100 * 1.5) + ((units - 100) * 2.5)
elif units <= 300:
    bill = (100 * 1.5) + (100 * 2.5) + ((units - 200) * 4)
else:
    bill = (100 * 1.5) + (100 * 2.5) + (100 * 4) + ((units - 300) * 5)

print("\n===== BILL DETAILS =====")
print("Customer Name:", name)
print("Units Consumed:", units)
print("Electricity Bill: ₹", bill)
