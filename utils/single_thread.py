# -*- coding: utf-8 -*-
import time
import threading
import thread

class SingleThread(object):
        
    def __init__(self, func, func_args=(), encoding='gbk', failed_delay=2, max_retry=10):
        self.encoding = encoding        
        self.lock = thread.allocate()
        self.failed_delay = failed_delay
        self.max_retry = max_retry
        self.finished = False
        self.retry_times = 0
        self.worker_func = func
        self.func_args = func_args
        self.thread = threading.Thread(target=self._func)

    def run(self):
        self.thread.start()
        while(True):            
            # Successful finished
            if(self.finished and not self.thread.is_alive()):
                return

            # Max tries reach, failed the task
            if(not self.finished and self.retry_times >= self.max_retry):
                raise Exception('Max tries reach. Task failed.')            
            
            # Retry when max retry not reach
            if(not self.thread.is_alive() and not self.finished):
                # Sleep a while
                time.sleep(self.failed_delay)

                # Create a new thread, and run it
                self.thread = threading.Thread(target=self._func)
                self.thread.start()
                self.retry_times += 1
            
    def _func(self):
        if(self.lock.acquire()):
            print('Thread start...')
            try:            
                self.worker_func(*self.func_args)
                self.finished = True
            finally:
                self.lock.release()
            
if __name__ == '__main__':     

    def test_func(name):
        print('Hello, {name}'.format(name=name))

    worker = SingleThread(test_func, func_args=('Enix',))
    worker.run()
                    
