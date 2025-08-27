from flask import Flask, request, jsonify
from models import db, Item
from flask_cors import CORS
from datetime import datetime
import os

def create_app():
    app = Flask(__name__)
    CORS(app, origins=["http://localhost:5173", "http://127.0.0.1:5173"])
    # Configuración desde variables de entorno
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Inicializar la base de datos
    db.init_app(app)
    
    # Crear tablas al iniciar
    with app.app_context():
        db.create_all()
        print("Base de datos creada exitosamente!")
    
    # Rutas de la API
    @app.route('/api/items', methods=['GET'])
    def get_items():
        items = Item.query.all()
        return jsonify([{
            'id': item.id,
            'name': item.name,
            'team': item.team,
            'created_at': item.created_at.isoformat()
        } for item in items])
    
    @app.route('/api/items', methods=['POST'])
    def create_item():
        data = request.get_json()
        
        if not data or 'name' not in data or 'team' not in data:
            return jsonify({'error': 'Se requieren name y team'}), 400
        
        new_item = Item(
            name=data['name'],
            team=data['team']
        )
        
        db.session.add(new_item)
        db.session.commit()
        return jsonify({
            'id': new_item.id,
            'name': new_item.name,
            'team': new_item.team,
            'created_at': new_item.created_at.isoformat()
        }), 201
    
    @app.route('/api/items/<int:item_id>', methods=['GET'])
    def get_item(item_id):
        item = Item.query.get_or_404(item_id)
        return jsonify({
            'id': item.id,
            'name': item.name,
            'team': item.team,
            'created_at': item.created_at.isoformat()
        })
    
    @app.route('/api/items/<int:item_id>', methods=['DELETE'])
    def delete_item(item_id):
        item = Item.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return jsonify({'message': 'Item eliminado correctamente'})
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)