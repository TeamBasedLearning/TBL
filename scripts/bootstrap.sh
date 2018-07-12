# Update apt-get
apt-get update

# Install dependencies
apt-get install -y \
  apt-transport-https \
  ca-certificates \
  curl \
  software-properties-common \
  nginx vim git

# Modify language to PT-BR
locale-gen pt_BR.UTF-8

# Get the GPG docker key
curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - && apt-key fingerprint 0EBFCD88

# Get the repository of docker and docker-compose
curl -L https://github.com/docker/compose/releases/download/1.21.0/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose && chmod +x /usr/local/bin/docker-compose && add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

 # Install docker CE
apt-get update && apt-get install -y docker-ce

docker --version && docker-compose --version

# Clone the TBL repository
git clone https://github.com/VictorArnaud/TBL.git
cd TBL

# Run deploy enviroment
docker-compose -f docker-compose.deploy.yml up -d --build

# Config NGINX
# Copying the nginx configuration file into the container
cp scripts/nginx.conf /etc/nginx/conf.d/nginx.conf
# Removing the nginx default page
rm -rf /usr/share/nginx/html/*
rm -rf /etc/nginx/sites-enabled/* && rm -rf /etc/nginx/sites-available/*

# Pick up the static files and insert them inside the nginx repository so that they are served
cp -r /home/vagrant/TBL/pgtbl/tbl/staticfiles/* /usr/share/nginx/html

# Run nginx
service nginx restart
systemctl status nginx.service
