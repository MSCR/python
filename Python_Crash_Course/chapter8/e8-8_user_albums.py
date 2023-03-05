def make_album(artist,title):
    """This function will create a album dictionary with artist name and title"""
    album = {'artist':artist,'title':title}
    return album

while True:
    print("\nLet's save an music album.")
    print("Enter 'q' to exit.")

    artist = input("\nEnter the name of the artist or group: ")
    if artist == 'q':
        break
    title = input("Enter the title of the album: ")
    if title == 'q':
        break

    album = make_album(artist, title)
    print("\nThis is the information of your album: ")
    print(album)