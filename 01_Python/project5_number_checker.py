# Project 5: Smart Number & Divisibility Analyzer (Medium)
# Step 1: User Input (Number Lena)

print("--- smart number analyazer ---")
num = int(input("Enter any integer number: "))

# step 2 Even /oodd cheak 
print("\n--- Analyasis Results ---")

if num % 2 == 0:
    print("Number type: EVEN Number")
else:
    print("Number type: ODD Number")

# step 3 Multiple of 7 check
if num % 7 == 0:
    print("Special Rule: Yes, it is a multiple of 7! ")
else:
    print("Special Rule: Not a Multiple of 7. ")
                