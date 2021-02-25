import connexion
import six

from swagger_server.models.info import Info  # noqa: E501
from swagger_server.models.subscription import Subscription  # noqa: E501
from swagger_server.models.subscriptions import Subscriptions  # noqa: E501
from swagger_server import util
from swagger_server.models.info_error import InfoError
from swagger_server import util
from flask import jsonify
from swagger_server.dbinterface import dbinterface as db


def create_subscription(body):  # noqa: E501
    """Create a subscription

    Create a subscription # noqa: E501

    :param body: Created subscription details
    :type body: dict | bytes

    :rtype: Subscription
    """
    if connexion.request.is_json:
        body = Subscription.from_dict(connexion.request.get_json())  # noqa: E501
    conn = db.DbInterface().connect()
    con = conn.cursor()
    con.execute(f"SELECT * FROM subscription WHERE user_id='{body.user_id}' and event_id='{body.event_id}'")
    rows = con.fetchall()
    if len(rows) > 0:
        return Info(error=InfoError("User already subscribed to the event")), 400

    con.execute(f"INSERT INTO subscription (user_id,event_id) VALUES ('{body.user_id}', '{body.event_id}'")
    conn.commit()
    con.execute(f"SELECT id,user_id,event_id FROM subscription WHERE user_id='{body.user_id}' and event_id='{body.event_id}'")
    rows = con.fetchall()
    event = User(id = rows[0][0],user_id = rows[0][1],event_id = rows[0][2])
    conn.close()
    return jsonify(event)

def delete_subscription_by_id(subscriptionid):  # noqa: E501
    """Delete subscription

    Delete subscription # noqa: E501

    :param subscriptionid: ID of the subscription to delete
    :type subscriptionid: int

    :rtype: Subscription
    """
    conn = db.DbInterface().connect()
    con = conn.cursor()
    con.execute(f"SELECT id,user_id,event_id FROM subscription WHERE id='{subsciptionid}'")
    rows = con.fetchall()
    if len(rows) > 0:
        object = Subscription(id=rows[0][0],user_id=rows[0][1],event_id=rows[0][2])
        con.execute(f"delete from subscription WHERE id='{subsciptionid}'")
        conn.commit()
        conn.close()
        return jsonify(object)
    return Info(error=InfoError("User not subscribed")), 400


def get_all_subscriptions():  # noqa: E501
    """Get all the subscriptions

    Get all the subscriptions # noqa: E501


    :rtype: Subscriptions
    """
    conn = db.DbInterface().connect()
    con = conn.cursor()
    con.execute(f"SELECT id,user_id,event_id FROM subscription")
    rows = con.fetchall()
    events = []
    if len(rows) > 0:
        for r in rows:
            events.append(Subscription(id=r[0],
                            user_id=r[1],
                            event_id=r[2]))
    conn.close()
    return jsonify(events)


def get_subscription_by_id(subscriptionid):  # noqa: E501
    """Get subscription by id

    Get subscription by id # noqa: E501

    :param subscriptionid: ID of the subscription to fetch
    :type subscriptionid: int

    :rtype: Subscriptions
    """
    conn = db.DbInterface().connect()
    con = conn.cursor()
    con.execute(f"SELECT id,user_id,event_id FROM subscription WHERE id='{subsciptionid}'")
    rows = con.fetchall()
    if len(rows) > 0:
        object = Subscription(id=rows[0][0],user_id=rows[0][1],event_id=rows[0][2])
        conn.close()
        return jsonify(object)
    conn.close()
    return Info(error=InfoError("Subscription id doesnt exists")), 400


def modify_subscription_by_id(subscriptionid, body):  # noqa: E501
    """Modify subscription

    Modify subscription # noqa: E501

    :param subscriptionid: ID of the subscription to modify
    :type subscriptionid: int
    :param body: ID of the subscription to modify
    :type body: dict | bytes

    :rtype: Subscription
    """
    if connexion.request.is_json:
        body = Subscription.from_dict(connexion.request.get_json())  # noqa: E501
    conn = db.DbInterface().connect()
    con = conn.cursor()
    con.execute(f"SELECT id,user_id,event_id FROM subscription WHERE id='{subsciptionid}'")
    rows = con.fetchall()
    if len(rows) > 0:
        con.execute(f"update subscription set(user_id = '{body.user_id}',event_id='{body.event_id}') where id={subscriptionid}")
        conn.commit()
        con.execute(f"select id,user_id,event_id subscription from where id={subscriptionid}")
        detail = con.fetchall()
        event = Subscription(id = detail[0][0],user_id = detail[0][1],event_id = detail[0][2])
        conn.close()
        return jsonify(event)
    conn.close()
    return Info(error=InfoError("No subscription found")), 400
