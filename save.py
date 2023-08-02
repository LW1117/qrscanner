import json


def savedata(data):
    if data != None:
        folder = open('C:/Users/aslam/Desktop/qrscan/store/store.json', 'a')
        json.dump(data+'\n', folder)
    else:
        print('Scan first')
