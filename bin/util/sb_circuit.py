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


def internals(config):

    nx, ny = config['grid']['nx'], config['grid']['ny']
    lines = config['lines']
    widths = config['widths']
    components = config['components']

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

    parser.add_argument('-pdf',
                        action='store_true',
                        help='Generate PDF using pdflatex')

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

    args = parser.parse_args()

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

    itext = internals(config)
    latex_content = wrap_latex(itext, args.border, args.bipole, args.scale)

    output_file = input_file.rsplit('.', 1)[0] + '.tex'
    with open(output_file, 'w') as f:
        f.write(latex_content)

    print('INFO: (sb --circuit) Generated {}'.format(output_file))

    if args.pdf:
        subprocess.run(['pdflatex', output_file])
        print('INFO: (sb --circuit) Generated {}'.format(output_file.rsplit('.', 1)[0] + '.pdf'))


if __name__ == '__main__':
    main()
