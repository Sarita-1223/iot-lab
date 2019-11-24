import urllib



def main():
	conn = urllib.urlopen("https://api.thingspeak.com/channels/ 893697/feeds.xml?api_key=1KA6JHBNEV875IVX&results=2")

	response = conn.read()
	print(response)
	print("http status code = %s" % (conn.getcode()))
	conn.close()

if __name__ == '__main__':
	main()


