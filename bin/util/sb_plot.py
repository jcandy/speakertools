#!/usr/bin/env python3

import sys
import os
import shutil
import numpy as np
import argparse
import textwrap
import matplotlib.pyplot as plt
from matplotlib import rc


# fonts
GFONTSIZE = 18
rc('text', usetex=True)
rc('font', size=GFONTSIZE)


def plotsetup(phase, linear, ext, title, xs, ys):
    """Set up plot frame and axis."""

    FHZ = r'$f\,(\mathrm{Hz})$'
    SPL = r'$\mathrm{SPL}\,\mathrm{(dB)}$'
    IMP = r'$|Z|\,(\Omega)$'
    TICKS = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]
    LABELS = [r'$10$', r'$20$', r'$50$', r'$100$', r'$200$', r'$500$',
              r'$1\mathrm{k}$', r'$2\mathrm{k}$', r'$5\mathrm{k}$',
              r'$10\mathrm{k}$', r'$20\mathrm{k}$']

    fig = plt.figure(figsize=(xs, ys))
    ax = fig.add_subplot(111)

    if title is not None:
        ax.set_title(r'$\mathrm{' + title + '}$', size=18)

    ax.grid(which="major", ls="-", alpha=0.4)
    ax.grid(which="minor", ls=":", alpha=0.4)
    ax.set_xlabel(FHZ)

    if linear:
        ax.set_xscale('linear')
    else:
        ax.set_xscale('log')
        ax.set_xticks(TICKS)
        ax.set_xticklabels(LABELS)

    if phase:
        ax.set_ylim(-180, 180)
        if ext.lower() == '.frd':
            ax.set_ylabel(r'$\arg(\mathrm{SPL}) ~ (\mathrm{degrees})$')
        else:
            ax.set_ylabel(r'$\arg(Z) ~ (\mathrm{degrees})$')
    else:
        if ext.lower() == '.frd':
            ax.set_ylabel(SPL)
        else:
            ax.set_ylabel(IMP)

    return fig, ax


def mycolor(i):
    """Generate distinct colors for multiple plot lines."""
    fr = fg = fb = 0.95
    t = np.pi / np.sqrt(3) * float(i)
    r = fr * np.cos(t)**4
    g = fg * np.cos(t + np.pi/4)**4
    b = fb * np.cos(t + np.pi/2)**4
    return (r, g, b)


def main():

    mytext = '''\
    description:
       sb --plot is a tool to plot frd (SPL data) and zma (impedance data) files.
    '''

    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        prog='sb --plot',
        description='Speakerbench Plot',
        epilog=textwrap.dedent(mytext))

    parser.add_argument('-c',
                        help='comma-separated list of frd or zma files',
                        metavar='FILES')

    parser.add_argument('-example',
                        help='Plot example (omit NAME to list available)',
                        nargs='?',
                        const='LIST',
                        metavar='NAME')
    parser.add_argument('-loc',
                        help='legend quadrant (1-4)',
                        type=int,
                        default=1)
    parser.add_argument('-amin',
                        help='amplitude minimum',
                        type=float,
                        default=None)
    parser.add_argument('-amax',
                        help='amplitude maximum',
                        type=float,
                        default=None)
    parser.add_argument('-fmin',
                        help='frequency minimum',
                        type=float,
                        default=10.0)
    parser.add_argument('-fmax',
                        help='frequency maximum',
                        type=float,
                        default=1e4)
    parser.add_argument('-o',
                        help='output (png,jpg,pdf,screen) | default: screen',
                        type=str,
                        default='screen')
    parser.add_argument('-gain',
                        help='comma-separated gain values',
                        type=str,
                        default=None)
    parser.add_argument('-t',
                        help='comma-separated legend text',
                        type=str,
                        default=None)
    parser.add_argument('-w',
                        help='comma-separated line widths',
                        type=str,
                        default=None)
    parser.add_argument('-phase',
                        help='toggle phase',
                        action='store_true')
    parser.add_argument('-title',
                        help='plot title',
                        type=str,
                        default=None)
    parser.add_argument('-linear',
                        help='linear frequency scale',
                        action='store_true')

    args = parser.parse_args()

    # Determine examples directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    examples_dir = os.path.join(script_dir, 'example_plot')

    # Handle -example option
    if args.example is not None:
        if args.example == 'LIST':
            print('Available examples:')
            for f in sorted(os.listdir(examples_dir)):
                if f.endswith('.frd') or f.endswith('.zma'):
                    print('   {}'.format(f))
            sys.exit(0)
        else:
            example_file = os.path.join(examples_dir, args.example)
            if not os.path.exists(example_file):
                print('ERROR: (sb --plot) Example {} not found'.format(args.example))
                sys.exit(1)
            # Copy example file to current working directory
            dest_file = os.path.join(os.getcwd(), args.example)
            shutil.copy(example_file, dest_file)
            print('INFO: (sb --plot) Copied {} to {}'.format(args.example, dest_file))
            myfiles = [dest_file]
    elif args.c is not None:
        myfiles = args.c.split(',')
    else:
        print('ERROR: (sb --plot) Must specify -c or -example')
        sys.exit(1)

    # Plot dimensions
    xs, ys = 12, 6
    name, ext = os.path.splitext(myfiles[0])
    fig, ax = plotsetup(args.phase, args.linear, ext, args.title, xs, ys)

    # Process datasets
    for p, x in enumerate(myfiles):
        try:
            # Detect header lines by finding first line with 3 numeric columns
            skip_lines = 0
            with open(x) as f:
                for line in f:
                    parts = line.split()
                    if len(parts) == 3:
                        try:
                            [float(val) for val in parts]
                            break
                        except ValueError:
                            pass
                    skip_lines += 1

            data = np.genfromtxt(x, skip_header=skip_lines)
        except FileNotFoundError:
            print('ERROR: (sb --plot) {} not found'.format(x))
            sys.exit(1)
        except Exception as e:
            print('ERROR: (sb --plot) Failed to parse {}: {}'.format(x, str(e)))
            sys.exit(1)

        freq = data[:, 0]
        g = 0.0 if args.gain is None else float(args.gain.split(',')[p])
        amp = data[:, 2] if args.phase else data[:, 1] + g

        if args.t is None:
            word = x.replace(r'_', r'\_')
            label = r'$\mathrm{' + word + '}$'
        else:
            label = r'$\mathrm{' + args.t.split(',')[p] + '}$'

        c0 = mycolor(p)
        s0 = '-'
        w0 = 1 if args.w is None else float(args.w.split(',')[p])

        ax.plot(freq, amp, linewidth=w0, label=label, color=c0, linestyle=s0)

    # Finalize plot
    ax.set_xlim(args.fmin, args.fmax)
    if args.amin is not None and args.amax is not None:
        ax.set_ylim(args.amin, args.amax)

    ax.legend(loc=args.loc)
    plt.tight_layout(pad=0.3)

    if args.o == 'screen':
        plt.show()
    else:
        plt.savefig(args.o)
        print('INFO: (sb --plot) Wrote plot to {}'.format(args.o))


if __name__ == '__main__':
    main()
