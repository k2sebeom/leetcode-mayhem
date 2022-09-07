import sys
import os
from glob import glob
from pyquery import PyQuery as pq
from yaml import load, Loader


def process_text(raw_text: str):
    idx = raw_text[3:].find("'''")
    meta = raw_text[3:idx + 1]
    data = load(meta, Loader)

    code = raw_text[idx + 3:]
    return data, code


if __name__ == "__main__":
    dir_name = sys.argv[1]

    target = f'docs/{dir_name}'
    if not os.path.isdir(target):
        os.mkdir(target)

        t = pq(filename='docs/template.html')
        t('title').text(f'LeetCode | {dir_name}')
        t('h1').text(dir_name)
        with open(os.path.join(target, 'index.html'), 'w') as f:
            f.write(t.html())

        d = pq(filename='docs/index.html')
        d('#dir').append(f'<a href="{dir_name}">{dir_name}</a>')
        
        with open('docs/index.html', 'w') as f:
            f.write(d.html())

    dom = pq(filename=os.path.join(target, 'index.html'))
    root = dom('#root')

    root.empty()

    for fname in glob(os.path.join(dir_name, '*.py')):
        with open(fname) as pfile:
            s = pfile.read()
        data, code = process_text(s)
        root.append(f'''
            <div>
                    <h3>{data['Title']}</h3>
                    <a href="{data['Source']}">link to leetcode</a>
                    <p>Comment: {data['Comment']}</p>
                    <pre><code>{code}</code></pre>
                </div>
        ''')

    with open(os.path.join(target, 'index.html'), 'w') as f:
        f.write(dom.html())
