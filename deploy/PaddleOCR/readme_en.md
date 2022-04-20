# Rapid deployment of universal character recognition PaddleOCR

Mirror making tutorialMirror making tutorial https://github.com/duolabmeng6/paddlehub_ppocr

```shell
s init PaddleOCR  # Initialize projectInitialize project
s deploy  # Deployment projectDeployment project
```

Enter the project and enter s deploy. The domain of the deployment project will be the API address identified by the APIEnter the project and enter s deploy. The domain of the deployment project will be the API address identified by the API

For example: http://asc.ccc.xxxx.cn-shenzhen.fc.devsapp.net/predict/ocr_system

# Call method

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