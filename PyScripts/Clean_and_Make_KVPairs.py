import json
import string
import re

input_file = 'DnD_Data\\nd-proceesed-dnd-players2.json'
output_file = 'DnD_Data\\nd-proceesed-dnd-players3.json'
# Dictionary Data is used for obtaining a single JSON object from the file and working with it 
data = {}
# raw lists are used to store data that can be made into CSV data to later be added to a table
raw_Classes = []
raw_Subclasses = []
raw_Feats = []
raw_Skills = []
raw_Spells = []
raw_Weapons = []
raw_Races=[]

processed_Classes = []
processed_Subclasses = []
processed_Feats = []
processed_Skills = []
processed_Spells = []
processed_Weapons = []
processed_Races=[]

raw_fields = []


def SplitData(raw_Lists, processed_List):
        for item in raw_Lists:
                item = set(item.split('|'))
                RetrieveList(item, processed_List)

def RetrieveList(setItems, processed_List):
        for word in setItems:
                if word in processed_List:
                        pass
                elif (word == "" or word == '' or word == '*' ):
                        pass
                else:
                        processed_List.append(word)
def AddToDictionary(parameter_list, fieldnames_List, filename):
        with open('DnD_Data\\nd-processed-dnd-' + filename + '.json', 'w+', newline= '') as f:
                count = 0
                while count < len(parameter_list):
                        data = {fieldnames_List[0]: count, fieldnames_List[1]: parameter_list[count]}
                        count = count +1
                        json.dump(data, f)
                        f.write('\n')


def AddToDictionary_2(parameter_list, fieldnames_List, filename, playerFile):
        data1 ={}
        data2 ={}

        with open('DnD_Data\\nd-processed-dnd-' + filename +'-bridge' +'.json', 'w+', newline= '') as f:
                with open('DnD_Data\\nd-processed-dnd-' + filename +'-helper' +'.json', 'w+', newline= '') as f2:

                                recordNum = 0
                                while recordNum < len(parameter_list):
                                        # if value is in field 
                                        data1 = {filename+'_'+fieldnames_List[0]: recordNum}

                                        countY = 1
                                        while countY < len(fieldnames_List):
                                                if fieldnames_List[countY] in parameter_list[recordNum] :
                                                        # enter field as true
                                                        data1.update({filename+'_'+fieldnames_List[countY]: True})
                                                else:
                                                        #  enter field as false
                                                        data1.update({filename+'_'+fieldnames_List[countY]: False})
                                                countY = countY + 1
                                        
                                        recordNum = recordNum +1
                                        json.dump(data1, f)
                                        
                                        f.write('\n')






                                recordNum = 0
                                # for each record
                                while recordNum < len(fieldnames_List)-1:
                                        # data3 = json.load(lines[lineNum])                          
                                        data2 = {fieldnames_List[0]: recordNum, filename+"_Name" : filename+'_'+fieldnames_List[recordNum]}
                                        # for record in PlayerFile:
                                        # data3[fieldnames_List[0]] = recordNum
                                        # if fieldnames_List[0] == data[fieldnames_List[0]]
                                                
                                        recordNum=recordNum+1
                                        json.dump(data2, f2)
                                        f2.write('\n')
                                
                                print(recordNum)


                                        

                                
                f2.close()
        f.close()

def ModifyPlayerRecords(fieldnames_List, playerFile, outputFile):
        lineNum = 0
        data3 ={}
        with open(playerFile , 'r+') as pf:
                with open(outputFile , 'w+') as of:
                        # for line in file add to list
                        for line in pf:
                                lineNum = lineNum + 1
                                data3 = json.loads(line)
                                # for record in list add to dictionary
                                        # -search for KvP
                                # change value in KvP to ordered number
                                for item in fieldnames_List:
                                
                                        data3[item] = lineNum      
      
                                # pf = data3.dumps([ row for row in reader ]) 
                                json.dump(data3, of)
                                of.write('\n')
                of.close()
        pf.close()



# def EditPlayers(parameter_list, fieldnames_List, playerFile, bridgeFile):
#         # for record in player File
#                 # for record in bridgeFile
#                         # if key from 
#         data3 ={}
#         data = {fieldnames_List[0]: recordNum}
#         pass

# collect all words for each Key
with open(input_file) as f:
        data = {}
        for line in f:
                data = json.loads(line)
                
                # collect all words for each Key   
                # for each word delimeted by | add to processed list (if word does not already exist)
                # Just Class (2)
                k = "Just Class"
                raw_Classes.append(data[k]) 
                
                # Subclass (3)
                        # has random |
                        # if there's whitespace before/after delimeter |, delete |
                        # if there's a word before and after delimeter |, make JSON array
                k = "Subclass"
                raw_Subclasses.append(data[k])
                # Feats (5)
                k = "Feats"
                raw_Feats.append(data[k])
                # Skills (14)
                k = "Skills"
                raw_Skills.append(data[k])
                # Processed Spells (17)
                k = "Processed Spells"
                raw_Spells.append(data[k])
                # Processed Weapons (18)
                k = "Processed Weapons"
                raw_Weapons.append(data[k])

                k = "Processed Race"
                raw_Races.append(data[k])
                data = {}
f.close()



