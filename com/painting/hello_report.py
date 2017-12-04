from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics import renderPDF

s = String(50, 50, 'Hello World', textAnchor='middle')
d = Drawing(100, 100)
d.add(s)

renderPDF.drawToFile(d, 'hello.pdf', 'a simple pdf file')