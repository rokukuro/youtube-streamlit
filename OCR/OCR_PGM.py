import pyocr
from PIL import Image,ImageGrab
import pyperclip as pc

pyocr.tesseract.TESSERACT_CMD = r"C:\Users\ken-ichi\AppData\Local\Tesseract-OCR\tesseract.exe"

tools = pyocr.get_available_tools()
tool = tools[0]

#OCR対象の画像ファイルを取り込む
img = ImageGrab.grabclipboard()
#img = Image.open(r"D:\MyPython\programs\OCR\image\1.png")

builder = pyocr.builders.TextBuilder(tesseract_layout=6)
text = tool.image_to_string(img, lang="jpn", builder=builder)

print(text)
pc.copy(text)