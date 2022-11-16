#!/bin/bash
set -e

# Set up the timezone
# ===================
sudo timedatectl set-timezone Asia/Jakarta

# Set up the repository
# =====================
sudo apt-get update
sudo apt-get install curl -y

# Install Docker Engine
# =====================
SERVER_VERSION=$(docker version -f "{{.Server.Version}}")
SERVER_VERSION_MAJOR=$(echo "$SERVER_VERSION"| cut -d'.' -f 1)
SERVER_VERSION_MINOR=$(echo "$SERVER_VERSION"| cut -d'.' -f 2)
SERVER_VERSION_BUILD=$(echo "$SERVER_VERSION"| cut -d'.' -f 3)

if [ "${SERVER_VERSION_MAJOR}" -ge 20 ] && \
   [ "${SERVER_VERSION_MINOR}" -ge 10 ]  && \
   [ "${SERVER_VERSION_BUILD}" -ge 5 ]; then
    echo "Docker version >= 20.10.5 it's ok"
else
    echo "Docker version less than 20.10.5 can't continue"
    curl -fsSL https://get.docker.com -o get-docker.sh
    sh get-docker.sh
fi

sudo chmod 777 /var/run/docker.sock
sudo usermod -aG docker $USER

# Install Docker Compose
# ======================
sudo curl -L "https://github.com/docker/compose/releases/download/v2.2.3/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Install Lazydocker
# ==================
sudo curl https://raw.githubusercontent.com/jesseduffield/lazydocker/master/scripts/install_update_linux.sh | bash

# Install sshpass
# ==================
sudo apt-get install sshpass 

# SwapMemory JetsonHacksNano
# ==================
sudo curl -o setSwapMemorySize.sh https://raw.githubusercontent.com/JetsonHacksNano/resizeSwapMemory/master/setSwapMemorySize.sh
sudo chmod +x setSwapMemorySize.sh
sudo ./setSwapMemorySize.sh -g 8


# Setup PWM Fan
# ==================
sudo mv rc.local /etc/
sudo chmod u+x /etc/rc.local
