import SimpleHTTPServer,SocketServer,sys
PORT=sys.argv[1] #when running this enter port from command_line
def runserver():
  try:
   httphandler=SimpleHTTPServer.SimpleHTTPRequestHandler
   httpd=SocketServer.TCPServer(("192.168.1.6 ",int(PORT)),httphandler)
   print "python web server serving at port," +PORT
   httpd.serve_forever()
  except (KeyboardInterrupt,SystemExit):
   print "exiting.."
   sys.exit
  except:
   print "THERE WAS A PROBLEM STARTING THE WEBSERVER"
runserver()
