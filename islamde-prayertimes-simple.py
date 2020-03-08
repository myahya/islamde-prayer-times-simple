#!/usr/bin/python

import getopt, os, string, sys, time
from datetime import date

def representsInt(s):
  """
  Returns True if the passed string can be represents an integer, False
  otherwise.
  """
  try:
    int(s)
    return True
  except ValueError:
    return False

def getTodayLine(prayertimefile):
  """
  Returns the line corresponding to today's entry.
  """
  f = open(prayertimefile, 'r')

  today = date.today()
  month_name = today.strftime('%B')
  day_num = today.day

  while True:
    if month_name in f.readline():
      break;

  f.readline()
  f.readline()
  f.readline()

  print month_name
  print day_num

  day_line = ''
  while True:
    day_line = f.readline()
    parts = string.split(day_line)
    if not parts:
      continue
    current_day_num = parts[0]
    if representsInt(current_day_num) and int(current_day_num) == day_num:
      break

  f.close()
  print day_line
  return day_line


def main(argv):
  """
  Main.
  """

  if (len(argv) < 2) or (argv[0] != "-i"):
    print "Error expecting `python islamde-prayertimes-simple.py -i <file-name>`"
    sys.exit(-1)

  inputfile = argv[1]

  print 'Running with input file: ', inputfile

  print getTodayLine(inputfile)

if __name__ == "__main__":
  main(sys.argv[1:])