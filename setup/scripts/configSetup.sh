#sets up rc.local
echo "making config"
echo '{
    "SLEEP": true,
    "CLIENT":"/Matt",
    "ERROR": false,
    "URL":"https://distance-pi.herokuapp.com",
    "EXPIRATION": 18000,
    "MORNING": 7,
    "EVENING": 22
}' > /home/pi/DistancePi/code/config.json
#
# {
#   "SLEEP": true,
#   "CLIENT":"/Rachel",
#   "ERROR": false,
#   "URL":"https://distance-pi.herokuapp.com",
#   "EXPIRATION": 18000,
#   "MORNING": 7,
#   "EVENING": 22
# }
