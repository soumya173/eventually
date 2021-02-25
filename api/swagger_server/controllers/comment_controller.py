import connexion
import six
from flask import jsonify

from swagger_server.models.comment import Comment  # noqa: E501
from swagger_server.models.comments import Comments  # noqa: E501
from swagger_server.models.info import Info  # noqa: E501
from swagger_server import util
from swagger_server.dbinterface import dbinterface as db

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def create_comment(body):  # noqa: E501
    """Create a comment

    Create a comment # noqa: E501

    :param body: Created comment details
    :type body: dict | bytes

    :rtype: Comment
    """
    if connexion.request.is_json:
        body = Comment.from_dict(connexion.request.get_json())  # noqa: E501

    con = db.DbInterface().connect()
    cur = con.cursor()

    if body.comment is None and body.rating is None:
        return Info(Error=f"Invalid request: No comment or rating provided"), 400

    if body.comment is None:
        body.comment = 'NULL'
    if body.rating is None:
        body.rating = 0

    sql = f"select * from submission where id = '{body.submission_id}';"
    print(sql)
    submsn = cur.execute(sql).fetchall()
    if not len(submsn):
        db.DbInterface().disconnect()
        return Info(critical=f"No Submission found with id: {body.submission_id} in this Event."), 404
 
    if body.rating != 0:
        sql = f" update comments set rating = 0 where user_id = '{body.user_id}' and submission_id = '{body.submission_id}';" # and rating != 0;"
        print(sql)
        cur.execute(sql)
        con.commit()

    sql2 = f"insert into comments (comment, user_id, submission_id, rating) values ( '{body.comment}', {body.user_id}, {body.submission_id}, {body.rating} );"
    print(sql2)
    cur.execute(sql2)
    con.commit()
    sql3 = f"SELECT last_insert_rowid();"
    cmt_id = cur.execute(sql3).fetchone()[0]
    db.DbInterface().disconnect()

    return get_comment_by_id(cmt_id)


def delete_comment_by_id(commentid):  # noqa: E501
    """Delete comment

    Delete comment # noqa: E501

    :param commentid: ID of the comment to delete
    :type commentid: int

    :rtype: Comment
    """
    con = db.DbInterface().connect()
    cur = con.cursor()
    sql = "select id,comment from comments where id = {};".format(commentid)
    print(sql)
    r = cur.execute(sql).fetchone()
    if r is None:
        db.DbInterface().disconnect()
        return Info(critical="No comment found with specified id: {}".format(commentid)), 404
    if r[0] == commentid:
        sql="delete from comments where id = {}".format(commentid)
        cur.execute(sql)
        con.commit()
        db.DbInterface().disconnect()
        return Info(info="Comment deleted: {}".format(r[1])), 200
    db.DbInterface().disconnect()
    return Info(error="Unknown Error: "), 501


def get_all_comments():  # noqa: E501
    """Get all the comments

    Get all the comments # noqa: E501


    :rtype: Comments
    """
    con = db.DbInterface().connect()
    con.row_factory = dict_factory
    cur = con.cursor()
    rows = cur.execute("select * from comments;").fetchall()
    db.DbInterface().disconnect()
    return jsonify(rows)


def get_comment_by_id(commentid):  # noqa: E501
    """Get comment by id

    Get comment by id # noqa: E501

    :param commentid: ID of the comment to fetch
    :type commentid: int

    :rtype: Comments
    """
    con = db.DbInterface().connect()
    con.row_factory = dict_factory
    cur = con.cursor()
    sql = "select * from comments where id = {};".format(commentid)
    print(sql)
    r = cur.execute(sql).fetchall()
    print(r)
    if r is None or len(r) == 0:
        db.DbInterface().disconnect()
        return Info(critical=f"No comments found with comment_id : {commentid}"), 404
    db.DbInterface().disconnect()
    return jsonify(r)


def modify_comment_by_id(commentid, body):  # noqa: E501
    """Modify comment

    Modify comment # noqa: E501

    :param commentid: ID of the comment to modify
    :type commentid: int
    :param body: ID of the comment to modify
    :type body: dict | bytes

    :rtype: Comment
    """
    if connexion.request.is_json:
        body = Comment.from_dict(connexion.request.get_json())  # noqa: E501

    con = db.DbInterface().connect()
    cur = con.cursor()

    sql = "select id,comment from comments where id = {};".format(commentid)
    print(sql)
    r = cur.execute(sql).fetchone()
    if r is None:
        db.DbInterface().disconnect()
        return Info(critical="No comment found with specified id: {}".format(commentid)), 404

    if body.comment is None and body.rating is None:
        return Info(Error=f"Invalid request: No comment or rating provided"), 400

    if body.comment is None:
        body.comment = 'NULL'
    if body.rating is None:
        body.rating = 0

    sql = f"select * from submission where id = '{body.submission_id}';"
    print(sql)
    submsn = cur.execute(sql).fetchall()
    if not len(submsn):
        db.DbInterface().disconnect()
        return Info(critical=f"No Submission found with id: {body.submission_id} in this Event."), 404
 
    if body.rating != 0:
        sql = f"update comments set rating = 0 where user_id = '{body.user_id}' and submission_id = '{body.submission_id}';" # and rating != 0;"
        print(sql)
        cur.execute(sql)
        con.commit()

    sql2 = f"update comments set comment='{body.comment}', user_id={body.user_id}, submission_id={body.submission_id}, rating={body.rating} where id = {commentid};"
    print(sql2)
    cur.execute(sql2)
    con.commit()
    db.DbInterface().disconnect()

    return get_comment_by_id(commentid)
