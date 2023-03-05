def make_album(artist,title):
    """This function will create a album dictionary with artist name and title"""
    album = {'artist':artist,'title':title}
    return album

album = make_album('Foo Fighters', 'Wasting Light')
print(album)

album = make_album('Avenge Sevenfold', 'Nightmare')
print(album)

album = make_album('Kings of Leon', 'Only by the night')
print(album)
