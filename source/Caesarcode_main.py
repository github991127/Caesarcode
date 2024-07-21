from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import QIcon

from list_themes import *
import Caesarcode


class Stats:
    def __init__(self):
        # 从ui文件中加载UI定义,从UI定义中动态创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了.比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('Caesarcode.ui')
        self.ui.pushButton.clicked.connect(self.handleCalc)
        self.ui.textEdit.returnPressed.connect(self.handleCalc)  # 单行文本框回车消息

    def handleCalc(self):  # ENTER按钮，将输入内容转换为int列表，传给cal计算
        self.ui.textBrowser.clear()
        cleartext = self.ui.textEdit.text()
        if cleartext == '':
            ciphertext = Caesarcode.Caesarcode()
        else:
            ciphertext = Caesarcode.Caesarcode(cleartext)
        i = 1
        for x in ciphertext:
            text = str(i) + ':' + x
            self.ui.textBrowser.append(text)
            i += 1


if __name__ == '__main__':
    app = QApplication([])
    app.setWindowIcon(QIcon('image.png'))
    apply_stylesheet(app, theme[0], extra=extra, invert_secondary=False)  # 默认dark-False
    w = QWidget()
    w.setWindowIcon(QIcon('image.png'))
    stats = Stats()
    stats.ui.show()
    app.exec_()
