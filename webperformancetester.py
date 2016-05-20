import webclient, os
def menu():
 os.system('clear')
 print '''
     ->->->->->->->->->->->->->->->->->->->->->->->
      WEB PERFORMANCE TESTING
     ->->->->->->->->->->->->->->->->->->->->->->->
  1.Test client connection to external web sites
  2.Test internal web server performance
  3.Display log file
  4.Exit
  ->->->->->->->->->->->->->->->->->->->->->->->
  '''
 choice=raw_input("\tEnter a choice and press enter:")
 return choice
 choice =""
 while choice!="4":
  choice=menu()
  if choice=='1':
   os.system('clear')
   sites=[]
   print'''
        ____________________
        |EXTERNAL SITE CHECK|
        |                   |
        _____________________
      '''
   siteresponse=raw_input("\tenter the website to check,give space between them:\n\n\t")
   sites=siteresponse.split()
   webclient.CheckExternalSites(sites)
  elif choice == '2':
   os.system('clear')
   servers = []
   print '''
========================================================
WEB PERFORMANCE TESTER - INTERNAL WEBSERVER CHECK
========================================================
         '''
   print ("Enter the ip addresses of the web servers\nrunning the Python Webserver, seperated by spaces:\n\t")
   serverresponse = raw_input('\t')
   servers = serverresponse.split()
   port = raw_input('Enter the port the web server is listening on: ')
   webclient.CheckInternalWebServers(servers, port)
  elif choice=='3':
   os.system("leafpad logfile.txt")