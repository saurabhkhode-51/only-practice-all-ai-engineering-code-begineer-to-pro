print("--- AI Prompt Variable & Methods Analyzer ---")

# Step 1: Base Dictionary Setup (Lecture 4)
prompt_config = {
    "role": "Generative AI Engineer",
    "task": "Build Guardrails",
    "Framework": "fastAPI",
    "version": 1.0
}

# Step 2: Safe Key Access using .get()
# Direct access `prompt_config["domain"]` error deta, par .get() safe default value deta hai
domain = prompt_config.get("domain", "Enterprise AI")
print("Target Domain (Safe Access):", domain)

# Part 2: Extracting Keys, Values, and Items (Tuple Format)
# # Step 3: Inspecting Dictionary Structure

keys_list = list(prompt_config.keys())
values_list = list(prompt_config.values())
all_pairs = list(prompt_config.items())

print("\n--- Inspecting Config Metadata ---")
print("Config Keys (Names) :", keys_list)
print("Config Values (Data ):", values_list)
print("Config Key-value pairs (Tuples):", all_pairs)

# Part 3: Sets Integration & Batch Updating (.update())
# Step 4: Using Set to find Unique Frameworks (Sets + Lecture 3 Lists)
required_skills = ["Python", "FastAPI", "Python", "Docker", "FastAPI"]
unique_skills = set(required_skills)  # Unique elements strictly maintain karega
print("\nUnique Required Skills (Set Data Type):", unique_skills)

# Step 5: Batch Update using .update()
new_settings = {
    "task": "Build RAG Pipeline",
    "status": "In Progress"
}
prompt_config.update(new_settings)

print("\nFinal Updated Dictionary:")
print(prompt_config)