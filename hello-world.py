# import modules used here -- sys is a very standard one
import sys
import datetime

# Gather our code in a main() function
def main():
    greetings()
    showdate()
   
def greetings():
    print('Hello there', sys.argv[1], sys.argv[2])
    # Command line args are in sys.argv[1], sys.argv[2] ...
    # sys.argv[0] is the script name itself and can be ignored

def showdate():   
    now = datetime.datetime.now()
    print ("Current date and time : ", now.strftime("%Y-%m-%d %H:%M:%S"))
    print ("your time zone is  : " , now.utcnow().astimezone().tzinfo)        ### displays the local time zone
   
# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()