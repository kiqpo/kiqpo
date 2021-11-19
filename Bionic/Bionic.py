#!/usr/bin/env python3
import sys
import shutil
import os
import Bionic
import requests
import zipfile


def CORE():
    global cmdNow
    cmdNow = ""
    global allagr
    allagr = []
    print(f"Arguments count: {len(sys.argv)}")
    for i in range(len(sys.argv)):
        if len(sys.argv) > 1:
            allagr.append(sys.argv[i])
        else:
            pass
    allagr.pop(0)
    cmdNow = ' '.join(map(str, allagr))

    # print(cmdNow)
    # print(allagr)

    def create(projct_name="Bionic"):
        url = 'https://api.github.com/repos/bionic-py/Bionic/releases'

        res = requests.get(url, allow_redirects=True)
        res_json = res.json()

        ZipFileUrl = (res_json[0]["zipball_url"])

        ZipFileData = requests.get(ZipFileUrl, allow_redirects=True)

        open(projct_name, 'wb').write(ZipFileData.content)
        with zipfile.ZipFile(projct_name, 'r') as zip_ref:
            zip_ref.extractall('./')
            os.remove(projct_name)
            ListFIle = os.listdir('./')
            os.rename(ListFIle[0], projct_name)

    if cmdNow.find("create") != -1:
        create()


# Bionic create projct_name
# python3 Bionic.py Bionic create projct_name
if __name__ == '__main__':
    CORE()
