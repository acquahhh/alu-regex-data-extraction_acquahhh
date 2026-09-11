# ALU Regex Data Extraction

## What it does
Extracts emails, credit card numbers, phone numbers, and hashtags from a messy support-ticket log using regex. Validates ALU email domains and credit card numbers (Luhn algorithm), and outputs verified/masked results as JSON.

## How to run
cd src
python3 main.py

Output is written to ../output/sample-output.json

## Data types implemented
- **Emails** (required)
- **Credit cards** (required)
- **Phone numbers** (chosen)
- **Hashtags** (chosen)

## Regex approach
- **Emails**: local-part + `@` + repeating (label + dot) domain segments in a non-capturing group, ending in a letters-only TLD — this prevents empty-label domains like `alueducation..cc` from matching.
- **Credit cards**: four groups of four digits with optional space/dash separators, validated further with a Luhn checksum; only Luhn-valid numbers appear in output, masked to the last 4 digits.
- **Phone numbers**: optional country code, optional parenthesized area code, three digit groups with flexible separators, optional extension. Card-shaped text is stripped from the input before phone matching to avoid false positives from overlapping digit patterns.
- **Hashtags**: `#` followed by a required leading letter (excluding ticket-number references like `#4471`), then word characters, using a negative lookbehind so a mid-word `#` (e.g. `price#1`) isn't matched.

## Security considerations
- ALU email domains are verified with an anchored suffix check (`.alueducation.com`), not a naive substring match — this rejects spoofed domains like `alueducation.com.evil.net` and `evilalueducation.com`.
- All patterns avoid nested/ambiguous quantifiers (e.g. `(a+)+`) to prevent ReDoS.
- Injection-style input in the sample data (`<script>...`, `DROP TABLE`) produces no valid extracted matches, showing malicious/malformed input isn't treated as structured data.
- Credit card numbers are masked in output (`**** **** **** 1234`) — only the last 4 digits are ever shown.

## Known limitations
- Phone number regex is a best-effort match across multiple international formats; some unusual formats may not be caught perfectly.
