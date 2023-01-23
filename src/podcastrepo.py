"""_summary_
handles podcast repository (1 rss subscription) and database connection
"""

import sqlite3
from podcastEpisodeItem import PodcastEpisodeItem

QUERY_CREATE_TABLE = 'CREATE TABLE podcasts(guid, title, url, pubDate, description, parentPodcast)'
QUERY_GET_ALL_EPISODES = 'SELECT * from podcasts where parentPodcast=(?)'
QUERY_INSERT_EPISODE = 'INSERT INTO podcasts VALUES(?,?,?,?,?,?)'

class PodcastRepo():
    def __init__(self, podcastName):
        self.podcastName = podcastName
        self.conn = self.__create_connection('database.db')
        pass

    def __del__(self):
        print("repository destroyed")
        pass
    
    def __create_connection(self, db_file):
        """ create a database connection to the SQLite database
            specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Exception as e:
            print(e)
        return conn


    def fetchEpisodes(self) -> list:
        cur = self.conn.cursor()
        res = cur.execute(QUERY_GET_ALL_EPISODES, (self.podcastName, ))      
        return map(lambda x: PodcastEpisodeItem(x[0], x[1], x[2], x[3], x[4], x[5]), res)
    # guid: str, title: str, url: QUrl, pubDate: datetime, description: str, parentPodcast: str):
    
    
    def insertEpisodes(self, episodes: list[PodcastEpisodeItem]) -> int:
        cur = self.conn.cursor()
        res = cur.executemany(QUERY_INSERT_EPISODE, map(lambda x: x.asList(), episodes))
        self.conn.commit()
        return cur.lastrowid