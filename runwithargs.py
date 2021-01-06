import os, sys
import time
from colorama import *
import time

init(convert=True)

# SECTION 1 -- DEFINE COMMAND LINE INTERFACE

def RWA_CLI(*args):
  
  os.system('cls')
  print(Fore.BLUE+ 'Run With Arguments - Copyright (c) 2020 EvilSquirrelGuy | All Rights Reserved')
  arguments = []
  try:
    if sys.argv[2] == 'raw':
      argument = input(Fore.BLUE + 'Enter arguments: ' + Fore.CYAN)
      os.system('%s %s' % (sys.argv[1], argument))
      print(Fore.GREEN + 'File executed, now exiting...')
      print(Fore.YELLOW + Back.RESET + 'Process terminated', end='')
      time.sleep(2)
      os.system('cls')
      exit()
  except Exception:
    print(Fore.YELLOW + Back.RESET + 'Process terminated', end='')
    time.sleep(2)
    os.system('cls')
    exit()
  
  print(Fore.BLUE + 'Enter "H" or "?" for help')
  while True:
    try:  
      rawcmd = input(Fore.BLUE + Back.RESET + 'Enter option: ' + Fore.CYAN)
      
      if rawcmd.lower() == 'h' or rawcmd == '?':
        
        print(Back.GREEN + Fore.WHITE + '''
******************* RWA Command Line Interface Help ********************
+---------+------------------------------------------------------------+
| COMMAND | FUNCTION                                                   |
+---------+------------------------------------------------------------+
| H or ?  | Shows this help page                                       |
| N or +  | Adds an argument to the execution                          |
| R or -  | Removes a previously added argument                        |
| RUN     | Runs the program with the arguments provided               |
| RAW     | Allows you to enter all the command line arguments manually|
| EX(IT)  | Exits the command line interface                           |
+---------+------------------------------------------------------------+\n''' + Back.RESET)
        
      elif rawcmd.lower() == 'n' or rawcmd == '+':
        print(Fore.MAGENTA + 'Argument ID:%s %s' % (Fore.CYAN, len(arguments)+1))
        argname = input(Fore.BLUE + 'Enter argument (including / or -) without value: ' + Fore.CYAN)
        argvalue = input(Fore.BLUE + 'Enter argument value (press return to skip): ' + Fore.CYAN)
        print(' ')
        
        if argvalue != '' and argvalue != None:
          argument = argname + ' ' + argvalue
        else:
          argument = argname
        arguments.append(argument)

      elif rawcmd.lower() == 'r' or rawcmd == '-':
        argId = int(input(Fore.BLUE + 'Enter ID of argument to remove: ' + Fore.CYAN))
        print(Fore.MAGENTA + 'Argument: ' + Fore.BLUE + arguments[argId-1])
        confirm = input(Fore.RED + 'Are you sure you want to delete this argument (N/y): ')
        print(Fore.BLUE, end='')
        if confirm.lower() == 'y':
          arguments.remove(arguments[argId-1])
          print(Fore.RED + 'Argument deleted' + Fore.BLUE)
        else:
          print('Deletion aborted')

      elif rawcmd.lower() == 'raw':
        print(Fore.RED + 'WARNING: Adding and removing arguments is no longer supported after using RAW\nTo skip, just press enter in the next prompt, otherwise only the RUN and EXIT commands will function properly' + Fore.BLUE)
        argument = input(Fore.BLUE + 'Enter arguments: ' + Fore.CYAN)
        if argument != '':
          arguments = argument

      elif rawcmd.lower() == 'exit' or rawcmd.lower() == 'ex':
        terminate = input(Fore.WHITE + Back.RED + '\nAre you sure you wish to exit the program (Y/n): ')
        if terminate.lower == 'n':
          continue
        elif terminate == '' or terminate.lower() == 'y':
          break
        else:
          continue

      elif rawcmd.lower() == 'run':
        temp=''
        for x in arguments:
          temp += x+' '
          
        os.system('%s %s' % (sys.argv[1], temp))
        temp=''
        break
  
    except KeyboardInterrupt:
      terminate = input(Fore.WHITE + Back.RED + '\nAre you sure you wish to exit the program (Y/n): ')
      if terminate.lower == 'n':
        continue
      elif terminate == '' or terminate.lower() == 'y':
        break
      else:
        continue
  print(Fore.YELLOW + Back.RESET + 'Process terminated', end='')
  time.sleep(2)
  os.system('cls')
  exit()



#SECTION 2 -- CHECK ARGUMENTS GIVEN AND EITHER SHOW HELP OR RUN COMMAND LINE INTERFACE

try:
  executable = sys.argv[1]
  test = open(executable) #check if file exists
  test.close()

except IndexError:
  print('=======================RUN WITH ARGUMENTS========================')
  print('Run with arguments is a script for running executables with')
  print('command line argumants, but without having to open powershell')
  print('and then open cmd.exe and type the executable path along with')
  print('all the arguments. RWA also allows you to save certain argument')
  print('combinations in a preferences file.\n')
  print('********* USAGE: ***********\n')
  print('RunWithArgs.py <executable path> [gui|nogui|raw]\n')
  print('gui - allows you to use a friendly GUI for easier usage')
  print('nogui - opens a terminal for you to simply type out all the arguments [default]')
  print('raw - allows you to just enter the arguments you want to run')
  input('Press return to exit...')
  exit()
  
except FileNotFoundError:
  print(Fore.RED + 'Invalid file name')
  input(Fore.BLUE + 'Press return to exit...')
  exit()

except Exception as e:
  print('The program failed to run: %s' % (e))

try:
  if sys.argv[2] == 'nogui' or sys.argv[2] == 'raw':
    raise IndexError('Not using GUI')
  elif sys.argv[2] == 'gui':
    print(Fore.RED + 'GUI is currently not supported\n')
    input(Fore.BLUE + 'Press return to exit...')
    exit()
except IndexError:
  print()
  RWA_CLI()
