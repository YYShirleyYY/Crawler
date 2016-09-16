# -*- coding: UTF-8 -*-

class HtmlOutputer(object):

	def __init__(self):
		self.datas=[]

	def collect_data(self,data):
		if data is None:
			return 
		self.datas.append(data)


	def output_html(self):
		fout=open('output.html','w')
		fout.write('<html>')
#写头信息，指定网页的编码方式UTF-8
		fout.write('<head><meta charset="UTF-8"></head>')
		fout.write('<body>')
		fout.write('<table>')
#python 默认编码：ascii
		for data in self.datas:
			fout.write('<tr>')
			fout.write('<td>%s</td>' %data['url'])
			fout.write('<td>%s</td>' %data['title'].encode('UTF-8'))
			fout.write('<td>%s</td>' %data['summary'].encode('UTF-8'))
			fout.write('</tr>')


		fout.write('</html>')
		fout.write('</body>')
		fout.write('</table>')
