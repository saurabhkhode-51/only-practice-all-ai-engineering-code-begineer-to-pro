'''Project 9 (AI Model Performance & Metric Evaluator) hamare Python Basics aur Lecture 3 (Lists & Tuples) ka sabse powerful, final capstone project hoga.

AI Engineering mein jab hum LLMs ya Machine Learning models ko test karte hain, toh unke performance outputs ko analyze aur score karne ke liye ye logic continuously use hota hai
print("--- AI Model Performance & Metric Evaluator ---")'''
print("--- AI Model Performance & Metric Evaluator ---")
# Step 1: Fixed Industry Benchmark Configuration (Tuple - Immutable)
Benchmark_CONFIG = (0.80, "Production Baseline v1.0")
print("Target Benchmark Score:", Benchmark_CONFIG[0])

# Step 2: Collecting Accuracy Scores for 3 AI Models
models = ["Gemini Pro", "Llama-3", "claude-3"]
scores = []

print("\nEnter Accuracy Scores (between 0.00 and 1.00):")
score1 = float(input(f"Score for {models[0]}: "))
score2 = float(input(f"score for {models[1]}: "))
score3 = float(input(f"score for {models[2]}: "))

scores.append(score1)
scores.append(score2)
scores.append(score3)


# Step 3: Performance Calculations
highest_score = max(scores)
lowest_score = min(scores)

# Best Model Finding via List Indexing
best_model_index = scores.index(highest_score)
best_model_name = models[best_model_index]

print("\n--- Evaluation Summary ---")
print("Model Evaluated:", models)
print("Collected Scores:", scores)
print(f"Top Performing Model: {best_model_name} With score {highest_score}")

# Step 4: Sort Scores (Highest to Lowest)
sorted_scores = scores.copy()
sorted_scores.sort(reverse=True)
print("Ranked Scores (Descending):", sorted_scores)

# Step 5: Benchmark Verification
if highest_score >= Benchmark_CONFIG[0]:
    print("Deployment Status: READY FORPRODUCTION")
else:
    print("Deployment Status: REJECTED (Below Target Threshold)")    