#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Analyze a passage, and show the result using the GUI.'

__author__ = 'Zheng Rachel'


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
import AnalyzeSentence

#建立描述GUI窗口的类
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = '分析文章中语句的情感倾向'
        self.left = 700
        self.top = 300
        self.width = 500
        self.height = 500
        self.initUI()
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        #Create a label in the window
        self.label = QLabel(self)
        self.label.move(50,100)
        # Create a button in the window
        self.button = QPushButton('点此查看下一句的分析', self)
        self.button.move(150, 400)

#此函数用于将文章分为单句向API发送，并确定需要在GUI的Label中显示的文本内容
def analyze_next_line(s, mygui):
    try:
        #在未达到文章末尾时，不断获得下一句待分析的语句
        string = next(s)
    except StopIteration:
        #达到文章末尾，显示提示用户退出程序的内容并返回
        text_content='文章已经分析完啦!请关闭对话框'
        mygui.label.setText(text_content)
        return
    #向API发送请求
    result = AnalyzeSentence.analyze_sentence(string)
    #根据API的返回内容确定Label上要显示的内容
    text_content='我们分析的语句是:\"'+result['text']+'\"\n积极程度:'+str(result['items'][0]['positive_prob'])+\
                 '\n消极程度:'+str(result['items'][0]['negative_prob'])+'\n置信度:'+str(result['items'][0]['confidence'])
    if result['items'][0]['sentiment']==1:
        text_content+='\n总的来说，这句话的情感倾向分类是:中性的'
    elif result['items'][0]['sentiment']==2:
        text_content += '\n总的来说，这句话的情感倾向分类是:积极的'
    else:
        text_content += '\n总的来说，这句话的情感倾向分类是:消极的'
    print(text_content)
    #在Label上显示
    mygui.label.setText(text_content)
    #为适应显示，自动调整Label的大小
    mygui.label.adjustSize()

#利用生成器，每遇到'\n'就获得一次字符串，从而将大段文字分成单句
def StringGenerator(str0):
    first_index=0
    for i in range(len(str0)):
        if str0[i] == '\n':
            yield str0[first_index:i]
            first_index = i

if __name__ == '__main__':
    app = QApplication(sys.argv)
    global mygui
    mygui = App()
    mygui.show()
    #打开文件，str0用于获得文章的全部内容
    with open("Passage.txt", "r") as f:
        str0 = f.read()
        print(str0)
    #利用生成器，将文章按'\n'分成单句
    s=StringGenerator(str0)
    mygui.button.clicked.connect(lambda:analyze_next_line(s, mygui))
    sys.exit(app.exec_())