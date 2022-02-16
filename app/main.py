import speedtest

st = speedtest.Speedtest()

print("Your download speed is: ", st.download()/1024/1024, " Mbit/s.")
print("Your upload speed is: ", st.upload()/1024/1024, " Mbit/s.")