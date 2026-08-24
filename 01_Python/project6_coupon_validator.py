"""roject 6: E-Commerce Coupon Validator (Advance)
Is project mein hum String Slicing ([start:end]), Length len(), aur Conditional Logic (if-elif-else) sabhi ko ek saath mix karenge—jaise Swiggy ya Amazon par coupon code check hota hai."""

print("--- E Commerce Coupon Code Validator ---")
coupon = input("Enter your coupon code (e.g., SAVE50PRO): ")

#Step 2: Slicing & Extraction
total_len = len(coupon)
code_prefix = coupon[0:4]
discount_part = coupon[4:6]

# spep 3 : validation logic
print("\n--- Coupon Varification ---")

if total_len != 9:
    print("Status: INVALID Coupon! (code 9 letters ka hona chahiye)")
elif not coupon.startswith("SAVE"):
    print("Status: INVALID Coupon! (Code 'SAVE' se shuru hona chahiye  )")
elif not coupon.endswith("pro"):
    print("Status: INVALID Coupon! (code 'pro' par lhatam hona chahiye )")
else: 
    print("Status: VALID Coupon Applied! 🎉")
    print("Prefix Detected:", code_prefix)
    print("Discount Amount:", discount_part + "% OFF")
          












