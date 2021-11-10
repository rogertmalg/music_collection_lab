import pdb 
from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository 
import repositories.album_repository as album_repository
import os


os.system('psql -d music_collection -f db/music_collection.sql')

artist_1 = Artist("James Blunt")
artist_repository.save(artist_1)

artist_2 = Artist("Dido")
artist_repository.save(artist_2)

artist_3 = Artist("Amy Winehouse")
artist_repository.save(artist_3)

album_1 = Album("Back to Bedlam", "rock", artist_1)
album_repository.save(album_1)

album_2 = Album("No Angel", "rock", artist_2)
album_repository.save(album_2)

album_3 = Album("Back to Black", "rock", artist_3)
album_repository.save(album_3)

artist_albums = artist_repository.albums(artist_3)
for album in artist_albums:
    print(album.__dict__)

find_artist = artist_repository.select(1)
print(find_artist.__dict__)

find_album = album_repository.select(1)
print(find_album.__dict__)

# album_repository.delete(1)

# artist_repository.delete(1)




pdb.set_trace()