#!/usr/bin/env python3

import argparse
import json
import os
import shutil
import subprocess
import sys
import numpy as np
import textwrap


def wrap_latex(internals, border, bipole, scale):
    """Wrap circuit drawing commands with LaTeX document structure."""

    latex = r"""\documentclass{{article}}
\usepackage[active,tightpage]{{preview}}
\setlength{{\PreviewBorder}}{{{}pt}}
\usepackage{{tikz}}
\usepackage{{circuitikz}}
\usepackage{{siunitx}}
\usepackage{{amsfonts}}

\begin{{document}}
\begin{{preview}}
\ctikzset{{bipoles/length={}cm}}
\begin{{circuitikz}}[scale={}]
""".format(border, bipole, scale)
    latex += internals
    latex += r"""
\end{circuitikz}
\end{preview}
\end{document}"""
    return latex


def make_draw(x1, y1, comp, x2, y2):
    """Generate a draw command, handling special component types."""
    if comp.startswith('thinbox'):
        # Replace thinbox with generic and wrap in scope with custom dimensions
        comp = comp.replace('thinbox', 'generic', 1)
        return (r"{{\ctikzset{{bipoles/generic/height=.15,bipoles/generic/width=1.2}}"
                r"\draw ({},{}) to[{}] ({},{});}}".format(x1, y1, comp, x2, y2))
    else:
        return r"\draw ({},{}) to[{}] ({},{});".format(x1, y1, comp, x2, y2)


def grid_internals(config):
    """Generate LaTeX to draw just the grid with line labels."""

    nx, ny = config['grid']['nx'], config['grid']['ny']
    widths = config['widths']

    x = np.zeros(nx)
    for i in range(nx-1):
        x[i+1] = x[i] + widths['x'][i]

    y = np.zeros(ny)
    for j in range(ny-1):
        y[j+1] = y[j] + widths['y'][j]

    itext = ""
    # Draw faint horizontal lines with labels (x, i, j)
    for j in range(ny):
        for i in range(nx-1):
            itext += r"\draw[gray!30] ({},{}) -- ({},{});".format(x[i], y[j], x[i+1], y[j])
            midx = (x[i] + x[i+1]) / 2
            itext += r"\node[above,scale=0.35,font=\sffamily] at ({},{}) {{x,{},{}}};".format(midx, y[j], i, j)
    # Draw faint vertical lines with labels (y, i, j)
    for i in range(nx):
        for j in range(ny-1):
            itext += r"\draw[gray!30] ({},{}) -- ({},{});".format(x[i], y[j], x[i], y[j+1])
            midy = (y[j] + y[j+1]) / 2
            itext += r"\node[right,scale=0.35,font=\sffamily] at ({},{}) {{y,{},{}}};".format(x[i], midy, i, j)
    # Draw nodes at each grid intersection
    for i in range(nx):
        for j in range(ny):
            itext += r"\node[circle,fill,inner sep=0.8pt] at ({},{}) {{}};".format(x[i], y[j])

    return itext


def internals(config):

    nx, ny = config['grid']['nx'], config['grid']['ny']
    lines = config.get('lines', {})
    widths = config['widths']
    components = config.get('components', [])

    ax = np.empty([nx-1, ny], dtype=object)
    ax[:, :] = 'null'
    ay = np.empty([nx, ny-1], dtype=object)
    ay[:, :] = 'null'

    x = np.zeros(nx)
    for i in range(nx-1):
        x[i+1] = x[i] + widths['x'][i]

    y = np.zeros(ny)
    for j in range(ny-1):
        y[j+1] = y[j] + widths['y'][j]

    for xl in lines.get('x', []):
        ax[:, xl] = 'short'

    for yl in lines.get('y', []):
        ay[yl, :] = 'short'

    for s, axis, i, j in components:
        if axis == 'x':
            ax[i, j] = s
        else:
            ay[i, j] = s

    itext = ""
    for j in range(ny):
        for i in range(nx-1):
            if ax[i,j] != 'null':
                itext += make_draw(x[i], y[j], ax[i,j], x[i+1], y[j])
    for i in range(nx):
        for j in range(ny-1):
            if ay[i,j] != 'null':
                itext += make_draw(x[i], y[j], ay[i,j], x[i], y[j+1])

    return itext


