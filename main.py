import sys
import os, glob
 
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QPushButton, QListWidget
from PyQt5.QtCore import QFile, QObject, QFileSystemWatcher
 
class Form(QObject):
 
    def __init__(self, ui_file, watchDir, parent=None):
        super(Form, self).__init__(parent)
        self.ui = loadUi(ui_file)
        self.watchDir = watchDir

        self.list = self.ui.findChild(QListWidget, 'listWidget')
 
        btn = self.ui.findChild(QPushButton, 'startButton')
        btn.clicked.connect(self.startHandler)
        self.ui.show()
 
    def startHandler(self):
        print("started")

        self.watcher = QFileSystemWatcher([self.watchDir])
        self.watcher.directoryChanged.connect(self.dirChanged)

    def latestFile(self, dir):
        files = glob.glob(dir + "/*")
        latestFile = max(files, key=os.path.getctime)
        return latestFile

    def dirChanged(self, dir):
        print(f"changed {self.latestFile(dir)}")
        self.list.addItem(self.latestFile(dir))

 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form('frame.ui', '/home/dave/temp/qt_dir_watch')
    sys.exit(app.exec_())