import data
import time
tic = time.perf_counter()
while 1:
    c=data.findInSetData('omid')
    data.updateDataBase('ufo',2)
    print(c)
    if c == 1:
        toc = time.perf_counter()
        print(f"Downloaded the tutorial in {toc - tic:0.4f} seconds")
        break
