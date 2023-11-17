def count_favourite_singers(n, songs):
    singer_count = {}

    # Count the occurrences of each singer
    for singer in songs:
        singer_count[singer] = singer_count.get(singer, 0) + 1

    # Find the maximum count
    max_count = max(singer_count.values())

    # Count the number of singers with the maximum count
    favourite_singers = sum(count == max_count for count in singer_count.values())

    return favourite_singers


if __name__ == "__main__":
    n = int(input().strip())
    songs = list(map(int, input().strip().split()))

    result = count_favourite_singers(n, songs)
    print(result)





