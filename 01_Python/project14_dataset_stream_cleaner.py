print("--- Production LLM Dataset Stream Cleaner & Normalizer ---")

# Step 1: Raw Messy Dataset Stream from Web Crawler
raw_dataset_stream = [
    "Generative AI is Changing automation. ",
    "",
    "   ",
    "Prompt Engineering is essential for LLMs.",
    "CRITICLE_SEFETY_VIOLATION_MALWARE_PROMPT",
    "Python data pipelines must be fast." 
]

cleaned_dataset = []

print("1. Processing Raw Dataset Stream...\n")

for chunk in raw_dataset_stream:
    stripped_chunk = chunk.strip()


    if len(stripped_chunk) == 0:
        print(" [SKIP] Empty chunk detected. Triggering 'continue'...")
        continue 



    if "SAFETY_VIOLATION" in stripped_chunk:
        print(" [ALERT] Security breach detected! Triggering 'break' to stop pipeline.")
        break


    if "LLM" in stripped_chunk:
        pass

normalized_chunk = stripped_chunk.upper()
cleaned_dataset.append(normalized_chunk)
print(f" [PROCESSED] Cleaned: '{normalized_chunk}'")


print("\n--- Final Cleaned Dataset Summary ---")
print(f"Total Processed Chunks: {len(cleaned_dataset)}")
print("Cleaned Data Array:", cleaned_dataset)
