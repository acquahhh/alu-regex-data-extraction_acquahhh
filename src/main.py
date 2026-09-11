import re
import json

# Load raw text from input file
with open("../input/raw-text.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

# --- Regex patterns go here ---
email_pattern = re.compile(r"[a-zA-Z0-9._+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.-]+") 
test_emails = email_pattern.findall(raw_text)
print(test_emails)
# phone_pattern = re.compile(r"...")
# card_pattern = re.compile(r"...")
# hashtag_pattern = re.compile(r"...")

# --- Extraction ---
# emails = email_pattern.findall(raw_text)
# ...

# --- Output ---
# results = {"emails": [...], "phone_numbers": [...], ...}
# with open("../output/sample-output.json", "w") as f:
#     json.dump(results, f, indent=2)
