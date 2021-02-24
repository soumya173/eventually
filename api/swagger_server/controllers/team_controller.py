import connexion
import six
import json
from flask import jsonify

from swagger_server.models.info import Info  # noqa: E501
from swagger_server.models.team import Team  # noqa: E501
from swagger_server.models.teams import Teams  # noqa: E501
from swagger_server import util
from swagger_server.dbinterface import dbinterface as db

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
	
def create_team(body):  # noqa: E501
    """Create a team

    Create a team # noqa: E501

    :param body: Created evenet details
    :type body: dict | bytes

    :rtype: Team
    """
    if connexion.request.is_json:
        body = Team.from_dict(connexion.request.get_json())  # noqa: E501
    
    if body.lead_user_id not in body.user_ids:
        return Info(error=f"The lead user must be a memeber in the team."), 400

    con = db.DbInterface().connect()
    cur = con.cursor()	

    sql = f"select * from teams where name = '{body.name}' and event_id = {body.event_id};"
    print(sql)
    teamid = cur.execute(sql).fetchall()
    if len(teamid):
        db.DbInterface().disconnect()
        return Info(critical=f"A team already exists with name: {body.name} in this Event. Please choose other name"), 400


    for user_id in body.user_ids:
        sql1 = f"select name from users where id = {user_id}"
        res = cur.execute(sql1).fetchone()
        if res is None:
            db.DbInterface().disconnect()
            return Info(critical=f"No user found with user_id: {user_id}"), 404

    sql = f"select user_ids from teams where event_id = {body.event_id}"
    users_in_this_event = cur.execute(sql).fetchall()
    for user_id in body.user_ids:
        for user in users_in_this_event:
            if user_id in eval(user[0]):
                db.DbInterface().disconnect()
                return Info(critical=f"User with id {user_id} is already in an other team"), 400

    if body.reward_id is None:
        body.reward_id = 'NULL'

    sql = f"select id,title from events where id = {body.event_id};"
    print(sql)
    r = cur.execute(sql).fetchone()
    if r is None:
        db.DbInterface().disconnect()
        return Info(critical="No event found with specified id: {}".format(body.event_id)), 404

    sql = f"select max_user, min_user from events where id = {body.event_id};"
    print(sql)
    max_user, min_user = cur.execute(sql).fetchone()
    print(max_user, min_user, "NIKIL")
    if len(body.user_ids) > max_user or len(body.user_ids) < min_user:
        return Info(error=f"Team Criteria Validation Error: minimum members allowed is {min_user} & maximum members allowed is {max_user}"), 400

    sql2 = f"insert into teams (event_id, name, reward_id, user_ids, lead_user_id, type) values ( {body.event_id}, '{body.name}', {body.reward_id}, '{body.user_ids}', {body.lead_user_id}, '{body.type}' );"
    print(sql2)
    cur.execute(sql2)
    con.commit()
    sql3 = f"SELECT last_insert_rowid();"
    teamid = cur.execute(sql3).fetchone()[0]
    db.DbInterface().disconnect()

    return get_team_by_id(teamid)


def delete_team_by_id(teamid):  # noqa: E501
    """Delete Team

    Delete team # noqa: E501

    :param teamid: ID of the event to delete
    :type teamid: int

    :rtype: Team
    """
    con = db.DbInterface().connect()
    cur = con.cursor()
    sql = "select id,name from teams where id = {};".format(teamid)
    print(sql)
    r = cur.execute(sql).fetchone()
    if r is None:
        db.DbInterface().disconnect()
        return Info(critical="No team found with specified id: {}".format(teamid)), 404
    if r[0] == teamid:
        sql="delete from teams where id = {}".format(teamid)
        cur.execute(sql)
        con.commit()
        db.DbInterface().disconnect()
        return Info(info="Team deleted: {}".format(r[1])), 200
    db.DbInterface().disconnect()
    return Info(error="Unknown Error: "), 501


def get_all_teams():  # noqa: E501
    """Get all the teams

    Get all the teams # noqa: E501


    :rtype: Teams
    """
    con = db.DbInterface().connect()
    con.row_factory = dict_factory
    cur = con.cursor()
    rows = cur.execute("select * from teams;").fetchall()
    # teams = []
    # for r in rows:
    #     print(r)
    #     teams.append(Team(r))
    db.DbInterface().disconnect()
    return jsonify(rows)


def get_team_by_id(teamid):  # noqa: E501
    """Get team by id

    Get team by id # noqa: E501

    :param teamid: ID of the event to fetch
    :type teamid: int

    :rtype: Team
    """
    con = db.DbInterface().connect()
    con.row_factory = dict_factory
    cur = con.cursor()
    sql = "select * from teams where id = {};".format(teamid)
    print(sql)
    r = cur.execute(sql).fetchone()
    print(r)
    if r is None or len(r) == 0:
        db.DbInterface().disconnect()
        return Info(critical=f"No team found with team_id: {teamid}"), 404
    db.DbInterface().disconnect()
    return jsonify(r) #return jsonify(Team(r[0], r[1], r[2], r[3], r[4], r[5], r[6]))


def modify_team_by_id(teamid, body):  # noqa: E501
    """Modify team

    Modify team # noqa: E501

    :param teamid: ID of the team to modify
    :type teamid: int
    :param body: ID of the event to modify
    :type body: dict | bytes

    :rtype: Team
    """

    con = db.DbInterface().connect()
    cur = con.cursor()

    sql = "select * from teams where id = {};".format(teamid)
    print(sql)
    r = cur.execute(sql).fetchone()
    print(r)
    if r is None:
        db.DbInterface().disconnect()
        return Info(critical=f"No team found with team_id: {teamid}"), 404

    if connexion.request.is_json:
        body = Team.from_dict(connexion.request.get_json())  # noqa: E501
    
    if body.lead_user_id not in body.user_ids:
        db.DbInterface().disconnect()
        return Info(error=f"The lead user must be a member in the team."), 400

    sql = f"select * from teams where name = '{body.name}' and event_id = {body.event_id};"
    print(sql)
    team_id = cur.execute(sql).fetchall()
    if len(team_id):
        return Info(critical=f"A team already exists with name: {body.name} in this Event. Please choose other name"), 400

    sql = f"select user_ids from teams where event_id = {body.event_id}"
    users_in_this_event = cur.execute(sql).fetchall()

    for user_id in body.user_ids:
        sql1 = f"select name from users where id = {user_id}"
        res = cur.execute(sql1).fetchone()
        if res is None:
            db.DbInterface().disconnect()
            return Info(critical=f"No user found with user_id: {user_id}"), 404

    for user_id in body.user_ids:
        for user in users_in_this_event:
            if user_id in eval(user[0]):
                db.DbInterface().disconnect()
                return Info(critical=f"User with id {user_id} is already in an other team"), 400

    if body.reward_id is None:
        body.reward_id = 'NULL'
    
    sql2 = f"update teams set event_id = {body.event_id}, name = '{body.name}', reward_id = {body.reward_id}, user_ids = '{body.user_ids}', lead_user_id = {body.lead_user_id}, type = '{body.type}' where id = {teamid};"
    print(sql2)
    cur.execute(sql2)
    con.commit()
    db.DbInterface().disconnect()

    return get_team_by_id(teamid)