def main():

    mytext = '''\
    description:
       Generate LaTeX circuit diagrams from JSON configuration files using circuitikz.
    '''

    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        prog='sb --circuit',
        description='Speakerbench Circuit',
        epilog=textwrap.dedent(mytext))

    parser.add_argument('-i',
                        help='Input JSON file',
                        metavar='JSONFILE')

    parser.add_argument('-example',
                        help='Run example (omit NAME to list available)',
                        nargs='?',
                        const='LIST',
                        metavar='NAME')

    parser.add_argument('-nopdf',
                        action='store_true',
                        help='Skip PDF generation (only output .tex)')

    parser.add_argument('-border',
                        help='Preview border in pt (default: 5)',
                        type=float,
                        default=5)

    parser.add_argument('-bipole',
                        help='Bipole length in cm (default: 0.85)',
                        type=float,
                        default=0.85)

    parser.add_argument('-scale',
                        help='Circuit scale (default: 1.2)',
                        type=float,
                        default=1.2)

    parser.add_argument('-grid',
                        action='store_true',
                        help='Draw only the grid with line labels (for design)')

    parser.add_argument('-nx',
                        help='Generate JSON with nx grid points',
                        type=int)

    parser.add_argument('-ny',
                        help='Generate JSON with ny grid points',
                        type=int)

    parser.add_argument('-o',
                        help='Output filename for generated JSON (default: grid.json)',
                        default='grid.json',
                        metavar='JSONFILE')

    args = parser.parse_args()

    # Handle -nx/-ny to generate a new JSON file
    if args.nx is not None and args.ny is not None:
        config = {
            "grid": {"nx": args.nx, "ny": args.ny},
            "widths": {
                "x": [1.0] * (args.nx - 1),
                "y": [1.0] * (args.ny - 1)
            },
            "lines": {},
            "components": []
        }
        with open(args.o, 'w') as f:
            json.dump(config, f, indent=4)
        print('INFO: (sb --circuit) Generated {}'.format(args.o))
        sys.exit(0)
    elif args.nx is not None or args.ny is not None:
        print('ERROR: (sb --circuit) Must specify both -nx and -ny')
        sys.exit(1)

    # Determine examples directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    examples_dir = os.path.join(script_dir, 'example_circuit')

    # Handle -example option
    if args.example is not None:
        if args.example == 'LIST':
            print('Available examples:')
            for f in sorted(os.listdir(examples_dir)):
                if f.endswith('.json'):
                    print('   {}'.format(f.replace('.json', '')))
            sys.exit(0)
        else:
            example_file = os.path.join(examples_dir, args.example + '.json')
            if not os.path.exists(example_file):
                print('ERROR: (sb --circuit) Example {} not found'.format(args.example))
                sys.exit(1)
            # Copy example file to current working directory
            dest_file = os.path.join(os.getcwd(), args.example + '.json')
            shutil.copy(example_file, dest_file)
            print('INFO: (sb --circuit) Copied {}.json to {}'.format(args.example, dest_file))
            input_file = dest_file
    elif args.i is not None:
        input_file = args.i
    else:
        print('ERROR: (sb --circuit) Must specify -i or -example')
        sys.exit(1)

    with open(input_file) as f:
        config = json.load(f)

    if args.grid:
        itext = grid_internals(config)
    else:
        itext = internals(config)
    latex_content = wrap_latex(itext, args.border, args.bipole, args.scale)

    output_file = input_file.rsplit('.', 1)[0] + '.tex'
    with open(output_file, 'w') as f:
        f.write(latex_content)

    print('INFO: (sb --circuit) Generated {}'.format(output_file))

    if not args.nopdf:
        subprocess.run(['pdflatex', output_file])
        print('INFO: (sb --circuit) Generated {}'.format(output_file.rsplit('.', 1)[0] + '.pdf'))


if __name__ == '__main__':
    main()
