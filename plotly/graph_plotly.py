#! /usr/bin/python

# prepare environment
import sys, psycopg2, datetime

# import visualizer
import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in("plotlyuser", "plotlypass")

### demo 1: just plot something
print 'demo 1, started at %s' % str(datetime.datetime.now())

cur = None

try:
   con = psycopg2.connect(host='123.456.789.123', database='db', user='dbuser', password='dbpassword') 
   cur = con.cursor()
   
   cur.execute('SELECT version()')
   version = cur.fetchone()
   print 'DB Server Version: %s' % version
   
   print "select data"
   
   cur.execute('SELECT timeutc FROM rinn_thal__temp1 WHERE scal != \'0\' ORDER BY timeutc ASC')
   data_temp1_timeutc = cur.fetchall()
   cur.execute('SELECT scal FROM rinn_thal__temp1 WHERE scal != \'0\' ORDER BY timeutc ASC')
   data_temp1_scal = cur.fetchall()
   
   cur.execute('SELECT timeutc FROM rinn_thal__temp2 WHERE scal != \'0\' ORDER BY timeutc ASC')
   data_temp2_timeutc = cur.fetchall()
   cur.execute('SELECT scal FROM rinn_thal__temp2 WHERE scal != \'0\' ORDER BY timeutc ASC')
   data_temp2_scal = cur.fetchall()
   
   cur.execute('SELECT timeutc FROM rinn_thal__hum1 WHERE scal != \'0\' ORDER BY timeutc ASC')
   data_hum1_timeutc = cur.fetchall()
   cur.execute('SELECT scal FROM rinn_thal__hum1 WHERE scal != \'0\' ORDER BY timeutc ASC')
   data_hum1_scal = cur.fetchall()
   
   cur.execute('SELECT timeutc FROM rinn_thal__hum2 WHERE scal != \'0\' ORDER BY timeutc ASC')
   data_hum2_timeutc = cur.fetchall()
   cur.execute('SELECT scal FROM rinn_thal__hum2 WHERE scal != \'0\' ORDER BY timeutc ASC')
   data_hum2_scal = cur.fetchall()
   
   print "concatenate, %s' % str(datetime.datetime.now())
   
   trace1 = Scatter(x=data_temp1_timeutc, y=data_temp1_scal, name='t1', line=Line(color='FF8080'))
   trace2 = Scatter(x=data_temp2_timeutc, y=data_temp2_scal, name='t2', line=Line(color='FF8080'))
   trace3 = Scatter(x=data_hum1_timeutc, y=data_hum1_scal, name='rh1', yaxis='y2', fill='tozeroy', fillcolor='rgba(218, 218, 255, 0.3)', line=Line(color='rgba(218, 218, 255, 1)')) #DADAFF
   trace4 = Scatter(x=data_hum2_timeutc, y=data_hum2_scal, name='rh2', yaxis='y2', fill='tozeroy', fillcolor='rgba(230, 230, 255, 0.3)', line=Line(color='rgba(230, 230, 255, 1)')) #E6E6FF
   
   data = Data([trace1, trace2, trace3, trace4])
   
   layout = Layout(
    title='',
    yaxis=YAxis(title=u'temperature [\N{DEGREE SIGN}C]', titlefont=Font(color='rgb(FF, 80, 80)'), tickfont=Font(color='rgb(FF, 80, 80)'), overlaying='n', side='left'),
    yaxis2=YAxis(title='humididty [%]', titlefont=Font(color='rgb(DA, DA, FF)'), tickfont=Font(color='rgb(DA, DA, FF)'), overlaying='y', side='right')
    )

   print "upload start, %s' % str(datetime.datetime.now())
   
   fig = Figure(data=data, layout=layout)
   plot_url = py.plot(fig, filename='fifth')
   
   print "upload completed, %s' % str(datetime.datetime.now())
   
except psycopg2.DatabaseError, e:
   print 'Error %s' % e    
   sys.exit(1)

finally:
   if con:
	con.close()
