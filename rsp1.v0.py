import csv
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

curr_month = 0
DayIdx = 0
IdxLast = 0
RSP_cnt = 0
do_month = True
df = 0
RSP_Capital = 1000
RSP_units = 0
RSP_bal = 0
RSP_total_units = 0
RSP_close = 0

def rounddown100(x):
  return int(math.floor(x / 100.0)) * 100

def doRSP(index):
  global do_month
  global df
  global RSP_bal
  global RSP_total_units
  global RSP_close
  do_month = False
  #RSP_close = df.loc[[index]]['Close']
  RSP_close = df.iloc[index]['Close']
  RSP_fresh = RSP_Capital + RSP_bal
  RSP_units = rounddown100(RSP_fresh / RSP_close)
  RSP_total_units += RSP_units
  RSP_bal = round((RSP_fresh - (RSP_units * RSP_close)),2)
  print('[',RSP_cnt,'] > Fresh [', RSP_fresh, '] Add close: [', RSP_close, '] gets [', RSP_units, '] units + carry-over [', RSP_bal, '] and total units [',RSP_total_units,']')
  #print('done RSP')
  if RSP_bal < 0: 
  	print('ERROR, Balance is -ve')
  	exit()

#row_cnt = 1
#FileName = 'z74.csv'
#with open(sys.argv[1], 'rt') as f:
#with open(FileName, newline='') as f:
#  reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
#  try:
#    for row in reader:
    #global row_cnt
    #row_cnt += 1
#      pass
#  except csv.Error as e:
#    sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))        

def Results():
  global RSP_cnt
  global RSP_bal
  global RSP_total_units
  global RSP_Capital
  global RSP_close
  print('Total Fresh [', RSP_Capital * RSP_cnt, '] Units [', RSP_total_units, '] = Current Val [', RSP_total_units * RSP_close, '] Gain = [', (RSP_Capital * RSP_cnt)-(RSP_total_units * RSP_close), ']')

def Main():
  print('Starting')
  global EOD_Date
  global IdxLast
  global DayIdx
  global getDate
  global getMonth
  global curr_month
  global do_month
  global RSP_cnt
  global df

  # this section opens the data file
  df = pd.read_csv(sys.argv[1], sep=',')
  #df = pd.read_csv('z74.csv')
  EOD_Date = df['Date'].str.split('/',2,expand=True)
  #print(EOD_Date[0])
  IdxLast = EOD_Date.tail(1).index 

  # this section evaluates the date
  while DayIdx < IdxLast:
    getDate = int(EOD_Date[0][DayIdx])
    getMonth = int(EOD_Date[1][DayIdx])
    #print('(',DayIdx,')--------- [',getDate,'][',getMonth,']')
    if (curr_month != getMonth):
      do_month = True
      curr_month = getMonth
    if do_month == False:
      #print('did')
      pass
    else:
      if (getDate < 18):
        #print('wait')
        pass
      elif (getDate >= 18):
        #print('(',DayIdx,')--------- [',getDate,'][',getMonth,']')
        #print('date = ', getDate, ' + done RSP #',RSP_cnt)
        doRSP(DayIdx)
        RSP_cnt += 1
      else:
        print('XXXXXXXXXXXXX')
    DayIdx += 1
  print('End')
  Results()

Main()