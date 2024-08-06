#!/usr/bin/env python3
import sys

# Reducer function
def reducer():
    current_anime = None
    current_sum = 0
    current_count = 0
    anime_ratings = []

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
                anime_ratings.append((current_anime, average_rating))
            current_anime = anime_title
            current_sum = rating
            current_count = 1

    if current_anime:
        average_rating = current_sum / current_count
        anime_ratings.append((current_anime, average_rating))

    # Sort the anime by average rating in descending order
    anime_ratings.sort(key=lambda x: x[1], reverse=True)
    # Print the sorted results
    for anime_title, average_rating in anime_ratings:
        print(f"{anime_title}\t{average_rating:.2f}")

if __name__ == "__main__":
    reducer()
