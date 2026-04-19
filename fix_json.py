import json

# Open the file with 'latin-1' (which can read almost anything)
with open('data.json', 'r', encoding='latin-1') as f:
    data = json.load(f)

# Save it back as 'utf-8' (which Django requires)
with open('data_fixed.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Success! 'data_fixed.json' has been created and is now clean.")