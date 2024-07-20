#!/usr/bin/env python3
import sys

# Reducer function
def reducer():
    current_anime = None
    current_sum = 0
    current_count = 0

    for line in sys.stdin:
        anime_title, rating = line.strip().split('\t')
        try:
            rating = float(rating)
        except ValueError:
            continue

        if current_anime == anime_title:
            current_sum += rating
            current_count += 1
        else:
            if current_anime:
                average_rating = current_sum / current_count
                print(f"{current_anime}\t{average_rating:.2f}")
            current_anime = anime_title
            current_sum = rating
            current_count = 1

    if current_anime:
        average_rating = current_sum / current_count
        print(f"{current_anime}\t{average_rating:.2f}")

if __name__ == "__main__":
    reducer()
