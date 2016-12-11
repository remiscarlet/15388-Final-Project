from PIL import Image
import numpy as np

def crop_and_scale_image(inp, minimum=75, isPath=True):
    print "Normalizing", inp
    if isPath:
      im = Image.open(path)
    else:
      im = inp

    arr = np.asarray(im)
    width,height = len(arr[0]), len(arr)
    shorter = min(width,height)
    longer = max(width,height)
    if shorter < minimum:
      return None
    diff = longer-shorter
    cropLAndR = (width > height)
    if shorter < minimum:
        return None
    
    if cropLAndR:
        top = 0
        bot = height
        left = diff/2
        right = left+height
    else:
        top = diff/2
        bot = top+width
        left = 0
        right = width
    #print (left,top,right,bot)
    cropped = im.crop((left,top,right,bot))
    cropped = cropped.convert("L")
    return cropped.resize((minimum,minimum), resample=Image.ANTIALIAS)

import os, sys
def main():
  basePath = "females_cleaned-v1/"
  newPath = basePath[:-1]+"_normalized/"
  if not os.path.isdir(newPath):
    os.mkdir(newPath)
  validExt = ["png", "jpg"]
  files = map(lambda path: basePath+path, os.listdir(basePath))
  for filepath in files:
    if filepath.split(".")[-1] in validExt:
      changed = crop_and_scale_image(filepath)
      if changed == None:
        continue
      newName = filepath.replace(basePath,newPath).split(".")
      newName[-2] = newName[-2]+"_normalized"
      newName = ".".join(newName)
      changed.save(newName)

if __name__ == "__main__":
  main()
