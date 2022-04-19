from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDir, Qt, QUrl
from PyQt6.QtWidgets import (QWidget,QMessageBox)
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QMainWindow,  QPushButton, QApplication,
                             QLabel, QFileDialog, QStyle, QVBoxLayout)


class VideoPlayer(QWidget):
    def __init__(self, parent):
        super(VideoPlayer, self).__init__(parent)
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.mediaPlayer.setMedia( QMediaContent(QUrl.fromLocalFile("static\movies\play.mkv")))
        self.playButton = QPushButton()
        self.playButton.clicked.connect(self.play)
        videoWidget = QVideoWidget()
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.addWidget(videoWidget)
        self.verticalLayout.addWidget(self.playButton)
        self.setLayout(self.verticalLayout_2)
        self.mediaPlayer.setVideoOutput(videoWidget)

    def play(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()