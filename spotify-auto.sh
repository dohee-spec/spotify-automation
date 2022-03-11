systemctl start docker
systemctl enable docker
curl -L "https://github.com/docker/compose/releases/download/1.26.2/docker-compose-$(uname -s)-$(uname -m)" \-o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
mkdir -p /home/pi/spotify-auto
FOLDER="https://raw.githubusercontent.com/dohee-spec/spotify-automation/main/"
curl -s --create-dirs -o "/home/pi/spotify-auto/app.py" -L "$FOLDER"app.py
curl -s --create-dirs -o "/home/pi/spotify-auto/secrets.py" -L "$FOLDER"secrets.py
curl -s --create-dirs -o "/home/pi/spotify-auto/spotify_client.py" -L "$FOLDER"spotify_client.py
curl -s --create-dirs -o "/home/pi/spotify-auto/tokens.py" -L "$FOLDER"tokens.py
curl -s --create-dirs -o "/home/pi/spotify-auto/requirements.txt" -L "$FOLDER"requirements.txt
curl -s --create-dirs -o "/home/pi/spotify-auto/Dockerfile" -L "$FOLDER"Dockerfile
curl -s --create-dirs -o "/home/pi/spotify-auto/docker-compose.yml" -L "$FOLDER"docker-compose.yml
cd /home/pi/spotify-auto
docker build -t dohee/spotify-auto:latest .
docker-compose up -d