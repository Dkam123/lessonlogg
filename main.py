import logging
import other

logging.basicConfig(level="DEBUG", filename="mylogs.log",
                    format="%(asctime)s | %(levelname)s: %(message)s")


logger = logging.getLogger("image")
logger.setLevel("DEBUG")

def dowload_image():
    logger.debug("dowload")
    print("скачую")
    logger.info("скачався файл")
    other.test()
    print("скачався файл")
dowload_image()
def cals(a, b):
    c = a + b *2
    logging.debug(f"call function calc: {a} and {b} = {c}")
    return c

a = int(input("a= "))
b = int(input("b= "))
print(cals(a, b))

try:
    file = open("config.txt")
except Exception as e:
    logging.error("something wrong" + str(e))


with open("test", "w") as a:
    a.write("test")


#from contextlib import contextmanager
#@contextmanager
#def my_open(name_file, mode):
#    try:
        #file = open(name_file, mode)
#        a = "test my str"
#        yield a
#    except FileNotFoundError:
#        print("warnin file")
#    finally:
#        pass
#        file.close()

#with my_open("test0.txt", "r") as f:
#    print(f)