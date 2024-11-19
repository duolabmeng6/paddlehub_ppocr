# 基于 Serverless 架构部署通用文字识别 PaddleOCR

[![github stars](https://img.shields.io/github/stars/duolabmeng6/paddlehub_ppocr?style=social)](https://github.com/duolabmeng6/paddlehub_ppocr)
[![gitee stars](https://gitee.com/duolabmeng666/paddlehub_ppocr/badge/star.svg?theme=dark)](https://gitee.com/duolabmeng666/paddlehub_ppocr/stargazers)

# 项目背景

在日常项目应用中，相信大家都希望自己项目中的Restful API服务，能够稳健的运行，并且最好拥有高并发，高可用的特性。云厂商提供的 Serverless 服务是最佳的选择。无需运维人员，无需自建 k8s，不需要担心服务崩溃不可用。

PaddleOCR 旨在打造一套丰富、领先、且实用的OCR工具库，助力使用者训练出更好的模型，并应用落地。PaddleOCR 项目地址: https://github.com/PaddlePaddle/PaddleOCR

我们把 PaddleOCR 服务打包成一个镜像，以便在 Docker 或 k8s 环境里，快速发布到线上使用。

本文将提供标准化的代码来实现这样的目标。

大家可以通过本项目提供的镜像，把 PaddleOCR 项目快速发布成可调用的Restful API服务。

阅读本文你将学会：

* 在 Serverless 架构中 docker 镜像制作的最佳实践，游刃有余的部署复杂场景下的深度学习模型
* 熟练的使用各厂商提供的 Serverless 服务，部署。
* 制作小巧精良的 docker 镜像


[docker制作paddleocr镜像部署到函数计算](https://www.bilibili.com/video/BV1iY411P7Dp/) 
[视频的项目资源](https://github.com/duolabmeng6/docker_paddle_ocr)

# 开箱即用

这里提供了开箱即用的 docker 镜像，可直接将 PaddleOCR 部署到本地服务器，阿里云函数计算，腾讯云函数中提供通用文字识别 api 接口。

[阿里云Serverless 应用中心一键体验 PaddleOCR](https://fcnext.console.aliyun.com/applications/create?template=PaddleOCR)

## 1. 部署 PaddleOCR 到本地

[PaddleOCR docker官网的 镜像地址](https://hub.docker.com/repository/docker/duolabmeng666/paddlehub_ppocr)

```shell
# 阿里云的镜像仓库地址
docker run -itd --name ppocr -p 9000:9000 registry.cn-hongkong.aliyuncs.com/llapi/ppocr:1.8 /bin/bash -c "sh /PaddleOCR/start.sh"

# 阿里云的镜像仓库地址 服务器端模型
docker run -itd --name ppocr -p 9000:9000 registry.cn-hongkong.aliyuncs.com/llapi/ppocr:1.6.server /bin/bash -c "sh /PaddleOCR/start.sh"
```

## 调用 OCR

1. 计算待识别图片的Base64编码
2. 发送服务请求（发送参数，参考下面命令）

```
curl -H "Content-Type:application/json" -X POST --data "{\"images\": [\"iVBORw0KGgoAAAANSUhEUgAAAHkAAAAnCAYAAAArfufOAAAEvElEQVR4nO1bMWsbSRT+clyv4sAWGAS5wpUN8UGuSmlQEBHpsp0LgZy4cOkuwhHqrDKFkERcpMqWQZcgkRQurrJBNifjwo3BYEcSpNAv2Huzu5JWu7Pe2dWubDLzNV7P7r5987733rx5Yz8yCFD4pfHbfSugkDwUyRJAkSwBFMkSQJEsARTJEkCRLAEUyRJAkSwBFMkSQJEsAbwkn+nQdqo4PBN4W+jZATrlKrTydww5d4dfGyRDx7mgwg8Vsc+D2bbZE/tuwHO/x6WTL/o9/NsHVvPrWIoqg024fj2XGtnXeyg8mf7OjLPbGoWWs5rfQiW3LPSs8DfSG3i/vzljn/MTmm/3mhznAqWahjXee2QXS/4FOdc6/xmMSe5/R6l8ikvHjU69io7QVJzPplDY30Y27VC2xeRmUGKGsclyGzwQTzToNb+bLFN8xCG8hgpGxt+AHvRwuNPGVSj5wd84b1ZRufWOrxX3oNv2quw0PHY19WGOz3EQNyyS05uo1DatkTBEBD1LzqN3WRSJGtImrM+uvQ4jHZhzvyYbfwZWZm4wO7UpsMiBBBw7wXRNitQpisnTdn2dpYd/zHQzIm+twiJ2D++7LM0lp9kU1/Z3xbHquPam49FUHs279DS8Rn4pvlLm6cnR/6/n0IvrM0O+JIdJ11ycHVkRyYnEqewMCvkU0ErNpDSrQEthJfEoni9dL+W2oeesazPtdmflMcLCwinTg4jLnS/JYdK1B2yNd4671nyn7CiGeHjo4bjrd08gWyTszAmkaztNU9oooW0VFeM1P4YqOV7Ml64nOLuYZL1jiujjp84AiVZ4xYn40zXbMrFKl9aFYbMdXbOFIJ7qmm13VtMpXPavcXVLP+sNrFDRuBGvspERf7pmUbtvXfKaH8EY4PSECo/0n9H31YuEuYPI4Fl+hMtWBtq+BrDoLOtUb4QR5NxZ3I3AAHRtq5JvhojCs26H3fNGwfzpmvUBkN+iqP08GVsrbqHQPAJuwkheRpZ2Flnf+1MnCNOQYXg4JDv36gvDnOmaMplZURfJ4F+dN4iwomYVld2YCi97t5LNb+CqdYTznKjeNsm8vVm0jhe4+7RIsCP7cdju2AIxvB1Rxtk2je2/NMVReE27Wy9ymxje0DvNnrCdTZLv3JvdF/o/zdT9OFaZ7vbtKHS6RusjNLNRY3XkConv5b3drSW2HFDq1poQIvrOdG15mbs3OkevOP0HrWmzhZqfg7EoYVHwd5xRfC9LwjwYr8PMoZzZgK3fz3FDy4cI0dzzZOvYjAgGpV4OkRuUQvWXP7FLz2g7DXQEKkIT6WUzMjsnQUdodruTnGIRFTZzZt6R6Xjc75g0UZjHuHYw1Xg9/HUUahTRt+1ADh5N/xfKUcKHWVcnKZBzAsXLBKINEXsbgIhHgjxMq1KriOq4xof9AZbSnKrVpTNve2nVNSlPWzP0UaPjW8Lty8k7Poc6jOTBl7rx6s2B8eHUiI4f34y3JOPtl/5kqNc4MF69+2YM5hAbL/pG+92BOVennqFgz9M9L8uGn4xewJgbUxv9Z3xgct/UjfaPaKqNeXR/0xHJCr8q1N94SQBFsgRQJEsARbIEUCRLAEWyBFAkSwBFsgT4HxQ8/CE4B3ErAAAAAElFTkSuQmCC\"]}" http://127.0.0.1:9000/predict/ocr_system
```

3. 返回结果（如果调用成功，会返回如下结果）

```
{"msg":"","results":[[{"confidence":0.9853195548057556,"text":"测试图像路径，可以是单张图片路径，也可以是图像集合目录路径","text_region":[[5,10],[466,10],[466,24],[5,24]]}]],"status":"000"}
```

## 调用 OCR 代码示例

[查看调用代码示例](https://github.com/duolabmeng6/paddlehub_ppocr/tree/master/demo)

![1](./demo/1.png)

```python
import requests
import base64

def ocr(文件地址):
    with open(文件地址, 'rb') as f:
        data = f.read(-1)
    image = str(base64.b64encode(data), encoding='utf-8')
    data = '{"images":["' + image + '"]}'
    txt = requests.post("http://127.0.0.1:9000/predict/ocr_system", data=data,
                        headers={'Content-Type': 'application/json'})
    return txt.content.decode("utf-8")

print(ocr("./test.png"))

```


## 2. 部署到阿里云函数计算

非常简单~

 [Serverless 应用中心一键体验 PaddleOCR](https://fcnext.console.aliyun.com/applications/create?template=PaddleOCR)

## 3. 部署到腾讯云函数

比较麻烦请看下面的教程 



# 项目开发

使用 [PaddleHub Serving 的服务部署](https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.2/deploy/hubserving/readme.md)
PaddleOCR

步骤如下：

1. 构建飞桨的运行环境
2. 用 PaddleHub Serving 的服务部署
3. 将 PaddleOCR 项目下载回来，编写 Dockerfile 文件
4. 在 Serverless 架构的中部署

# docker 中构建飞桨的运行环境

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
# 进入容器内安装飞桨的运行环境
docker exec -it testppocr /bin/bash 
```

> 在部署深度学习模型时， docker 中 python 环境不建议使用 alpine 版本 例如 `python:3.7-alpine` 原因使用 alpine 版本，需要花费大量时间来安装系统依赖，收益不大，最终镜像的大小，与 slim 版本的基本相同。如果环境难以安装也可以选择 `python:3.7-buster` 镜像，最终制作完成通常比 slim 大100MB-300MB，但安装难度会极大地降低，也是可以接受的。推荐新手使用 buster 版本制作镜像。如需体积较小的镜像时再用 slim 版本制作。在 Serverless 环境中需要体积较小的镜像来提高函数的启动速度，所以选择 slim 版本制作镜像。

## 2. 安装依赖

> 确定系统需要什么依赖，是通过代码运行来确定的。`docker exec -it testppocr /bin/bash` 进入运行好的基础环境，进入容器内终端后，运行你的代码，确定所需要安装的依赖。 

`requirements.txt ` 这里需要注意依赖包的版本，否则版本太高了会失败。建议固定版本，防止以后没有办法重建镜像。

```
shapely==1.8.1.post1
scikit-image==0.17.2
imgaug==0.4.0
pyclipper==1.3.0.post2
lmdb==1.3.0
tqdm==4.64.0
numpy==1.21.6
visualdl==2.2.3
python-Levenshtein==0.12.2
opencv-contrib-python==4.2.0.32
paddlenlp==2.0.0
paddle2onnx==0.5.1
paddlepaddle==2.0.2
paddlehub==2.1.0
```

开始安装系统依赖和python依赖

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

## 3. 用 PaddleHub Serving 的服务部署

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

识别地址就是 http://127.0.0.1:9000/predict/ocr_system

测试没问题，到这里运行镜像就构建好了

最后将容器内无用文件删除，减小容器的体积

```shell
rm -rf /root/.cache/* \
&& rm -rf /var/lib/apt/lists/* \
&& rm -rf /app/test/pg/*
```

保存并推送到对应厂商的容器镜像仓库

这里以阿里云容器镜像仓库作为例子

请自行修改参数推送，这里是我的账户命令

```shell
docker commit testppocr paddlehub_ppocr:1.0
docker tag paddlehub_ppocr:1.0 registry.cn-hongkong.aliyuncs.com/llapi/ppocr:1.0
docker push registry.cn-hongkong.aliyuncs.com/llapi/ppocr:1.0
```

## 4. 编写 Dockerfile

上面的过程是构建飞桨的基础运行环境的 那么以后就可以用该基础镜像部署任意飞桨模型了

```
FROM registry.cn-hongkong.aliyuncs.com/llapi/pphub:base

COPY PaddleOCR /PaddleOCR

WORKDIR /PaddleOCR

RUN mkdir -p /PaddleOCR/inference/
ADD https://paddleocr.bj.bcebos.com/dygraph_v2.0/ch/ch_ppocr_mobile_v2.0_det_infer.tar /PaddleOCR/inference/
RUN tar xf /PaddleOCR/inference/ch_ppocr_mobile_v2.0_det_infer.tar -C /PaddleOCR/inference/

ADD https://paddleocr.bj.bcebos.com/dygraph_v2.0/ch/ch_ppocr_mobile_v2.0_cls_infer.tar /PaddleOCR/inference/
RUN tar xf /PaddleOCR/inference/ch_ppocr_mobile_v2.0_cls_infer.tar -C /PaddleOCR/inference/

ADD https://paddleocr.bj.bcebos.com/dygraph_v2.0/ch/ch_ppocr_mobile_v2.0_rec_infer.tar /PaddleOCR/inference/
RUN tar xf /PaddleOCR/inference/ch_ppocr_mobile_v2.0_rec_infer.tar -C /PaddleOCR/inference/

RUN hub install deploy/hubserving/ocr_system/
RUN hub install deploy/hubserving/ocr_cls/
RUN hub install deploy/hubserving/ocr_det/
RUN hub install deploy/hubserving/ocr_rec/

EXPOSE 9000

CMD ["/bin/bash","-c","hub serving start --modules ocr_system ocr_cls ocr_det ocr_rec -p 9000"]
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

在阿里云函数计算控制台中， 新建服务，创建函数，根据下面信息填写，创建函数后，绑定域名即可提供 api 识别接口。

容器镜像地址 `registry.cn-hongkong.aliyuncs.com/llapi/ppocr:1.0`

启动命令 `["sh","/PaddleOCR/start.sh"]`

需要绑定域名

识别地址就是 http://绑定域名/predict/ocr_system

![2](./demo/2.png)

![3](./demo/3.png)

## 部署到腾讯云函数

这里已经准备好可用镜像了

在腾讯云函数控制台中，需要将镜像推送至自己账户中的镜像仓库，随后创建云函数，即可提供 api 识别接口。

1. 需要将镜像推送至腾讯云的镜像仓库
2. 创建云函数

```shell
docker pull duolabmeng666/paddlehub_ppocr:1.2
docker tag duolabmeng666/paddlehub_ppocr:1.2 ccr.ccs.tencentyun.com/llapixxx/ppocr:1.2
docker push ccr.ccs.tencentyun.com/llapixxx/ppocr:1.2
```

推送镜像至腾讯云以后就可以创建云函数了

识别地址就是 https://创建云函数后可以看到.gz.apigw.tencentcs.com/release/predict/ocr_system



由于腾讯云云函数容器的文件的限制只允许 `/tmp` 可读可写，所以我们需要修改代码以支持云函数的部署。

### 解决方案

* 了解 docker 镜像制作与推送
* 云函数中报错解决思路

### 分析 docker 中写出的文件

将我们前面部署好的镜像，在自己电脑上运行起来

```shell
docker run -itd --name ppocr -p 9000:9000 ccr.ccs.tencentyun.com/llapi/pphubocr:1.0
```

查看文件差异信息，发现运行以后，在非 `/tmp` 目录进行了写文件操作，所以导致在云函数中无法启动容器。
现在我们要做的事情就是将路径处理到 `/tmp` 目录中

```shell
docker diff ppocr
C /root
C /root/.paddlehub
C /root/.paddlehub/conf
A /root/.paddlehub/conf/serving_9000.json
C /root/.paddlehub/log
A /root/.paddlehub/log/HubServing-2021_08_12.log
```

通过查看源代码可以发现 `/paddlehub/env.py` 是控制这些文件写出目录的文件

将文件复制出来放置 `./tx/env.py` 并在最后增加以下代码

```shell
CONF_HOME = "/tmp"
LOG_HOME = "/tmp"
TMP_HOME = "/tmp"
```

### 编写 Dockerfile

在项目目录中创建文件 `Dockerfile_TX`

```shell
FROM ccr.ccs.tencentyun.com/llapi/pphubocr:1.0

WORKDIR /PaddleOCR

COPY ./tx/env.py /usr/local/lib/python3.7/site-packages/paddlehub/env.py

CMD ["/bin/bash","-c","hub serving start --modules ocr_system ocr_cls ocr_det ocr_rec -p 9000"]
```

### 构建镜像测试

```shell
docker build -f ./Dockerfile_TX -t paddlehub_ppocr:1.0 .
docker rm -f ppocr
docker run -itd --name ppocr -p 9000:9000 paddlehub_ppocr:1.0
docker logs ppocr
docker diff ppocr
```

可以发现镜像在镜像中依然存在非 /tmp 文件的读写 但是这些文件在保存容器镜像以后 不会在读写 所以接下来只需要保存镜像推送即可

```shell
docker diff ppocr
C /usr
C /usr/local
C /usr/local/lib
C /usr/local/lib/python3.7
C /usr/local/lib/python3.7/site-packages
C /usr/local/lib/python3.7/site-packages/paddlehub
C /usr/local/lib/python3.7/site-packages/paddlehub/__pycache__
C /usr/local/lib/python3.7/site-packages/paddlehub/__pycache__/env.cpython-37.pyc
C /tmp
A /tmp/HubServing-2021_08_12.log
A /tmp/cache.yaml
A /tmp/config.yaml
A /tmp/serving_9000.json
```

### 打包镜像推送

```shell
# 保存镜像
docker commit ppocr ccr.ccs.tencentyun.com/llapi/pphubocr:1.2

# 测试一下这个镜像是否还存文件读写的情况 没有问题的话就可以推送了
docker rm -f ppocr
docker run -itd --name ppocr -p 9000:9000 ccr.ccs.tencentyun.com/llapi/pphubocr:1.2
docker logs ppocr
docker diff ppocr

# 经过前面的检查确定镜像没有问题，推送镜像
docker push ccr.ccs.tencentyun.com/llapi/pphubocr:1.2
```

### 在腾讯云函数中创建

选择镜像直接部署就可以拿到识别地址了

![4](./demo/4.png)
![5](./demo/5.png)





## 使用 Serverless Devs 部署到阿里云函数计算

Serverless Devs是一个开源开放的Serverless开发者平台，您无需关心底层资源。通过Serverless Devs，您不仅可以可插拔式地使用Serverless的服务和框架，也可以参与组件和插件的开发，提高运维效率。同时，您也可以更简单、快速地开发、创建、测试和部署项目，实现项目全生命周期的管理。[Github](https://github.com/Serverless-Devs/Serverless-Devs/blob/master/readme_zh.md) [文档地址](https://www.serverless-devs.com/docs/intro)

[安装 Serverless Devs](https://help.aliyun.com/document_detail/195474.htm)

```
npm install @serverless-devs/s -g
```

[配置Serverless Devs](https://help.aliyun.com/document_detail/295894.html)

在使用Serverless Devs前，您需要配置Serverless Devs，以阿里云密钥为例。[教程地址](https://help.aliyun.com/document_detail/295894.html)


进入本项目目录 `deploy\aliyun_fc`

```
# 进入目录
cd deploy\aliyun_fc

# 输入命令后一步一步添加阿里云秘钥
s config add

# 部署ppocr
s deploy
```
![5](./demo/7.png)

执行成功以后就得到识别地址例如 `http://ppocr.ppocr.创建好以后你将看到.cn-shenzhen.fc.devsapp.net/predict/ocr_system`

# Serverless应用中心 应用上架


快速完成 Serverless Devs 应用开发并发布到 Regsitry https://github.com/Serverless-Devs/Serverless-Devs/discussions/439

参考视频教程 https://example-static.oss-cn-beijing.aliyuncs.com/video/202203231823.mp4

提交申请 https://survey.aliyun.com/apps/zhiliao/YdBrsSK0f

经验之谈

建议看完视频 直接下载项目 todolist-app 然后修修改改

https://github.com/devsapp/start-web-framework/tree/master/example/todolist-app

```shell
s cli registry login # 登录授权 一次就行
s cli registry publish # 发布包
s cli registry list # 查看子机已发布的包

s init PaddleOCR # 自己测试应用的效果
s deploy # 部署项目试试
```


# 使用服务端模型

dockerfile 文件修改为以下内容

```
RUN mkdir -p /PaddleOCR/inference/
ADD https://paddleocr.bj.bcebos.com/dygraph_v2.0/ch/ch_ppocr_mobile_v2.0_det_infer.tar /PaddleOCR/inference/
RUN tar xf /PaddleOCR/inference/ch_ppocr_mobile_v2.0_det_infer.tar -C /PaddleOCR/inference/

ADD https://paddleocr.bj.bcebos.com/dygraph_v2.0/ch/ch_ppocr_mobile_v2.0_cls_infer.tar /PaddleOCR/inference/
RUN tar xf /PaddleOCR/inference/ch_ppocr_mobile_v2.0_cls_infer.tar -C /PaddleOCR/inference/

ADD https://paddleocr.bj.bcebos.com/dygraph_v2.0/ch/ch_ppocr_server_v2.0_rec_infer.tar /PaddleOCR/inference/
RUN tar xf /PaddleOCR/inference/ch_ppocr_server_v2.0_rec_infer.tar -C /PaddleOCR/inference/
```

`\PaddleOCR\deploy\hubserving\ocr_rec\params.py`

```
    # cfg.rec_model_dir = "./inference/ch_ppocr_mobile_v2.0_rec_infer/"
    cfg.rec_model_dir = "./inference/ch_ppocr_server_v2.0_rec_infer/"
```

`\PaddleOCR\deploy\hubserving\ocr_system\params.py`

```
    # cfg.rec_model_dir = "./inference/ch_ppocr_mobile_v2.0_rec_infer/"
    cfg.rec_model_dir = "./inference/ch_ppocr_server_v2.0_rec_infer/"
```


# 总结

在 Serverless 架构下部署深度学习模型变得非常简单且能提供无限的并发支持，我们可以将镜像部署到各个提供 Serverless 的服务商中，可提供稳定可靠弹性的推理服务。

在构建镜像方面，[飞桨官方提供的 docker 镜像](https://hub.docker.com/r/paddlepaddle/paddle/tags?page=1&ordering=last_updated)，动辄 4GB、8GB，在镜像如此大的情况下基本无缘 Serverless 。

本文所构建的的镜像仅 564MB ，在 Serverless 架构下部署 ，启动速度理想。

# 鸣谢

感谢各厂商大佬提供的技术支持

* 百度飞桨 https://www.paddlepaddle.org.cn/
* PaddleOCR https://github.com/PaddlePaddle/PaddleOCR
* 腾讯云函数 https://cloud.tencent.com/product/scf
* 阿里云函数计算 https://www.aliyun.com/product/fc
* Serverless Devs https://www.serverless-devs.com/


# 图书推荐

Serverless工程实践：从入门到进阶 https://item.jd.com/13366562.html

![5](./demo/6.png)

# 本文作者

多啦b梦 [Github](https://github.com/duolabmeng6) 

转载本文请注明来源，谢谢。

# 赞赏

如果觉得项目对你有帮助，可以请作者喝杯咖啡

![swskm](https://github.com/user-attachments/assets/83557145-89aa-4c34-9cbf-a6e31701b702)

