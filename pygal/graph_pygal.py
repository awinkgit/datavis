#! /usr/bin/python

# prepare environment
import psycopg2, datetime

# import visualizer
import pygal
from pygal.style import LightenStyle, LightColorizedStyle

### demo 1: just plot something
print 'demo 1, started at %s' % str(datetime.datetime.now())

# first demo copied from http://pygal.org/chart_types/#idbasic
line_chart = pygal.Line()
line_chart.title = 'Browser usage evolution (in %)'
line_chart.x_labels = map(str, range(2002, 2013))
line_chart.add('Firefox', [None, None, 0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
line_chart.add('Chrome',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
line_chart.add('IE',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
line_chart.add('Others',  [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])
line_chart.render_to_file('demo_pygal_1.svg')

### demo 2: database-connection and plot data
print 'demo 2, started at %s' % str(datetime.datetime.now())

cur = None

try:
   con = psycopg2.connect(host='123.456.789.123', database='db', user='dbuser', password='dbpassword') 
   cur = con.cursor()
   
   cur.execute('SELECT version()')
   version = cur.fetchone()
   print 'DB Server Version: %s' % version
   
   cur.execute('SELECT timeutc, scal FROM rinn_thal__temp1 WHERE scal != \'0\' ORDER BY timeutc ASC LIMIT 10000')
   t1 = cur.fetchall()
   #cur.execute('SELECT timeutc, scal FROM rinn_thal__temp1 WHERE scal != \'0\' ORDER BY timeutc ASC')
   #t2 = cur.fetchall()
   cur.execute('SELECT timeutc, scal FROM rinn_thal__hum1 WHERE scal != \'0\' ORDER BY timeutc ASC LIMIT 10000')
   h1 = cur.fetchall()
   
   dark_lighten_style = LightenStyle('#336676', base_style=LightColorizedStyle)
   
   datey = pygal.DateY(x_label_rotation=20, dots_size=1, order_min=-1, style=dark_lighten_style)
   datey.add("Temp1", t1)
   #datey.add("Temp2", t2)
   datey.add("Hum1", h1, secondary=True)
   
   datey.x_label_format = "%Y-%m-%d"
   datey.render_to_file('demo_pygal_2.svg')

except psycopg2.DatabaseError, e:
   print 'Error %s' % e    
   sys.exit(1)

finally:
   if con:
	con.close()
