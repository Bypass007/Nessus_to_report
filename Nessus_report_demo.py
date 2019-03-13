#! /usr/bin/env python
# _*_  coding:utf-8 _*_
#Author：Aaron

from lxml import etree
import csv
import sys

host=''
title=''
result_list=[]	
def htm_parse(l):		
	if '#d43f3a' in etree.tostring(l):
		info=u"严重 - "+l.text
	elif '#ee9336' in etree.tostring(l):
		info=u"高危 - "+l.text
	elif '#fdc431' in etree.tostring(l):
		info=u"中危 - "+l.text
	elif '#3fae49' in etree.tostring(l):
		info=u"低危 - "+l.text			
	elif '#0071b9' in etree.tostring(l):
		info=u'信息泄露 - '+l.text
	else:
		info='Parsing error,Check that the versions are consistent.'
	return info
def main(filename):
	html = etree.parse(filename,etree.HTMLParser())
	title =html.xpath('/html/body/div[1]/h3/text()')[0]
	ls =html.xpath('/html/body/div[1]/div[3]/div')
	for i in ls:
		if "font-size: 22px; font-weight: bold; padding: 10px 0;" in etree.tostring(i):
			host=i.text
		elif "this.style.cursor" in etree.tostring(i):
			result=host+" - "+htm_parse(i)
			#print result
			result_list.append(result)
	return result_list	
if __name__ == '__main__':
	filename=sys.argv[1]
	list_host =  main(filename)
	with open('result.csv','wb') as f:
		f.write(u'\ufeff'.encode('utf8'))
		w = csv.writer(f)
		w.writerow(['服务器IP','漏洞级别','漏洞编号','漏洞名称'])
		for i in list_host:
			data=i.split('-',3)
			w.writerow([item.encode('utf8') for item in data])
