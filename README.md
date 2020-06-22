# rain_alert

if ubuntu, you can install notify-send by `apt install libnotify-bin`

if linux, set schedule with crontab
```
crontab -e
0 20 * * * {path}/rain_alert.py #edit it, add this
```
then it will work every day at 20:00.