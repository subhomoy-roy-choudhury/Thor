from speech import *
from heart_disease_predict import *
import subprocess


# num = take_command()
# num=float(num)
# num=num+12
# print(type(num))
# talk("The input is " + str(num))

def run():
    command = take_command()
    print(command)
    if 'stop' in command:
        exit()
    elif 'heart' in command:
       heart_disease_predict()
    elif 'hash' in command:
        proc=subprocess.Popen(["python","hash.py"])
    

if __name__ == '__main__':
    while True:
        run()
        
