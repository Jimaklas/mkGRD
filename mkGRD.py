# -*- coding: utf-8 -*-
from input import INP_FILENAME, OUT_FILENAME

inpf = open(INP_FILENAME, "r")
outf = open(OUT_FILENAME, "a")
for line in inpf:
    section, station, x, h = line.strip().split(",")
    x = float(x)
    h = float(h)

    if section:
        assert station
        station = float(station)
        outf.write("*\n")
        outf.write("%s      %.2f\n" % (section, station))
        outf.write("%.2f  %.2f\n" % (x, h))
    else:
        outf.write("%.2f  %.2f\n" % (x, h))

outf.write("*\n")
inpf.close()
outf.close()
