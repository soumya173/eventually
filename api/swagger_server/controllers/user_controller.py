import connexion
import six

from swagger_server.models.info import Info  # noqa: E501
from swagger_server.models.login_details import LoginDetails  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.models.info_error import InfoError
from swagger_server import util
from flask import jsonify
from swagger_server.dbinterface import dbinterface as db


def create_user(body):  # noqa: E501
    """Create user

    This can only be done by the logged in user. # noqa: E501

    :param body: Created user object
    :type body: dict | bytes

    :rtype: User
    """

    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    conn = db.DbInterface().connect()
    con = conn.cursor()
    con.execute(f"SELECT * FROM users WHERE name='{body.name}'")
    rows = con.fetchall()
    if len(rows) > 0:
        return Info(error=InfoError("User already exists")), 400

    con.execute(f"INSERT INTO users (name, password, type, email) VALUES ('{body.name}', '{body.password}', '{body.type}', '{body.email}')")
    conn.commit()
    con.execute(f"SELECT id,name,email,type FROM users WHERE name='{body.name}'")
    rows = con.fetchall()
    event = User(id = rows[0][0],name = rows[0][1],email = rows[0][2], type = rows[0][3])
    conn.close()
    return jsonify(event)

def delete_user_by_id(userid):  # noqa: E501
    """Delete user

    This can only be done by the logged in user. # noqa: E501

    :param userid: The name that needs to be deleted
    :type userid: int

    :rtype: User
    """
    if userid == 1:
        return Info(error=InfoError(f"Cannot delete a user with userid={userid} since its a admin user")), 400

    conn = db.DbInterface().connect()
    con = conn.cursor()
    con.execute(f"select id,name,type from users where id='{userid}'")
    rows = con.fetchall()
    if len(rows) > 0:
        event = User(rows[0][0],rows[0][1],rows[0][2])
        con.execute(f"delete from users where id='{userid}'")
        conn.commit()
        conn.close()
        return jsonify(event)

    conn.close()
    return Info(error=InfoError(f"User doesnot exists with userid={userid}")), 400

def get_all_users():  # noqa: E501
    """Get all users

     # noqa: E501


    :rtype: User
    """
    conn = db.DbInterface().connect()
    con = conn.cursor()
    con.execute("select id,name,type,email,logged from users")
    rows = con.fetchall()
    events = []
    if len(rows) > 0:
        for r in rows:
            events.append(User(id=r[0],
                            name=r[1],
                            type=r[2],
                            email=r[3],
                            logged=r[4]))
    conn.close()
    return jsonify(events)

def get_user_by_id(userid):  # noqa: E501
    """Get user by user id

     # noqa: E501

    :param userid: The id that needs to be fetched.
    :type userid: int

    :rtype: User
    """
    conn = db.DbInterface().connect()
    con = conn.cursor()
    con.execute(f"select id,name,type,email,logged from users where id='{userid}'")
    rows = con.fetchall()
    if len(rows) > 0:
        event = User(id = rows[0][0],name = rows[0][1],type = rows[0][2],email = rows[0][3],logged = rows[0][4])
        conn.close()
        return jsonify(event)
    conn.close()
    return Info(error=InfoError(f"User doesnot exists with userid={userid}")), 400


def login_user(body):  # noqa: E501
    """Logs user into the system

     # noqa: E501

    :param body: Username and password
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = LoginDetails.from_dict(connexion.request.get_json())  # noqa: E501
    conn = db.DbInterface().connect()
    con = conn.cursor()
    con.execute(f"select id,name,password,type,email from users where name='{body.name}'")
    rows = con.fetchall()
    if len(rows) > 0:
        if rows[0][2] == body.password:
            con.execute(f"update users set logged=true where id='{rows[0][0]}'")
            conn.commit()
            event = User(id = rows[0][0],name = rows[0][1],type = rows[0][3],email = rows[0][4])
            conn.close()
            return jsonify(event)
        else:
            return Info(error=InfoError(f"Invalid Password")), 400
    conn.close()
    return 'do some magic!'

def logout_user(userid):  # noqa: E501
    """Logs user into the system

     # noqa: E501

    :param userid: Username that needs to be logged out.
    :type userid: int

    :rtype: None
    """
    conn = db.DbInterface().connect()
    con = conn.cursor()
    con.execute(f"select logged,id,name,type,email from users where id={userid}")
    rows = con.fetchall()
    if len(rows) > 0:
        if rows[0][0] == 1:
            event = User(id = rows[0][1],name = rows[0][2],type = rows[0][3],email = rows[0][4])
            con.execute(f"update users set logged=false where id={userid}")
            conn.commit()
            conn.close()
            return jsonify(event)
        else:
            return Info(error=InfoError(f"User not logged in")), 500

    return Info(error=InfoError(f"Unable to find user")), 400


def modify_user_by_id(userid, body):  # noqa: E501
    """Update user

    This can only be done by the logged in user. # noqa: E501

    :param userid: id that need to be updated
    :type userid: int
    :param body: Update user object
    :type body: dict | bytes

    :rtype: User
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    conn = db.DbInterface().connect()
    con = conn.cursor()
    con.execute(f"select logged,id,name,type,email from users where id='{userid}'")
    rows = con.fetchall()
    if len(rows) > 0:
        con.execute(f"update users set name='{body.name}',password='{body.password}',email='{body.email}' where id={userid}")
        conn.commit()
        con.execute(f"select id,name,type,email,logged from users where id={userid}")
        detail = con.fetchall()
        event = User(id = detail[0][0],name = detail[0][1],type = detail[0][2],email = detail[0][3],logged = detail[0][4])
        conn.close()
        return jsonify(event)
    conn.close()
    return Info(error=InfoError(f"Unable to find user")), 400
