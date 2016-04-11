#!python
# encoding:utf-8

def test_parse_xml():
	from urllib import urlopen
	from xml.etree.ElementTree import parse
	#Download the RSS feed and parse it
	u = urlopen('http://planet.python.org/rss20.xml')
	doc = parse(u)
	#Extract and output tags of interest
	for item in doc.iterfind('channel/item'):
		title = item.findtext('title')
		date = item.findtext('pubDate')
		link = item.findtext('link')
		print title
		print date
		print link
		print 

def main():
	test_parse_xml()

if __name__ == '__main__':
	main()