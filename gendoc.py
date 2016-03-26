#-*- encoding: utf-8 -*-

import os
import re

popular_modules = ('win32api', 'win32gui', 'win32ui', 'win32process',
        'win32console', 'win32event', 'win32net', 'win32service', 
        'win32security', 'win32file',)

docs = {}

def escape(s):
    to_escape = '\`*_{}[]()#+.!'
    s = ['\\' + c if c in to_escape else c for c in s]
    return ''.join(s)

def split_fname(fname):
    if fname.endswith('.html'): fname = fname[:-5]
    if fname.endswith('_meth'): fname = fname[:-5]
    fname = fname.replace('__', '_', 1)
    if '_' in fname[1:]:
        if fname[0] == '_':
            _, modname, attrname = fname.split('_', 2)
            modname = '_' + modname
        else:
            modname, attrname = fname.split('_', 1)
    else:
        modname, attrname = fname, ''
    return modname, attrname

def parse(fname, badhtml):
    modname, attrname = split_fname(fname)

    tmpl_tag = re.compile(r'<(/?[a-zA-Z0-9]*)[^>]*>')
    tmpl_href = re.compile(r'''href=["'](.*?)["']''', re.I)
    boundaries = ('title', '/title', 'p', 'h1', 'h3', 'dd', 'dt', 'br')
    ignores = ('title', '/title')

    length = len(badhtml)
    pos = 0
    lines = []
    curline = ''
    while True:
        m = tmpl_tag.search(badhtml, pos)
        if not m:
            text = badhtml[pos:].strip()
            if text: lines.append(text)
            break

        s, e, tag = m.start(), m.end(), m.group(1).lower()
        if tag in ignores:
            pos = e
            continue
        curline = curline + escape(badhtml[pos:s])

        # print pos, s, e, tag
        if tag in boundaries:
            lines.append(curline)
            if tag == 'title':
                curline = '# '
            elif tag == 'h1':
                curline = '## '
            elif tag == 'h3':
                curline = '#### '
            elif tag == 'dt':
                curline = '  - '
            elif tag == 'dd':
                curline = '    '
            else:
                curline = ''
        else:
            if tag in ('/h1', '/h3'):
                curline += '\n'
            if tag == 'a':
                curline += '['
                urlm = tmpl_href.search(m.group())
                if urlm:
                    url = urlm.group(1)
                    _m, _a = split_fname(url)
                    _t = ('#%s%s' % (_m.lower(), _a.lower())) if _a else ('#%s' % _m.lower() if (_m ==modname) else '')
                    url = '%s.md%s' % (_m, _t)
                else:
                    url = ''
            elif tag == '/a':
                curline += '](%s)' % url
                url = ''
            # elif tag == 'b' :
            #     curline += ' __'
            # elif tag == '/b':
            #     curline += '__ '
            # elif tag =='i':
            #     curline += ' *'
            # elif tag == '/i':
            #     curline += '* '
        pos = e

    text = '\n'.join(lines)
    text = re.sub(r'\n{3,}', '\n\n', text)
    attrname = attrname or '__module_doc__'
    return text, modname, attrname

def parse_html(root):
    global docs
    for fname in os.listdir(root):
        if not fname.endswith('.html'):
            continue
        fpath = os.path.join(root, fname)
        try:
            f = open(fpath)
        except IOError as e:
            print str(e)
            continue
        else:
            try:
                html = f.read()
                text, modname, attrname = parse(fname, html)
                if not text:
                    print "Warning: %s processed as blank." % fname
            except:
                print "Warning: %s not processed." % fname
                continue
            finally:
                f.close()

        docs.setdefault(modname, {})
        docs[modname][attrname] = text

def write_markdown(root):
    readme = {}
    readme_main = {}
    for modname, attrs in docs.iteritems():
        lines = []
        lines.append('# %s' % modname)

        if '__module_doc__' in attrs:
            s = attrs.pop('__module_doc__')
            readme[modname] = s
            if modname in popular_modules:
                readme_main[modname] = s
            lines.append(s)

        for a in sorted(attrs.keys()):
            lines.append(attrs[a])

        md = os.path.join(root, '%s.md' % modname)
        with open(md, 'w') as f:
            f.write('\n'.join(lines))

    with open(os.path.join(root, 'README.md'), 'w') as f:
        for modname in sorted(readme.keys()):
            details = readme[modname]
            f.write('- [%s](%s.md)\n' % (modname, modname))

    with open(os.path.join(root, '..', 'README.md'), 'w') as f:
        f.write('''## pywin32doc
Selected documents of [pywin32 project](https://sourceforge.net/projects/pywin32)
Generated from .chm documents.

pywin32 version: Build 220\n\n''')
        for modname in sorted(readme_main.keys()):
            details = readme_main[modname]
            f.write('- [%s](md/%s.md)\n' % (modname, modname))


if __name__ == '__main__':
    if not os.path.exists('doc'):
        os.makedirs('doc')
        os.system('hh.exe -decompile PyWin32.chm doc/') ## failed on my laptop :(

    parse_html('doc')
    write_markdown('md')