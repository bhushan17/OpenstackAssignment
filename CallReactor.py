#code written at very basic level, copied most of it from google.
# this may not be the efficient way. Intention was to show concepts behind it.

from bottle import route,run
from OLD_Hub import Hub

print ("Connection established, waiting for user requests")

hub = Hub()
hub.registerHandlers()
count = 0
@route ('/callReactor/<eventname>')
def callReactor(eventname):
    global count
    count += 1
    eventname = count%3
    #print eventname
    if(eventname==''):
        eventname = '0'
    print eventname    
    hub.emit(eventname, [])

#run(host='10.222.72.48', port=8181, debug=True)
run(host='10.44.77.215', port=8181, debug=True)
