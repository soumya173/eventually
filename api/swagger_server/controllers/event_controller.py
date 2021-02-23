import connexion
import six
import json
from swagger_server.models.event import Event  # noqa: E501
from swagger_server.models.events import Events  # noqa: E501
from swagger_server.models.info import Info  # noqa: E501
from swagger_server.models.info_error import InfoError
from swagger_server import util
from flask import jsonify
from swagger_server.dbinterface import dbinterface as db

def create_event(body):  # noqa: E501
    """Create a event

    Create a event # noqa: E501

    :param body: Created evenet details
    :type body: dict | bytes

    :rtype: Event
    """
    if connexion.request.is_json:
        body = Event.from_dict(connexion.request.get_json())  # noqa: E501
    conn = db.DbInterface().connect()
    con = conn.cursor()
    con.execute(f"SELECT * FROM events WHERE title='{body.title}' and description='{body.description}'")
    rows = con.fetchall()
    if len(rows) > 0:
        return Info(error=InfoError("Event already exists"))

    con.execute(f"INSERT INTO events (title, description, event_start_date, event_end_date, reg_start_date, reg_end_date, max_user, min_user, accept_file_type, accept_video_file, location) VALUES ('{body.title}', '{body.description}', '{body.event_start_date}', '{body.event_end_date}', '{body.reg_start_date}', '{body.reg_end_date}', {body.max_user}, {body.min_user}, '{body.accept_file_type}', {body.accept_video_file}, '{body.location}')")
    conn.commit()
    con.execute(f"SELECT * FROM events WHERE title='{body.title}' and description='{body.description}'")
    rows = con.fetchall()
    event = Event(rows[0][0], rows[0][1], rows[0][2], rows[0][3], rows[0][4], rows[0][5], rows[0][6],
                    rows[0][7], rows[0][8], rows[0][9], rows[0][10], rows[0][11], rows[0][12])
    return jsonify(event)


def delete_event_by_id(eventid):  # noqa: E501
    """Delete event

    Delete event # noqa: E501

    :param eventid: ID of the event to delete
    :type eventid: int

    :rtype: Event
    """
    conn = db.DbInterface().connect()
    con = conn.cursor()
    con.execute(f"SELECT * FROM events WHERE id={eventid}")
    rows = con.fetchall()
    if len(rows) > 0:
        event = Event(rows[0][0], rows[0][1], rows[0][2], rows[0][3], rows[0][4], rows[0][5], rows[0][6],
                        rows[0][7], rows[0][8], rows[0][9], rows[0][10], rows[0][11], rows[0][12])
        con.execute(f"DELETE FROM events WHERE id={eventid}")
        con.commit()
    else:
        return Info(error=InfoError("Event not found"))
    return jsonify(event)


def get_active_event():  # noqa: E501
    """Get active event

    Get active event # noqa: E501


    :rtype: Events
    """
    return 'do some magic!'


def get_all_events():  # noqa: E501
    """Get all the events

    Get all the events # noqa: E501


    :rtype: Events
    """
    conn = db.DbInterface().connect()
    con = conn.cursor()
    con.execute("SELECT * FROM events")
    rows = con.fetchall()
    events = []
    for r in rows:
        events.append(Event(r[0], r[1], r[2], r[3], r[4], r[5], r[6],
                            r[7], r[8], r[9], r[10], r[11], r[12]))
    return jsonify(events)


def get_event_by_id(eventid):  # noqa: E501
    """Get event by id

    Get event by id # noqa: E501

    :param eventid: ID of the event to fetch
    :type eventid: int

    :rtype: Event
    """
    conn = db.DbInterface().connect()
    con = conn.cursor()
    con.execute(f"SELECT * FROM events WHERE id={eventid}")
    rows = con.fetchall()
    if len(rows) > 0:
        event = Event(rows[0][0], rows[0][1], rows[0][2], rows[0][3], rows[0][4], rows[0][5], rows[0][6],
                        rows[0][7], rows[0][8], rows[0][9], rows[0][10], rows[0][11], rows[0][12])
    else:
        return Info(error=InfoError("Event not found"))
    return jsonify(event)


def get_subscribed_event(user_id):  # noqa: E501
    """Get subscribed event

    Get subscribed event # noqa: E501

    :param user_id:
    :type user_id: int

    :rtype: Events
    """
    conn = db.DbInterface().connect()
    con = conn.cursor()
    con.execute(f"SELECT * FROM events WHERE id=(SELECT eventid FROM subscription where user_id={user_id})")
    rows = con.fetchall()
    events = []
    for r in rows:
        events.append(Event(r[0], r[1], r[2], r[3], r[4], r[5], r[6],
                            r[7], r[8], r[9], r[10], r[11], r[12]))
    return jsonify(events)


def get_upcoming_event():  # noqa: E501
    """Get upcoming event

    Get upcoming event # noqa: E501


    :rtype: Events
    """
    return 'do some magic!'


def modify_event_by_id(eventid, body):  # noqa: E501
    """Modify event

    Modify event # noqa: E501

    :param eventid: ID of the event to modify
    :type eventid: int
    :param body: ID of the event to modify
    :type body: dict | bytes

    :rtype: Event
    """
    if connexion.request.is_json:
        body = Event.from_dict(connexion.request.get_json())  # noqa: E501
    conn = db.DbInterface().connect()
    con = conn.cursor()
    con.execute(f"SELECT * FROM events WHERE id={eventid}")
    rows = con.fetchall()
    if len(rows) > 0:
        con.execute(f"UPDATE events SET (title, description, event_start_date, event_end_date, reg_start_date, reg_end_date, max_user, min_user, accept_file_type, accept_video_file, location) VALUES ('{body.title}', '{body.description}', '{body.event_start_date}', '{body.event_end_date}', '{body.reg_start_date}', '{body.reg_end_date}', {body.max_user}, {body.min_user}, '{body.accept_file_type}', {body.accept_video_file}, '{body.location}') WHERE id={eventid}")
        con.commit()
        con.execute(f"SELECT * FROM events WHERE id={eventid}")
        rows = con.fetchall()
        event = Event(rows[0][0], rows[0][1], rows[0][2], rows[0][3], rows[0][4], rows[0][5], rows[0][6],
                        rows[0][7], rows[0][8], rows[0][9], rows[0][10], rows[0][11], rows[0][12])
    else:
        return Info(error=InfoError("Event not found"))
    return jsonify(event)


def search_events_by_keyword(keyword):  # noqa: E501
    """Search events by keyword

    Search events by keyword # noqa: E501

    :param keyword:
    :type keyword: str

    :rtype: Events
    """
    conn = db.DbInterface().connect()
    con = conn.cursor()
    con.execute(f"SELECT * FROM events WHERE title LIKE %{keyword}% or description LIKE %{keyword}%")
    rows = con.fetchall()
    events = []
    for r in rows:
        events.append(Event(r[0], r[1], r[2], r[3], r[4], r[5], r[6],
                            r[7], r[8], r[9], r[10], r[11], r[12]))
    return jsonify(events)
