#!/usr/bin/python
# -*- coding:utf-8 -*- 


import sys
from lxml import etree
import sqlite3
import unicodecsv as ucsv

host=''
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
    ls =html.xpath('/html/body/div[1]/div[3]/div')
    for i in ls:
        if "font-size: 22px; font-weight: bold; padding: 10px 0;" in etree.tostring(i):
            host=i.text
        elif "this.style.cursor" in etree.tostring(i):
            result=host+" - "+htm_parse(i)
            print result
            result_list.append(result)
    return result_list 
	
		
def select(ip,id):
	conn = sqlite3.connect('vuln.db')
	conn.text_factory=str
	cursor = conn.cursor()
	for row in cursor.execute("select * from VULNDB where Plugin_ID=?", (id,)):
		return [ip,row[1],row[2],row[3],row[4]]
		

if __name__ == '__main__':
	filename=sys.argv[1]
	list_host =  main(filename)
	#list_host=[u'192.168.98.254 - 高危 - 10203 - rexecd Service Detection',u'192.168.98.254 - 高危 - 11233 - rexecd Service Detection']
	
	with open('result.csv', 'wb') as f:
		w = ucsv.writer(f, encoding = 'gbk')
		title=[u'服务器IP',u'漏洞名称',u'风险级别',u'漏洞描述',u'修复建议']
		w.writerow(title)
		for i in list_host:
			info=i.split('-',3)
			result=select(info[0],info[2])
			if result is not None:
				data=result
			else:
				data=info[0],info[3],info[1]
			w.writerow(data)
			

