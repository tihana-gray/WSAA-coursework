import requests
import csv
from xml.dom.minidom import parseString

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)
doc = parseString(page.content)

# check it works
#print(doc.toprettyxml())   # output to console — comment this out once you know it works

# if I want to store the xml in a file. You can comment this out later
#with open("trainxml.xml","w") as xmlfp:
    #doc.writexml(xmlfp)

#objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
#for objTrainPositionsNode in objTrainPositionsNodes:
    #traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
    #traincode = traincodenode.firstChild.nodeValue.strip()
    #print (traincode)
    
#objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
#for objTrainPositionsNode in objTrainPositionsNodes:
    # get latitude node
    #latNode = objTrainPositionsNode.getElementsByTagName("TrainLatitude").item(0)
    #latitude = latNode.firstChild.nodeValue.strip()

    #print(latitude)
    
#with open(r"C:\Users\tihan\OneDrive\Desktop\ATU\WSAA-coursework\labs\lab02.3-trains\week03_train.csv", mode='w', newline='') as train_file:
    #train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    #objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
    #for objTrainPositionsNode in objTrainPositionsNodes:
        #traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
        #traincode = traincodenode.firstChild.nodeValue.strip()

        #dataList = []
        #dataList.append(traincode)
        #train_writer.writerow(dataList)
        
retrieveTags=['TrainStatus',
'TrainLatitude',
'TrainLongitude',
'TrainCode',
'TrainDate',
'PublicMessage',
'Direction'
]


with open(r"C:\Users\tihan\OneDrive\Desktop\ATU\WSAA-coursework\labs\lab02.3-trains\trainxml.xml",
          "w",
          encoding="utf-8") as xmlfp:
    doc.writexml(xmlfp)


with open(r"C:\Users\tihan\OneDrive\Desktop\ATU\WSAA-coursework\labs\lab02.3-trains\week03_train.csv",
          mode='w',
          newline='',
          encoding="utf-8") as train_file:

    train_writer = csv.writer(train_file,
                              delimiter='\t',
                              quotechar='"',
                              quoting=csv.QUOTE_MINIMAL)

    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")

    for objTrainPositionsNode in objTrainPositionsNodes:

        dataList = []
        for retrieveTag in retrieveTags:
            datanode = objTrainPositionsNode.getElementsByTagName(retrieveTag).item(0)
            dataList.append(datanode.firstChild.nodeValue.strip())

        train_writer.writerow(dataList)