SplitData(raw_Classes, processed_Classes)
SplitData(raw_Subclasses, processed_Subclasses)
SplitData(raw_Feats, processed_Feats)
SplitData(raw_Skills, processed_Skills)
SplitData(raw_Spells, processed_Spells)
SplitData(raw_Weapons, processed_Weapons)
SplitData(raw_Races, processed_Races)




# print(processed_Classes)
# print(processed_Subclasses)
# print(processed_Feats)
# print(processed_Skills)
# print(processed_Spells)
# print(processed_Weapons)

# will make a json file of IDs and Names for dimension table
fieldnames_List = ['classID','className']   
AddToDictionary(processed_Classes, fieldnames_List, 'classes')
print(processed_Classes)
print()
print(fieldnames_List)
fieldnames_List = ['subclassID','subclassName']   
AddToDictionary(processed_Subclasses, fieldnames_List, 'subclasses')
print()
print(processed_Subclasses)
print()
print(fieldnames_List)
fieldnames_List = ['featID','featName']   
AddToDictionary(processed_Feats, fieldnames_List, 'feats')
fieldnames_List = ['skillID','skillName']   
AddToDictionary(processed_Skills, fieldnames_List, 'skills')
fieldnames_List = ['spellID','spellName']   
AddToDictionary(processed_Spells, fieldnames_List, 'spells')
fieldnames_List = ['weaponID','weaponName']   
AddToDictionary(processed_Weapons, fieldnames_List, 'weapons')

# extract from each field into new record table 

Subclass_Bridge = []
Feats_Bridge = []
Skills_Bridge = []
Spells_Bridge = []
Weapons_Bridge = []



fieldnames_List = ['classID']
for fieldName in processed_Classes:
        fieldnames_List.append(fieldName)
AddToDictionary_2(raw_Classes, fieldnames_List, "class", input_file)

fieldnames_List = ['subclassID']
for fieldName in processed_Subclasses:
        fieldnames_List.append(fieldName)
AddToDictionary_2(raw_Classes, fieldnames_List, "subclass", input_file)

fieldnames_List = ['featID']
for fieldName in processed_Feats:
        fieldnames_List.append(fieldName)
AddToDictionary_2(raw_Classes, fieldnames_List, "feats", input_file)

fieldnames_List = ['skillID']
for fieldName in processed_Skills:
        fieldnames_List.append(fieldName)
AddToDictionary_2(raw_Classes, fieldnames_List, "skills", input_file)

fieldnames_List = ['spellID']
for fieldName in processed_Spells:
        fieldnames_List.append(fieldName)
AddToDictionary_2(raw_Classes, fieldnames_List, "spells", input_file)

fieldnames_List = ['weaponID']
for fieldName in processed_Weapons:
        fieldnames_List.append(fieldName)
AddToDictionary_2(raw_Classes, fieldnames_List, "weapons", input_file)

# list needs to change as Keys are much different in the player file
fieldnames_List = ["Just Class","Subclass","Feats","Skills","Processed Spells","Processed Weapons"]
ModifyPlayerRecords(fieldnames_List, input_file, output_file)



# Keys need to be renamed for BigQuery
def RenameKeys(parameter_list, fieldnames_List, Ifile): 
        with open(Ifile, "r+") as f:
                count = 0
                fileContent = f.read()
                while count < len(fieldnames_List):
                        fileContent = re.sub("\a*"+fieldnames_List[count]+"", ""+parameter_list[count]+"", fileContent.rstrip())
                        count = count + 1
                f.seek(0)
                f.truncate()
                f.write(fileContent)
        f.close()

def RenameAlignments(proc_L,Ifile):
        with open(Ifile, "r+") as f:

                fileContent = f.read()
                
                fileContent = re.sub("\a*(\"LG)", "\"1", fileContent.rstrip())
                fileContent = re.sub("\a*(\"LN)", "\"2", fileContent.rstrip())
                fileContent = re.sub("\a*(\"LE)", "\"3", fileContent.rstrip())

                fileContent = re.sub("\a*(\"NG)", "\"4", fileContent.rstrip())
                fileContent = re.sub("\a*(\"NN)", "\"5", fileContent.rstrip())
                fileContent = re.sub("\a*(\"NE)", "\"6", fileContent.rstrip())

                fileContent = re.sub("\a*(\"CG)", "\"7", fileContent.rstrip())
                fileContent = re.sub("\a*(\"CN)", "\"8", fileContent.rstrip())
                fileContent = re.sub("\a*(\"CE)", "\"9", fileContent.rstrip())
                count = 0
                while count < len(proc_L):
                        fileContent = re.sub("\a*(\""+proc_L[count]+"\")", ""+str(count)+"", fileContent.rstrip())
                        count = count + 1

                        
                
                f.seek(0)
                f.truncate()
                f.write(fileContent)

        f.close()



fieldnames_List = ["Name","Date","Just Class","Subclass","Level","Feats","Skills","Processed Alignment","Processed Race","Processed Spells","Processed Weapons"]
parameter_list = ["Players_Name","Players_Date_Created","Players_Classes","Players_Subclasses","Players_Level","Players_Feats","Players_Skills","Players_Alignment","Players_Race","Players_Spells","Players_Weapons"]
RenameKeys(parameter_list,fieldnames_List, output_file)

RenameAlignments(processed_Races, output_file)