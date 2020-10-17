import connexion
import six

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.note import Note  # noqa: E501
from openapi_server.models.page_response import PageResponse  # noqa: E501
from openapi_server import util
import openapi_server.db_connection as db
import os
import json
from flask import jsonify, make_response


def notes_read(id_):  # noqa: E501
    """Get a clinical note by ID

    Returns the clinical note for a given ID # noqa: E501

    :param id: The ID of the clinical note to fetch
    :type id: str

    :rtype: Note
    """
    res = None
    try:
        values = db.load_config()

        conn = db.get_connection_local_pg(values)
        cursor = conn.cursor()
        select_notes = 'SELECT id, text from i2b2_data.public.pat_notes where id = %s'

        cursor.execute(select_notes, (id_,))
        row = cursor.fetchone()

        if row == None:
            res = {
                'title': "The specified resource was not found",
                'status': 404
            }
        else:
            res = {'id': row[0], 'text': row[1]}
    except Exception as error:
        res = {
            'title': "Internal error",
            'status': 500
        }
    finally:
        cursor.close()
        conn.close()

    return jsonify(res)


def notes_read_all(limit=None, offset=None):  # noqa: E501
    """Get all clinical notes

    Returns the clinical notes # noqa: E501

    :param limit: Maximum number of results returned
    :type limit: int
    :param offset: Index of the first result that must be returned
    :type offset: int

    :rtype: PageResponse
    """
    res = None
    try:
        counter = 0
        items = []
        #if connexion.request.is_json:
        # limit =  AnyType.from_dict(connexion.request.get_json())
        values = db.load_config()

        conn = db.get_connection_local_pg(values)
        cursor = conn.cursor()
        select_notes = 'SELECT id, text from i2b2_data.public.pat_notes LIMIT %s OFFSET %s'
        cursor.execute(select_notes, (limit, offset))
        all_rows = cursor.fetchall()
        counter= len(all_rows)

        for row in all_rows:
            id = row[0]
            dict = { 'id': id , 'text':row[1] }
            items.append( dict )

        next = {"next" : "/api/v1/ui/#/Note/notes_read_all?limit=10" }
        res = {'links': next, 'items': items}
    except Exception as error:
        res = {
            'title': "Internal error",
            'status': 500
        }
    finally:
        cursor.close()
        conn.close()

    return jsonify(res)
