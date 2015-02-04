#!/usr/bin/env python

# prepare environment
import datetime, psycopg2
from numpy import arange

# import visualizer
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

### demo 1: just plot something
print 'demo 1, started at %s' % str(datetime.datetime.now())

plt.plot([1,2,3])
plt.savefig('demo_matplotlib_1.png')

### demo 2: datetime-plot
print 'demo 2, started at %s' % str(datetime.datetime.now())

from matplotlib.dates import DayLocator, HourLocator, DateFormatter, drange

date1 = datetime.datetime( 2000, 3, 2)
date2 = datetime.datetime( 2000, 3, 6)
delta = datetime.timedelta(hours=6)
dates = drange(date1, date2, delta)

y = arange( len(dates)*1.0)

fig, ax = plt.subplots()
ax.plot_date(dates, y*y)

ax.set_xlim( dates[0], dates[-1] )

ax.xaxis.set_major_locator( DayLocator() )
ax.xaxis.set_minor_locator( HourLocator(arange(0,25,6)) )
ax.xaxis.set_major_formatter( DateFormatter('%Y-%m-%d') )

ax.fmt_xdata = DateFormatter('%Y-%m-%d %H:%M:%S')
fig.autofmt_xdate()

plt.savefig('demo_matplotlib_2.png')

### demo 3: database-connection and plot data
print 'demo 3, started at %s' % str(datetime.datetime.now())

import matplotlib.dates as mdates

years = mdates.YearLocator()
months = mdates.MonthLocator()
days = mdates.DayLocator()
hours = mdates.HourLocator()
minutes = mdates.MinuteLocator()
yearsFmt = mdates.DateFormatter('%Y')
daysFmt = mdates.DateFormatter('%Y-%m-%d')

cur = None

try:
   con = psycopg2.connect(host='123.456.789.123', database='db', user='dbuser', password='dbpassword') 
   cur = con.cursor()
   
   cur.execute('SELECT version()')
   version = cur.fetchone()
   print 'DB Server Version: %s' % version
   
   print "select data"
   
   cur.execute('SELECT timeutc FROM rinn_thal__temp1 WHERE scal != \'0\' ORDER BY timeutc ASC LIMIT 10000')
   t1_datestamps = cur.fetchall()
   cur.execute('SELECT scal FROM rinn_thal__temp1 WHERE scal != \'0\' ORDER BY timeutc ASC LIMIT 10000')
   t1_data = cur.fetchall()
   
   cur.execute('SELECT timeutc FROM rinn_thal__temp2 WHERE scal != \'0\' ORDER BY timeutc ASC LIMIT 10000')
   t2_datestamps = cur.fetchall()
   cur.execute('SELECT scal FROM rinn_thal__temp2 WHERE scal != \'0\' ORDER BY timeutc ASC LIMIT 10000')
   t2_data = cur.fetchall()
   
   cur.execute('SELECT timeutc FROM rinn_thal__hum1 WHERE scal != \'0\' ORDER BY timeutc ASC LIMIT 10000')
   h1_datestamps = cur.fetchall()
   cur.execute('SELECT scal FROM rinn_thal__hum1 WHERE scal != \'0\' ORDER BY timeutc ASC LIMIT 10000')
   h1_data = cur.fetchall()
   
   #dates = [q[0] for q in t1_datestamps]
   #opens = [q[0] for q in t1_data]
   
   fig, ax1 = plt.subplots()
   lns1 = ax1.plot_date(t1_datestamps, t1_data, '-', color='#FF4D4D', antialiased=True, label='temperature, sensor t1')
   lns2 = ax1.plot_date(t2_datestamps, t2_data, '-', color='#FF7373', antialiased=True, label='temperature, sensor t2')
   
   ax2 = ax1.twinx()
   lns3 = ax2.plot_date(h1_datestamps, h1_data, '-', color='#DADAFF', antialiased=True, label='humidity')
   
   ax1.set_ylabel('Temperature $^\circ$C', fontsize=11, color='#FF8080')
   ax2.set_ylabel(r"Humidity $\%$", fontsize=11, color='#DADAFF')
   
   ax1.tick_params(axis='both', which='major', labelsize=8)
   ax2.tick_params(axis='both', which='major', labelsize=8)
   
   ax1.set_ylim([0, 50])
   ax2.set_ylim([30, 80])
   
   #for label in ax2.get_yticklabels():
   #    label.set_color("red")
   
   lns = lns1+lns2+lns3
   labs = [l.get_label() for l in lns]
   ax1.legend(lns, labs, loc=0)
   
   #ax1.legend(bbox_to_anchor=(1.05, 1), loc=3, borderaxespad=0.)
   
   
   # format the ticks
   ax1.xaxis.set_major_locator(days)
   ax1.xaxis.set_major_formatter(daysFmt)
   ax1.xaxis.set_minor_locator(hours)
   ax1.autoscale_view()
   
   # format the coords message box
   def temperature(x): return '$%1.2f'%x
   ax1.fmt_xdata = mdates.DateFormatter('%Y-%m-%d')
   ax1.fmt_ydata = temperature
   ax1.grid(True)
   
   #fig.autofmt_xdate()
   plt.savefig('demo_matplotlib_3.png', dpi = 600)
   plt.savefig('demo_matplotlib_3.svg')

except psycopg2.DatabaseError, e:
   print 'Error %s' % e    
   sys.exit(1)

finally:
   if con:
	con.close()


