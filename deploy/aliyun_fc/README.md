
## 环境变量

新建 .env 文件，文件内容如下：

```
export AccessKeyID=xxx
export AccessKeySecret=xxx
export AccountID=xxx
export aliasName=default    # 需要与 s.yml 中的 access 字段保持一致

```

## 启动

运行 ``sh setup.sh`` 执行构建镜像、推送镜像以及部署镜像的操作。

