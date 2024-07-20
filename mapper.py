#!/usr/bin/env python3
import sys
import csv

# Mapper function
def mapper():
    reader = csv.reader(sys.stdin)
    next(reader)  # Skip header row
    for row in reader:
        if len(row) == 5:
            anime_title, rating = row[3], row[4]
            if rating != 'rating':
                try:
                    rating = float(rating)
                    print(f"{anime_title}\t{rating}")
                except ValueError:
                    continue

if __name__ == "__main__":
    mapper()
