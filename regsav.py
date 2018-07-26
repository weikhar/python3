# find out the value of Regular Savings Plan by pumping in a fixed amount per month, 
# and use the available fund to buy units of the same stock.
# takes in stock's historical EOD prices, the monthly amount, 
# at the same date each month (or the nearest following trading day), 
# using the close price of the trade day
# this script does not account for dividend reinvestment

# 
# specify the CSV input file  in the command line arguement
# run this script by: py regsav.py <datafile.csv>
# * <datafile.csv> is comma seperated with columns [D, O, H, L, C, AC, V]
# output file will be the input filename pre-pended with 'out_'
# 

import csv
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

RSP_Capital     = 1000				    # invest this amount every month
RSP_Trade_Date  = 18              # trade on this day every month, or the next earliest trading day
ofilename = 'out_' + sys.argv[1]  #file name for the output file
img_name =  sys.argv[1].replace('.', '_') + '.png'

curr_month      = 0               # store of current month; if month is changed, store int(new month), and set do_month = True
do_month        = True            # true if not yet done RSP for the month; false after done
DayIdx          = 0               # marker for data index
IdxLast         = 0               # marker for last index of data
RSP_cnt         = 1               # count number of RSP cycles
df              = 0               # pandas dataframe placeholder
RSP_units       = 0               # number of units for this RSP
RSP_bal         = 0               # balance amount after purchase RSP_units
RSP_total_units = 0               # accumulated total numer of RSP_units
Pclose          = 0               # EOD price
RSP_avg_cost    = 0               # average cost of RSP_total_units
RSP_unit_Pdelta = 0               # EOD price - RSP_avg_cost; (+ve ? Gain : Loss)
RSP_curr_cgain  = 0               # total current gain
RSP_curr_loss   = 0               # total current loss
RSP_curr_val    = 0               # total current value of RSP_total_units



#df2 = pd.DataFrame(columns=['Date','Fresh','P.close','New Units', 'Carry-over', 'Total Units'])
COLUMNS = ['Cnt','Date','Available','P.close','New Units', 'Carry-over', 'Total Units', 'Avg Cost','RSP_unit_Pdelta','RSP_curr_val']
rsp_array = []

# minimum number of units to be purchased >= 100
def rounddown100(x):
  return int(math.floor(x / 100.0)) * 100

def doRSP(index):
  global do_month
  global df
  global RSP_bal
  global RSP_total_units
  global Pclose
  global df2
  global rsp_array
  global RSP_curr_cgain
  global RSP_curr_loss
  global RSP_curr_val

  do_month = False
  Pclose = df.iloc[index]['Close']
  AvailableAmt = RSP_Capital + RSP_bal
  RSP_units = rounddown100(AvailableAmt / Pclose)
  RSP_total_units += RSP_units
  RSP_bal = round((AvailableAmt - (RSP_units * Pclose)),2)
  if (RSP_total_units > 0):
    RSP_avg_cost = round(((RSP_Capital * RSP_cnt) / RSP_total_units), 3)
  else:
  	RSP_avg_cost = 0
  RSP_unit_Pdelta = round((Pclose - RSP_avg_cost),2)
  if (RSP_unit_Pdelta > 0):
    RSP_curr_cgain += 1
  elif (RSP_unit_Pdelta < 0):
  	RSP_curr_loss += 1
  else:
    pass
  RSP_curr_val = round((RSP_total_units * Pclose),2)
  print('[' + str(RSP_cnt) + '] (' + df.iloc[index]['Date'] + ') > Avail [' + str(AvailableAmt) + '] for P.close [' + str(Pclose) + '] gets [' + str(RSP_units) + '] units + carry-over [' + str(RSP_bal) + '] and total units [' + str(RSP_total_units) + ']')
  rsp_array.append([RSP_cnt,df.iloc[index]['Date'], AvailableAmt, Pclose, RSP_units, RSP_bal, RSP_total_units, RSP_avg_cost,RSP_unit_Pdelta,RSP_curr_val])
  #print('done RSP')
  if RSP_bal < 0: 
    print('XXXXXX ERROR #1 [-ve balance] XXXXXXX')
    exit()

#row_cnt = 1
#FileName = 'z74.SI.csv'
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
  global Pclose
  global df2
  global rsp_array
  #print(rsp_array)
  my_rsp = np.array(rsp_array, dtype=object)
  #print(my_rsp)
  df2 = pd.DataFrame(data=my_rsp[:],columns=COLUMNS)
  df2 = df2.drop(['Cnt'], axis=1)
  print(df2)

  RSP_curr_cost = RSP_Capital * RSP_cnt
  RSP_curr_val = round((RSP_total_units * Pclose),2)
  RSP_gain = round((RSP_curr_val - RSP_curr_cost),2)
  RSP_gain_pct = round((RSP_gain / RSP_curr_cost * 100),2)
  print('Amt Available [' + str(RSP_curr_cost) + '] Units [' + str(RSP_total_units) + '] = Current Val [' + str(RSP_curr_val) + '] Total Gain = [' + str(RSP_gain) + '] = [' + str(RSP_gain_pct) + ']% Avg Gain.pa [' + str(round((RSP_gain_pct/(RSP_cnt//12)),2)) + ']%.pa')
  print('Total intervals [' + str(RSP_cnt) + '] Total InFlow [' + str(RSP_curr_cost) + '] Avg Cost per unit [' + str(round((RSP_curr_cost/RSP_total_units),3)) + '] W:L = [' +  str(RSP_curr_cgain) + ']:[' + str(RSP_curr_loss) + ']')
  #df2.plot(x='Avg Cost', y='col_name_2', style='o')
  
  df2.plot(y=['P.close','Avg Cost'])
  plt.xlabel('Months')
  plt.ylabel('Price')
  plt.title(img_name)
  plt.savefig(img_name)
  df2.to_csv(ofilename, sep=',')
  plt.show()

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
  global Pclose

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
      if (getDate < RSP_Trade_Date):
        #print('wait')
        pass
      elif (getDate >= RSP_Trade_Date):
        #print('(',DayIdx,')--------- [',getDate,'][',getMonth,']')
        #print('date = ', getDate, ' + done RSP #',RSP_cnt)
        if not math.isnan(df.iloc[DayIdx]['Close']):
          doRSP(DayIdx)
          RSP_cnt += 1
        else:
          print('Check Data valid: p.close [' + str(Pclose) + ']')
      else:
        print('XXXXXX ERROR #2 XXXXXXX')
    DayIdx += 1
  print('End')
  Results()

Main()