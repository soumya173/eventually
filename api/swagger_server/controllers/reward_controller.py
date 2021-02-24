import connexion
import six
from flask import jsonify

from swagger_server.models.info import Info  # noqa: E501
from swagger_server.models.reward import Reward  # noqa: E501
from swagger_server.models.rewards import Rewards  # noqa: E501
from swagger_server import util
from swagger_server.dbinterface import dbinterface as db

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def create_reward(body):  # noqa: E501
    """Create a reward

    Create a reward # noqa: E501

    :param body: Created reward details
    :type body: dict | bytes

    :rtype: Reward
    """
    if connexion.request.is_json:
        body = Reward.from_dict(connexion.request.get_json())  # noqa: E501

    con = db.DbInterface().connect()
    cur = con.cursor()

    sql = f"select * from rewards where title = '{body.title}' and event_id = {body.event_id};"
    print(sql)
    rwds = cur.execute(sql).fetchall()
    if len(rwds):
        db.DbInterface().disconnect()
        return Info(error=f"A reward already exists for the title: {body.title} in this Event. Please choose other title"), 400

    sql = f"select * from events where id = '{body.event_id}';"
    print(sql)
    evnts = cur.execute(sql).fetchall()
    if not len(evnts):
        db.DbInterface().disconnect()
        return Info(critical=f"No Event found with id: {body.event_id}"), 404

    if body.type is None:
        body.type = 'NULL'
    if body.amount is None:
        body.amount = 0
    
    sql2 = f"insert into rewards (event_id, amount, type, title, position) values ( {body.event_id}, {body.amount}, '{body.type}', '{body.title}', {body.position} );"
    print(sql2)
    cur.execute(sql2)
    con.commit()
    sql3 = f"SELECT last_insert_rowid();"
    rwd_id = cur.execute(sql3).fetchone()[0]
    db.DbInterface().disconnect()

    return get_reward_by_id(rwd_id)


def delete_reward_by_id(rewardid):  # noqa: E501
    """Delete Reward

    Delete reward # noqa: E501

    :param rewardid: ID of the reward to delete
    :type rewardid: int

    :rtype: Reward
    """

    con = db.DbInterface().connect()
    cur = con.cursor()
    sql = "select id,title from rewards where id = {};".format(rewardid)
    print(sql)
    r = cur.execute(sql).fetchone()
    if r is None:
        db.DbInterface().disconnect()
        return Info(critical="No reward found with specified id: {}".format(rewardid)), 404
    if r[0] == rewardid:
        sql="delete from rewards where id = {}".format(rewardid)
        cur.execute(sql)
        con.commit()
        db.DbInterface().disconnect()
        return Info(info="Reward deleted: {}".format(r[1])), 200
    db.DbInterface().disconnect()
    return Info(error="Unknown Error: "), 501


def get_all_rewards():  # noqa: E501
    """Get all the rewards

    Get all the rewards # noqa: E501


    :rtype: Rewards
    """
    con = db.DbInterface().connect()
    con.row_factory = dict_factory
    cur = con.cursor()
    rows = cur.execute("select * from rewards;").fetchall()
    db.DbInterface().disconnect()
    return jsonify(rows)


def get_reward_by_event_id(eventid):  # noqa: E501
    """Get reward by event id

    Get reward by event id # noqa: E501

    :param eventid: ID of the event to fetch
    :type eventid: int

    :rtype: Rewards
    """
    con = db.DbInterface().connect()
    con.row_factory = dict_factory
    cur = con.cursor()
    sql = "select * from rewards where event_id = {};".format(eventid)
    print(sql)
    r = cur.execute(sql).fetchall()
    print(r)
    if r is None:
        db.DbInterface().disconnect()
        return Info(critical=f"No rewards found for the event with event_id : {eventid}"), 404
    db.DbInterface().disconnect()
    return jsonify(r)


def get_reward_by_id(rewardid):  # noqa: E501
    """Get reward by id

    Get reward by id # noqa: E501

    :param rewardid: ID of the reward to fetch
    :type rewardid: int

    :rtype: Reward
    """
    
    con = db.DbInterface().connect()
    con.row_factory = dict_factory
    cur = con.cursor()
    sql = "select * from rewards where id = {};".format(rewardid)
    print(sql)
    r = cur.execute(sql).fetchone()
    print(r)
    if r is None:
        db.DbInterface().disconnect()
        return Info(critical=f"No reward found with reward_id: {rewardid}"), 404
    db.DbInterface().disconnect()
    return jsonify(r) #return jsonify(Reward(r[0], r[1], r[2], r[3], r[4], r[5], r[6]))


def modify_reward_by_id(rewardid, body):  # noqa: E501
    """Modify reward

    Modify reward # noqa: E501

    :param rewardid: ID of the reward to modify
    :type rewardid: int
    :param body: ID of the reward to modify
    :type body: dict | bytes

    :rtype: Reward
    """

    if connexion.request.is_json:
        body = Reward.from_dict(connexion.request.get_json())  # noqa: E501

    con = db.DbInterface().connect()
    cur = con.cursor()

    sql = "select * from rewards where id = {};".format(rewardid)
    print(sql)
    r = cur.execute(sql).fetchone()
    print(r)
    if r is None:
        db.DbInterface().disconnect()
        return Info(critical=f"No reward found with reward_id: {rewardid}"), 404

    sql = f"select * from rewards where title = '{body.title}' and event_id = {body.event_id};"
    print(sql)
    rwds = cur.execute(sql).fetchall()
    if len(rwds):
        db.DbInterface().disconnect()
        return Info(error=f"A reward already exists for the title: {body.title} in this Event. Please choose other title"), 400

    sql = f"select * from events where id = '{body.event_id}';"
    print(sql)
    evnts = cur.execute(sql).fetchall()
    if not len(evnts):
        db.DbInterface().disconnect()
        return Info(critical=f"No Event found with id: {body.event_id}"), 404

    if body.type is None:
        body.type = 'NULL'
    if body.amount is None:
        body.amount = 0
    
    sql2 = f"update rewards set event_id={body.event_id}, amount={body.amount}, type='{body.type}',title='{body.title}',position={body.position};"
    print(sql2)
    cur.execute(sql2)
    con.commit()
    db.DbInterface().disconnect()

    return get_reward_by_id(rewardid)
