import pickle
import dill # pip install dill

square = lambda x: x*x
# my_pickle = pickle.dumps(square)
my_pickle = dill.dumps(square)
print(my_pickle)