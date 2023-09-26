import threading
import time

def print_cube(num):
	"""
	fungsi untuk mencetak kubus dengan sisi $num
	"""
	print("Kubus: {}".format(num*num*num))
	#time.sleep(2)

def print_square(num):
	"""
	fungsi untuk mencetak persegi dengan sisi $num
	"""
	print("Square: {}".format(num*num))
	#time.sleep(2)

if __name__ == "__main__":
	t1 = threading.Thread(target=print_square, args=(10,))
	t2 = threading.Thread(target=print_cube, args=(10,))

	t1.start()
	t2.start()

	t1.join()

	print("Done!")
