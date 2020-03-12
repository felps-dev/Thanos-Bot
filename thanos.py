import facebook
from random import randint
import time
from google_images_download import google_images_download
PAGE_ID = ''
TOKEN_ID = ''
graph = facebook.GraphAPI(TOKEN_ID, version="3.1")
cel_names = open('cele.txt').readlines()
cel_ar = []
while 1 == 1:
    cel_ar = open('celear.txt')
    cear_list = cel_ar.readlines()
    found_cel = False
    while not found_cel:
        found_cel = True
        cel_name = (cel_names[randint(0,len(cel_names) - 1)].split(',')[1])
        for cear in cear_list:
            if cel_name == cear:
                found_cel = False
    cel_ar.close;
    response = google_images_download.googleimagesdownload()
    arguments = {"keywords":cel_name,"limit":1, "no_directory":"true"}
    paths = response.download(arguments)[cel_name][0]
    photo = open(paths, "rb")
    graph.put_photo(parent_object=PAGE_ID, connection_name='feed', message=cel_name, image=photo.read())
    cel_ar = open('celear.txt', 'a')
    cel_ar.write(cel_name)
    cel_ar.close;
    time.sleep(3600)
