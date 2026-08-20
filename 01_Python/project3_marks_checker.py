print("--- Student Result & Grade Checker ---")

sub1 = float(input("Enter marks for subject 1 (out of 100): "))
sub2 = float(input("Enter marks for subject 2 (out of 100): "))
sub3 = float(input("Enter marks for subject 3 (out of 100): "))

# total & percentage calculations 
total_marks = sub1 + sub2 + sub3
percentage = (total_marks /300) *100

# Result Display & Decision Making (if / elif / else)
print("\n--- Result Summary ---")
print("Total Marks:", total_marks, "/ 300")
print("Percentage:", percentage, "%")

# Pass / Fail Check
if percentage >= 40:
    print("Status:  PASSED")

# Grade Check (Nested Level)
    if percentage >= 75:
        print("Grade: A (Distinction)")
    elif percentage >= 60:
        print("Grade: B (First Class)")
    else:
        print("Grade: C (Pass Class)")
else:
    print("Status: FAILED")
    print("Grade: No Grade (Needs Improvement)")    