#import xml.etree.ElementTree as ET
import xml.etree.cElementTree as ET

def parseXML(xml_file):
    
    tree = ET.ElementTree(file=xml_file)
    print(tree.getroot())
    
    root = tree.getroot()
    print(f'tag={root.tag}, attrib={root.attrib}')
    
    for child in root:
        print(child.tag, child.attrib)
        
        if child.tag == 'appointment':
            for step_child in child:
                print(step_child.tag)
                
    
    print('-' * 40)
    print("Iterating using a tree iterator")
    print("-" * 40)
    
    iter_ = tree.getiterator()
    
    for elem in iter_:
        print(elem.tag)
        
    print('-' * 40)
    print("Processing child elements useing getchildren()")
    print("-" * 40)
    
    appointments= root.getchildren()
    
    for appointment in appointments:
        appt_children = appointment.getchildren()
        
        for appt_child in appt_children:
            print(f'{appt_child.tag}={appt_child.text}')
            
if __name__ == '__main__':
    parseXML('appt.xml')