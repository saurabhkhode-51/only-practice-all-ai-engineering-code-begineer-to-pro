print("--- Production-Grade RAG Token Optimizer & Vector Indexer ---")
#  Step 1: Raw Unstructured Data Input
raw_token_stream = ["rag", "vector", "llm", "rag", "embeddings", "llm", "prompts", "vector"]
print("1. Raw Token Stream(Count:", len(raw_token_stream), "):", raw_token_stream)

# Step 2: Set Deduplication #(Engine Air-Filter)
# Set duplicates ko automatic clean karke unique elements rakhta hai
unique_vocab_set = set(raw_token_stream)
print("2. Optimized Unique Vocabulary (set):", unique_vocab_set)
print("     Tokens Saved:", len(raw_token_stream) - len(unique_vocab_set))

# Step 3: Raw Document Metadata (Dictionary Setup)
doc_metadata = {
    "doc_id": "doc_101",
    "author": "saurabh",
    "chunk_size": "512",
}

# Step 4: Safe Fallback Retrieval using .get()
environment = doc_metadata.get("environment", "Production")
# Step 5: Batch Metadata Update using .update()
system_updates = {
    "token_count": len(unique_vocab_set),
    "environment": environment,
    "status": "INDEXED" 

}

doc_metadata.update(system_updates)

print("\n--- Part 2: Standardized Vector Metadata ---")
print("Indexed Metadata:", doc_metadata)

# Step 6: Security Clearance & Access Check using Set Intersection
user_permissions = {"developer", "analyst", "guest"}
doc_security_tags = {"developer", "finance_admin"}

# Set Intersection (&): Sirf wahi elements nikalta hai jo DONON sets mein common hon
# Boolean evaluation (if matched_permissions has items, access granted)
matched_permissions = user_permissions.intersection(doc_security_tags)
is_access_granted = len(matched_permissions) > 0

# Step 7: Final RAG Payload Assembly for Vector DB
final_rag_payload = {
    "unique_vocab_": unique_vocab_set,
    "metadata": doc_metadata,
    "security": {
        "access_granted": is_access_granted,
        "matched_granted": matched_permissions
    }

}

print("\n--- Part 3: Final Production RAG Payload ---")
print("Access Grantede:", is_access_granted)
print("Matched Security Roles:", matched_permissions)
print("\nComplete Output Payload:")
print(final_rag_payload)