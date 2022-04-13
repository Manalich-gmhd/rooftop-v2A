from rtu_app import app
#from gevent import monkey
#monkey.patch_all()
from gevent.pywsgi import WSGIServer

http_server = WSGIServer(('0.0.0.0', 8000), app)
http_server.serve_forever() 
 
#Antes estaba asi   
#if __name__ == '__main__':
#   app.run(port=8080,debug = True,threaded=True)   
#   app.run(host='0.0.0.0',port=8000,debug = False,threaded=False,processes=1)   
#   app.run(debug = False)   
