from sqlalchemy import text
import uuid


def create_user(Session, author_name, uid):
    session = Session()
    id = uuid.uuid4()
    try:
        session.execute(statement=text(
            "INSERT INTO authors (uid, author_name, id) VALUES (:el1, :el2, :el3);"),
            params={"el1": uid, "el2": author_name, "el3": id})
        session.commit()
        return {"Status": "Success", "Data": str(id)}
    except:
        try:
            session = Session()
            result = session.execute(statement=text("SELECT * FROM authors WHERE uid = :el1;"),
                                     params={"el1": uid}).fetchall()
            if len(result) < 1:
                return {"Status": "Error", "Data": "Unexpected Error1"}
            return {"Status": "Success",
                    "Data": str(result[0][2])}
        except:
            return {"Status": "Error", "Data": "Unexpected Error2"}


def get_user(Session, id):
    session = Session()
    try:
        result = session.execute(statement=text("SELECT * FROM authors WHERE id = :el1;"),
                                 params={"el1": id}).fetchall()
        if len(result) < 1:
            return {"Status": "Not Success", "Data": "Not Found"}
        return {"Status": "Success",
                "Data": {"id": str(result[0][0]), "name": str(result[0][1]), "uid": str(result[0][2])}}
    except:
        return {"Status": "Error", "Data": "Unexpected Error"}
