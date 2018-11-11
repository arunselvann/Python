import os, csv
import xml.etree.ElementTree as et
import re

file_name = 'C:/Users/arunatesan/Downloads/WORKFLOW_DEPLOYMENT_1.XML'
tree = et.parse(file_name)
root = tree.getroot()
targets = root.findall('REPOSITORY/FOLDER/TARGET')
for target in targets:
    if target.get('NAME') == 'SAFETY_ETL_CONTROL':
        print(target.get('NAME'))
        target_fields = target.findall('TARGETFIELD')
        for target_field in target_fields:
            print(target_field.get('NAME'),target_field.get('DATATYPE'),target_field.get('PRECISION'),target_field.get('SCALE'))
        print()


file_name1 = 'C:/Users/arunatesan/Downloads/safetyabc.hdbdd'
dict_data_type = {}
with open(file_name1) as f:
    for line in f:
        a = line.split()
        if len(a) > 0:
            if a[0].lower() == 'type':
                a = list(re.sub('[^A-Za-z0-9_]+', '', _) for _ in a)
                dict_data_type[a[1]] = a[2]
    print(dict_data_type)

with open(file_name1) as f:
    Entity = False
    Table_name = ''
    dict_col_list = {}
    for line in f:
        a = line.split()
        if len(a) > 0:
            a = list(re.sub('[^A-Za-z0-9_@]+', '', _) for _ in a)
            if a[0].lower() == 'entity':
                Entity = True
                Table_name = a[1]
            if Entity and a[0] != '' and a[0][0] != '@' and a[0].lower() != 'type' and a[0].lower() != 'key' and a[0].lower() != 'entity':
                try:
                    a.remove('')
                except ValueError:
                    pass
                dict_col_list[Table_name+':'+a[0]] = a[1]
    print(dict_col_list)

