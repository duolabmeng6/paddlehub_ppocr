[toc]

# 基于 Serverless 架构部署通用文字识别 PaddleOCR

# 项目背景

PaddleOCR 旨在打造一套丰富、领先、且实用的OCR工具库，助力使用者训练出更好的模型，并应用落地。

PaddleOCR 项目地址: https://github.com/PaddlePaddle/PaddleOCR

# 开箱即用

这里提供了可开箱即用的docker镜像 可直接用于部署到本地或函数计算中

## 部署 PaddleOCR 到本地

```
docker run -itd --name ppocr -p 9000:9000 duolabmeng666/paddlehub_ppocr:1.0 /bin/bash -c "sh /PaddleOCR/start.sh"
```

## 调用 OCR

```
curl -H "Content-Type:application/json" -X POST --data "{\"images\": [\"iVBORw0KGgoAAAANSUhEUgAAAHkAAAAnCAYAAAArfufOAAAEvElEQVR4nO1bMWsbSRT+clyv4sAWGAS5wpUN8UGuSmlQEBHpsp0LgZy4cOkuwhHqrDKFkERcpMqWQZcgkRQurrJBNifjwo3BYEcSpNAv2Huzu5JWu7Pe2dWubDLzNV7P7r5987733rx5Yz8yCFD4pfHbfSugkDwUyRJAkSwBFMkSQJEsARTJEkCRLAEUyRJAkSwBFMkSQJEsAbwkn+nQdqo4PBN4W+jZATrlKrTydww5d4dfGyRDx7mgwg8Vsc+D2bbZE/tuwHO/x6WTL/o9/NsHVvPrWIoqg024fj2XGtnXeyg8mf7OjLPbGoWWs5rfQiW3LPSs8DfSG3i/vzljn/MTmm/3mhznAqWahjXee2QXS/4FOdc6/xmMSe5/R6l8ikvHjU69io7QVJzPplDY30Y27VC2xeRmUGKGsclyGzwQTzToNb+bLFN8xCG8hgpGxt+AHvRwuNPGVSj5wd84b1ZRufWOrxX3oNv2quw0PHY19WGOz3EQNyyS05uo1DatkTBEBD1LzqN3WRSJGtImrM+uvQ4jHZhzvyYbfwZWZm4wO7UpsMiBBBw7wXRNitQpisnTdn2dpYd/zHQzIm+twiJ2D++7LM0lp9kU1/Z3xbHquPam49FUHs279DS8Rn4pvlLm6cnR/6/n0IvrM0O+JIdJ11ycHVkRyYnEqewMCvkU0ErNpDSrQEthJfEoni9dL+W2oeesazPtdmflMcLCwinTg4jLnS/JYdK1B2yNd4671nyn7CiGeHjo4bjrd08gWyTszAmkaztNU9oooW0VFeM1P4YqOV7Ml64nOLuYZL1jiujjp84AiVZ4xYn40zXbMrFKl9aFYbMdXbOFIJ7qmm13VtMpXPavcXVLP+sNrFDRuBGvspERf7pmUbtvXfKaH8EY4PSECo/0n9H31YuEuYPI4Fl+hMtWBtq+BrDoLOtUb4QR5NxZ3I3AAHRtq5JvhojCs26H3fNGwfzpmvUBkN+iqP08GVsrbqHQPAJuwkheRpZ2Flnf+1MnCNOQYXg4JDv36gvDnOmaMplZURfJ4F+dN4iwomYVld2YCi97t5LNb+CqdYTznKjeNsm8vVm0jhe4+7RIsCP7cdju2AIxvB1Rxtk2je2/NMVReE27Wy9ymxje0DvNnrCdTZLv3JvdF/o/zdT9OFaZ7vbtKHS6RusjNLNRY3XkConv5b3drSW2HFDq1poQIvrOdG15mbs3OkevOP0HrWmzhZqfg7EoYVHwd5xRfC9LwjwYr8PMoZzZgK3fz3FDy4cI0dzzZOvYjAgGpV4OkRuUQvWXP7FLz2g7DXQEKkIT6WUzMjsnQUdodruTnGIRFTZzZt6R6Xjc75g0UZjHuHYw1Xg9/HUUahTRt+1ADh5N/xfKUcKHWVcnKZBzAsXLBKINEXsbgIhHgjxMq1KriOq4xof9AZbSnKrVpTNve2nVNSlPWzP0UaPjW8Lty8k7Poc6jOTBl7rx6s2B8eHUiI4f34y3JOPtl/5kqNc4MF69+2YM5hAbL/pG+92BOVennqFgz9M9L8uGn4xewJgbUxv9Z3xgct/UjfaPaKqNeXR/0xHJCr8q1N94SQBFsgRQJEsARbIEUCRLAEWyBFAkSwBFsgT4HxQ8/CE4B3ErAAAAAElFTkSuQmCC\"]}" http://127.0.0.1:9000/predict/ocr_system
```

```
{"msg":"","results":[[{"confidence":0.9853195548057556,"text":"测试图像路径，可以是单张图片路径，也可以是图像集合目录路径","text_region":[[5,10],[466,10],[466,24],[5,24]]}]],"status":"000"}
```

