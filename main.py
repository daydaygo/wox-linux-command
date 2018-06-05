# encoding=utf8
import requests
import webbrowser
from wox import Wox


class Main(Wox):
    def query(self, query):
        if not query:
            return ""

        r = requests.get(
            'https://unpkg.com/linux-command@1.0.6/dist/data.json')
        j = r.json()
        results = []
        for k in j:
            if k.find(query)!=-1 :
                res = {}
                res["Title"] = j[k]['n']
                res["SubTitle"] = j[k]['d']
                res["IcoPath"] = "icon.png"
                res["JsonRPCAction"] = {
                    "method": "openUrl", "parameters": ['http://wangchujiang.com/linux-command/c' + j[k]['p']]}
                results.append(res)
        return results

    def openUrl(self, url):
        webbrowser.open(url)


if __name__ == "__main__":
    Main()
