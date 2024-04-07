import time
import requests
from bs4 import BeautifulSoup as bf 
import fire
import os
import subprocess
# replace your vercel domain
import requests
from agi.base import BaseAGI 

class Suno(BaseAGI):
    def __init__(self, suno_api_path="/mnt/d/workspace/projects/suno-api"):
        """
        checkout https://github.com/gcui-art/suno-api for more details about suno api
        """
        super(self).__init__()
        base_url = 'http://localhost:3000'
        #base_url="http://172.29.12.50:3000"
        import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip=s.getsockname()[0]
        print(local_ip)
        s.close()
        self.base_url=f"http://{local_ip}:3000"
        self.suno_api_path = suno_api_path
        self.start_suno_server()
        return

    def start_suno_server(self):
        status, ret = subprocess.getstatusoutput(f"cd {self.suno_api_path} && npm run dev")
        print(f"cd {self.suno_api_path} && npm run dev" + f"{status}, {ret}")
        if ret != 0:
            raise ValueError("Failed to start suno server")


    def query(self, prompt: str, mode: str) -> Any:
        # return super().query(prompt, mode)
        return self.generate_audio_by_prompt(prompt)
    
    @staticmethod
    def download_audio(url, output_path='./music.mp3'):  
        """  
        从给定的URL下载音频文件，并将其保存到指定的输出路径。  
        
        :param url: 音频文件的URL  
        :param output_path: 要保存音频文件的路径（包括文件名）  
        """  
        response = requests.get(url, stream=True)  
        
        # 检查请求是否成功  
        if response.status_code == 200:  
            # 打开文件以二进制写入模式  
            with open(output_path, 'wb+') as file:  
                # 使用Response.iter_content方法逐块下载文件  
                for chunk in response.iter_content(1024):  
                    file.write(chunk)  
            print(f"音频文件已成功下载到 {output_path}")  
        else:  
            print(f"无法从 {url} 下载音频文件。状态码：{response.status_code}")  

    def custom_generate_audio(self, payload):
        url = f"{self.base_url}/api/custom_generate"
        response = requests.post(url, json=payload, headers={'Content-Type': 'application/json'})
        return response.json()

    def generate_audio_by_prompt(self, payload):
        url = f"{self.base_url}/api/generate"
        response = requests.post(url, json=payload, headers={'Content-Type': 'application/json'})
        print(response)
        print(response.content)
        return response.json()

    def get_audio_information(self.audio_ids):
        url = f"{self.base_url}/api/get?ids={audio_ids}"
        response = requests.get(url)
        return response.json()

    def get_quota_information(self.):
        url = f"{self.base_url}/api/get_limit"
        response = requests.get(url)
        return response.json()
