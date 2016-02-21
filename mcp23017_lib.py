#!/usr/bin/python
# Filename: mcp23017_lib.py
"""This module provides an easy interface for the MCP23017"""

__license__ = "GPLv3"

import smbus

i2c = smbus.SMBus(1)

DIRA = str(bin(i2c.read_byte_data(0x26, 0x00))).replace("0b", "").rjust(8, '0')
DIRB = str(bin(i2c.read_byte_data(0x26, 0x01))).replace("0b", "").rjust(8, '0')

LATA = str(bin(i2c.read_byte_data(0x26, 0x14))).replace("0b", "").rjust(8, '0')
LATB = str(bin(i2c.read_byte_data(0x26, 0x15))).replace("0b", "").rjust(8, '0')

OUT = 0
IN = 1
BANK_A = 0
BANK_B = 1
ALL = 2
LAT_A = 3
LAT_B = 4
HIGH = 1
LOW = 0

def dirRead(bank=-1):
   """
   Reads and returns the direction registers from both GPIO banks
   
   - **parameters**, **types** and **return**::
   
      :param bank: select which bank/s should be returned. Use BANK_A, BANK_B, ALL or leave blank
      for a default graphic diagram.
      :type bank: Integer.
      :return: returns the selected bank/s. If blank, a graphic diagram will be returned instead.
   """
   if(bank == BANK_A):
      print DIRA
   elif(bank == BANK_B):
      print DIRB
   elif(bank == ALL):
      print DIRA, DIRB
   else:
      print " --------"
      print DIRB[7] + "|8    9|" + DIRA[0]
      print DIRB[6] + "|7   10|" + DIRA[1]
      print DIRB[5] + "|6   11|" + DIRA[2]
      print DIRB[4] + "|5   12|" + DIRA[3]
      print DIRB[3] + "|4   13|" + DIRA[4]
      print DIRB[2] + "|3   14|" + DIRA[5]
      print DIRB[1] + "|2   15|" + DIRA[6]
      print DIRB[0] + "|1   16|" + DIRA[7]
      print " --------"

def latRead(bank=-1):
   """
   Reads and returns the latch registers from both GPIO banks

   - **parameters**, **types** and **return**::

      :param bank: select which latch/es should be returned. Use LAT_A, LAT_B, ALL or leave blank
      for a default graphic diagram.
      :type bank: Integer.
      :return: returns the selected latch/es. If blank, a graphic diagram will be returned instead.
   """
   if(bank == LAT_A):
      print LATA
   elif(bank == LAT_B):
      print LATB
   elif(bank == ALL):
      print LATA, LATB
   else:
      print " --------"
      print LATB[7] + "|8    9|" + LATA[0]
      print LATB[6] + "|7   10|" + LATA[1]
      print LATB[5] + "|6   11|" + LATA[2]
      print LATB[4] + "|5   12|" + LATA[3]
      print LATB[3] + "|4   13|" + LATA[4]
      print LATB[2] + "|3   14|" + LATA[5]
      print LATB[1] + "|2   15|" + LATA[6]
      print LATB[0] + "|1   16|" + LATA[7]
      print " --------"

def setup(pin, mode):
   """
   Writes direction (IN, OUT) based on pin number
   """
   global DIRA, DIRB
   if(str(pin).isdigit() and (0 < pin < 17)):
      if(mode == OUT or mode == IN):
         if(0 < pin < 9):
            DIRB = DIRB[0:pin - 1] + str(mode) + DIRB[pin:]
            i2c.write_byte_data(0x26, 0x01, int(DIRB, 2))
         elif(8 < pin < 17):
            DIRA = DIRA[0:(pin - 8) - 1] + str(mode) + DIRA[(pin - 8):]
            i2c.write_byte_data(0x26, 0x00, int(DIRA, 2))
      else:
         raise ValueError(str(mode) + " is not a valid mode")
   else:
      raise ValueError(str(pin) + " is not a valid pin number")

def output(pin, dir):
   """
   Writes state (HIGH, LOW) based on pin number
   """
   global LATA, LATB
   if(str(pin).isdigit() and (0 < pin < 17)):
      if(dir == HIGH or dir == LOW):
         if(0 < pin < 9):
            LATB = LATB[0:pin - 1] + str(dir) + LATB[pin:]
            i2c.write_byte_data(0x26, 0x15, int(LATB, 2))
         elif(8 < pin < 17):
            LATA = LATA[0:(pin - 8) - 1] + str(dir) + LATA[(pin - 8):]
            i2c.write_byte_data(0x26, 0x14, int(LATA, 2))
      else:
         raise ValueError(str(dir) + " is not a valid state")
   else:
      raise ValueError(str(pin) + " is not a valid number")
def input(pin):
   """
   Reads and returns pin state.
   """
   if(str(pin).isdigit() and (0 < pin < 17)):
      if(0 < pin < 9):
         out = str(bin(i2c.read_byte_data(0x26, 0x13))).replace("0b", "").rjust(8, '0')[pin - 1]
      elif(8 < pin < 17):
         out = str(bin(i2c.read_byte_data(0x26, 0x12))).replace("0b", "").rjust(8, '0')[pin - 9]
      return True if out == "1" else False
