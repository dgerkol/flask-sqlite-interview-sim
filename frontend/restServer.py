from flask import Flask, render_template, request, jsonify
from envConstants import REST_LOG
import backend.DBquery as db
import logging


def runServer():
    app = Flask(__name__, template_folder='frontend/templates')
    
    
    @app.route('/')
    def home():
        return render_template('home.html')
    
    
    #*   handle user dir   *#
    @app.route('/user', methods = ['GET', 'POST'])
    def userDir():
        if request.method == 'GET':
            query = db.selectUser()
            
            if query[0]:
                return jsonify(query[1])
            else:
                return jsonify({"operation":"get_users", "success":query[0], "error":query[1]})
            
        else:
            req_data = request.get_json(silent = True)
            if not req_data:
                return jsonify({"status": 400, "error": "Bad Request", "message": "Request body syntax error or bad media type"})
            
            query = db.createUser(req_data['name'], req_data['password'], req_data['uid'])
            
            if query[0]:
                return jsonify({"operation":"add_user", "success":query[1]})
            else:
                return jsonify({"operation":"add_user", "success":query[0], "error":query[1]})
    
    
    @app.route('/user/<int:uid>', methods = ['GET', 'PUT', 'DELETE'])
    def userIdDir(uid):
        if request.method == 'GET':
            
            query = db.selectUser(uid)
            
            if query[0]:
                return jsonify(query[1])
            else:
                return jsonify({"operation":"get_user", "success":query[0], "error":query[1]})
            
        elif request.method == 'PUT':
            req_data = request.get_json(silent = True)
            if not req_data:
                return jsonify({"status": 400, "error": "Bad Request", "message": "Request body syntax error or bad media type"})
            
            query = db.updateUser(uid, req_data['cell'], req_data['data'])
            
            if query[0]:
                return jsonify({"operation":"update_user", "success":query[1]})
            else:
                return jsonify({"operation":"update_user", "success":query[0], "error":query[1]})
        
        else:
            query = db.deleteUser(uid)
            
            if query[0]:
                return jsonify({"operation":"delete_user", "success":query[1]})
            else:
                return jsonify({"operation":"delete_user", "success":query[0], "error":query[1]})
    
    
    #*   handle tickets dir   *#
    @app.route('/tickets', methods = ['GET', 'POST'])
    def ticketDir():
        if request.method == 'GET':
            query = db.selectTicket()
            
            if query[0]:
                return jsonify(query[1])
            else:
                return jsonify({"operation":"get_tickets", "success":query[0], "error":query[1]})
            
        else:
            req_data = request.get_json(silent = True)
            if not req_data:
                return jsonify({"status": 400, "error": "Bad Request", "message": "Request body syntax error or bad media type"})
            
            query = db.createTicket(req_data['uid'], req_data['fid'])
            
            if query[0]:
                return jsonify({"operation":"add_ticket", "success":query[1]})
            else:
                return jsonify({"operation":"add_ticket", "success":query[0], "error":query[1]})
    
    @app.route('/tickets/<int:tid>', methods = ['GET', 'PUT', 'DELETE'])
    def ticketIdDir(tid):
        if request.method == 'GET':
            query = db.selectTicket(tid)
            
            if query[0]:
                return jsonify(query[1])
            else:
                return jsonify({"operation":"get_ticket", "success":query[0], "error":query[1]})
            
        elif request.method == 'PUT':
            req_data = request.get_json(silent = True)
            if not req_data:
                return jsonify({"status": 400, "error": "Bad Request", "message": "Request body syntax error or bad media type"})
            
            query = db.updateTicket(tid, req_data['cell'], req_data['data'])
            
            if query[0]:
                return jsonify({"operation":"update_ticket", "success":query[1]})
            else:
                return jsonify({"operation":"update_ticket", "success":query[0], "error":query[1]})
        
        else:
            query = db.deleteTicket(tid)
            
            if query[0]:
                return jsonify({"operation":"delete_ticket", "success":query[1]})
            else:
                return jsonify({"operation":"delete_ticket", "success":query[0], "error":query[1]})
    
    
    #*   handle flights dir   *#
    @app.route('/flights', methods = ['GET', 'POST'])
    def flightDir():
        if request.method == 'GET':
            query = db.selectFlight()
            
            if query[0]:
                return jsonify(query[1])
            else:
                return jsonify({"operation":"get_flights", "success":query[0], "error":query[1]})
            
        else:
            req_data = request.get_json(silent = True)
            if not req_data:
                return jsonify({"status": 400, "error": "Bad Request", "message": "Request body syntax error or bad media type"})
            
            query = db.createFlight(req_data['timestamp'], req_data['seats'], req_data['orig'], req_data['dest'])
            
            if query[0]:
                return jsonify({"operation":"add_flight", "success":query[1]})
            else:
                return jsonify({"operation":"add_flight", "success":query[0], "error":query[1]})
    
    
    @app.route('/flights/<int:fid>', methods = ['GET', 'PUT', 'DELETE'])
    def flightIdDir(fid):
        if request.method == 'GET':
            query = db.selectFlight(fid)
            
            if query[0]:
                return jsonify(query[1])
            else:
                return jsonify({"operation":"get_flight", "success":query[0], "error":query[1]})
            
        elif request.method == 'PUT':
            req_data = request.get_json(silent = True)
            if not req_data:
                return jsonify({"status": 400, "error": "Bad Request", "message": "Request body syntax error or bad media type"})
            
            query = db.updateFlight(fid, req_data['cell'], req_data['data'])
            
            if query[0]:
                return jsonify({"operation":"update_flight", "success":query[1]})
            else:
                return jsonify({"operation":"update_flight", "success":query[0], "error":query[1]})
        
        else:
            query = db.deleteFlight(fid)
            
            if query[0]:
                return jsonify({"operation":"delete_flight", "success":query[1]})
            else:
                return jsonify({"operation":"delete_flight", "success":query[0], "error":query[1]})
    
    
    #*   handle countries dir   *#
    @app.route('/countries', methods = ['GET', 'POST'])
    def countryDir():
        if request.method == 'GET':
            query = db.selectCountry()
            
            if query[0]:
                return jsonify(query[1])
            else:
                return jsonify({"operation":"get_countries", "success":query[0], "error":query[1]})
            
        else:
            req_data = request.get_json(silent = True)
            if not req_data:
                return jsonify({"status": 400, "error": "Bad Request", "message": "Request body syntax error or bad media type"})
            
            query = db.createCountry(req_data['name'])
            
            if query[0]:
                return jsonify({"operation":"add_country", "success":query[1]})
            else:
                return jsonify({"operation":"add_country", "success":query[0], "error":query[1]})
    
    
    @app.route('/countries/<int:cid>', methods = ['GET', 'PUT', 'DELETE'])
    def countryIdDir(cid):
        if request.method == 'GET':
            query = db.selectCountry(cid)
            
            if query[0]:
                return jsonify(query[1])
            else:
                return jsonify({"operation":"get_country", "success":query[0], "error":query[1]})
            
        elif request.method == 'PUT':
            req_data = request.get_json(silent = True)
            if not req_data:
                return jsonify({"status": 400, "error": "Bad Request", "message": "Request body syntax error or bad media type"})
            
            query = db.updateCountry(cid, req_data['cell'], req_data['data'])
            
            if query[0]:
                return jsonify({"operation":"update_country", "success":query[1]})
            else:
                return jsonify({"operation":"update_country", "success":query[0], "error":query[1]})
        
        else:
            query = db.deleteCountry(cid)
            
            if query[0]:
                return jsonify({"operation":"delete_country", "success":query[1]})
            else:
                return jsonify({"operation":"delete_country", "success":query[0], "error":query[1]})
    
    
    app.run(debug = True)