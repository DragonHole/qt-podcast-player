from PySide6.QtWidgets import (
    QWidget,
    QListView,
    QHBoxLayout,
    QMessageBox,
    QSlider,
    QLabel,
    QPushButton
)

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
        
        # connect player error
        layout = QHBoxLayout(self)
        #layout.setSpacing(5)
        self._back15SButton = QPushButton("<15")
        self._forw15SButton = QPushButton(">15")
        self._playButton = QPushButton("Play/Pause")
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

    # because slider handles only integers, but AudioOutput needs a volume in range [0, 1]
    @Slot()
    def dummyvolumefunc(self, volume):
        self.dummyVolumeSignal.emit(volume / 100)
    
    @Slot()
    def togglePlayButton(self):
        print("toggled play button")
        print(self._audio_output.volume())
        if self._media_player.playbackState() == QMediaPlayer.StoppedState:
            self._media_player.play()
        else:
            self._media_player.stop()
        
    @Slot()
    def setPlayingMedia(self, url):
        print(url)
        self._media_player.setSource(QUrl(url))
        self._media_player.play()

        