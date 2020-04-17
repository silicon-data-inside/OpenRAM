# See LICENSE for licensing information.
#
# Copyright (c) 2016-2019 Regents of the University of California and The Board
# of Regents for the Oklahoma Agricultural and Mechanical College
# (acting for and on behalf of Oklahoma State University)
# All rights reserved.
#
import debug
import utils
from tech import GDS, layer
from tech import cell_properties as props
import bitcell_base


class dummy_bitcell_1w_1r(bitcell_base.bitcell_base):
    """
    A single bit cell which is forced to store a 0.
    This module implements the single memory cell used in the design. It
    is a hand-made cell, so the layout and netlist should be available in
    the technology library. """

    pin_names = [props.bitcell.cell_1w1r.pin.bl0,
                 props.bitcell.cell_1w1r.pin.br0,
                 props.bitcell.cell_1w1r.pin.bl1,
                 props.bitcell.cell_1w1r.pin.br1,
                 props.bitcell.cell_1w1r.pin.wl0,
                 props.bitcell.cell_1w1r.pin.wl1,
                 props.bitcell.cell_1w1r.pin.vdd,
                 props.bitcell.cell_1w1r.pin.gnd]
    type_list = ["OUTPUT", "OUTPUT", "INPUT", "INPUT",
                 "INPUT", "INPUT", "POWER", "GROUND"]
    (width, height) = utils.get_libcell_size("dummy_cell_1w_1r",
                                             GDS["unit"],
                                             layer["boundary"])
    pin_map = utils.get_libcell_pins(pin_names,
                                     "dummy_cell_1w_1r",
                                     GDS["unit"])

    def __init__(self, name=""):
        # Ignore the name argument
        bitcell_base.bitcell_base.__init__(self, "dummy_cell_1w_1r")
        debug.info(2, "Create dummy bitcell 1w+1r object")

        self.width = dummy_bitcell_1w_1r.width
        self.height = dummy_bitcell_1w_1r.height
        self.pin_map = dummy_bitcell_1w_1r.pin_map
        self.add_pin_types(self.type_list)


