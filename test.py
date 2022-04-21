from pyefun import *
a="""cn-beijing
cn-hangzhou
cn-shanghai
cn-qingdao
cn-zhangjiakou
cn-huhehaote
cn-chengdu
cn-hongkong"""
import pexpect

arr = 分割文本(a, '\n')
for v in arr:
    # shell = """docker login --username=duolabmeng666 registry.{区域}.aliyuncs.com""".format(区域=v)
    # print(shell)
    # child = pexpect.spawn(shell)
    # child.sendline('')
    # child.expect(pexpect.EOF)
    # result = child.before.decode()
    # print(result)

    shell = """docker tag registry.cn-shenzhen.aliyuncs.com/duolabmeng/ppocr:1.8 registry.{区域}.aliyuncs.com/duolabmeng/ppocr:1.8""".format(区域=v)
    print(shell)

    shell = """docker push registry.{区域}.aliyuncs.com/duolabmeng/ppocr:1.8""".format(区域=v)
    print(shell)