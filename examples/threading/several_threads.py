import threading
import logging
import time

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)
    
    
if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    
    threads = list()
    
    for idx in range(5):
        logging.info(f'Main: create and start thread {idx}')
        x = threading.Thread(target=thread_function, args=(idx,))
        threads.append(x)
        x.start()
        
    for idx, thread in enumerate(threads):
        logging.info(f'Main: joining thread {idx}')
        thread.join()
        logging.info(f'Main: thread {idx} done')