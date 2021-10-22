#!/usr/bin/python3
#!/usr/bin/env python
import sys

page_rank=0
prevdest=None

for line in sys.stdin:
    dest,contribution = line.split(",")
    dest = int(dest.strip())
    try:
    	contribution=float(contribution.strip())
    except:
    	continue
    
    if dest==prevdest or prevdest is None:
        page_rank+=contribution
    else:
        rank=0.150 +0.850*page_rank
        print(prevdest,round(rank,2),sep=',')
        page_rank=contribution
    prevdest=dest

rank=0.15+0.85*page_rank
print(prevdest,round(rank,2),sep=',')
