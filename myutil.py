import sys
import os
import time

import Image # PIL
 
def save_or_show(img, outfile=None):
    if outfile:
        img.save(outfile)
    else:
        outfile = "myutil_tmp.png"
        img.save(outfile)
        os.system("open %s" % outfile)
        time.sleep(1)
        os.system("rm -f %s" % outfile)
