import numpy as np
import requests
from termcolor import cprint

#You can change these
CONFIGPATH = "./config"

Channels = np.loadtxt(CONFIGPATH,dtype="str")
for channel in Channels:
    r = requests.get("https://twitch.com/"+channel)
    if "isLiveBroadcast" in r.text:
        cprint (channel + " : Live", 'green', attrs=['bold'])
    else:
        cprint(channel + " : Offline", 'red')
