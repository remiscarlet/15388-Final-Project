import flickr_api
from flickr_api import Walker
from flickr_api import Photo

search_string = "female portrait"
download_folder = "female_portrait_medium/"
photo_size = "Medium"


flickr_api.set_keys(api_key = '379349b3d19ede46a5324cc98c574fa5', api_secret = 'da768ffaa1899bd')


w = Walker(Photo.search, text=search_string)
print len(w)
counter = 0
for photo in w:
	if (counter < 2000): 
		print photo
		try:
			photo.save(download_folder+photo.id+".jpg", size_label = photo_size)
			print "saved!"
		except:
			print "size not available skipping to next photo"
	counter += 1


