from curses import raw
import sys
import os
from glob import glob


def process_text(raw_text: str):
    raw_text = raw_text.replace("'''", '')
    raw_text = raw_text.replace('Title:', '##')
    raw_text = raw_text.replace('Source:', '- Source:')
    raw_text = raw_text.replace('Comment:', '- Comment:')

    raw_text = raw_text.replace('class Solution', '```python\nclass Solution')
    raw_text += '\n```\n'
    return raw_text


if __name__ == "__main__":
    dir_name = sys.argv[1]
    with open(os.path.join(dir_name, 'README.md'), 'w') as f:
        f.write('# Study Note')
        for fname in glob(os.path.join(dir_name, '*.py')):
            with open(fname) as pfile:
                s = pfile.read()
            f.write(process_text(s))
