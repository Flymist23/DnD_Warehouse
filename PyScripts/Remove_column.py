import csv

input_file = '\\DnD_Warehouse\\DnD_DataBuffers\\Raw_GitHub_Datatset.csv'
output_file = '\\DnD_Warehouse\\DnD_DataBuffers\\buffer.csv'
cols_to_remove = [1,2,4,17,19,20,21,23,24,28] # Column indexes to be removed (starts at 0)
# 5,6,8,18,26,27

cols_to_remove = sorted(cols_to_remove, reverse=True) # Reverse so we remove from the end first
row_count = 0 # Current amount of rows processed

with open(input_file, "r") as source:
    reader = csv.reader(source)
    next(reader, None)
    with open(output_file, "w+", newline='') as result:
        writer = csv.writer(result)
        for row in reader:
            for col_index in cols_to_remove:
                del row[col_index]
            writer.writerow(row)
    result.close()
source.close()


# "Name","Date","Just Class","Subclass","Level","Feats"
# ,"HP","AC","Str","Dex","Con","Int","Wis","Cha"
# ,"Skills","Processed Alignment","Processed Race", "Processed Spells", "Processed Weapons"
# 
# name, Race, BackG, Date, Class, JClass, SClass, lvl, Feats
# 0     1       2       3   4       5       6       7   8
# hp, AC, Str, Dex, Con, Int, Wis, Cha, Alignment, Skills, 
# 9     10   11  12  13    14    15  16      17      18
# Weapons, Spells, Day, P-Align, Good, Lawful, P-Race, P-Spells, P-Wep, LvlG
# 19        20      21      22    23    24      25      26          27    28 
# 
# we only want: 0, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 22, 25, 26, 27
#   don't want: 1,2,4,17,19,20,21,23,24,28

# 20622f,
# 2018-06-15T04:04:59Z,
# Fighter,
# Battle Master,
# 15,
# Crossbow Expert|Sharpshooter,
# 170,
# 16,
# 8,
# 20,
# 18,
# 9,
# 14,
# 10,
# Athletics|Perception|Survival|Intimidation,
# ,
# NA,
# NA,
# Elf,
# Crossbow,
# Heavy|Crossbow,
# Light,
# 12-15