## 调用OCR代码示例

https://github.com/duolabmeng6/paddlehub_ppocr/tree/master/demo

![1](README.assets/1.png)


```python
import requests
from pyefun import *
from pyefun.encoding.ebase64 import *

# 用 docker 部署 PaddleOCR 开箱即用 通用文字识别
# https://github.com/duolabmeng6/paddlehub_ppocr

def ocr(文件地址):
    image = base64编码(读入文件(文件地址))
    data = '{"images":["' + image + '"]}'
    txt = requests.post("http://127.0.0.1:9000/predict/ocr_system", data=data,
                        headers={'Content-Type': 'application/json'})
    return txt.content.decode("utf-8")

print(ocr("./test.png"))

```

## 阿里云函数计算部署

启动命令 `["sh","/PaddleOCR/start.sh"]`

需要绑定域名

## 腾讯云函数无法部署

原因 腾讯云云函数容器镜像部署无法写文件导致容器无法正常启动.

容器内文件读写权限

* 默认/tmp可读可写，建议输出文件时选择/tmp。
* 避免使用其他用户的存在限制访问或执行的文件。
* 容器内文件可写层存储空间限制为512M。


# 项目开发

使用 [PaddleHub Serving 的服务部署](https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.2/deploy/hubserving/readme.md) PaddleOCR

步骤如下：

1. 构建飞浆的运行环境
2. 用 PaddleHub Serving 的服务部署 .
3. 将 PaddleOCR 项目下载回来，编写 Dockerfile 文件
4. 在 Serverless 架构的中部署

# docker中构建飞浆的运行环境

## 1.构建 python3.7 运行环境

新建以下文件和目录
```
/test_ppocr
-- PaddleOCR (https://github.com/PaddlePaddle/PaddleOCR 项目的文件)
-- Dockerfile (docker 构建的文件)

```

```shell
# 创建 python 的基础的运行环境
docker run -itd --name testppocr -p 9000:9000 -v /test_ppocr:/test_ppocr python:3.7.10-slim /bin/bash #
# 进入容器内安装飞浆的运行环境
docker exec -it testppocr /bin/bash 
```
## 2. 安装依赖

```shell
apt install g++
apt install libglib2.0-dev
apt install libgl1-mesa-glx
apt install libsm6
apt install libxrender1

# 离线下载 python 安装包 由于构建时经常重试所以下载离线包调试速度会加快
pip download -r requirements.txt -d ./pg
pip download paddlepaddle==2.0.2 -i https://mirror.baidu.com/pypi/simple -d ./pg
pip download paddlehub -d ./pg

# 安装 python 包
pip install -r requirements.txt --find-links ./pg
pip install paddlepaddle --find-links ./pg
pip install paddlehub -U --no-index --find-links ./pg

```

用 PaddleHub Serving 的服务部署

```shell
hub install deploy/hubserving/ocr_system/
hub install deploy/hubserving/ocr_cls/
hub install deploy/hubserving/ocr_det/
hub install deploy/hubserving/ocr_rec/
```

到这里 PaddleHub Serving 运行环境就安装好了 运行起来看一下效果 

```shell
hub serving start --modules ocr_system ocr_cls ocr_det ocr_rec -p 9000
```

测试没问题 到这里运行镜像就构建好了

将容器内无用文件删除减小容器的体积

```shell
rm -rf /root/.cache/* \
&& rm -rf /var/lib/apt/lists/* \
&& rm -rf /app/test/pg/*
```


# 在 Serverless 架构的中部署

需要将docker镜像推送至对应平台的镜像仓库中

这里以阿里云容器镜像仓库作为例子

请自行修改参数推送，这里是我的账户命令

```shell
docker commit testppocr paddlehub_ppocr:1.0
docker tag paddlehub_ppocr:1.0 registry.cn-hongkong.aliyuncs.com/llapi/ppocr:1.0
docker push registry.cn-hongkong.aliyuncs.com/llapi/ppocr:1.0
```

## 部署到阿里云函数计算

容器镜像地址 `registry.cn-hongkong.aliyuncs.com/llapi/ppocr:1.0`
启动命令 `["sh","/PaddleOCR/start.sh"]`
需要绑定域名

![2](README.assets/2.png)
![2](README.assets/3.png)

识别地址就是 http://绑定域名/predict/ocr_system

## 腾讯云函数无法部署

原因 腾讯云云函数容器镜像部署无法写文件导致容器无法正常启动.

容器内文件读写权限

* 默认/tmp可读可写，建议输出文件时选择/tmp。
* 避免使用其他用户的存在限制访问或执行的文件。
* 容器内文件可写层存储空间限制为512M。

# 总结

在 Serverless 架构下部署深度学习模型变得非常简单且能提供无限的并发支持，我们可以将镜像部署到各个提供 Serverless 的服务商中。

# 学习交流

pyefun 易函数 qq群:1017240979

# 项目相关

pyefun 易函数 https://github.com/duolabmeng6/pyefun

为python提供强大且易用的中文函数库，完整的封装了易语言核心支持库所有功能，以及易语言中简单易用的函数
