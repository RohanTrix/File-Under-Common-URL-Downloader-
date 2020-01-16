"""
author: ROHAN SIROHIA aka RohanTrix
"""
import time
import requests
url= "https://sites.math.rutgers.edu/~ajl213/CLRS/Ch"
for i in range(1,25):
    n=url+str(i)+".pdf"
    r = requests.get(n)
    with open("Ch"+str(i)+".pdf", "wb") as code:
        code.write(r.content)
    time.sleep(0.2)
