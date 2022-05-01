# 快速部署通用文字识别 PaddleOCR

大家可以通过本项目提供的镜像，把 PaddleOCR 快速发布成可调用的Restful API服务。

# 部署方法

# 1. 在阿里云函数计算应用中心里立即创建

# 2. 终端上输入命令创建

```shell

s init PaddleOCR  # 初始化项目
s deploy  # 部署项目

```

输入 `s init PaddleOCR` 后进入项目

输入 `s deploy` 部署项目

出现 domain 即可为识别的api地址

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

# 本应用的镜像开发教程

https://github.com/duolabmeng6/paddlehub_ppocr

阅读本文你将学会：

在 Serverless 架构中 docker 镜像制作的最佳实践，游刃有余的部署复杂场景下的深度学习模型

熟练的使用各厂商提供的 Serverless 服务，部署。

制作小巧精良的 docker 镜像