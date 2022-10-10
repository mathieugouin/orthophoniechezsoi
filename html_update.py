#!/usr/bin/python
from __future__ import print_function

import re
import os

"""
    /* @import_begin("style.css") */
    ...
    /* @import_end */

    or

    <!-- @import_begin("signature.html") -->
    ...
    <!-- @import_end -->
"""


def read_import(f):
    content = None
    with open(f, 'r') as fh:
        content = fh.read()
        # remove last newline in the import file content
        content = re.sub('\n$', '', content)
    return content


def update(f):
    print("Processing {} ...".format(f))
    infile_content = None
    with open(f, 'r') as fh:
        infile_content = fh.read()

    if infile_content is not None:
        with open(f, 'w') as fh:
            import_content = None
            for l in infile_content.splitlines():

                m = re.search(r'@import_end', l)
                if m is not None:
                    print("  Found {}".format(m.group(0)))
                    import_content = None

                if import_content is None:
                    fh.write(l + '\n')

                m = re.search(r'@import_begin\("(.+?)"\)', l)
                if m is not None:
                    print("  Found {}".format(m.group(0)))
                    import_content = read_import(m.group(1))
                    fh.write(import_content + '\n')


def main():
    for f in os.listdir('.'):
        if f.endswith('.html'):
            update(f)


if __name__ == "__main__":
    main()
