from sqlalchemy import text
import uuid


def get_All_Post(Session):
    session = Session()
    try:
        result = session.execute(statement=text("SELECT * FROM articles ORDER BY time DESC LIMIT 15;")).fetchall()
        if len(result) < 1:
            return {"Status": "Not Success", "Data": "Not Found"}
        return {"Status": "Found", "Data": result}
    except:
        return {"Status": "Error", "Data": "Unexpected Error"}


def get_single_Post(Session, pid):
    session = Session()
    try:
        result = session.execute(statement=text("SELECT * FROM articles WHERE id = :el1;"),
                                 params={"el1": pid}).fetchall()
        if len(result) < 1:
            return {"Status": "Not Success", "Data": "Not Found"}
        return {"Status": "Success", "Data": result[0]}
    except:
        return {"Status": "Error", "Data": "Unexpected Error"}


def add_Post(Session, title, body, author_name, author_id):
    session = Session()
    id = uuid.uuid4()
    try:
        session.execute(statement=text(
            "INSERT INTO articles (id, title, body, author_name, author_id) VALUES (:el5, :el1, :el2, :el3, :el4);"),
            params={"el1": title, "el2": body, "el3": author_name, "el4": author_id, "el5": id})
        session.commit()
        return {"Status": "Success", "Data": id}
    except:
        return {"Status": "Error", "Data": "Unexpected Error"}
