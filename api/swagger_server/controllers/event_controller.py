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
from datetime import datetime

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
    con.execute(f"SELECT id, title, description, event_start_date, event_end_date, reg_start_date, reg_end_date, created_at, max_user, min_user, location, accept_file_type, accept_video_file FROM events WHERE title='{body.title}' and description='{body.description}'")
    rows = con.fetchall()
    if len(rows) > 0:
        return Info(error=InfoError("Event already exists"))

    con.execute(f"INSERT INTO events (title, description, event_start_date, event_end_date, reg_start_date, reg_end_date, max_user, min_user, accept_file_type, accept_video_file, location) VALUES ('{body.title}', '{body.description}', '{body.event_start_date}', '{body.event_end_date}', '{body.reg_start_date}', '{body.reg_end_date}', {body.max_user}, {body.min_user}, '{body.accept_file_type}', {body.accept_video_file}, '{body.location}')")
    conn.commit()
    con.execute(f"SELECT id, title, description, event_start_date, event_end_date, reg_start_date, reg_end_date, created_at, max_user, min_user, location, accept_file_type, accept_video_file FROM events WHERE title='{body.title}' and description='{body.description}'")
    rows = con.fetchall()
    event = Event(id=rows[0][0],
                    title=rows[0][1],
                    description=rows[0][2],
                    event_start_date=rows[0][3],
                    event_end_date=rows[0][4],
                    reg_start_date=rows[0][5],
                    reg_end_date=rows[0][6],
                    created_at=rows[0][7],
                    max_user=rows[0][8],
                    min_user=rows[0][9],
                    location=rows[0][10],
                    accept_file_type=rows[0][11],
                    accept_video_file=rows[0][12])
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
    con.execute(f"SELECT id, title, description, event_start_date, event_end_date, reg_start_date, reg_end_date, created_at, max_user, min_user, location, accept_file_type, accept_video_file FROM events WHERE id={eventid}")
    rows = con.fetchall()
    if len(rows) > 0:
        event = Event(id=rows[0][0],
                        title=rows[0][1],
                        description=rows[0][2],
                        event_start_date=rows[0][3],
                        event_end_date=rows[0][4],
                        reg_start_date=rows[0][5],
                        reg_end_date=rows[0][6],
                        created_at=rows[0][7],
                        max_user=rows[0][8],
                        min_user=rows[0][9],
                        location=rows[0][10],
                        accept_file_type=rows[0][11],
                        accept_video_file=rows[0][12])
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
    date_format = "%Y-%m-%d %H:%M:%S"
    events = get_all_events()
    events_json = json.loads(events.get_data(as_text=True))
    active_events = []
    now = datetime.strptime(datetime.today().strftime(date_format), date_format)
    for event in events_json:
        event_start = datetime.strptime(event['event_start_date'], date_format)
        event_end = datetime.strptime(event['event_end_date'], date_format)
        if event_start < now and event_end > now:
            active_events.append(Event(id=event['id'],
                            title=event['title'],
                            description=event['description'],
                            event_start_date=event['event_start_date'],
                            event_end_date=event['event_end_date'],
                            reg_start_date=event['reg_start_date'],
                            reg_end_date=event['reg_end_date'],
                            created_at=event['created_at'],
                            max_user=event['max_user'],
                            min_user=event['min_user'],
                            location=event['location'],
                            accept_file_type=event['accept_file_type'],
                            accept_video_file=event['accept_video_file']))
    return active_events


