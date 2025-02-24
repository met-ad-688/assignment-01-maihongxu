#!/bin/bash

FILES=("questions.csv" "question_tags.csv")
TOTAL_COUNT=0

for FILE in "${FILES[@]}"; do

    COUNT=$(grep -i "python" "$FILE" | wc -l)
    TOTAL_COUNT=$((TOTAL_COUNT + COUNT))

done

echo "Total number of lines containing 'python' in all files: $TOTAL_COUNT"

