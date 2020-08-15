import pymongo
from pymongo import MongoClient
from random import randint
import tqdm
from ner import process_NL


class DataGen():
    def __init__(self):
        self.name = "Class for population of database"
        self.client = MongoClient("mongodb://localhost:27017")
        self.db = self.client["phonesDB"]
        self.col = self.db["phone1"]



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


    #=== generate sample data ===
    def populate(self):
        # === attribute for phone ===
        attributes = ['camera', 'flash', 'size', 'network', 'processor', 'storage', 'operating system']
        cam = ['2MP', '4MP', '8MP', '12MP', '16MP', '20MP', '32MP', '64MP', '100MP']
        fla = ['integrated', 'not integrated']
        siz = ['3-inch', '4-inch', '4.5-inch', '5-inch', '5.1-inch', '5.2-inch']
        net = ['wireless supported', 'ieee 802.11 supported', '3g supported', '4g supported', 'lte supported']
        pro = ['snapdragon', 'qualcom', 'intel']
        sto = ['2GB', '4GB', '8GB', '16GB', '32GB', '64GB', '128GB', '256GB', '512GB', '1TB']
        os  = ['iOS', 'android', 'symbian OS']

        # === model of phone ===
        models = ['iphone','iphone' 'samsung', 'xiaomi','redmi pro', 'redmi note']

        # === data of each phone ===
        data = ['4', '5', '6', '7', '8', '10', '11', 'samsung', 'xiaomi', 'redmi pro', 'snapdragon', 'screen', 'size', 'x']

        l = []
        for i in tqdm.tqdm(range(100000)):
            final_attributes = {
            'attribute': attributes[randint(0, len(attributes)-1)],
            'camera' : cam[randint(0, len(cam)-1)],
            'flash' : fla[randint(0, len(fla)-1)],
            'size' : siz[randint(0, len(siz)-1)],
            'network' : net[randint(0, len(net)-1)],
            'processor' : pro[randint(0, len(pro)-1)],
            'storage' : sto[randint(0, len(sto)-1)],
            'operating system' : os[randint(0, len(os)-1)],
            'model' : models[randint(0, len(models)-1)],
            'data' : data[randint(0, len(data)-1)]
            }
            l.append(final_attributes)
            #print("==========={}%================{}".format(int(i/1000), final_attributes), end='\n\n')
            result = self.col.insert_one(final_attributes) # already inserted

        print("the last Created as {}".format(result.inserted_id))
        #
        # print("Insertion finished of 500 business reviews")

if __name__ == '__main__':

    dg = DataGen()
    print("population of database ....")
    dg.populate()
    print("====================\npopulation generated ....")
    dg.show()
    #q = input("Hi, enter a querry about your phone. \n-> ")

    #result = dg.search(q)
    # if result == None:
    #     print("None object found")
    # else:
    #     for e in result:
    #         print("=",e)
