#!/usr/bin/python3
#!/usr/bin/env python
import sys
source_list=[]
one=1

f=open('v.txt','w')
prevsource=None
for line in sys.stdin:
    source, dest = line.split(",")
    source = source.strip()
    dest = dest.strip()
    
    if source==prevsource or prevsource==None:
        source_list.append(dest)
    else:
        print(prevsource,source_list)
        f.write(prevsource + ", 1\n")
        source_list.clear()
        source_list.append(dest)
    prevsource=source

print(prevsource,source_list)
f.write(prevsource + ", 1\n")