
# local cloned repository required: https://github.com/oganm/dnddata

# code obtained from, https://stackoverflow.com/questions/29759305/how-do-i-convert-a-tsv-to-csv
import re
tsv = open('From_GitHub\\uniqueTable.tsv', 'r')
fileContent =  tsv.read()

# fileContent = re.sub("", r'\1', fileContent.rstrip())

 # escape all especial charaters (" ' ,) rfc4180
fileContent = re.sub("\\u00e2\\u20ac\\u2122", "", fileContent.rstrip())

fileContent = re.sub("(\a*\t)", ">", fileContent) # convert from tab to >
fileContent = re.sub("""(?ism)(,)""", r'\1', fileContent)
fileContent = re.sub("(\a*>)", ",", fileContent) # convert from tab to >

fileContent = re.sub("\|(,)", r'\1', fileContent.rstrip())
fileContent = re.sub("(Fighter) 1",  r'\1', fileContent.rstrip())


fileContent = re.sub("(,)\|", r'\1', fileContent.rstrip())
fileContent = re.sub(",( )", r'\1', fileContent.rstrip())
fileContent = re.sub("\a*(Crossbow),(Heavy|heavy)", "Heavy CBow", fileContent.rstrip())
fileContent = re.sub("\a*((Crossbow),(hand|Hand)|(hand|Hand) Crossbow)", "Hand CBow", fileContent.rstrip())
fileContent = re.sub("\a*((Crossbow),(Light|light)(Crossbow))", "Light CBow", fileContent.rstrip())
fileContent = re.sub("\a*(Crossbow)", "CBow", fileContent.rstrip())

fileContent = re.sub("(,)NA", r'\1', fileContent.rstrip())
fileContent = re.sub("(,) ", r'\1', fileContent.rstrip())
fileContent = re.sub("(,)\*", r'\1', fileContent.rstrip())
fileContent = re.sub("\*", "_", fileContent.rstrip())
fileContent = re.sub(" ", "", fileContent.rstrip())

csv_file = open("DnD_DataBuffers\Raw_GitHub_Datatset.csv", "w+")
csv_file.write(fileContent)
csv_file.close()
