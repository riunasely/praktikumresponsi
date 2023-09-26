import concurrent.futures
import logging
import time

class FakeDatabase:
    def __init__(self):
        self.value = 0
    
    def update(self, name):
        logging.info("Thread %s: memulai update", name)
        local_copy = self.value
        local_copy+=1
        time.sleep(0.1)
        self.value = local_copy
        logging.info("Thread %s: menyelesaikan update", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format,
                        level=logging.INFO,
                        datefmt="%H:%M:%S")
    
    database = FakeDatabase()
    logging.info("Mencoba update. Nilai awal adalah %d.", database.value)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(3):
            executor.submit(database.update, index)
    logging.info("Mencoba update. Nilai akhir adalah %d.", database.value)
