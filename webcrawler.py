#!/usr/bin/env python
# -*- coding:utf-8 -*-


def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ''


def get_all_links(page):
    try:
        import re
        filelinks_pat = re.compile('href[\s]*=[\s]*"([^"]*?zip|[^"]*?rar|[^"]*?pdf)"')
        links = filelinks_pat.findall(page)
        #按后缀名排序
        return sorted(links, cmp=lambda x, y: 1 if x[-3:] > y[-3:] else -1)
    except:
        return []


def store_links(url, file_name):
    links = get_all_links(get_page(url))
    #print links
    try:
        import codecs
        f = codecs.open(u'downloadlist_%s.txt' % file_name, 'w', 'utf-8')
        f.write(u'downloadlist_%s\n' % file_name)
        for link in links:
            link = verify_link(url, link)
            f.write('%s\n' % link)
        f.close()
        print u'下载列表保存完毕\n'
    except Exception as e:
        print u'无法保存下载链接\n%s' % e

def verify_link(url, link):
    link = link.replace(u'&amp;', u'&')
    if link.startswith('http'):
        return link
    else:
        return url[:url.rfind('/')]+link

def main(url, file_name):
    store_links(url, file_name)

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print u'请输入url与要保存的课程名称'
    else:
        main(sys.argv[1], sys.argv[2])
