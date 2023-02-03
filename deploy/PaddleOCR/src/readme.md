
> 注：当前项目为 Serverless Devs 应用，由于应用中会存在需要初始化才可运行的变量（例如应用部署地区、服务名、函数名等等），所以**不推荐**直接 Clone 本仓库到本地进行部署或直接复制 s.yaml 使用，**强烈推荐**通过 `s init ` 的方法或应用中心进行初始化，详情可参考[部署 & 体验](#部署--体验) 。

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

PaddleOCR 是百度开源的 PaddlePaddle 项目，基于 PaddleOCR，可以快速实现通用 OCR 能力

</description>

<codeUrl>

- [:smiley_cat: 代码](https://github.com/duolabmeng6/paddlehub_ppocr/tree/master/deploy/PaddleOCR)

</codeUrl>
<preview>



</preview>


## 前期准备

使用该项目，您需要有开通以下服务：

<service>



| 服务 |  备注  |
| --- |  --- |
| 函数计算 FC |  创建函数，承载核心业务逻辑 |
| 容器镜像服务 CR |  通过容器镜像进行产物交付 |

</service>

推荐您拥有以下的产品权限 / 策略：
<auth>



| 服务/业务 |  权限 |  备注  |
| --- |  --- |   --- |
| 函数计算 | AliyunFCFullAccess |  创建函数等，功能和新模块 |
| 函数计算 | AliyunContainerRegistryFullAccess |  该应用通过容器镜像进行交付； |

</auth>

<remark>



</remark>

<disclaimers>

免责声明：   
本项目采用了 PaddleOCR 项目实现，在使用时请遵循开源项目 PaddleOCR 的相关规范和要求

</disclaimers>

## 部署 & 体验

<appcenter>
   
- :fire: 通过 [Serverless 应用中心](https://fcnext.console.aliyun.com/applications/create?template=PaddleOCR) ，
  [![Deploy with Severless Devs](https://img.alicdn.com/imgextra/i1/O1CN01w5RFbX1v45s8TIXPz_!!6000000006118-55-tps-95-28.svg)](https://fcnext.console.aliyun.com/applications/create?template=PaddleOCR) 该应用。
   
</appcenter>
<deploy>
    
- 通过 [Serverless Devs Cli](https://www.serverless-devs.com/serverless-devs/install) 进行部署：
  - [安装 Serverless Devs Cli 开发者工具](https://www.serverless-devs.com/serverless-devs/install) ，并进行[授权信息配置](https://docs.serverless-devs.com/fc/config) ；
  - 初始化项目：`s init PaddleOCR -d PaddleOCR `
  - 进入项目，并进行项目部署：`cd PaddleOCR && s deploy - y`
   
</deploy>

## 应用详情

<appdetail id="flushContent">

PaddleOCR 旨在打造一套丰富、领先、且实用的OCR工具库，助力使用者训练出更好的模型，并应用落地。PaddleOCR 项目地址:  https://github.com/PaddlePaddle/PaddleOCR

我们把 PaddleOCR 服务打包成一个镜像，以便在 Docker 或 k8s 环境里，快速发布到线上使用。

通过本应用，您可以部署一个 OCR 识别应用，效果如下：

![](http://image.editor.devsapp.cn/evBw7lh8ktv6xDBzSSzvjr1ykchAF9hG41gf1ek1sk8tr4355A/fbGf9C9yCeG98qetk69v.png)

通过对该应用的部署，您可以获得到：
1. 一个OCR识别的 API
2. 一个测试 OCR 识别效果的测试页面

</appdetail>

## 使用文档

<usedetail id="flushContent">

项目部署完成会出现系统分配的域名地址，该域名地址可作为 API 地址。

例如，在应用中心完成业务功能部署：

![](http://image.editor.devsapp.cn/evBw7lh8ktv6xDBzSSzvjr1ykchAF9hG41gf1ek1sk8tr4355A/By5yx1ASkD94ud5vBhyg.png)

可以看到测试域名，通过该测试域名可以快速体验该应用：

![](http://image.editor.devsapp.cn/evBw7lh8ktv6xDBzSSzvjr1ykchAF9hG41gf1ek1sk8tr4355A/GBecZA4q7GaExZA1aaA4.png)

除此之外，还可以通过该接口进行使用，与自身的业务逻辑进行结合：


接口地址：`http://系统下发的域名信息/predict/ocr_system`

参数：
- Headers:
  - Content-type: `application/json`
- Body: `{"images":["图片Base64后的字符串"]}`


以Python 语言为例，测试代码可以是：
    
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

</usedetail>


<devgroup>


## 开发者社区

您如果有关于错误的反馈或者未来的期待，您可以在 [Serverless Devs repo Issues](https://github.com/serverless-devs/serverless-devs/issues) 中进行反馈和交流。如果您想要加入我们的讨论组或者了解 FC 组件的最新动态，您可以通过以下渠道进行：

<p align="center">  

| <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407298906_20211028074819117230.png" width="130px" > | <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407044136_20211028074404326599.png" width="130px" > | <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407252200_20211028074732517533.png" width="130px" > |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| <center>微信公众号：`serverless`</center>                                                                                         | <center>微信小助手：`xiaojiangwh`</center>                                                                                        | <center>钉钉交流群：`33947367`</center>                                                                                           |
</p>
</devgroup>
