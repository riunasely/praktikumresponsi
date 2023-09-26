import concurrent.futures
import logging
import threading
import time

class FakeDatabase:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def locked_update(self, name):
        logging.info("Thread %s: memulai update:", name)
        logging.debug("Thread %s tambahkan ke lock", name)
        with self._lock:
            logging.debug("Threading %s memiliki lock", name)
            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy
            logging.debug("Thread %s baru saja melepas lock", name)
        logging.debug("Thread %s: setelah melepas", name)
        logging.info("Thread %s: selesai update", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    database = FakeDatabase()
    logging.info("Testing locked update. Nilai awalnya adalah %d.", database.value)
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        for index in range (3):
            executor.submit(database.locked_update, index)
    logging.info("Testing locked update. Nilai akhirnya adalah %d.", database.value)
