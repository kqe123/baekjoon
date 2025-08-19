import math
import time


a = {i for i in range(1,1000001)}

start = time.time()

result = 0
if 999999 in a :
    result += 1
print(result)

end = time.time()

print(f"{end - start:.5f} sec")