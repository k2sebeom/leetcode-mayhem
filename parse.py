import sys
import os
from glob import glob
from pyquery import PyQuery as pq
from yaml import load, Loader


def process_text(raw_text: str):
    idx = raw_text[3:].find("'''") + 3
    meta = raw_text[3:idx - 2]
    data = load(meta, Loader)
    code = raw_text[idx + 3:].lstrip()
    return data, code


def parse_problem(root, fname: str) -> str:
    with open(fname) as pfile:
        s = pfile.read()
    data, code = process_text(s)
    num_code = os.path.splitext(os.path.basename(fname))[0]
    root.append(f'''
        <div class="problem" id="problem-{num_code}">
                <h3>{data['Title']}</h3>
                <a href="{data['Source']}">link to leetcode</a>
                <p>Comment: {data['Comment']}</p>
                <pre><code>{code}</code></pre>
            </div>
    ''')


if __name__ == "__main__":
    with open('./doc_target.txt', 'r') as f:   
        targets = f.read().split('\n')

    index = pq(filename='docs/template.html')
    index('title').text(f'LeetCode Mayhem')
    index('h1').text("LeetCode Mayhem")

    for dir_name in targets:
        if len(dir_name) == 0:
            continue
        target = f'docs/{dir_name}'

        index('#dir').append(f'<a href="{dir_name}">{dir_name}</a>')

        t = pq(filename='docs/template.html')
        t('title').text(f'LeetCode | {dir_name}')
        t('h1').text(dir_name)
        with open(os.path.join(target, 'index.html'), 'w') as f:
            f.write(t.html())

        dom = pq(filename=os.path.join(target, 'index.html'))
        root = dom('#root')

        root.empty()

        for fname in glob(os.path.join(dir_name, '*.py')):
            parse_problem(root, fname)
            parse_problem(index('#root'), fname)

        with open(os.path.join(target, 'index.html'), 'w') as f:
            f.write(dom.html(method='html'))
    
    with open('docs/index.html', 'w') as f:
        f.write(index.html(method='html'))
