# eventually
Event management system

# Setup local backend server (for testing)
- Install pyhton 3 (https://www.python.org/downloads/)
- For windows, Open command prompt
  - Win + R
  - type 'cmd'
  - Enter
- Navigate to the local repo directory
  - cd /path/to/directory/
- Create virtual environment (not mandatory but better to handle dependancies)
  - pytho3 -m pip install --user virtualenv
  - python3 -m venv env
- Activate the virtual environment
  - .\env\Scripts\activate
- Install required packages
  - pip3 install -r requirements.txt
- Run flask server in localhost
  - python3 -m /app/directory (where __main__.py is present)

After this your server should be running and the requests should be processed properly.
