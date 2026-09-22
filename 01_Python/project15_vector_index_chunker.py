import json

print("--- 2027 Production Vector Database Index Chunking Engine ---")

raw_document = (
    "Generative AI infrastructure relies heavily on Vector Databases. "
    "Vector embeddings map semantic meaning into high_dimensional numrical spaces. "
    "To index massive datasets, text must be devided into smaller chunks using precise renges. "
    "Retrieval Augmented Generation (RAG) fetches these relevant chunks to eliminate hallucinations."
)

chunk_size = 100
overlap = 20
total_length = len(raw_document)

chunks_payload = []

chunk_id = 0

for start_idx in range(0, total_length, chunk_size - overlap):
    end_idx = min(start_idx + chunk_size, total_length)
    chunk_text = raw_document[start_idx:end_idx]

    chunk_data = {
        "chunk_id": f"chunk_{chunk_id}",
        "start_idx": start_idx,
        "end_idx":end_idx,
        "char_length": len(chunk_text),
        "text": chunk_text
    }  

    chunks_payload.append(chunk_data)
    chunk_id += 1

    if end_idx == total_length:
        break

print(f"Total Chunks Generated: {len(chunks_payload)}")


html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Vector DB Chunking Visualizer</title>
    <style>
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-sarif; background-color: #0f172a; color: #f8fafc; padding: 20px; }}
        h1 {{ color: #38bdf8; text-align: center; }}
        .stats {{ background-color: #1e293b; padding: 15px; border-radius: 8px; margin-bottom: 20px; text-align: center; }}
        .chunk-card {{ background-color: #1e293b; border-left: 4px solid #38bdf8; padding: 15px; border-radius: 6px; }}
        .badge {{ background-color: #0284c7; color: white; padding: 3px 8px; border-radius: 4px; font-size: 12px; font-weight: bold; }}
        .text-content {{ background-color: #0f172a; padding: 10px; bprder-radius: 4px; font-family: monospace; color: #a5f3fc; margin-top: 8px; }}
    </style> 
</head>
<body>
    <h1>2027 Vector Indexing pipeline Report</h1>
    <div class="stats">
        <strong>Total Document Length:</strong> {total_length} chars 
        <strong>Chunk Size:</strong> {chunk_size} 
        <strong>Overlap:</strong> {overlap}
        <strong>Generated Chunks:</strong> {len(chunks_payload)}
    </div>
    <h2>Indexed Vector Chunks</h2>          
"""    

for item in chunks_payload:
    html_content += f"""
    <div class="chunk-card">
        <span class="badge">{item['chunk_id'].upper()}</span>
        <small style="color: #94a3b8;"> (span: {item['start_idx']} to {item['end_idx']})</small>
        <div class="text-content">{item['text']}</div>
     </div>
    """

html_content += """
</body>
</html>
"""

with open("Vector_chunks_report.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("\n[SUCCESS] Vector DB Indexing Complete!")
print("[REPORT GENERATED] Open 'Vector_chunks_report.html' in your browser to view the visual dashboard!")    