FROM ccr.ccs.tencentyun.com/llapi/pphubocr:1.0

WORKDIR /PaddleOCR

COPY ./tx/env.py /usr/local/lib/python3.7/site-packages/paddlehub/env.py

CMD ["/bin/bash","-c","hub serving start --modules ocr_system ocr_cls ocr_det ocr_rec -p 9000"]