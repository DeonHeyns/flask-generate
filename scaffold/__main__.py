# -*- coding: utf-8 -*-
__author__ = 'DeonHeyns'

import argparse
import os

import templates


def main():
    parser = argparse.ArgumentParser(description='Scaffolding tool for Flask projects',
                                     epilog='Report any issues to [Github url]')

    parser.add_argument('-p', '--project', required=True, nargs=1,
                        help='The name of the project to create')

    parser.add_argument('-d', '--dir', required=False, nargs=1,
                        help='The directory in which to create the project (creates in current directory by default)')

    args = parser.parse_args()

    target_dir = args.dir[0]

    if not os.path.exists(target_dir):
        os.mkdir(target_dir)

    dir_structure = filter(None, templates.STRUCTURE.replace('$project$', args.project[0]).split('\n'))
    file_structure = filter(None, templates.FILES.replace('$project$', args.project[0]).split('\n'))

    for s in dir_structure:
        p = os.path.join(target_dir, s)
        os.mkdir(p)

    for d in file_structure:
        file_name = os.path.basename(d)
        content = templates.RUN if 'run.py' in file_name else ''
        content = templates.INIT if 'app/__init__.py' in d else content
        content = templates.CONFIG if 'config.py' in file_name else content
        with open(os.path.join(target_dir, d), 'wb') as f:
            f.write(content)


if __name__ == "__main__":
    main()