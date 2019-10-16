import csv  
import json  
from io import StringIO

def JsonConvertIntoLineDeliniated(source,sink):
    from io import StringIO
    with open(source + ".json", "r") as read_file:
        data = json.load(read_file)


    result = [json.dumps(record) for record in data]
    with open("DnD_Data\\nd-proceesed-"+sink+".json", 'w+') as obj:
        for i in result:
            obj.write(i+'\n')

# Open the CSV  
f = open( 'DnD_DataBuffers\\buffer.csv', 'r' )  
# Change each fieldname to the appropriate field name. I know, so difficult.  
reader = csv.DictReader( f, fieldnames = ( "Name","Date","Just Class","Subclass","Level","Feats","HP","AC","Str","Dex","Con","Int","Wis","Cha","Skills","Processed Alignment","Processed Race", "Processed Spells", "Processed Weapons" ))  
# Parse the CSV into JSON                   20622f,2018-06-15T04:04:59Z,Fighter,Battle Master,15,Crossbow Expert|Sharpshooter,170,16,8,20,18,9,14,10,Athletics|Perception|Survival|Intimidation,,NA,NA,Elf,Crossbow,Heavy|Crossbow,Light,12-15
out = json.dumps( [ row for row in reader ] )  

# Save the JSON  
f = open( 'DnD_DataBuffers\\dnd_players.json', 'w+')  
f.write(out)  
f.close()
JsonConvertIntoLineDeliniated("DnD_DataBuffers\\dnd_players","dnd-players" )

