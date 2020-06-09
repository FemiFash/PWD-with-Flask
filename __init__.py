from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flaskext.markdown import Markdown
from flask_uploads.uploads import UploadSet, configure_uploads, IMAGES
"""
                                NOTE
Had to amend flask_uploads.uploads.py file as I am using werkzeug version 1.0. and dont 
want to go down to werkzeug version 0.16.0

The line... 
	from werkzeug import secure_filename, FileStorage 
has to be changed to..... 
	from werkzeug.utils import secure_filename
	from werkzeug.datastructures import FileStorage
	
Therefore have to figure a work around in the requirements.txt file as the line....
	-e git+https://github.com/fromzeroedu/flask_uploads#egg=flask_uploads
will cause migration ImportErrors if user is not using werkzeug version 0.16.0
Fix may be uploading my version to Git and pointing my requirements.txt to my version of flask_uploads
"""


app = Flask(__name__)
app.config.from_object('settings')
db = SQLAlchemy(app)

# Migrations
migrate = Migrate(app, db)

# Markdown
Markdown(app)

# Images
uploaded_images = UploadSet('images', IMAGES)
configure_uploads(app, uploaded_images)

from blog import views
from author import views
