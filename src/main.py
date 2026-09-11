import re
import json

# Load raw text from input file
with open("../input/raw-text.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

# --- Regex patterns go here ---
# Domain requires a letter/digit/hyphen before each dot, so two dots in a row (like "alueducation..cc") won't match
email_pattern = re.compile(r"[a-zA-Z0-9._+-]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]+")
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

alu_domains = ("alueducation.com", "alumni.alueducation.com", "si.alueducation.com")

def is_alu_email(email):
    domain = email.split("@")[-1]
    return domain in alu_domains or any(domain.endswith("." + d) for d in alu_domains)

alu_verified = [e for e in test_emails if is_alu_email(e)]
print(alu_verified)


card_pattern = re.compile(r"\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b")
test_cards = card_pattern.findall(raw_text)
print(test_cards)

def luhn_check(card_number):
    digits = [int(d) for d in card_number if d.isdigit()]
    checksum = 0
    reverse_digits = digits[::-1]
    for i, d in enumerate(reverse_digits):
        if i % 2 == 1:
            d *= 2
            if d > 9:
                d -= 9
        checksum += d
    return checksum % 10 == 0

def mask_card(card_number):
    digits = [d for d in card_number if d.isdigit()]
    last4 = "".join(digits[-4:])
    return f"**** **** **** {last4}"

valid_cards = []
for card in test_cards:
    if luhn_check(card):
        valid_cards.append(mask_card(card))

print(valid_cards) 

hashtag_pattern = re.compile(r"(?<!\w)#[a-zA-Z]\w*") 
test_hashtags = hashtag_pattern.findall(raw_text)
print(test_hashtags)


text_without_cards = card_pattern.sub("[CARD]", raw_text)

phone_pattern = re.compile(r"(?:\+\d{1,3}[-.\s]?)?\(?\d{2,4}\)?[-.\s]?\d{3,4}[-.\s]?\d{2,4}(?:\s?(?:ext\.?|x)\s?\d+)?")
test_phones = phone_pattern.findall(text_without_cards)
print(test_phones)


results = {
    "emails": test_emails,
    "alu_emails_verified": alu_verified,
    "credit_cards_masked": valid_cards,
    "hashtags": test_hashtags,
    "phone_numbers": test_phones
}

with open("../output/sample-output.json", "w") as f:
    json.dump(results, f, indent=2)

print("Extraction complete. Results written to ../output/sample-output.json")
