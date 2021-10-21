import math

similarity= lambda v1, v2 : sum(x*y for x, y in zip(v1, v2)) / (math.sqrt(sum(i*i for i in v1)) * math.sqrt(sum(i*i for i in v2)))
for i in dest:
    sim=similarity(temp[source],temp[i])