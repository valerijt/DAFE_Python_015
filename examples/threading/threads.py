import threading
import logging
import time


def thread_function(name):
    logging.info(f'Thread {name}: starting')
    time.sleep(3)
    logging.info(f'Thread {name}: finishng')
    
if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info('Main: before creating thread')
    
    x = threading.Thread(target=thread_function, args=(1,), daemon=True)
    logging.info('Main: Before running thread')
    
    x.start()
    logging.info('Main: Wait for the thread to finish')
    
    x.join()
    logging.info('Main: all done')