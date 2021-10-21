#!/usr/bin/python3
#!/usr/bin/env python
import sys

page_rank=0
prevdest=None
prevsource=None
for line in sys.stdin:
    dest, source,contribution = line.split(",")
    source = int(source.strip())
    dest = dest.strip()
    contribution=int(contribution.strip())
    
    if dest==prevdest or prevdest==None:
        page_rank+=contribution
    else:
        rank=0.15+0.85*page_rank
        print(prevsource,",", rank)
        page_rank=contribution
    prevdest=dest
    prevsource=source

rank=0.15+0.85*page_rank
print(prevsource,",", rank)
