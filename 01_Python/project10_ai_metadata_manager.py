#$Project 10: LLM Metadata & Token Configuration Manager
# File Name: project10_ai_metadata_manager.py

# Real-World Purpose: AI Models (ChatGPT/Gemini) ko run karte waqt unke metadata parameters (model name, temperature, max tokens, system role) ko Dictionary (key:value) mein store, retrieve, aur update karna.

# Concepts Used: Dictionary Creation, Key Accessing, Key Updating, New Key Insertion
print("--- LLM Metadata & Token Configuration Manager ---")

# Step 1: Dictionary Creation (Key : Value Pairs)
ai_config = { 
    "model_name": "Gemini-Pro",
    "temperature": 0.7, 
    "max_tokens": 2048,
    "environment": "Development" 
}

# Step 2: Accessing Values using Keys
print("\nInitial AI Configuration:")
print("Model Name:", ai_config["model_name"])
print("Temperature:", ai_config["temperature"])
print("Max Tokens:", ai_config["max_tokens"])

#Part 2: Updating & Adding New Keys (Dynamic Change)
# Step 3: Updating Existing Key Value (Mutable Data Type)
# Production level ke liye temperature low karn
ai_config["temperature"] = 0.2
print("\nUpdated Temperature for Accuracy:", ai_config["temperature"])

# Step 4: Adding New Key:Value Pair
ai_config["System_role"] = "Senior AI Coding Mentor"
ai_config["is_active"] = True

# Printing Complete Updated Dictionary
print("\nFinal Model Configuration Metadata:")
print(ai_config)