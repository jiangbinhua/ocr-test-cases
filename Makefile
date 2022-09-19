
install-paddleocr:
	pip install paddlepaddle paddleocr -i https://pypi.tuna.tsinghua.edu.cn/simple

prepare-legal:
    rm -rf ../tif-files/* &&\
	python ocreval.py --ds-dir=./legal.4B --action=prepare

prepare-bus:
	rm -rf ../tif-files/* &&\
	python ocreval.py --ds-dir=./bus.4B --action=prepare

paddleocr-legal:
	rm -rf ../paddleocr-output/* &&\
	rm -rf ../paddleocr-accuracy/* &&\
	rm -rf ../paddleocr-wordacc/* &&\
	python ocreval.py --ds-dir=./legal.4B --action=paddleocr

paddleocr-bus:
	rm -rf ../paddleocr-output/* &&\
	rm -rf ../paddleocr-accuracy/* &&\
	rm -rf ../paddleocr-wordacc/* &&\
	python ocreval.py --ds-dir=./bus.4B --action=paddleocr

paddleocr-ocreval-legal:
	python ocreval.py --ds-dir=./legal.4B --action=ocreval --ocr-name=paddleocr

paddleocr-ocreval-bus:
	python ocreval.py --ds-dir=./bus.4B --action=ocreval --ocr-name=paddleocr

abbyyocr-legal:
	python ocreval.py --ds-dir=./legal.4B --action=abbyyocr

abbyyocr-bus:
	python ocreval.py --ds-dir=./bus.4B --action=abbyyocr

abbyyocr-ocreval-legal:
	python ocreval.py --ds-dir=./legal.4B --action=ocreval --ocr-name=abbyy

abbyyocr-ocreval-bus:
	python ocreval.py --ds-dir=./bus.4B --action=ocreval --ocr-name=abbyy

ymocr-legal:
	python ocreval.py --ds-dir=./legal.4B --action=ymocr

ymocr-bus:
	python ocreval.py --ds-dir=./bus.4B --action=ymocr

ymocr-ocreval-legal:
	python ocreval.py --ds-dir=./legal.4B --action=ocreval --ocr-name=ymocr

ymocr-ocreval-bus:
	python ocreval.py --ds-dir=./bus.4B --action=ocreval --ocr-name=ymocr

