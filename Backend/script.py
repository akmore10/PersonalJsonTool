import pandas as pd
from functools import cmp_to_key
from pandas import DataFrame


class Video:
    def __init__(self,name,views,link,video):
        self.name = name
        self.views = views
        self.link = link
        self.video = video
    def __str__(self) -> str:
        return "{} {} {} {}".format(self.name , self.views,self.link,self.video)
    
class VideoAnalysis:
    def __init__(self,data : DataFrame):
        self.data = data
    
    def analyze(self):
        result = self._createVideoObjects()
        print(result)
        result = sorted(result,key=cmp_to_key(VideoAnalysis.compare))
        return result

    def _createVideoObjects(self):
        result = []
        for id in self.data:
            name , views ,link,videCode= "",0,"",""
            for res in self.data[id].items():
                if res[0] == "title":
                    name = res[1]
                if res[0] == "stats":
                    views = res[1]["likeCount"]
                if res[0] == "videoTrailer":
                    link = res[1]
                if res[0] == "video":
                    print("here")
                    videoCode = res[1]
                
            obj = Video(name , views,link,videoCode)
            result.append(obj)

        return result
    
    @staticmethod
    def compare(a , b):
        if a.views > b.views:
            return -1
        else:
            return 1
    
