'''1. AI Dataset Cleaner & Batch Processor
Logic & Scope: Gen AI models ko train karne ke liye raw text data clean karna padta hai. Is project mein user multiple text entries/prompts daalega (List). Program invalid spaces, length check, case-normalization (.lower()), duplicates remove karega aur finalized datasets ko sorted order mein show karega.

Topics Used: Variables, Data Types, Strings, Slicing, Conditional (if-elif-else), List Methods (.append(), .sort(), len()).'''

# Step 1: Raw AI Prompts Collection (List)
# Uncleaned data stored in a list

print("--- AI Dataset Cleaner & Batch Processor ---")

row_prompts = []

prompt1 = input("Enter Prompt 1: ")
row_prompts.append(prompt1)
prompt2 = input("Enter Prompt 2: ")
row_prompts.append(prompt2)
prompt3 = input("Enter prompt 3: ")
row_prompts.append(prompt3)

print("\nRow Prompts List:", row_prompts)

# Step 2: Cleaning Data using String Methods & List Operations
clean_prompts = []

p1_clean = prompt1.strip().lower()
clean_prompts.append(p1_clean)
p2_clean = prompt2.strip().lower()
clean_prompts.append(p2_clean)
p3_clean = prompt3.strip().lower()
clean_prompts.append(p3_clean)

print("Cleaned Prompts List:", clean_prompts)

 # Part 2: Sorting & Batch Summary (Step 3)
# Step 3: Sorting & Final Batch Summary

clean_prompts.sort()

print("\n--- Final Cleaned Dataset Summary ---")
print("Sorted Prompts List:", clean_prompts)
print("Total Prompts Processed:", len(clean_prompts))

# Tuple for Fixed Dataset Config (Immutable Data)

dataset_config = ("v1.0", "UTF-8", len(clean_prompts))
print("Dataset Metdata (Tuple):", dataset_config)

