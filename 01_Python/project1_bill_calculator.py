print("--- welcome to smart bill calculator ---")

total_bill = float(input("enter total bill amount (Rs.):"))
tip_percent = float(input("enter tip percentage (e.g., 10,15):"))
people = int(input("enter of  people splitting the bill: "))

tip_amount = (total_bill * tip_percent) /100
final_bill = total_bill + tip_amount
price_per_person = final_bill / people

print("\n--- Bill Details---")
print("Total Tip: Rs.", tip_amount)
print("Grand Total: Rs.", final_bill)
print("Amount Per Person: Rs,", price_per_person)


