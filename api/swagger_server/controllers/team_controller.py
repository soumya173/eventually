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
    
    event_id = body['event_id']
    name = body['name']
    user_ids = body['user_ids']
    lead_user_id = body['lead_user_id']
    type = body['type']  

    sql = "insert into teams (event_id, name, user_ids, lead_user_id, type) values ( {}, '{}', '{}', {}, '{}');".format(event_id, name, user_ids, lead_user_id, type)
    print(sql)
    con = db.DbInterface()
    con.connect()
    cur = con.cursor()
    rs = cur.execute(sql)
    con.commit()
    sql2 = "SELECT last_insert_rowid();"
    teamid = cur.execute(sql2).fetchone()[0]
    con.disconnect()
    if connexion.request.is_json:
        body = Team.from_dict(connexion.request.get_json())  # noqa: E501
    return get_team_by_id(teamid)


def delete_team_by_id(teamid):  # noqa: E501
    """Delete Team

    Delete team # noqa: E501

    :param teamid: ID of the event to delete
    :type teamid: int

    :rtype: Team
    """
    con = db.DbInterface()
    con.connect()
    con.row_factory = dict_factory
    cur = con.cursor()
    sql = "select id,name from teams where id = {};".format(teamid)
    print(sql)
    r = cur.execute(sql).fetchone()
    if r is None:
        con.disconnect()
        return Info(critical="No team found with specified id: {}".format(teamid)), 400
    if r[0] == teamid:
        sql="delete from teams where id = {}".format(teamid)
        cur.execute(sql)
        con.disconnect()
        return Info(info="Team deleted: {}".format(r[1])), 200
    con.disconnect()
    return Info(error="Unknown Error: "), 501


def get_all_teams():  # noqa: E501
    """Get all the teams

    Get all the teams # noqa: E501


    :rtype: Teams
    """
    con = db.DbInterface()
    con.connect()
    con.row_factory = dict_factory
    cur = con.cursor()
    rows = cur.execute("select * from teams;").fetchall()
    teams = []
    for r in rows:
        teams.append(Team(r[0:]))
    con.disconnect()
    return jsonify(Team(rows))


def get_team_by_id(teamid):  # noqa: E501
    """Get team by id

    Get team by id # noqa: E501

    :param teamid: ID of the event to fetch
    :type teamid: int

    :rtype: Team
    """
    con = db.DbInterface()
    con.connect()
    con.row_factory = dict_factory
    cur = con.cursor()
    sql = "select * from teams where id = {};".format(teamid)
    print(sql)
    r = cur.execute(sql).fetchone()
    print(r)
    teams = []
    con.disconnect()
    return jsonify(Team(r[0], r[1], r[2], r[3], r[4], r[5], r[6]))


def modify_team_by_id(teamid, body):  # noqa: E501
    """Modify team

    Modify team # noqa: E501

    :param teamid: ID of the team to modify
    :type teamid: int
    :param body: ID of the event to modify
    :type body: dict | bytes

    :rtype: Team
    """
    event_id = body['event_id']
    name = body['name']
    user_ids = body['user_ids']
    lead_user_id = body['lead_user_id']
    type = body['type']
    if 'reward_id' in body.keys():
        reward_id = body['reward_id']
    else:
         reward_id = 'NULL'

	

    sql = "update teams set event_id = {}, name = '{}', user_ids = '{}', lead_user_id = {}, type = '{}', reward_id = {} where id = {};".format(event_id, name, user_ids, lead_user_id, type, reward_id, teamid)
    print(sql)
    con = db.DbInterface()
    con.connect()
    cur = con.cursor()
    rs = cur.execute(sql)
    con.commit()
    con.disconnect()
    if connexion.request.is_json:
        body = Team.from_dict(connexion.request.get_json())  # noqa: E501
    return get_team_by_id(teamid)
