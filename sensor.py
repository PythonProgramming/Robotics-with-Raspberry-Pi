import RPi.GPIO as gpio
import time

def distance(measure='cm'):
    try:
        gpio.setmode(gpio.BOARD)
        gpio.setup(12, gpio.OUT)
        gpio.setup(16, gpio.IN)
        
        gpio.output(12, False)
        while gpio.input(16) == 0:
            nosig = time.time()

        while gpio.input(16) == 1:
            sig = time.time()

        tl = sig - nosig

        if measure == 'cm':
            distance = tl / 0.000058
        elif measure == 'in':
            distance = tl / 0.000148
        else:
            print('improper choice of measurement: in or cm')
            distance = None

        gpio.cleanup()
        return distance
    except:
        distance = 100
        gpio.cleanup()
        return distance

if __name__ == "__main__":
    print(distance("cm"))
