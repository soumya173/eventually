import connexion
import six

from swagger_server.models.info import Info  # noqa: E501
from swagger_server.models.submission import Submission  # noqa: E501
from swagger_server.models.submissions import Submissions  # noqa: E501
from swagger_server import util
from flask import jsonify, send_file
from swagger_server.models.info_error import InfoError
from swagger_server.dbinterface import dbinterface as db
import os
import glob
import json

def create_submission(body):  # noqa: E501
    """Create a submission

    Create a submission # noqa: E501

    :param body: Created submission details
    :type body: dict | bytes

    :rtype: Submission
    """
    print("Before converison")
    if connexion.request.is_json:
        body = Submission.from_dict(connexion.request.get_json())  # noqa: E501
    print("inside create_submission")
    response = get_all_submissions()
    submissions = json.loads(response.get_data(as_text=True))
    print(submissions)
    submission_present = False
    for sub in submissions:
        if sub['title'] == body.title and sub['event_id'] == body.event_id and sub['team_id'] == body.team_id:
            submission_present = True
            break
    print(submission_present)
    if submission_present:
        return Info(error=InfoError("Submission already exists")), 400
    print("Creating new sub")
    conn = db.DbInterface().connect()
    con = conn.cursor()
    con.execute(f"INSERT INTO submission (event_id, title, team_id, video_file, views) VALUES ({body.event_id}, '{body.title}', {body.team_id}, '{body.video_file}, 0')")
    conn.commit()
    con.execute(f"SELECT id, event_id, title, team_id, video_file, submitted_at, views FROM submission WHERE event_id={body.event_id} AND team_id={body.team_id} AND title='{body.title}'")
    rows = con.fetchall()
    if len(rows) > 0:
        return Submission(id=rows[0][0],
                            event_id=rows[0][1],
                            title=rows[0][2],
                            team_id=rows[0][3],
                            video_file=rows[0][4],
                            submitted_at=rows[0][5],
                            views=rows[0][6])
    return Info(error=InfoError("Failed to insert submission data")), 500

def delete_submission_by_id(submissionid):  # noqa: E501
    """Delete submission

    Delete submission # noqa: E501

    :param submissionid: ID of the submission to delete
    :type submissionid: int

    :rtype: Submission
    """
    response = get_all_submissions()
    submissions = json.loads(response.get_data(as_text=True))
    submission_present = False
    deleted_submission = None
    for sub in submissions:
        if sub['id'] == submissionid:
            submission_present = True
            deleted_submission = sub
            break
    if not submission_present:
        return Info(error=InfoError("Submission not found")), 404
    conn = db.DbInterface().connect()
    con = conn.cursor()
    con.execute(f"DELETE FROM submission WHERE id={submissionid}")
    conn.commit()
    return jsonify(deleted_submission)


def delete_submitted_file_by_id(submissionid):  # noqa: E501
    """Delete submitted file

    Delete submitted file by id # noqa: E501

    :param submissionid: ID of the submitted file to delete
    :type submissionid: int

    :rtype: Info
    """
    directory = os.path.join('swagger_server', 'uploads', f"{submissionid}")
    if os.path.exists(directory):
        download_file = ''
        for t1, t2, filenames in os.walk(directory):
            for f in filenames:
                print(f)
                if f.endswith('.tar'):
                    download_file = f
                    break
        file_path = os.path.join('uploads', f"{submissionid}", download_file)
        os.remove(file_path)
    else:
        return Info(error=InfoError("Submission files not found")), 404
    return Info(info=InfoInfo("Submission files deleted successfully"))

def download_submission_by_id(submissionid):  # noqa: E501
    """Download submission by id

    Download submission by id # noqa: E501

    :param submissionid: ID of the submission to fetch
    :type submissionid: int

    :rtype: Submission
    """
    directory = os.path.join('swagger_server', 'uploads', f"{submissionid}")
    if not os.path.exists(directory):
        return Info(error=InfoError("Submission files not found")), 404
    download_file = ''
    for t1, t2, filenames in os.walk(directory):
        for f in filenames:
            print(f)
            if f.endswith('.tar'):
                download_file = f
                break
    file_path = os.path.join('uploads', f"{submissionid}", download_file)
    return send_file(file_path, as_attachment=True)


