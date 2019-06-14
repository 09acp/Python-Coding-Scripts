# Author: https://dzone.com/articles/simple-examples-of-downloading-files-using-python

# pip install urllib3
import urllib3, shutil
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/daily-min-temperatures.csv"
c = urllib3.PoolManager()
filename = "temps.txt"
with c.request('GET', url, preload_content=False) as res, open(filename, 'wb') as out_file:
    shutil.copyfileobj(res, out_file)
