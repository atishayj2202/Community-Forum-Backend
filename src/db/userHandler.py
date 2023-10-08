from sqlalchemy import text
import uuid
def create_user(Session, author_name, uid):
    session = Session()
    id = uuid.uuid4()
    try:
        session.execute(statement=text(
            "INSERT INTO authors (uid, author_name, id) VALUES (:el1, :el2, :el3);"),
            params={"el1": uid, "el2": author_name,"el3":id})
        session.commit()
        return {"Status": "Success", "Data": id}
    except:
        return {"Status": "Error", "Data": "Unexpected Error"}

def get_user(Session, id):
    session = Session()
    try:
        result = session.execute(statement=text("SELECT * FROM authors WHERE id = :el1;"),
                                 params={"el1": id}).fetchall()
        if len(result) < 1:
            return {"Status": "Not Success", "Data": "Not Found"}
        return {"Status": "Success", "Data": result[0]}
    except:
        return {"Status": "Error", "Data": "Unexpected Error"}