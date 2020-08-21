import pymongo
from pymongo import MongoClient
from random import randint
import tqdm
from .ner import process_NL


class Query():
    def __init__(self):
        self.name = "Class for population of database"
        self.client = MongoClient("mongodb://localhost:27017")
        self.db = self.client["phonesDB"]
        self.col = self.db["phone4"]



    def show(self):
        #result = self.col.find()
        result = self.col.find({
                        'data' : "xiaomi",
                        'attribute' : "camera",
                        },
                        { 'storage':1, 'model' : 1, 'camera':1, 'flash':1, '_id': 0} ).limit(4)
        i = 1
        for r in result:
            print(r); i+= 1
        print(i)

    def search(self, querry):

        result = process_NL(querry)

        if len(result) == 1 and result[0][1] == "table":
            return self.col.find({},
                            { 'storage':1, 'model' : 1, 'camera':1, 'flash':1, '_id': 0} ).limit(4)
        elif len(result) > 1:

            data = []
            attribute = []
            model = []
            for elt in result:
                if elt[1] == "data":
                    data.append(elt[0])
                if elt[1] == "attribute":
                    attribute.append(elt[0])
                if elt[1] == "model":
                    model.append(elt[0])

            if len(data)>0:
                if len(attribute)>0:
                    if len(model)>0:
                        print("d>0,ad>0,m>0")
                        return self.col.find({
                                        'data' : data[0],
                                        'attribute' : attribute[0],
                                        'model': model[0]
                                        },
                                        { 'storage':1, 'model' : 1, 'camera':1, 'flash':1, '_id': 0} ).limit(4)
                    else:
                        print("d>0,a>0,m<0")
                        return self.col.find({
                                        'data' : data[0],
                                        'attribute' : attribute[0],
                                        },
                                        { 'storage':1, 'model' : 1, 'camera':1, 'flash':1, '_id': 0} ).limit(4)
                else:
                    if len(model)>0:
                        print("d>0,a<0,m>0")
                        return self.col.find({
                                        'data' : data[0],
                                        'model': model[0],
                                        },
                                        { 'storage':1, 'model' : 1, 'camera':1, 'flash':1, '_id': 0} ).limit(4)
                    else:
                        print("d>0,a<0,m<0")
                        return self.col.find({
                                        'data' : data[0],
                                        'attribute': 'camera'
                                        },
                                        { 'storage':1, 'model' : 1, 'camera':1, 'flash':1, '_id': 0} ).limit(4)
            else:
                if len(attribute)>0:
                    if len(model)>0:
                        print("d<0,a>0,m>0")
                        return self.col.find({
                                        'attribute' : attribute[0],
                                        'model': model[0]
                                        },
                                        { 'storage':1, 'model' : 1, 'camera':1, 'flash':1, '_id': 0} ).limit(4)
                    else:
                        print("d<0,a>0,m<0")
                        return self.col.find({
                                        'attribute' : attribute[0],
                                        },
                                        { 'storage':1, 'model' : 1, 'camera':1, 'flash':1, '_id': 0} ).limit(4)
                else:
                    if len(model)>0:
                        print("d<0,a<0,m>0")
                        return self.col.find({
                                        'model': model[0],
                                        'attribute': 'camera'
                                        },
                                        { 'storage':1, 'model' : 1, 'camera':1, 'flash':1, '_id': 0} ).limit(4)
                    else:
                        print("d<0,a<0,m<0")
                        return None



if __name__ == '__main__':

    print("mongo db...")
    query = Query()
    query.search()
