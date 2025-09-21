import logging
from time import sleep

logging.basicConfig(level=logging.INFO)

def your_first_function():
    logging.info("Picker is AI powered Smart System that supports Web3.")
    sleep(1)
    logging.warning("This is a test warning message.")
    sleep(1)
    logging.error("This is a test error message.")

# main.py
def main():
    your_first_function()

if __name__ == '__main__':

    main()
