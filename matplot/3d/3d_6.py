import matplotlib
matplotlib.use('Agg')

from mpl_toolkits.mplot3d import Axes3D
from matplotlib.collections import PolyCollection
from matplotlib.colors import colorConverter
import matplotlib.pyplot as plt
import numpy as np

import matplotlib.dates as dates

fig = plt.figure()
ax = fig.gca(projection='3d')

cc = lambda arg: colorConverter.to_rgba(arg, alpha=0.6)

WL_uv = [200.00, 201.00, 202.00, 203.00, 204.00, 205.00, 206.00, 207.00, 208.00, 209.00, 210.00, 211.00, 212.00, 213.00, 214.00, 215.00, 216.00, 217.00, 218.00, 219.00, 220.00, 221.00, 222.00, 223.00, 224.00, 225.00, 226.00, 227.00, 228.00, 229.00, 230.00, 231.00, 232.00, 233.00, 234.00, 235.00, 236.00, 237.00, 238.00, 239.00, 240.00, 241.00, 242.00, 243.00, 244.00, 245.00, 246.00, 247.00, 248.00, 249.00, 250.00, 251.00, 252.00, 253.00, 254.00, 255.00, 256.00, 257.00, 258.00, 259.00, 260.00, 261.00, 262.00, 263.00, 264.00, 265.00, 266.00, 267.00, 268.00, 269.00, 270.00, 271.00, 272.00, 273.00, 274.00, 275.00, 276.00, 277.00, 278.00, 279.00, 280.00, 281.00, 282.00, 283.00, 284.00, 285.00, 286.00, 287.00, 288.00, 289.00, 290.00, 291.00, 292.00, 293.00, 294.00, 295.00, 296.00, 297.00, 298.00, 299.00, 300.00, 301.00, 302.00, 303.00, 304.00, 305.00, 306.00, 307.00, 308.00, 309.00, 310.00, 311.00, 312.00, 313.00, 314.00, 315.00, 316.00, 317.00, 318.00, 319.00, 320.00, 321.00, 322.00, 323.00, 324.00, 325.00, 326.00, 327.00, 328.00, 329.00, 330.00, 331.00, 332.00, 333.00, 334.00, 335.00, 336.00, 337.00, 338.00, 339.00, 340.00, 341.00, 342.00, 343.00, 344.00, 345.00, 346.00, 347.00, 348.00, 349.00, 350.00, 351.00, 352.00, 353.00, 354.00, 355.00, 356.00, 357.00, 358.00, 359.00, 360.00, 361.00, 362.00, 363.00, 364.00, 365.00, 366.00, 367.00, 368.00, 369.00, 370.00, 371.00, 372.00, 373.00, 374.00, 375.00, 376.00, 377.00, 378.00, 379.00, 380.00, 381.00, 382.00, 383.00, 384.00, 385.00, 386.00, 387.00, 388.00, 389.00, 390.00, 391.00, 392.00, 393.00, 394.00, 395.00, 396.00, 397.00, 398.00, 399.00, 400.00, 401.00, 402.00, 403.00, 404.00, 405.00, 406.00, 407.00, 408.00, 409.00, 410.00, 411.00, 412.00, 413.00, 414.00, 415.00, 416.00, 417.00, 418.00, 419.00, 420.00]

#xs = np.arange(0, 10, 0.4)
xs = WL_uv

import psycopg2
con = psycopg2.connect(host='128.130.103.172', database='tuwien_zentrale', user='tuwienuser', password='Tuw13nus3R226')
cur = con.cursor()
cur.execute('SELECT timeutc FROM komozak_hka__spc_in_abs_uv ORDER BY timeutc ASC LIMIT 5')
time = cur.fetchall()
cur.execute('SELECT fingerprint FROM komozak_hka__spc_in_abs_uv ORDER BY timeutc ASC LIMIT 5')
fingerprint = cur.fetchall()

time_conv = []

for t in time:
    time_conv.append(dates.date2num(t[0]))

print time_conv

zs = [0.0, 1.0, 2.0, 3.0]
#zs = time_conv

verts = []

for z in zs:
    ys = np.random.rand(len(xs))
    ys[0], ys[-1] = 0, 0
    print list(zip(xs, ys))
    verts.append(list(zip(xs, ys)))

#print verts

poly = PolyCollection(verts, facecolors = [cc('r'), cc('g'), cc('b'),
                                           cc('y')])
poly.set_alpha(0.5)
ax.add_collection3d(poly, zs=zs, zdir='y')

ax.set_xlabel('X')
ax.set_xlim3d(200, 420)
ax.set_ylabel('Y')
ax.set_ylim3d(0,10)
ax.set_zlabel('Z')
#ax.set_zlim3d(auto=True)


plt.savefig('3d_6.png', dpi = 600)
