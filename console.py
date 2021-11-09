import pdb 
from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository 
import repositories.album_repository as album_repository
import os


os.system('psql -d task_manager -f db/task_manager.sql')

pdb.set_trace()