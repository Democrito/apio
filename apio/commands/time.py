# -*- coding: utf-8 -*-
# -- This file is part of the Apio project
# -- (C) 2016 FPGAwars
# -- Author Jesús Arroyo
# -- Licence GPLv2

import click

from apio.managers.scons import SCons

# Python3 compat
try:
    unicode = str
except NameError:  # pragma: no cover
    pass


@click.command('time')
@click.pass_context
@click.option('--board', type=unicode, metavar='board',
              help='Set the board')
@click.option('--fpga', type=unicode, metavar='fpga',
              help='Set the FPGA')
@click.option('--size', type=unicode, metavar='size',
              help='Set the FPGA type (1k/8k)')
@click.option('--type', type=unicode, metavar='type',
              help='Set the FPGA type (hx/lp)')
@click.option('--pack', type=unicode, metavar='package',
              help='Set the FPGA package')
def cli(ctx, board, fpga, pack, type, size):
    """Bitstream timing analysis."""

    # Run scons
    exit_code = SCons().time({
        'board': board,
        'fpga': fpga,
        'size': size,
        'type': type,
        'pack': pack
    })
    ctx.exit(exit_code)
