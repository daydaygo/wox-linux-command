# encoding=utf8
import requests
import json
import webbrowser
from wox import Wox


class Main(Wox):
    def query(self, query):
        if not query:
            return ""
        if query == 'update':
            r = requests.get(
                'https://raw.githubusercontent.com/jaywcjlove/linux-command/master/dist/data.json')
            with open('lc_data.json', 'w') as f:
                f.write(r.text)
            return [{'Title': 'update success', 'SubTitle': 'update success', 'IcoPath': 'icon.png'}]

        results = []
        with open('lc_data.json', 'r') as f:
            j = json.load(f)
            for k in j:
                if k.find(query) != -1:
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
