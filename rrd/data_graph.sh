#!/bin/bash

WEATHERPATH=/home/pi/datavis/rrd
FAXIS=8

current_time=$(date "+%Y.%m.%d, %H:%M:%S")
current_timefile=$(date "+%Y-%m-%d_%H%M%S")
starttime="20140930"
endtime="20141013"
W=1024
H=600

date

pt=$(date +"%s")

rrdtool graph $WEATHERPATH/demo_rrd.png --start $starttime --end $endtime \
--width $W --height $H --y-grid 5:1 --x-grid MINUTE:720:HOUR:24:HOUR:24:0:%Y.%m.%d \
--slope-mode \
--title "$1" \
--vertical-label "temperature [°C]" \
--right-axis 1:30 \
--right-axis-label "humidity [%]" \
--upper-limit 50 --lower-limit 0 --rigid \
--color CANVAS#FFFFFF --color BACK#FFFFFF --color GRID#CDCDCD --color MGRID#B3B3B3 --color SHADEA#FFFFFF --color SHADEB#FFFFFF \
--grid-dash 3:1 \
--font DEFAULT:11:DroidSansMono \
--font TITLE:14:DroidSansMono \
--font AXIS:$FAXIS:DroidSansMono \
--font UNIT:12:DroidSansMono \
--font WATERMARK:8:DroidSansMono \
--disable-rrdtool-tag \
DEF:t1=$WDE1PATH/weather_wde1.rrd:temps1:AVERAGE \
DEF:tmin1=$WDE1PATH/weather_wde1.rrd:temps1:MIN \
DEF:tmax1=$WDE1PATH/weather_wde1.rrd:temps1:MAX \
DEF:rh1=$WDE1PATH/weather_wde1.rrd:hums1:AVERAGE \
DEF:t2=$WDE1PATH/weather_wde1.rrd:temps2:AVERAGE \
DEF:tmin2=$WDE1PATH/weather_wde1.rrd:temps2:MIN \
DEF:tmax2=$WDE1PATH/weather_wde1.rrd:temps2:MAX \
DEF:rh2=$WDE1PATH/weather_wde1.rrd:hums2:AVERAGE \
DEF:t3=$WDE1PATH/weather_wde1.rrd:temps3:AVERAGE \
DEF:tmin3=$WDE1PATH/weather_wde1.rrd:temps3:MIN \
DEF:tmax3=$WDE1PATH/weather_wde1.rrd:temps3:MAX \
CDEF:rh1_e=rh1,10,- \
CDEF:rh2_e=rh2,10,- \
LINE:-20 \
COMMENT:"humidity\:\n" \
COMMENT:"     " \
AREA:rh1_e#DADAFF:"ambient rh1        ":STACK \
GPRINT:rh1:LAST:"%8.0lf    %% act," \
GPRINT:rh1:MIN:"%8.0lf    %% min," \
GPRINT:rh1:MAX:"%8.0lf    %% max," \
GPRINT:rh1:AVERAGE:"%8.0lf    %% in Ø\n" \
LINE:-20 \
COMMENT:"     " \
AREA:rh2_e#E6E6FF:"cabinet rh2        ":STACK \
GPRINT:rh2:LAST:"%8.0lf    %% act," \
GPRINT:rh2:MIN:"%8.0lf    %% min," \
GPRINT:rh2:MAX:"%8.0lf    %% max," \
GPRINT:rh2:AVERAGE:"%8.0lf    %% in Ø\n" \
LINE:-20 \
LINE1:rh1_e#8080FF::STACK \
LINE:-20 \
LINE1:rh2_e#7070FF::STACK \
\
LINE1:0#FFB3B3 \
COMMENT:"temperature\:\n" \
COMMENT:"     " \
LINE1:t1#ff8080:"ambient, sensor t1 ":dashes=5,3 \
GPRINT:t1:LAST:"%10.1lf °C act," \
GPRINT:t1:MIN:"%10.1lf °C min," \
GPRINT:t1:MAX:"%10.1lf °C max," \
GPRINT:t1:AVERAGE:"%10.1lf °C in Ø\n" \
\
COMMENT:"     " \
LINE1:t3#ff8080:"ambient, sensor t2 ":dashes=5,3 \
GPRINT:t3:LAST:"%10.1lf °C act," \
GPRINT:t3:MIN:"%10.1lf °C min," \
GPRINT:t3:MAX:"%10.1lf °C max," \
GPRINT:t3:AVERAGE:"%10.1lf °C in Ø\n" \
\
COMMENT:"     " \
CDEF:tout=t1,t3,+,2,/ \
CDEF:rhout=rh1,rh2,+,2,/ \
VDEF:avgtout=tout,AVERAGE \
LINE2:tout#ff4D4D:"ambient, avg       " \
GPRINT:tout:LAST:"%10.1lf °C act," \
GPRINT:tout:MIN:"%10.1lf °C min," \
GPRINT:tout:MAX:"%10.1lf °C max," \
GPRINT:tout:AVERAGE:"%10.1lf °C in Ø" \
LINE1:avgtout#FFB3B3:" \n":dashes=15,5 \
\
CDEF:trendt1=t1,86400,TREND \
LINE1:trendt1#FF8080::dashes=5,10 \
\
CDEF:tau1=243.12,17.62,t1,*,243.12,t1,+,/,rh1,100,/,LOG,1,EXP,LOG,/,+,*,17.62,243.12,*,243.12,t1,+,/,rh1,100,/,LOG,1,EXP,LOG,/,-,/ \
CDEF:tauout=243.12,17.62,tout,*,243.12,tout,+,/,rhout,100,/,LOG,1,EXP,LOG,/,+,*,17.62,243.12,*,243.12,t1,+,/,rhout,100,/,LOG,1,EXP,LOG,/,-,/ \
COMMENT:"     " \
LINE1:tau1#FFCDCD:"dew point using t/rh 1  " \
GPRINT:tau1:LAST:"%5.1lf °C act\n" \
\
LINE:0 \
\
COMMENT:"difference t2 - t1\:" \
CDEF:diff1=t3,t1,- \
GPRINT:diff1:LAST:"%5.1lf °C act\n" \
\
COMMENT:"ambient temperature" \
AREA:2#B3B3FF:"below  /":STACK \
CDEF:toutvsavg=tout,avgtout,GE,2,0,IF \
LINE:0 \
AREA:toutvsavg#FFB3B3:"above average\n":STACK 

date

exit 0
