#!/usr/bin/env python
import os
import requests

url = 'https://www.cwb.gov.tw/V8/C/W/Town/MOD/Week/6501000_Week_PC.html?T=2020052521-4'
#headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0'}
data = requests.get(url)#, headers=headers)

rainProb = []

if data.status_code == 200:
    tempStr = data.text.split('rainful d')
    for i in range(1, 7):
        tempRain = tempStr[i].split('<br>')
        prob = tempRain[1][0:2]
        if prob[-1]=='%':
            rainProb.append(int(prob[0:-1]))
        else:
            rainProb.append(int(prob))
    if ((rainProb[0] > 0) or (rainProb[1] > 0)):
        sysMsg = 'echo "Remember to bring umbrella tomorrow.\nProbability of Precipitation during daytime : ' + str(rainProb[0]) + '\nProbability of Precipitation during night : ' + str(rainProb[1]) + '"'
        os.system(sysMsg)
        os.system('notify-send "Rainy tomorrow"' + sysMsg[4:]) # if installed notify-send

'''
<tr class="data-title">
    <th colspan="14" id="rainful"><span class="h4">ééæ©çï¼%ï¼</span></th>
</tr>
<tr>
    <td headers="day1 rainful d1d"><i class="icon-umbrella" title="ééæ©ç"></i><br>90%</td>
    <td headers="day1 rainful d1n"><i class="icon-umbrella" title="ééæ©ç"></i><br>40%</td>
    <td headers="day2 rainful d2d"><i class="icon-umbrella" title="ééæ©ç"></i><br>30%</td>
    <td headers="day2 rainful d2n"><i class="icon-umbrella" title="ééæ©ç"></i><br>20%</td>
    <td headers="day3 rainful d3d"><i class="icon-umbrella" title="ééæ©ç"></i><br>80%</td>
    <td headers="day3 rainful d3n"><i class="icon-umbrella" title="ééæ©ç"></i><br>10%</td>
    <td headers="day4 rainful d4d"><span class="sr-only">ç¡è³æ</span></td>
    <td headers="day4 rainful d4n"><span class="sr-only">ç¡è³æ</span></td>
    <td headers="day5 rainful d5d"><span class="sr-only">ç¡è³æ</span></td>
    <td headers="day5 rainful d5n"><span class="sr-only">ç¡è³æ</span></td>
    <td headers="day6 rainful d6d"><span class="sr-only">ç¡è³æ</span></td>
    <td headers="day6 rainful d6n"><span class="sr-only">ç¡è³æ</span></td>
    <td headers="day7 rainful d7d"><span class="sr-only">ç¡è³æ</span></td>
    <td headers="day7 rainful d7n"><span class="sr-only">ç¡è³æ</span></td>
</tr>
'''
