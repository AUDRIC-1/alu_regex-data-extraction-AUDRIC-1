import re

regex_patterns = {
    "emails": r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b",
    "urls": r"\bhttps?:\/\/(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(\/\S*)?\b",
    "phone_numbers": r"\b(?:\(\d{3}\)\s?|\d{3}[-.])\d{3}[-.]\d{4}\b",
    "credit_cards": r"\b(?:\d{4}[-\s]?){3}\d{4}\b"
}

def extract_data(text):
    results = {}
    for label, pattern in regex_patterns.items():
        matches = re.findall(pattern, text)
        results[label] = matches
    return results

if __name__ == "__main__":
    try:
        with open("sample_text.txt", "r") as file:
            text = file.read()
    except FileNotFoundError:
        print("Error: 'sample_text.txt' not found.")
        exit()

    extracted = extract_data(text)

    for label, matches in extracted.items():
        print(f"\n{label.upper()}:")
        for match in matches:
            print(f"  - {match}")

