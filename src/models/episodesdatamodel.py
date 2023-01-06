from PySide6.QtCore import QAbstractItemModel, Qt, QModelIndex

# need to reimplement all the interfaces if were to use QAbstractListModel
class EpisodesDataModel(QAbstractItemModel): 
    def __init__(self, *args, episodes=None, **kwargs):
        super(EpisodesDataModel, self).__init__(*args, **kwargs)
        self.episodes = episodes or [] # [(Title: str, url: QUrl), ...]
    
    def data(self, index, role):
        if role == Qt.DisplayRole:
            title, _ = self.episodes[index.row()]
            return title
        
        if role == Qt.UserRole:
            _, episode_url = self.episodes[index.row()]
            return episode_url
        
        if role == Qt.DecorationRole:
            _, status = self.episodes[index.row()]
            if status: # todo: change to url
                return status

    def rowCount(self, index):
        return len(self.episodes)
    
    def columnCount(self, index):
        return 2

    def index(self, row, column, parent=QModelIndex):
        table_row = self.episodes[row]
        return self.createIndex(row, column, table_row)

    def parent(self, child): # todo: 
        return None
       # return self.createIndex(-1, -1, None)

    def clear(self):
        self.episodes.clear()