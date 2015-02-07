#! /usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Raúl Jornet Calomarde'
__contact__ = 'rjornetc@openmailbox.org'
__copyright__ = 'Copyright © 2015, Raúl Jornet Calomarde'
__license__ = '''License GPLv3+: GNU GPL version 3 or any later
This program isfree software: you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the
Free Software Foundation, either version 3 of the License, or any later
version. This program is distributed  in the hope that it will be
useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
Public License for more details.
<http://www.gnu.org/licenses/>'''
__date__ = '06/02/2015'
__version__ = '1.3.1'

import sys, getopt

def regular(unity):
    return unity+unity+unity


def irregular(unity,j):
    unityVoid=''
    for i in range(0,j):
        unityVoid+=' '
    return unity+unityVoid+unity


def mod(a,b):
    if a%b<0:
        return a%b+b
    else:
        return a%b
      
      
def print_sponge(unity, iterations, unity_length):
      for i in range(0,3**iterations):
          current_unity=unity
          for j in range(0,iterations):
              if mod((i-3**j),(3**(j+1)))>=3**j:
                  current_unity=regular(current_unity)
              else:
                  current_unity=irregular(current_unity,3**j*unity_length)
          print current_unity


if __name__ == '__main__':

    iterations = 1
    unity = '█▊'
    unity_length = 2

    try:
        opts, args = getopt.getopt(sys.argv[1:],'hvi:u:l:',['help',
                                                            'version',
                                                            'iterations=',
                                                            'unity=',
                                                            'length='])
    except getopt.GetoptError:
        print('''menger.py [-h] [-v]
menget.py [-i <iterations>] [-u <unity>] [-l <length>]''')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print('''menger.py [-h] [-v]
menget.py [-i <iterations>] [-u <unity>] [-l <length>]''')
            sys.exit()
        elif opt in ('-v', '--version'):
            print ('py-menger ' + __version__ + '\n' +\
                   __copyright__ + '\n' +\
                   __license__)
            sys.exit()
        elif opt in ('-i', '--iterations'):
            iterations = int(arg)
        elif opt in ('-u', '--unity'):
            unity = str(arg)
        elif opt in ('-l', '--length'):
            unity_length = int(arg)
        
    print_sponge(unity, iterations, unity_length)