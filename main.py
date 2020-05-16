import random as r
import MainWindow
import sys
from PyQt5 import QtWidgets, QtCore, QtGui

class Password():
    opts = {
        'amount': 8,
        'ABC': 2,
        'abc': 2,
        'number': 1,
        'symbol': 1
    }
    password = ''
    abc = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k',
           'm', 'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    ABC = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K',
           'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
    Numeral = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
    Symbols = ('%', '!', '$', '#')
    Container = (abc, ABC, Numeral, abc, Symbols, ABC)

    def generate(self):
        self.password = ''
        while len(self.password) < self.opts['amount']:
            i = r.randint(0, len(self.Container) - 1)
            j = r.randint(0, len(self.Container[i]) - 1)
            self.password += self.Container[i][j]
            continue


        check = {
            'up': 0,
            'down': 0,
            'num': 0,
            'sym': 0
        }

        while 0 in check.values():
            #Первоначальная проверка
            up = 0
            down = 0
            num = 0
            sym = 0

            for symbol in self.password:
                if symbol in self.abc:
                    down += 1
                    continue
                elif symbol in self.ABC:
                    up += 1
                    continue
                elif symbol in self.Numeral:
                    num += 1
                    continue
                elif symbol in self.Symbols:
                    sym += 1
                    continue

            #Проверка количества больший букв
            if up < self.opts['ABC']:
                while True:
                    #Попытка замены буквы на заглавную
                    try:
                        i = r.randint(0, len(self.password) - 1)
                        self.password = self.password[0:i] + self.ABC[r.randint(0, len(self.ABC) - 1)] \
                                           + self.password[i + 1:len(self.password)]
                        up += 1
                        break
                    #Если вместо буквы цифра или символ
                    except FileNotFoundError:
                        continue
                #Проверка на количество букв после завершение цикла
                if up >= self.opts['ABC']:
                    check['up'] = 1
                else:
                    continue
            else:
                check['up'] = 1

            #Проверка на количество маленьких букв
            if down < self.opts['abc']:
                while True:
                    # Попытка замены буквы на маленькую
                    try:
                        i = r.randint(0, len(self.password) - 1)
                        self.password = self.password[0:i] + self.abc[r.randint(0, len(self.abc) - 1)] \
                                           + self.password[i + 1:len(self.password)]
                        down += 1
                        break
                    # Если вместо буквы цифра или символ
                    except:
                        continue
                # Проверка на количество букв после завершение цикла
                if down >= self.opts['abc']:
                    check['down'] = 1
                else:
                    continue
            else:
                check['down'] = 1

            #Проверка на количество цифр
            if num < self.opts['number']:
                while True:
                    # Попытка замены символа на цифру
                    try:
                        i = r.randint(0, len(self.password) - 1)
                        self.password = self.password[0:i] + self.Numeral[r.randint(0, len(self.Numeral) - 1)] \
                                           + self.password[i + 1:len(self.password)]
                        num += 1
                        break
                    # Если не получилось
                    except:
                        continue
                # Проверка на количество букв после завершение цикла
                if num >= self.opts['number']:
                    check['num'] = 1
                else:
                    continue
            else:
                check['num'] = 1

            #Проверка на количество символов
            if sym < self.opts['symbol']:
                while True:
                    # Попытка замены на символ
                    try:
                        i = r.randint(0, len(self.password) - 1)
                        self.password = self.password[0:i] + self.Symbols[r.randint(0, len(self.Symbols) - 1)] \
                                           + self.password[i + 1:len(self.password)]
                        sym += 1
                        break
                    # Если не получилось
                    except:
                        continue
                # Проверка на количество букв после завершение цикла
                if sym >= self.opts['symbol']:
                    check['sym'] = 1
                else:
                    continue
            else:
                check['sym'] = 1
            #Конечная проверка
            up = 0
            down = 0
            num = 0
            sym = 0

            for symbol in self.password:
                if symbol in self.abc:
                    down += 1
                    continue
                elif symbol in self.ABC:
                    up += 1
                    continue
                elif symbol in self.Numeral:
                    num += 1
                    continue
                elif symbol in self.Symbols:
                    sym += 1
                    continue

            if up < self.opts['ABC']:
                check['up'] = 0
            if down < self.opts['abc']:
                check['down'] = 0
            if num < self.opts['number']:
                check['num'] = 0
            if sym < self.opts['symbol']:
                check['sym'] = 0

            if 0 in check.values():
                continue
            else:
                return self.password

class Core(QtWidgets.QWidget, MainWindow.Ui_Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.generate)
        self.optsButton.clicked.connect(self.hideOpts)
        self.amountSpin.valueChanged.connect(self.changeSpin)
        self.AAASpin.valueChanged.connect(self.changeSpin)
        self.aaaSpin.valueChanged.connect(self.changeSpin)
        self.numberSpin.valueChanged.connect(self.changeSpin)
        self.symbolSpin.valueChanged.connect(self.changeSpin)
        self.amountSpin.setValue(8)
        self.AAASpin.setValue(2)
        self.aaaSpin.setValue(2)
        self.numberSpin.setValue(1)
        self.symbolSpin.setValue(1)
        self.hideOpts()

    def generate(self):
        message = passw.generate()
        self.passwordLine.setText(message)

    def changeSpin(self):
        sender = self.sender()
        if sender.objectName() == 'amountSpin':
            passw.opts['amount'] = sender.value()
            print(sender.objectName(), sender.value())
        elif sender.objectName() == 'AAASpin':
            passw.opts['ABC'] = sender.value()
            print(sender.objectName(), sender.value())
        elif sender.objectName() == 'aaaSpin':
            passw.opts['abc'] = sender.value()
            print(sender.objectName(), sender.value())
        elif sender.objectName() == 'numberSpin':
            passw.opts['number'] = sender.value()
            print(sender.objectName(), sender.value())
        else:
            passw.opts['symbol'] = sender.value()
            print(sender.objectName(), sender.value())

    def hideOpts(self):
        self.optsFrame.hide()
        self.setMaximumHeight(130)
        self.setMinimumHeight(130)
        self.resize(480, 130)
        self.optsButton.disconnect()
        self.optsButton.clicked.connect(self.showOpts)

    def showOpts(self):
        self.optsFrame.show()
        self.setMaximumHeight(235)
        self.setMinimumHeight(235)
        self.optsButton.disconnect()
        self.optsButton.clicked.connect(self.hideOpts)

passw = Password()
#while True:
    #passw.generate()
App = QtWidgets.QApplication(sys.argv)
main = Core()
main.show()
App.exec_()