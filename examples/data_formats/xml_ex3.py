import time
import xml.etree.ElementTree as ET

def editXML(filename):
    tree = ET.ElementTree(file=filename)
    root = tree.getroot()
    
    for begin_time in root.iter("begin"):
        begin_time.text = time.ctime(int(begin_time.text))
        
    tree = ET.ElementTree(root)
    tree.write('updated.xml')
    
if __name__ == '__main__':
    editXML('appt.xml')