# 快速部署通用文字识别 PaddleOCR

镜像制作教程 https://github.com/duolabmeng6/paddlehub_ppocr

```shell
s init PaddleOCR  # 初始化项目
s deploy  # 部署项目
```

进入项目 输入 s deploy 部署项目 出现 domain 即可为api识别的api地址

例如: http://asc.ccc.xxxx.cn-shenzhen.fc.devsapp.net/predict/ocr_system

# 调用方法
```python

import requests
import base64

def ocr(imagePath):
    with open(imagePath, 'rb') as f:
        data = f.read(-1)
    image = str(base64.b64encode(data), encoding='utf-8')
    data = '{"images":["' + image + '"]}'
    txt = requests.post("http://asc.ccc.xxxx.cn-shenzhen.fc.devsapp.net/predict/ocr_system", data=data,
                        headers={'Content-Type': 'application/json'})
    return txt.content.decode("utf-8")

print(ocr("./test.png"))




```