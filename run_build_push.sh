docker build -f ./Dockerfile -t paddlehub_ppocr:1.0 .
docker rm -f ppocr
docker run -itd --name ppocr -p 9000:9000 paddlehub_ppocr:1.0
docker logs ppocr
docker diff ppocr

#没问题的话就可以执行推送命令
#docker tag paddlehub_ppocr:1.0 registry.cn-hongkong.aliyuncs.com/duolabmeng/ppocr:1.8
#docker push registry.cn-hongkong.aliyuncs.com/duolabmeng/ppocr:1.8
