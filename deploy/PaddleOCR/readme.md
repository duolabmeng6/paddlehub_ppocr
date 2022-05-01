# PaddleOCR 帮助文档

<p align="center" class="flex justify-center">
    <a href="https://www.serverless-devs.com" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=PaddleOCR&type=packageType">
  </a>
  <a href="http://www.devsapp.cn/details.html?name=PaddleOCR" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=PaddleOCR&type=packageVersion">
  </a>
  <a href="http://www.devsapp.cn/details.html?name=PaddleOCR" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=PaddleOCR&type=packageDownload">
  </a>
</p>

<description>

> ***PaddleOCR 是百度开源的 PaddlePaddle 项目，基于 PaddleOCR，可以快速实现通用 OCR 能力***

</description>

<table>

## 前期准备
使用该项目，推荐您拥有以下的产品权限 / 策略：

| 服务/业务 | 函数计算 |     
| --- |  --- |   
| 权限/策略 | AliyunFCFullAccess</br>AliyunContainerRegistryFullAccess |     



</table>

<codepre id="codepre">

# 代码 & 预览

- [:smiley_cat: 源代码](https://github.com/duolabmeng6/paddlehub_ppocr)

        

</codepre>

<deploy>

## 部署 & 体验

<appcenter>

- :fire: 通过 [Serverless 应用中心](https://fcnext.console.aliyun.com/applications/create?template=PaddleOCR) ，
[![Deploy with Severless Devs](https://img.alicdn.com/imgextra/i1/O1CN01w5RFbX1v45s8TIXPz_!!6000000006118-55-tps-95-28.svg)](https://fcnext.console.aliyun.com/applications/create?template=PaddleOCR)  该应用。 

</appcenter>

- 通过 [Serverless Devs Cli](https://www.serverless-devs.com/serverless-devs/install) 进行部署：
    - [安装 Serverless Devs Cli 开发者工具](https://www.serverless-devs.com/serverless-devs/install) ，并进行[授权信息配置](https://www.serverless-devs.com/fc/config) ；
    - 初始化项目：`s init PaddleOCR -d PaddleOCR`   
    - 进入项目，并进行项目部署：`cd PaddleOCR && s deploy -y`

</deploy>

<appdetail id="flushContent">

# 应用详情


项目部署完成会出现 domain 即可为api识别的api地址

例如: http://asc.ccc.xxxx.cn-shenzhen.fc.devsapp.net/predict/ocr_system

可以通过以下方式调用：
    
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
   

</appdetail>

<devgroup>

## 开发者社区

您如果有关于错误的反馈或者未来的期待，您可以在 [Serverless Devs repo Issues](https://github.com/serverless-devs/serverless-devs/issues) 中进行反馈和交流。如果您想要加入我们的讨论组或者了解 FC 组件的最新动态，您可以通过以下渠道进行：

<p align="center">

| <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407298906_20211028074819117230.png" width="130px" > | <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407044136_20211028074404326599.png" width="130px" > | <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407252200_20211028074732517533.png" width="130px" > |
|--- | --- | --- |
| <center>微信公众号：`serverless`</center> | <center>微信小助手：`xiaojiangwh`</center> | <center>钉钉交流群：`33947367`</center> | 

</p>

</devgroup>





