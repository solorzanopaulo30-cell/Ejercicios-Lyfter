
def read_songs(path):
    with open(path, "r") as file:
        songs = file.readlines()
    return songs


def print_songs(song_list):
    for number, song in enumerate(song_list, start=1):
        print(number, song.strip())


def sort_songs(output_path, songs):
    songs.sort()
    songs = "".join(songs)
    with open(output_path, 'w') as file:
        file.write(songs)


def main():
    song_list = read_songs("songs.txt")
    print_songs(song_list)
    sort_songs('sorted_songs.txt', song_list)


if __name__ == '__main__':
    main()