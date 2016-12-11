from PIL import Image
import os

def resizer(data, width, height):
  return data.resize((width,height), resample=Image.ANTIALIAS)


def main():
  width = 50
  height = 50
  base = "male_cropped_normalized-flickr"
  files = os.listdir(base)
  files = map(lambda path: base+"/"+path, files)
  files = filter(lambda path: path.find("jpg") > -1 or path.find("png") > -1, files)
  for f in files:
    fname = f.split("/")[-1]

    newPath = base+"-resized-{}x{}/".format(width,height)+fname
    folderPath = "/".join(newPath.split("/")[:-1])

    if not os.path.isdir(folderPath):
      os.mkdir(folderPath)

    im = Image.open(f)
    print "Resizing %s" % f
    resized = resizer(im, width, height)
    resized.save(newPath)

if __name__ == "__main__":
  main()
