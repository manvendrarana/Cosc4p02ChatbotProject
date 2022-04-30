# Back-End

## Requirements

- Node.js envoirment
- Node modules
    - Socket.io
    - python-shell
- Python 3.9.0 local enviornment named "venv".
- Python modules
    - pandas.
    - selenium.
    - Haystack from https://haystack.deepset.ai/overview/installation. (pip install farm-haystack) recommended.
    - pytorch-scatter.
    - unidecode.

### Initialization steps

- npm install on the "Back-end" directory.
- create a local python 3.9.0 library called "venv". 
- install required modules.
- npm start
- During initial lauch the Ai module will download Google Tapas models and Bert model which might cause it to take a while to initialize.
- make sure .env in the root back-end folder has
- MYSQL_USER, MYSQL_PASSWORD, SALT, ADMIN_PASSWORD.

### Additional info

- The username for admin login on front end is "admin" as functionality for addition or removal of admins to sql server was not implemented.
- Admin can be access by entering "font-end url"/admin
- At any point the server is down the wifi icon on the screen will flash both for admin and user. They can try to reconnect by clicking on that icon.
