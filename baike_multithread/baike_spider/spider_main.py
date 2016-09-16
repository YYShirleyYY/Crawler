# -*- coding: UTF-8 -*-

#爬虫总调度程序,入口程序，SpiderMain()
import url_manager,html_downloader,html_parser,html_outputer

class SpiderMain(object):
	"""docstring for SpiderMain"""
	def __init__(self):
		self.urls=url_manager.UrlManager()
		self.downloader=html_downloader.HtmlDownloader()
		self.parser=html_parser.HtmlParser()
		self.outputer=html_outputer.HtmlOutputer()

	def craw(self,root_url):
		count=1
		self.urls.add_new_url(root_url)
		while self.urls.has_new_url():
			try:	
				new_url=self.urls.get_new_url()
#				print 'craw %d: %s' %(count,new_url)
				html_cont=self.downloader.download(new_url)
#				print '2craw %d: %s' %(count,new_url)
				new_urls,new_data=self.parser.parse(new_url,html_cont)
#				print '3craw %d: %s' %(count,new_url)
				self.urls.add_new_urls(new_urls)
#				print '4craw %d: %s' %(count,new_url)
				self.outputer.collect_data(new_data)
#				print '5craw %d: %s' %(count,new_url)

				
				if count==10:
					break
				count=count+1

			except:	
				print 'failed'

		self.outputer.output_html()


if __name__ == '__main__':
	root_url='http://baike.baidu.com/view/21087.htm'
	obj_spider=SpiderMain()
	obj_spider.craw(root_url)
