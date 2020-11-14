import concurrent.futures
import threading
import logging
import time

class FakeDatabase:
    
    def __init__(self):
        self.value = 0
        
    def update(self, name):
        logging.info("Thread %s: starting update", name)
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy
        logging.info("Thread %s: finishing update", name)
    
if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    
    database = FakeDatabase()
    logging.info(f'Testing update. Starting value is {database.value}')
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for idx in range(2):
            executor.submit(database.update, idx)
            
    logging.info(f'Testing update. Ending value is {database.value}')