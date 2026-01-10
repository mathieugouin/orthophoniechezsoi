"""
This script updates HTML files by importing content from external files
based on specific markers within the HTML files.

Example usage within an HTML file:

    /* @import_begin("style.css") */
    ...
    /* @import_end */

    or

    <!-- @import_begin("signature.html") -->
    ...
    <!-- @import_end -->
"""

import re
import os


def read_import(file):
    """Read the content of the import file."""
    content = None
    with open(file, 'r', encoding="utf-8") as fh:
        content = fh.read()
        # remove last newline in the import file content
        content = re.sub('\n$', '', content)
    return content


def update(file):
    """Update the given HTML file by updating the imported content."""
    print(f"Processing {file} ...")
    infile_content = None
    with open(file, 'r', encoding="utf-8") as fh:
        infile_content = fh.read()

    if infile_content is not None:
        with open(file, 'w', encoding="utf-8") as fh:
            import_content = None
            for line in infile_content.splitlines():

                m = re.search(r'@import_end', line)
                if m is not None:
                    print(f"  Found {m.group(0)}")
                    import_content = None

                if import_content is None:
                    fh.write(line + '\n')

                m = re.search(r'@import_begin\("(.+?)"\)', line)
                if m is not None:
                    print(f"  Found {m.group(0)}")
                    import_content = read_import(m.group(1))
                    fh.write(import_content + '\n')


def main():
    """Main function to process all HTML files in the current directory."""
    for f in sorted(os.listdir('.')):
        if f.endswith('.html'):
            update(f)


if __name__ == "__main__":
    main()
