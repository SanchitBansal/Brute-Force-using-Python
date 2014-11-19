import mechanize
import cookielib

class Browsers:
	'''
	class to define all browser handling functions
	'''
	def __init__(self):

		# Browser
		self.br = mechanize.Browser()
		
		# Cookie Jar
		self.cj = cookielib.LWPCookieJar()
		self.br.set_cookiejar(self.cj)


	def setBrowserOptions(self):
		self.br.set_handle_equiv(True)
		self.br.set_handle_gzip(True)
		self.br.set_handle_redirect(True)
		self.br.set_handle_referer(True)
		self.br.set_handle_robots(False)

		# Follows refresh 0 but not hangs on refresh > 0
		self.br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)


	def getUrlSource(self, url):
		try:
		    r = self.br.open(url)
		    return (True, r.read())
		except Exception as e:
		    return (False, e)

	def getUrlTitle(self, url):
		try:
		    self.br.open(url)
		    return (True, self.br.title())
		except Exception as e:
		    return (False, e)

	def getResponseHeader(self, url):
		try:
		    self.br.open(url)
		    return (True, self.br.response().info())
		except Exception as e:
		    return (False, e)

	def openurl(self, url):
		try:
		    self.br.open(url)
		    return True,"Url open successful"
		except Exception as e:
		    return False,e

	def submit_form_by_name(self, url, nextUrl, formName, keyValues,bfkey,bfval):
		try:
		    self.br.select_form(name = formName)
		    for key, val in keyvalues.iteritems():
			self.br.form[str(key)] = val
		    self.br.form[str(bfkey)] = bfval

		    self.br.submit()
		    if self.br.response().geturl().strip('/') == str(nextUrl).strip('/'):
		        return (True, "Login Successful")
		    else:
			return (False, "Login Failed")

		except Exception as e:
		    return (False, e)

	def select_from_by_index(self, url, nextUrl, index, keyValues,bfkey,bfval):
		try:
		    self.br.select_form(nr = index)
		    for key, val in keyValues.iteritems():
			self.br.form[str(key)] = val
		    self.br.form[str(bfkey)] = bfval

		    self.br.submit()
		    if self.br.response().geturl().strip('/') == str(nextUrl).strip('/'):
                        return (True, "Login Successful")
                    else:
                        return (False, "Login Failed")

		except Exception as e:
		    return (False, e)

	def closeconn(self):
		self.br.close()