def get_all_submissions():  # noqa: E501
    """Get all the submissions

    Get all the submissions # noqa: E501


    :rtype: Submissions
    """
    conn = db.DbInterface().connect()
    con = conn.cursor()
    con.execute("SELECT id, event_id, title, team_id, video_file, submitted_at, views FROM submission")
    rows = con.fetchall()
    submissions = []
    for r in rows:
        submissions.append(Submission(id=r[0],
                                        event_id=r[1],
                                        title=r[2],
                                        team_id=r[3],
                                        video_file=r[4],
                                        submitted_at=r[5],
                                        views=r[6]))
    return jsonify(submissions)

def get_submission_by_id(submissionid):  # noqa: E501
    """Get submission by id

    Get submission by id # noqa: E501

    :param submissionid: ID of the submission to fetch
    :type submissionid: int

    :rtype: Submission
    """
    conn = db.DbInterface().connect()
    con = conn.cursor()
    con.execute(f"SELECT id, event_id, title, team_id, video_file, submitted_at, views FROM submission WHERE id={submissionid}")
    rows = con.fetchall()
    if len(rows) > 0:
        submission = Submission(id=rows[0][0],
                                event_id=rows[0][1],
                                title=rows[0][2],
                                team_id=rows[0][3],
                                video_file=rows[0][4],
                                submitted_at=rows[0][5],
                                views=rows[0][6])
    else:
        return Info(error=InfoError("Submission not found")), 404
    return jsonify(submission)


def modify_submission_by_id(submissionid, body):  # noqa: E501
    """Modify submission

    Modify submission # noqa: E501

    :param submissionid: ID of the submission to modify
    :type submissionid: int
    :param body: ID of the submission to modify
    :type body: dict | bytes

    :rtype: Submission
    """
    if connexion.request.is_json:
        body = Submission.from_dict(connexion.request.get_json())  # noqa: E501
    conn = db.DbInterface().connect()
    con = conn.cursor()
    con.execute(f"SELECT id, event_id, title, team_id, video_file, submitted_at, views FROM submission WHERE id={submissionid}")
    rows = con.fetchall()
    if len(rows) > 0:
        con.execute(f"UPDATE submission SET id={body.id}, event_id={body.event_id}, title='{body.title}', team_id={body.team_id}, video_file='{body.video_file}', submitted_at='{body.submitted_at}', views={body.views} WHERE id={submissionid}")
        conn.commit()
        con.execute(f"SELECT id, event_id, title, team_id, video_file, submitted_at, views FROM submission WHERE id={submissionid}")
        rows = con.fetchall()
        submission = Submission(id=rows[0][0],
                                event_id=rows[0][1],
                                title=rows[0][2],
                                team_id=rows[0][3],
                                video_file=rows[0][4],
                                submitted_at=rows[0][5],
                                views=rows[0][6])
    else:
        return Info(error=InfoError("Submission not found")), 404
    return jsonify(submission)


def upload_submission_file_by_id(submissionid, datafile):  # noqa: E501
    """Upload a submission file

    Upload a  submission file # noqa: E501

    :param submissionid: ID of the submission to modify
    :type submissionid: int
    :param datafile: Submission File
    :type datafile: werkzeug.datastructures.FileStorage

    :rtype: Info
    """
    directory = os.path.join('swagger_server', 'uploads', f"{submissionid}")
    if not os.path.exists(directory):
        os.makedirs(directory)
    filename = "submission.tar"
    print(os.path.join(directory, filename))
    if os.path.exists(os.path.join(directory, filename)):
        os.remove(os.path.join(directory, filename))
    datafile.save(directory, filename)
    return Info(info=InfoInfo("File uploaded successfully"))
