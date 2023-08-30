System Available storage space check:
Use shutil (sh util module) disk_usage method
```Python
import shutil
du = shutil.disk_usage("/")
print(du) # usage(total=1254879230064, used=11327320064, free=107742113792)
du.free/du.total*100

import psutil # For CPU Usage
psutil.cpu_percentage(0.1) # Finding Current CPU Usage with input 0.1 seconds
#each time this above line execute, gives different values like 0.0, 4.3, 4.9, 2.5, 5.0
#If we check for 0.5 sec, we get 0.5, 1.0, 0.5, 1.0, this because we give more seconds, Computer will average use. So its mostly same. No huge  ups and downs.
