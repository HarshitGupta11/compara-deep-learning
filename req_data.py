import os
import pandas
import sys
import urllib.request as urllib
import pandas as pd
import json
import requests
import time

from process_data import create_map_list


lf=[]

def download_data(x,dir_name):
    fname=x.split("/")[-1]
    path=os.path.join(dir_name,fname)
    urllib.urlretrieve(x,path)

def get_data_file(file,dir):
    if not os.path.isfile(file):
        print("The specified file does not exist!!!")
        sys.exit(1)

    with open(file,"r")as f:
        lf=f.read().splitlines()

    if not os.path.exists(dir):
        os.mkdir(dir)
    for x in lf:
        download_data(x,dir)

def download_data_h_post(lsy):
    g=[]
    for x in lsy:
        g.append(str(x))
        xl=lsy[x]['b']
        xr=lsy[x]['f']
        for gxl in xl:
            g.append(str(gxl))
        for gxr in xr:
            g.append(str(gxr))
    assert(len(g)==len(lsy)*5)

    gd=create_map_list(g)

    g={"ids":list(gd.keys())}

    print("Sending post request.............................")


    start=time.time()
    server = "https://rest.ensembl.org"
    ext = "/sequence/id"
    headers={ "Content-Type" : "application/json", "Accept" : "application/json"}
    r = requests.post(server+ext, headers=headers, data=json.dumps(g) )
    end=time.time()

    print("Post request complete...............................")

    print("Time taken:",end-start)

    if not r.ok:
        r.raise_for_status()
        sys.exit()

    return r.json(),gd
