# -*- coding:utf-8 -*-

import unicodedata
from sqlalchemy.sql import text

def deleteAccent(string):
    if string is None:
        return None
    return unicodedata.normalize("NFD", string).encode("ascii", "ignore").decode("utf-8")


def findPath(row):
    if row.chemin == None and row.url == None:
        return None
    elif row.chemin != None and row.chemin != "":
        return row.chemin
    else:
        return row.url
    
def check_database_column_existence(connection, col_name,schema_name, view_name):
    # with app.app_context():
        sql = f"""
                SELECT *
                FROM {schema_name}.{view_name}
                LIMIT 1
        """
        # connection = db.engine.connect()
        result = connection.execute(text(sql), schema_name=schema_name, view_name=view_name)
        columns = result.keys()
        cols = [col for col in columns ]
        if col_name in cols :
            return
        else:
            raise KeyError(
                f"The specified sort column '{col_name}' does not exist in view '{schema_name}.{view_name}', default column used to sort medias is 'date_media'."
            )
