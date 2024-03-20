import cv2
import sys
import os

inputdir=sys.argv[1]
outputdir=sys.argv[2]
transform_val=int(sys.argv[3])

for filename in os.listdir(inputdir):
    f = os.path.join(inputdir, filename)
    if os.path.isfile(f):
        img = cv2.imread(f)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        median = cv2.medianBlur(img, transform_val)
        img = median
        outfile = outputdir + '/' + os.path.basename(filename)
        cv2.imwrite(outfile, img)
