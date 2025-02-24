import csv

# List of files
files = ["questions.csv", "question_tags.csv"]  # Replace with actual file names

# Initialize counter
count = 0

# Iterate through each file
for file in files:
    with open(file, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        # Iterate through each row
        for row in reader:
            if any("github" in str(cell) for cell in row):
                count += 1

print(f"Total lines containing 'GitHub': {count}")
