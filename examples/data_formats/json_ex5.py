import json

z = 3 + 8j

# print(z.real)
# print(z.imag)
# 
# print(complex(3, 8) == z)

# print(type(z))
#json.dumps(z)

def encode_complex(z):
    if isinstance(z, complex):
        return (z.real, z.imag)
    else:
        type_name = z.__class__.name
        raise TypeError(f"Object of type '{type_name}' is not JSON serializable")
    
class ComplexEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, complex):
            return (z.real, z.imag)
        else:
            super().default(self, z)
            
# print(json.dumps(9 + 5j, cls=ComplexEncoder))
    
# print(json.dumps(9 + 5j, default=encode_complex))

# encoder = ComplexEncoder()
# print(encoder.encode(3+6j))

'''
{
    "__complex__": true,
    "real": 42,
    "imag": 36
}
'''

def decode_complex(dct):
    if "__complex__" in dct:
        return complex(dct["real"], dct["imag"])
    
    return dct

with open('complex_data.json', 'r') as complex_data:
    data = complex_data.read()
    z = json.loads(data, object_hook=decode_complex)
    
    print(z)
    print(type(z))