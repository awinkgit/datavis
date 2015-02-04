import matplotlib
matplotlib.use('Agg')

from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
import matplotlib.dates as dt
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.collections import PolyCollection
from matplotlib.colors import colorConverter

import psycopg2
con = psycopg2.connect(host='128.130.103.172', database='tuwien_zentrale', user='tuwienuser', password='Tuw13nus3R226')
cur = con.cursor()
cur.execute('SELECT timeutc FROM komozak_hka__spc_in_abs_uv ORDER BY timeutc ASC LIMIT 4')
time = cur.fetchall()
cur.execute('SELECT fingerprint FROM komozak_hka__spc_in_abs_uv ORDER BY timeutc ASC LIMIT 4')
fingerprint = cur.fetchall()

#WL_uvvis = [200.00, 202.50, 205.00, 207.50, 210.00, 212.50, 215.00, 217.50, 220.00, 222.50, 225.00, 227.50, 230.00, 232.50, 235.00, 237.50, 240.00, 242.50, 245.00, 247.50, 250.00, 252.50, 255.00, 257.50, 260.00, 262.50, 265.00, 267.50, 270.00, 272.50, 275.00, 277.50, 280.00, 282.50, 285.00, 287.50, 290.00, 292.50, 295.00, 297.50, 300.00, 302.50, 305.00, 307.50, 310.00, 312.50, 315.00, 317.50, 320.00, 322.50, 325.00, 327.50, 330.00, 332.50, 335.00, 337.50, 340.00, 342.50, 345.00, 347.50, 350.00, 352.50, 355.00, 357.50, 360.00, 362.50, 365.00, 367.50, 370.00, 372.50, 375.00, 377.50, 380.00, 382.50, 385.00, 387.50, 390.00, 392.50, 395.00, 397.50, 400.00, 402.50, 405.00, 407.50, 410.00, 412.50, 415.00, 417.50, 420.00, 422.50, 425.00, 427.50, 430.00, 432.50, 435.00, 437.50, 440.00, 442.50, 445.00, 447.50, 450.00, 452.50, 455.00, 457.50, 460.00, 462.50, 465.00, 467.50, 470.00, 472.50, 475.00, 477.50, 480.00, 482.50, 485.00, 487.50, 490.00, 492.50, 495.00, 497.50, 500.00, 502.50, 505.00, 507.50, 510.00, 512.50, 515.00, 517.50, 520.00, 522.50, 525.00, 527.50, 530.00, 532.50, 535.00, 537.50, 540.00, 542.50, 545.00, 547.50, 550.00, 552.50, 555.00, 557.50, 560.00, 562.50, 565.00, 567.50, 570.00, 572.50, 575.00, 577.50, 580.00, 582.50, 585.00, 587.50, 590.00, 592.50, 595.00, 597.50, 600.00, 602.50, 605.00, 607.50, 610.00, 612.50, 615.00, 617.50, 620.00, 622.50, 625.00, 627.50, 630.00, 632.50, 635.00, 637.50, 640.00, 642.50, 645.00, 647.50, 650.00, 652.50, 655.00, 657.50, 660.00, 662.50, 665.00, 667.50, 670.00, 672.50, 675.00, 677.50, 680.00, 682.50, 685.00, 687.50, 690.00, 692.50, 695.00, 697.50, 700.00, 702.50, 705.00, 707.50, 710.00, 712.50, 715.00, 717.50, 720.00, 722.50, 725.00, 727.50, 730.00, 732.50, 735.00, 737.50, 740.00, 742.50, 745.00, 747.50, 750.00]
WL_uv = [200.00, 201.00, 202.00, 203.00, 204.00, 205.00, 206.00, 207.00, 208.00, 209.00, 210.00, 211.00, 212.00, 213.00, 214.00, 215.00, 216.00, 217.00, 218.00, 219.00, 220.00, 221.00, 222.00, 223.00, 224.00, 225.00, 226.00, 227.00, 228.00, 229.00, 230.00, 231.00, 232.00, 233.00, 234.00, 235.00, 236.00, 237.00, 238.00, 239.00, 240.00, 241.00, 242.00, 243.00, 244.00, 245.00, 246.00, 247.00, 248.00, 249.00, 250.00, 251.00, 252.00, 253.00, 254.00, 255.00, 256.00, 257.00, 258.00, 259.00, 260.00, 261.00, 262.00, 263.00, 264.00, 265.00, 266.00, 267.00, 268.00, 269.00, 270.00, 271.00, 272.00, 273.00, 274.00, 275.00, 276.00, 277.00, 278.00, 279.00, 280.00, 281.00, 282.00, 283.00, 284.00, 285.00, 286.00, 287.00, 288.00, 289.00, 290.00, 291.00, 292.00, 293.00, 294.00, 295.00, 296.00, 297.00, 298.00, 299.00, 300.00, 301.00, 302.00, 303.00, 304.00, 305.00, 306.00, 307.00, 308.00, 309.00, 310.00, 311.00, 312.00, 313.00, 314.00, 315.00, 316.00, 317.00, 318.00, 319.00, 320.00, 321.00, 322.00, 323.00, 324.00, 325.00, 326.00, 327.00, 328.00, 329.00, 330.00, 331.00, 332.00, 333.00, 334.00, 335.00, 336.00, 337.00, 338.00, 339.00, 340.00, 341.00, 342.00, 343.00, 344.00, 345.00, 346.00, 347.00, 348.00, 349.00, 350.00, 351.00, 352.00, 353.00, 354.00, 355.00, 356.00, 357.00, 358.00, 359.00, 360.00, 361.00, 362.00, 363.00, 364.00, 365.00, 366.00, 367.00, 368.00, 369.00, 370.00, 371.00, 372.00, 373.00, 374.00, 375.00, 376.00, 377.00, 378.00, 379.00, 380.00, 381.00, 382.00, 383.00, 384.00, 385.00, 386.00, 387.00, 388.00, 389.00, 390.00, 391.00, 392.00, 393.00, 394.00, 395.00, 396.00, 397.00, 398.00, 399.00, 400.00, 401.00, 402.00, 403.00, 404.00, 405.00, 406.00, 407.00, 408.00, 409.00, 410.00, 411.00, 412.00, 413.00, 414.00, 415.00, 416.00, 417.00, 418.00, 419.00, 420.00]

time_conv = []

for t in time:
    time_conv.append(dt.date2num(t[0]))

print time_conv

zah = np.arange(0,len(time_conv),1)
print zah

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#for c, z in zip(['r', 'g', 'b', 'y'], [0, 10, 20, 30, 40]):
for ind in zah:
    xs = WL_uv
    ys = np.random.rand(len(WL_uv))
#    ys = np.squeeze(np.asarray(fingerprint[1]))
#    ys = 1
    ax.plot(xs, ys, zs=ind, alpha=0.8) # bei zs bzw ys muss timeconv rein aber da hats was mit float
#    ax.fill_between(xs, 0, 0)

#fig = plt.figure()
#ax1 = fig.add_subplot(111, projection='3d')
#ax1.plot_date(t1_datestamps, t1_data, 1, '-', color='#FF4D4D', antialiased=True, label='temperature, sensor t1')
#ax1.plot_date(t2_datestamps, t2_data, 2, '-', color='#FF7373', antialiased=True, label='temperature, sensor t2')


ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')



plt.savefig('3d_5.png', dpi = 600)
#plt.show()
