from flask import Flask
from flaskext.mysql import MySQL
import pandas as pd
from datetime import datetime
from spotify_client import *

# Create an object named app 
app = Flask(__name__)

# Configure plays_db MySQL database
app.config['MYSQL_DATABASE_HOST'] = 'database'
app.config['MYSQL_DATABASE_USER'] = 'dohee'
app.config['MYSQL_DATABASE_PASSWORD'] = 'doheepassword'
app.config['MYSQL_DATABASE_DB'] = 'plays_db'
app.config['MYSQL_DATABASE_PORT'] = 3306
mysql = MySQL()
mysql.init_app(app)
connection = mysql.connect()
connection.autocommit(True)
cursor = connection.cursor()

# Execute the code below only once.
def init_plays_db():
    tracks_table = """CREATE TABLE IF NOT EXISTS plays_db.tracks(
        song_name VARCHAR(200),
        artist_name VARCHAR(200),
        played_at VARCHAR(200),
        timestamp VARCHAR(200),
        CONSTRAINT primary_key_constraint PRIMARY KEY (played_at);
    )
    """
    cursor.execute(tracks_table)
    print("Opened database successfully")

def insert_tracks(song_name, artist_name, played_at, timestamp):
    pass

# Validate downloaded data
def check_if_valid_data(df: pd.DataFrame) -> bool:
    # Check if dataframe is empty
    if df.empty:
        print("No songs downloaded. Finishing execution")
        return False

    # Primary Key check
    if pd.Series(df['played_at']).is_unique:
        pass
    else:
        raise Exception("Primary Key Check failed")

    # Check for nulls
    if df.isnull().values.any():
        raise Exception("Null value found")

    #Check that all timestamps are from yesterday's date
    # yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
    # yesterday = yesterday.replace(hour=0, minute=0, second=0, microsecond=0)

    # timestamps = df["timestamp"].tolist()
    # for timestamp in timestamps:
    #     if datetime.datetime.strptime(timestamp, '%Y-%m-%d') != yesterday:
    #         raise Exception("At least one of returned songs does not come from within the last 24 hours")
    
    return True

def download_tracks():
    # Extract part of the ETL process
    spotify_client = SpotifyClient()
    data = spotify_client.get_recent_tracks(50, 2)

    song_names = []
    artist_names = []
    played_at_list = []
    timestamps = []

    # Extracting only the relevant bits of data from the json object      
    for song in data["items"]:
        song_names.append(song["track"]["name"])
        artist_names.append(song["track"]["album"]["artists"][0]["name"])
        played_at_list.append(song["played_at"])
        timestamps.append(song["played_at"][0:10])
        
    # Prepare a dictionary in order to turn it into a pandas dataframe below       
    song_dict = {
        "song_name" : song_names,
        "artist_name": artist_names,
        "played_at" : played_at_list,
        "timestamp" : timestamps
    }

    song_df = pd.DataFrame(song_dict, columns = ["song_name", "artist_name", "played_at", "timestamp"])
    
    return song_df

@app.route('/')
def home():
    # Extract
    tracks_df = download_tracks()
    print("Downloaded tracks played in the past 2 hours")

    # Validate
    if check_if_valid_data(tracks_df):
        print("Data valid, proceed to Load stage")
    
    # Load
    insert_tracks(tracks_df)
    print("Loaded tracks into plays_db.tracks")

    return "Loaded to plays_db"+tracks_df

if __name__ == '__main__':
    init_plays_db()
    app.run(host='0.0.0.0', port=80)