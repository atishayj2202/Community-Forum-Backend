from sqlalchemy import text


def get_All_Post(Session):
    session = Session()
    try:
        result = session.execute(statement=text("SELECT * FROM articles ORDER BY time DESC LIMIT 5;")).fetchall()
        return {"Status": "Found", "Data": result}
    except:
        return {"Status": "Error", "Data": "Unexpected Error"}
