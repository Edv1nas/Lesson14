import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
# logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

def add_few_number(a: int, b:int) -> int:
    logging.warning(f"Recieved number: a:{a} and b:{b}")
    return a + b

add_few_number(a=6, b=7)

# def money_collected(amount: float) -> None:
#     logging.info(f"Amount money recieved: {20000}")
#     if amount == 0:
#         logging.warning("expected amount larger than 0")


# try:
#     # some code
# except Exception as e:
#     logging.error(f"Error received: {e}")

def emergency_stop(is_stop_event: bool) -> None:
    if is_stop_event:
        logging.critical(f"Had to stop device due to unexpected stop event")
        # func stop()

emergency_stop(True)