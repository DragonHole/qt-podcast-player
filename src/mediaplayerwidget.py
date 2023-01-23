from PySide6.QtWidgets import (
    QWidget,
    QListView,
    QHBoxLayout,
    QMessageBox,
    QSlider,
    QLabel,
    QPushButton,
    QStyle, 
    QGroupBox
)
from PySide6.QtGui import QAction, QIcon, QKeySequence, QScreen
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import Slot, QXmlStreamReader, QIODevice, QFile, Qt, QUrl, Signal
from util import class_name, init_widget, embed_into_vbox_layout

DIR_OPEN_ICON = ":/qt-project.org/styles/commonstyle/images/diropen-128.png"


class MediaPlayerWidget(QWidget):
    dummyVolumeSignal = Signal(float)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self._playing_url: QUrl = QUrl()
        self._playlist: list[QUrl] = []
        self._playlist_index = -1 # current playing index
        
        self._audio_output = QAudioOutput()
        self._audio_output.setVolume(0.5)
        self._media_player = QMediaPlayer()
        self._media_player.setAudioOutput(self._audio_output)
        
        style = self.style()
        groupHBox = QGroupBox(self)
        # groupHBox.setFixedWidth(500)
        # connect player error
        layout = QHBoxLayout(groupHBox)
        #layout.setSpacing(5)
        self._back15SButton = QPushButton("<15")
        self._forw15SButton = QPushButton(">15")
        self._playButton = QPushButton("", icon=QIcon.fromTheme("media-playback-start.png",
                               style.standardIcon(QStyle.SP_MediaPlay)))
        layout.addWidget(self._back15SButton)
        layout.addWidget(self._playButton)
        layout.addWidget(self._forw15SButton)
        
        self._volume_slider = QSlider()
        self._volume_slider.setOrientation(Qt.Horizontal)
        #available_width = self.screen().availableGeometry().width()
        #self._volume_slider.setFixedWidth(available_width / 10)
        self._volume_slider.setValue(self._audio_output.volume() * 100) # because volumn range in [1, 0]
        self._volume_slider.setRange(0, 100)
        #self._volume_slider.setTickPosition(QSlider.TicksLeft)
        self._volume_slider.setToolTip("Volume")
        #self._volume_slider.valueChanged.connect(self._audio_output.setVolume)
        self._volume_slider.valueChanged.connect(self.dummyvolumefunc)
        self.dummyVolumeSignal.connect(self._audio_output.setVolume)
        layout.addWidget(self._volume_slider)
        
        self._label = QLabel()
        self._label.setText("Hello world")
        layout.addWidget(self._label)
        
        self._playButton.clicked.connect(self.togglePlayButton)
        self._back15SButton.clicked.connect(self.toggleBack15SButton)
        self._forw15SButton.clicked.connect(self.toggleForw15SButton)
        

    # because slider handles only integers, but AudioOutput needs a volume in range [0, 1]
    @Slot()
    def dummyvolumefunc(self, volume):
        self.dummyVolumeSignal.emit(volume / 100)
    
    @Slot()
    def togglePlayButton(self):
        if self._media_player.playbackState() == QMediaPlayer.PausedState:
            self._media_player.play()
        else:
            self._media_player.pause()
            
    @Slot()
    def toggleBack15SButton(self):
        self._media_player.setPosition(self._media_player.position() - 15*1000)
    
    @Slot()
    def toggleForw15SButton(self):
        self._media_player.setPosition(self._media_player.position() + 15*1000)
        
    @Slot()
    def setPlayingMedia(self, url):
        
        self._media_player.setSource(QUrl(url))
        self._media_player.play()

    
        