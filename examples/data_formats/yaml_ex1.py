# pip install pyyaml

import yaml

yaml_file = open('yaml_example.yml', 'r')
yaml_content = yaml.load(yaml_file)

print("Key: Value")
for key, value in yaml_content.items():
    print(f'{key}: {value}')
    
    
# .NAN, .inf, -.inf -> nan, inf -inf
# True, False, On, Yes, No, Off
# null, ~
'''
set: !!set
? 1
? 2
? 2
? 3
'''

'''Anchors:

data: &duplicate_data Hello

duplicate_data: *duplicate_data
'''