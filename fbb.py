import cookielib
import urllib2
import mechanize
import facebook

# Browser
br = mechanize.Browser()

# To enable cookies
cookiejar = cookielib.LWPCookieJar()
br.set_cookiejar( cookiejar )

# Browser settings
br.set_handle_equiv( True )
br.set_handle_gzip( True )
br.set_handle_redirect( True )
br.set_handle_referer( True )
br.set_handle_robots( False )


br.set_handle_refresh( mechanize._http.HTTPRefreshProcessor(), max_time = 1 )

br.addheaders = [ ( 'User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1' ) ]

# To authenticate
br.open("https://www.facebook.com/")
br.select_form(nr = 0)        #first form is a login form

br[ "email" ] = "your email/phone no"
br[ "pass" ] = "your password"
res = br.submit()

br.geturl()

tokeen=''
  
def auto_post():
    graph = facebook.GraphAPI(access_token=tokeen,version='2.2')
    post = graph.get_object(id="me")
    msg=str(input("Enter your message : "))
    graph.put_object(parent_object='me', connection_name='feed',message=msg)

    
if __name__ == '__main__':
    auto_post()

print "Success!\n"



