import sys
from PySide6.QtWidgets import (QApplication, QLabel)
 
app = QApplication(sys.argv)
 
rotulo = QLabel("Olá, PySide6!")
rotulo.show()
 
app.exec() 