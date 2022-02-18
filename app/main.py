from datetime import datetime
import speedtest
import math
from datetime import datetime

now = datetime.now()

st = speedtest.Speedtest()

dl = math.ceil(st.download()/1024/1024)
ul = math.ceil(st.upload()/1024/1024)

print(now,":",dl,":",ul)