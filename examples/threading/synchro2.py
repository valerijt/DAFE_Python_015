import threading

sem = threading.Semaphore()

timer = threading.Timer(20.0, my_function)
timer.start()

timer.cancel()


barrier = threading.Barrier()