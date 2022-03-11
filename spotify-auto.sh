systemctl start docker
systemctl enable docker
curl -L "https://github.com/docker/compose/releases/download/1.26.2/docker-compose-$(uname -s)-$(uname -m)" \
-o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
mkdir -p /home/pi/spotify-auto
FOLDER="https://github.com/dohee-spec/spotify-automation/main/"
curl -s --create-dirs -o "/home/pi/spotify-automation/app.py" -L "$FOLDER"app.py
curl -s --create-dirs -o "/home/pi/spotify-automation/app.py" -L "$FOLDER"secrets.py
curl -s --create-dirs -o "/home/pi/spotify-automation/app.py" -L "$FOLDER"spotify_client.py
curl -s --create-dirs -o "/home/pi/spotify-automation/app.py" -L "$FOLDER"tokens.py
curl -s --create-dirs -o "/home/pi/spotify-automation/requirements.txt" -L "$FOLDER"requirements.txt
curl -s --create-dirs -o "/home/pi/spotify-automation/Dockerfile" -L "$FOLDER"Dockerfile
curl -s --create-dirs -o "/home/pi/spotify-automation/docker-compose.yml" -L "$FOLDER"docker-compose.yml
cd /home/pi/spotify-auto
docker build -t dohee/spotify-auto:latest .
docker-compose up -d