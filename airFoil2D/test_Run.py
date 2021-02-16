import os
from subprocess import call
import linecache
call(['bash', './Allrun'])

u = float(linecache.getline("PARM/parm/u", 1))
v = float(linecache.getline("PARM/parm/v", 1))

print(u)
print(v)

#print(os.environ['u'])
#print(os.environ['v'])

#print(f1)
#print(f2)