def get_all_events():  # noqa: E501
    """Get all the events

    Get all the events # noqa: E501


    :rtype: Events
    """
    conn = db.DbInterface().connect()
    con = conn.cursor()
    con.execute("SELECT id, title, description, event_start_date, event_end_date, reg_start_date, reg_end_date, created_at, max_user, min_user, location, accept_file_type, accept_video_file FROM events")
    rows = con.fetchall()
    events = []
    for r in rows:
        events.append(Event(id=r[0],
                        title=r[1],
                        description=r[2],
                        event_start_date=r[3],
                        event_end_date=r[4],
                        reg_start_date=r[5],
                        reg_end_date=r[6],
                        created_at=r[7],
                        max_user=r[8],
                        min_user=r[9],
                        location=r[10],
                        accept_file_type=r[11],
                        accept_video_file=r[12]))
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
    con.execute(f"SELECT id, title, description, event_start_date, event_end_date, reg_start_date, reg_end_date, created_at, max_user, min_user, location, accept_file_type, accept_video_file FROM events WHERE id={eventid}")
    rows = con.fetchall()
    if len(rows) > 0:
        event = Event(id=rows[0][0],
                        title=rows[0][1],
                        description=rows[0][2],
                        event_start_date=rows[0][3],
                        event_end_date=rows[0][4],
                        reg_start_date=rows[0][5],
                        reg_end_date=rows[0][6],
                        created_at=rows[0][7],
                        max_user=rows[0][8],
                        min_user=rows[0][9],
                        location=rows[0][10],
                        accept_file_type=rows[0][11],
                        accept_video_file=rows[0][12])
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
    con.execute(f"SELECT id, title, description, event_start_date, event_end_date, reg_start_date, reg_end_date, created_at, max_user, min_user, location, accept_file_type, accept_video_file FROM events WHERE id=(SELECT eventid FROM subscription where user_id={user_id})")
    rows = con.fetchall()
    events = []
    for r in rows:
        events.append(Event(id=r[0],
                        title=r[1],
                        description=r[2],
                        event_start_date=r[3],
                        event_end_date=r[4],
                        reg_start_date=r[5],
                        reg_end_date=r[6],
                        created_at=r[7],
                        max_user=r[8],
                        min_user=r[9],
                        location=r[10],
                        accept_file_type=r[11],
                        accept_video_file=r[12]))
    return jsonify(events)


def get_upcoming_event():  # noqa: E501
    """Get upcoming event

    Get upcoming event # noqa: E501


    :rtype: Events
    """
    date_format = "%Y-%m-%d %H:%M:%S"
    events = get_all_events()
    events_json = json.loads(events.get_data(as_text=True))
    upcoming_events = []
    now = datetime.strptime(datetime.today().strftime(date_format), date_format)
    for event in events_json:
        event_start = datetime.strptime(event['event_start_date'], date_format)
        event_end = datetime.strptime(event['event_end_date'], date_format)
        if event_start > now:
            upcoming_events.append(Event(id=event['id'],
                            title=event['title'],
                            description=event['description'],
                            event_start_date=event['event_start_date'],
                            event_end_date=event['event_end_date'],
                            reg_start_date=event['reg_start_date'],
                            reg_end_date=event['reg_end_date'],
                            created_at=event['created_at'],
                            max_user=event['max_user'],
                            min_user=event['min_user'],
                            location=event['location'],
                            accept_file_type=event['accept_file_type'],
                            accept_video_file=event['accept_video_file']))
    return upcoming_events


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
    con.execute(f"SELECT id, title, description, event_start_date, event_end_date, reg_start_date, reg_end_date, created_at, max_user, min_user, location, accept_file_type, accept_video_file FROM events WHERE id={eventid}")
    rows = con.fetchall()
    if len(rows) > 0:
        con.execute(f"UPDATE events SET title='{body.title}', description='{body.description}', event_start_date='{body.event_start_date}', event_end_date='{body.event_end_date}', reg_start_date='{body.reg_start_date}', reg_end_date='{body.reg_end_date}', max_user={body.max_user}, min_user={body.min_user}, accept_file_type='{body.accept_file_type}', accept_video_file={body.accept_video_file}, location='{body.location}' WHERE id={eventid}")
        conn.commit()
        con.execute(f"SELECT id, title, description, event_start_date, event_end_date, reg_start_date, reg_end_date, created_at, max_user, min_user, location, accept_file_type, accept_video_file FROM events WHERE id={eventid}")
        rows = con.fetchall()
        print(rows)
        event = Event(id=rows[0][0],
                        title=rows[0][1],
                        description=rows[0][2],
                        event_start_date=rows[0][3],
                        event_end_date=rows[0][4],
                        reg_start_date=rows[0][5],
                        reg_end_date=rows[0][6],
                        created_at=rows[0][7],
                        max_user=rows[0][8],
                        min_user=rows[0][9],
                        location=rows[0][10],
                        accept_file_type=rows[0][11],
                        accept_video_file=rows[0][12])
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
    con.execute(f"SELECT id, title, description, event_start_date, event_end_date, reg_start_date, reg_end_date, created_at, max_user, min_user, location, accept_file_type, accept_video_file FROM events WHERE title LIKE %{keyword}% or description LIKE %{keyword}%")
    rows = con.fetchall()
    events = []
    for r in rows:
        events.append(Event(id=r[0],
                        title=r[1],
                        description=r[2],
                        event_start_date=r[3],
                        event_end_date=r[4],
                        reg_start_date=r[5],
                        reg_end_date=r[6],
                        created_at=r[7],
                        max_user=r[8],
                        min_user=r[9],
                        location=r[10],
                        accept_file_type=r[11],
                        accept_video_file=r[12]))
    return jsonify(events)
