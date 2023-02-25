from flask import Blueprint, jsonify, request
from models.entities.Author import Author
from models.AuthorModel import AuthorModel
import uuid
main = Blueprint('author_blueprint', __name__)


@main.route('/')
def get_authors():
    try:
        authors = AuthorModel.get_authors()
        return jsonify(authors)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/<id>')
def get_author(id):
    try:
        author = AuthorModel.get_author(id)
        if author != None:
            return jsonify(author)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/', methods=['POST'])
def add_author():
    try:
        first_name = request.json['first_name']
        last_name = request.json['last_name']
        author = Author("", first_name, last_name)
        affected_rows = AuthorModel.add_author(author)

        if affected_rows == 1:
            return jsonify({'message': "OK"})
        else:
            return jsonify({'message': "Error on insert"}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/<id>', methods=['DELETE'])
def delete_author(id):
    try:
        author = Author(id)

        affected_rows = AuthorModel.delete_author(author)

        if affected_rows == 1:
            return jsonify(author.id)
        else:
            return jsonify({'message': "No author deleted"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/<id>', methods=['PUT'])
def update_author(id):
    try:
        first_name = request.json['first_name']
        last_name = request.json['last_name']
        author = Author(id, first_name, last_name)
        affected_rows = AuthorModel.update_author(author)

        if affected_rows == 1:
            return jsonify({'message': "OK"})
        else:
            return jsonify({'message': "No author updated"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
