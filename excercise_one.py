import logging

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')


def division(number_one: int, number_two: int) -> int:
    

    try:
        div_number = number_one / number_two
        logging.debug(f"first input number {number_one} divided from second input number {number_two} and result is equal to {div_number}")
        return int(div_number)
    
    except ZeroDivisionError:
        logging.warning("Zero Division Error occured")

    except Exception as e:
        logging.warning(f"Error: {e}")
    

    
        

if __name__ == "__main__":

    number_one = int(input("Please enter first number: "))
    number_two = int(input("Please enter second number: "))

    division(number_one, number_two)


