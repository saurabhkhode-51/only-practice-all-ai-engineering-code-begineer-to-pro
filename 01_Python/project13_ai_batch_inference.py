print("--- Production AI Batch Inference Engine (Retry logic) ---")
 
 # Step 1: Configuration & Initial State Variables
prompt = "Analyze market sentiment for Q3"
max_retries = 3
attempt = 0
is_successful = False


# Step 2: Primary Control Loop (while loop)
while attempt < max_retries and not is_successful:
    attempt += 1
    print(f"\n[Attempt {attempt}/{max_retries}] Sending prompt to LLM API...")

# Step 3: Simulating Network/API Response (Simulated Failure on Attempt 1)
if attempt < 2:
    api_stattus =500
    print(f" Result: API Error {api_stattus} (Payload Received Successfully)")
else:
    api_status = 200 
    is_successful = True
    print(f" Result: API Status {api_status} (Payload Received Successfuly)")

# Step 4: Final Resilience Log Payload
execution_log = {
    "prompt": prompt,
    "total_attempts_taken": attempt,
    "final_status": "SUCCESS_200" if is_successful else "FAILED_500",
    "is_completed": is_successful
}    

print("\n--- Final Resilience Execution Log ---")
print(execution_log)
