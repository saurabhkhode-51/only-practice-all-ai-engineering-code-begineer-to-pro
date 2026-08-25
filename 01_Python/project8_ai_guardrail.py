'''Project 8: GenAI Prompt Safety & Guardrail System
AI engineering (LLMs/LangChain) mein sabse pehla real-world task hota hai Guardrails lagana—yani user ke bad ya malicious prompts ko API tak jaane se pehle hi block karna.

File Name: project8_ai_guardrail.py

Concepts Used: Tuples (Banned System Keywords), Lists (Approved Prompts Queue), String Methods (.lower(), .contains/in), Conditionals (if-else), Slicing.'''

print("--- GenAI Prompt Safety & Guardrail System ---")
# System Fixed Security Configuration (Tuple - Cannot be altered)

BANNED_KEYWORDS = ("hack","bypass", "system prompt", "drop table", "ignore previous instructions")
SYSTEM_CONFIG = ("Model: Gemini-Pro", "Safety Level : Strict")

print("Guardrail Active With Config:", SYSTEM_CONFIG)

# Dynamic Queue for Approved Prompts (List)

Approved_prompts = []
# User Input
user_prompt = input("\nEnter Your LLM prompt: ")
prompt_clean = user_prompt.strip().lower()

'''Part 2: Security Validation & Queue System
Python
# Part 2: Security Verification Logic

# Step 1: Check if prompt contains any banned keywords'''
is_safe = True
if BANNED_KEYWORDS[0] in prompt_clean or BANNED_KEYWORDS[1] in prompt_clean:
    is_safe = False
elif BANNED_KEYWORDS[2] in prompt_clean or BANNED_KEYWORDS[3] in prompt_clean:
    is_safe = False
elif BANNED_KEYWORDS[4] in prompt_clean:
    is_safe = False

    # Step 2: Decision Making & Processing

if is_safe:
    print("Status: PROMPT APPROVED (Safe for LLM Processing)")        

# Store approved prompt in the queue list
    Approved_prompts.append(prompt_clean)

    print("Current Queue:", Approved_prompts)
    print("Total Queued Prompts:", len(Approved_prompts))
    print("Prompt Preview (First 15 Chars):", prompt_clean[0:15])
else:
    print("Status: PROMPT REJECTED! Security VIolation Detected. ")
    print("Warning: Banned Keywords like hack /bypass/System Prompt are restricted.")