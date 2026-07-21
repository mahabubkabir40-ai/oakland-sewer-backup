import json
import re

with open('royal-oak-sewer-cleanup.html', 'r', encoding='utf-8') as f:
    content = f.read()

scripts = re.findall(r'<script type="application/ld\+json">(.*?)</script>', content, re.DOTALL)

print(f"Found {len(scripts)} JSON-LD blocks:")
for idx, s in enumerate(scripts, 1):
    try:
        data = json.loads(s.strip())
        print(f"\nBlock {idx}: Valid {data.get('@type')} Schema")
        if data.get('@type') == 'FAQPage':
            print(f"  Entities: {len(data.get('mainEntity', []))} Questions")
            for q in data.get('mainEntity', []):
                print(f"   - Question: {q['name']}")
    except Exception as e:
        print(f"\nBlock {idx}: INVALID JSON-LD - {e}")
