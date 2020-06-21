#!/usr/bin/env python
"""
Gcode cleaner to work around prusa slic3r annoyances for multi-filament
single-tool printing on non-Prusa printers.
This gist can be found here:
* https://gist.github.com/ex-nerd/22d0a9796f4f5df7080f9ac5a07a381f
Bugs this attempts to work around:
* https://github.com/prusa3d/Slic3r/issues/557
* https://github.com/prusa3d/Slic3r/issues/559
* https://github.com/prusa3d/Slic3r/issues/560
"""

import os
import re
import argparse


def comment(str):
    return '; ' + str

def rewrite(infile, outfile, verbose=False):
    WIPE = 1
    UNLOAD = 2
    LOAD = 3
    toolchange = 0
    priming = False
    temp_change = None
    for line in infile:
        # Priming
        if line.startswith('; CP PRIMING'):
            if 'START' in line:
                priming = True
            elif 'STOP' in line:
                priming = False
        # Detect toolchange state
        elif line.startswith('; CP TOOLCHANGE'):
            if 'WIPE' in line:
                toolchange = WIPE
            elif 'UNLOAD' in line:
                toolchange = UNLOAD
            elif 'LOAD' in line:
                toolchange = LOAD
            else:
                toolchange = 0

        # Process the various lines
        if line.startswith(';'):
            outfile.write(line)
        elif line.rstrip() in ('G4 S0', ):
            outfile.write(comment(line))
        elif line.startswith('M907 '):
            outfile.write(comment(line))
        elif priming:
            outfile.write(comment(line))
        elif toolchange in (LOAD, UNLOAD):
            if line.startswith('G1'):
                # Only remove integer-value E moves (part of the Prusa load/unload routine?)
                # The other E values appear to be part of the actual wipe tower.
                if re.search(r'E-?\d+\.0000', line):
                    outfile.write(comment(line))
                elif re.search(r'E-?\d+\.5000', line):
                    outfile.write(comment(line))
                else:
                    outfile.write(line)
            elif line.startswith('T'):
                outfile.write(line)
                if temp_change:
                    # Duplicate the last temperature change.
                    # https://github.com/prusa3d/Slic3r/issues/559
                    outfile.write(temp_change)
                    temp_change = None
            else:
                if line.startswith('M104 S'):
                    temp_change = line
                outfile.write(line)
        else:
            outfile.write(line)


def parse_args():
    parser = argparse.ArgumentParser(
        description='Gcode cleaner to work around some multi-extruder bugs in slic3r Prusa edition.'
    )
    parser.set_defaults(
        verbose=False,
        overwrite=False,
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help="Enable additional debug output",
    )
    parser.add_argument(
        '--overwrite',
        action='store_true',
        help="Overwrite the input file",
    )
    parser.add_argument(
        'filename',
        type=argparse.FileType('r'),
        nargs='+',
        help="One or more paths to .gcode files to clean",
    )
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    for infile in args.filename:
        infilename = infile.name
        tmpfilename = '{}.tmp{}'.format(*os.path.splitext(infilename))
        with open(tmpfilename, 'w') as tmpfile:
            rewrite(infile, tmpfile, args.verbose)
        if args.overwrite:
            outfilename = infilename
        else:
            outfilename = '{}{}'.format(*os.path.splitext(infilename))
        os.rename(tmpfilename, outfilename)
        print("{}\n  => {}".format(infilename, outfilename))
        infile.close()