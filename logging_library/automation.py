import logging

logging.basicConfig(
    filename='deploy.log', 
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

a = 10
b = 0

try:
    c = a // b
    logging.info(f"{a} // {b} == {c}")
except ZeroDivisionError as e:
    logging.error("Error Dividing by Zero", exc_info=True)