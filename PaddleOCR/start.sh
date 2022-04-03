#!/bin/bash
cd /PaddleOCR && hub serving start --modules ocr_system ocr_cls ocr_det ocr_rec -p 9000
