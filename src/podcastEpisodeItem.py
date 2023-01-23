from datetime import datetime 
from enum import Enum
from PySide6.QtCore import Slot, QXmlStreamReader, QIODevice, QFile, Qt, QUrl, Signal

class PodcastEpisodeItem:
    ListenState = Enum('ListenState', ['UNHEARD', 'FINISHED', 'INPROGRESS'])
    
    def __init__(self, guid: str, title: str, url: QUrl, pubDate: datetime, description: str, parentPodcast: str):
        self.guid = guid
        self.title = title
        self.url = url
        self.pubDate = pubDate
        self.description = description
        self.parentPodcast = parentPodcast # not sure yet
        self.lastTimestamp: int = 0 
    
    def __eq__(self, other):
        return (isinstance(other, PodcastEpisodeItem) 
                and self.guid == other.guid
               )
    
    def asList(self):
        return (self.guid, self.title, self.url, self.pubDate.strftime("%m/%d/%Y)"), self.description, self.parentPodcast)
        
    def listenState(self):
        if self.lastTimestamp == 0:
            return self.ListenState.UNHEARD
        elif self.lastTimestamp == -1:
            return self.ListenState.FINISHED
        else:
            return self.ListenState.INPROGRESS
    
    