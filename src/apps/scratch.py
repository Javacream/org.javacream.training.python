import sys

sys.path.append('/home/rainersawitzki/git/org.javacream.training.python/src/apps/postalcode')
#print(sys.modules)
print(sys.path)

dir(sys)

#import postalCodes
#print(dir (postalCodes))

#postalCodes.__hidden__()

from postalCodes import *

add()
__hidden__()

