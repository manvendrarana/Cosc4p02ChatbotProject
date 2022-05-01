# Back-End

## Requirements

- Node.js envoirment
- MySQl
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
- create a local python 3.9.0 enviornment called "venv". 
- install required modules.
- Run the following SQL queries in the MySql work bench DROP DATABASE IF EXISTS testDb; CREATE DATABASE testDb; ALTER DATABASE testDb CHARACTER SET utf8;
- npm start
- During initial lauch the Ai module will download Google Tapas models and Bert model which might cause it to take a while to initialize.
- make sure .env in the root back-end folder has MYSQL_USER, MYSQL_PASSWORD, SALT, ADMIN_PASSWORD.

### Additional info

- The username for admin login on front end is "admin" as functionality for addition or removal of admins to sql server was not implemented.
- Admin can be access by entering "font-end url"/admin
- At any point the server is down the wifi icon on the screen will flash both for admin and user. They can try to reconnect by clicking on that icon.
- MySql can be installed from here https://www.mysql.com/downloads/

### Credit for Ai models

- https://haystack.deepset.ai/tutorials/table-qa
- https://arxiv.org/abs/2108.04049
- https://huggingface.co/google/tapas-large-finetuned-sqa
- https://www.microsoft.com/en-us/research/publication/search-based-neural-structured-learning-sequential-question-answering/
