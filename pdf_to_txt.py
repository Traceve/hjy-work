# -*- coding:utf-8 -*-
import sys
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')


def readPDF(pdfFile):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    process_pdf(rsrcmgr, device, pdfFile)
    device.close()
    content = retstr.getvalue()
    retstr.close()
    return content


def saveTxt(txt):
    with open("istxt.txt", "w", encoding='utf-8') as f:
        # with open("istxt.txt", "wb") as f:
        f.write(txt)


txt = readPDF(open('7036524.pdf', 'rb'))
