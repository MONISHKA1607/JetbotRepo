# =========================
# CONNECT TO JETBOT
# =========================

ssh csed@192.168.55.1

# PASSWORD
cslab768


# =========================
# CONNECT WIFI
# =========================

sudo nmcli device wifi connect AI-Lab password ai@tiet25


# =========================
# CHECK DOCKER IMAGES
# =========================

sudo docker images


# =========================
# ENABLE DOCKER
# =========================

sudo systemctl enable docker


# =========================
# START JUPYTER
# =========================

cd jetbot
./enable.sh $HOME


# =========================
# CHECK IP
# =========================

ifconfig


# =========================
# OPEN JUPYTER
# =========================

https://<jetbot_ip>:8888


# =========================
# INSTALL REQUIREMENTS
# =========================

pip3 install -r requirements.txt


# =========================
# RUN PROJECT
# =========================

python3 hand_guided_navigation.py


# =========================
# STOP ROBOT
# =========================

CTRL + C
