import requests

class anonymfile:
    def __init__(self):
        self.headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
        self.api_upload = 'https://anonymfile.com/api/v1/upload'

    def upload(self,file_path):
        res = requests.post(self.api_upload,headers=self.headers,files={'file': open(file_path, 'rb')}).json()
        try:
            status = res['status']
            if status:
                url = res['data']['file']['url']['short']
                name = res['data']['file']['metadata']['name']
                new_res = {'name': name,'url': url}
        except:
            status = res.get('status', False)
            if not status:
                print('upload fail!')
            new_res = {}
        return new_res