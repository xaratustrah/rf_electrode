#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
"""
Create a fully parametric model of an rf electrode

Design based on the following paper:

F. Caspers, CERN-ATS-Note-2011-075 TECH, http://cds.cern.ch/record/1380889

Using Open SCAD and solidpython

Xaratustra
2017-ä

"""
import os
from solid.utils import *

SEGMENTS = 400

cell_x = 40
cell_y = cell_x / 2
num_x = 4
num_y = 20


@bom_part("Piece", 0.20, currency="€", link="http://example.net", leftover=10)
def cell():
    slot_size = cell_y / 3

    a = square([cell_x, cell_y], center=True)
    c1 = circle(slot_size / 2)
    c2 = square([cell_x / 2, slot_size], center=True)
    hole = c2 + right(cell_x / 4)(c1) + left(cell_x / 4)(c1)
    a = a - hole \
        - forward(cell_y / 2)(left(cell_x / 2)(hole)) \
        - forward(cell_y / 2)(right(cell_x / 2)(hole)) \
        - back(cell_y / 2)(left(cell_x / 2)(hole)) \
        - back(cell_y / 2)(right(cell_x / 2)(hole))

    return a


def multiply_cell():
    a = cell()
    b = a
    for i in range(1, num_x):
        b += right(i * cell_x)(a)
    c = b
    for j in range(1, num_y):
        c += forward(j * cell_y)(b)
    return c


def add_taper(obj):
    vec = [[-cell_x / 2, -cell_y * 1 / 4],
           [cell_x * (num_x - 0.5), -cell_y * 1 / 4],
           [cell_x * (num_x - 1) / 2, -cell_x * (num_x - 0.5)]]
    tap1 = polygon(vec)
    tap2 = translate([0, (num_y - 1) * cell_y, 0])(mirror([0, 1, 0])(tap1))
    return obj + tap1 + tap2


def assembly():
    a = multiply_cell()
    return add_taper(a)


def finalize():
    a = assembly()
    a = linear_extrude(height=1, center=True)(a)
    a = color(Oak)(a)
    return a


if __name__ == '__main__':
    assert num_y >= 1 and num_x >= 1 and cell_x > 0

    out_dir = sys.argv[1] if len(sys.argv) > 1 else os.curdir
    filename_wo_ext = os.path.splitext(sys.argv[0])[0]
    file_out = os.path.join(out_dir, '{}.scad'.format(filename_wo_ext))

    obj = finalize()

    print("%(__file__)s: SCAD file written to: \n%(file_out)s" % vars())

    scad_render_to_file(obj, file_out, include_orig_code=True)
    # to the end of the generated
    # OpenSCAD code.
    bom = bill_of_materials(csv=True)
    print(bom)
