from db.db import get_connection
from .entities.Author import Author


class AuthorModel():
    @classmethod
    def get_authors(self):
        try:
            connection = get_connection()
            authors = []

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, first_name, last_name FROM authors;")
                resultset = cursor.fetchall()

                for row in resultset:
                    author = Author(row[0], row[1], row[2])
                    authors.append(author.to_JSON())

            connection.close()
            return authors
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_author(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, first_name, last_name FROM authors WHERE id = %s", (id,))
                row = cursor.fetchone()

                author = None
                if row != None:
                    author = Author(row[0], row[1], row[2])
                    author = author.to_JSON()

            connection.close()
            return author
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_author(self, author):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    """INSERT INTO authors (first_name, last_name) VALUES (%s, %s)""", (author.first_name, author.last_name))

                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_author(self, author):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM authors WHERE id = %s", (author.id,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_author(self, author):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    """UPDATE authors SET first_name = %s, last_name = %s 
                    WHERE id = %s""", (author.first_name, author.last_name, author.id))

                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
