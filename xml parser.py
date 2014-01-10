import sys

import xml.etree.ElementTree as ET

tree = ET.parse('sample.xml')
root = tree.getroot()

print root.tag
    
for f in root.findall("food"):
    for i in f.iterfind('name'):
        if i.text == 'Belgian Waffles':
            i.set('asd','007')
            for j in f.iterfind('price'):             
                print 'using iterfind: food name=',i.text,'price=',j.text
                j.text = '$9.996'
            break
 
tree.write('sample.xml')  
    
    
    
    

        


    
    
