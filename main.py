from src.summarizer import stxt
from src.reader import rpdf
from src.sketcher import draw, draw2
from src.keyw import ext
a = rpdf()
b = stxt(a)
ori = len(a.replace(' ',''))
sur = len(b.replace(' ',''))
draw(ori,sur)
c =ext(b)
draw2(c)
print('For more information and future updates of this project please read the ReadME text file.')