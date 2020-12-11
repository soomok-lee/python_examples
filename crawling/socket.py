'''
NETWORK PROGRAMMING
서로 다른 원격지의 컴퓨터끼리 일련의 데이터를 주고 받을 수 있느 기능이 포함된 프로그램을 만드는 것

PROTOCOL
원거리의 컴퓨터 혹은 통신장비 사이에 메세지를 주고 받는 양식 혹은 규칙을 말합니다.
컴퓨터(통신기기)끼리 무언가를 주고 받기 위한 약속
EX) HTTP, HTTPS, FTP, SMTP, WIFI(IEEE 802.XXX...), BLUETOOTH ETC..

HTTP(S) 통신
CLIENT -> SERVER REQUEST
CLIENT <- SERVER RESPONSE

SESSION - 정보가 서버에 저장됨
COOKIE - 정보가 내 컴퓨터에 저장됨
'''
# SOCKET 통신
import socket 

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

google_ip = socket.gethostbyname("google.com") # DNS(domain-ip) - ip
sock.connect((google_ip, 80))

sock.send("GET / HTTP/1.1\n".encode()) # binary 
sock.send("\n".encode())

buffer = sock.recv(4096) # receive 4096 byte
# decode the byte data and replace carriage return with python. 
buffer = buffer.decode().replace("\r\n", "\n") 
sock.close()

print(buffer)

'''
HTTP/1.1 200 OK
Date: Fri, 11 Dec 2020 20:22:46 GMT
Expires: -1
Cache-Control: private, max-age=0
Content-Type: text/html; charset=ISO-8859-1
P3P: CP="This is not a P3P policy! See g.co/p3phelp for more info." 
Server: gws
X-XSS-Protection: 0
X-Frame-Options: SAMEORIGIN
Set-Cookie: 1P_JAR=2020-12-11-20; expires=Sun, 10-Jan-2021 20:22:46 
GMT; path=/; domain=.google.com; Secure
Set-Cookie: NID=204=LxBcGqm-87yYX3OCi056Po0_l5_nS_eOvWjZ9ihGHuWBhBb_NLMTf0YiQXM_LJM5deRoPBgi9JV8jLg2kMizaYkr-rSNQAM4YTOxAul4xjB-sxyBn6u8Sn0JsuajKzAQHKxyWAL7r7yZme9MPOjROZ6noUtbzWApt0y8n61OeRs; expires=Sat, 12-Jun-2021 20:22:46 GMT; path=/; domain=.google.com; HttpOnly    
Accept-Ranges: none
Vary: Accept-Encoding
Transfer-Encoding: chunked

4957
<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="en"><head><meta content="Search the world's information, including webpages, images, videos and more. Google has many special features to help you find exactly what you're looking for." name="description"><meta content="noodp" name="robots"><meta content="text/html; charset=UTF-8" http-equiv="Content-Type"><meta content="/logos/doodles/2020/december-holidays-days-2-30-6753651837108830.3-law.gif" 
itemprop="image"><meta content="December Holidays" property="twitter:title"><meta content="December Holidays 2020 #GoogleDoodle" property="twitter:description"><meta content="December Holidays 2020 #GoogleDoodle" property="og:description"><meta content="summary_large_image" property="twitter:card"><meta content="@GoogleDoodles" property="twitter:site"><meta content="https://www.google.com/logos/doodles/2020/december-holidays-days-2-30-6753651837108830.3-2xa.gif" property="twitter:image"><meta content="https://www.google.com/logos/doodles/2020/december-holidays-days-2-30-6753651837108830.3-2xa.gif" property="og:image"><meta content="1100" property="og:image:width"><meta content="440" property="og:image:height"><meta content="https://www.google.com/logos/doodles/2020/december-holidays-days-2-30-6753651837108830.3-2xa.gif" property="og:url"><meta content="video.other" property="og:type"><title>Google</title><script nonce="6YVU4Eitsn0JfWqX/zmtNA==">(function(){window.google={kEI:'FtXTX_-dN-XY9AP_pJC4Dg',kEXPI:'0,1359409,730,224,5104,207,2415,789,10,1144,82,364,1499,817,383,246,5,1184,170,4414,3,65,454,315,217,272,992,860,1567,1612,7,858,939,2195,1112996,1233,1196465,585,7,328977,13677,4855,32691,16115,28684,9188,8384,4859,1361,9290,3030,4738,12841,4020,978,7931,5297,2054,920,873,4192,6430,1142,6290,7095,4518,2777,919,2277,8,2796,889,704,1279,2213,529,149,1943,519,1464,56,4258,109,203,1135,1,3,2063,606,2023,1777,143,377,1947,2209,113,328,1284,2943,2246,3600,605,2622,2845,7,4808,791,6755,4455,641,7877,4928,108,1456,27,1924,908,2,941,2614,2398,1385,8927,432,3,1546,44,1,820,1,4624,148,5990,4055,3930,4,1528,2304,1236,271,874,405,1459,401,2393,74,463,42,1212,266,2163,17,447,459,1555,4067,1036,1315,3,3280,1426,374,2110,1714,603,1,693,1753,2658,239,4003,519,912,564,213,468,8,431,30,1303,2551,138,2884,211,874,116,52,3285,1076,2064,1,470,908,638,37,630,827,130,475,2,568,1,1,386,2672,1032,319,990,758,613,55,744,213,3625,776,2,69,1131,789,28,11,687,44,64,601,324,13,1357,451,1768,2,772,1122,1336,756,55,353,48,308,171,12,548,594,112,2,1148,58,545,233,4,84,256,19,17,19,241,113,1020,1728,6,523,385,3,163,39,387,2,3,2,2,715,214,1341,673,1,806,116,27,566,488,397,1009,647,17,877,102,238,59,232,345,91,488,92,2,400,704,149,800,439,3,580,3,114,498,4,2,7,143,147,288,226,347,358,360,2,5,2,8,603,180,1286,459,1,282,569,261,68,513,151,246,39,419,242,272,23,245,831,742,91,712,724,938,578,128,18,252,1424,680,5718250,3775,95,35,5996794,2801217,549,333,444,1,2,80,1,900,897,2,7,2,2551,1,748,141,59,736,563,1,4265,1,1,2,1017,9,305,3299,248,595,1,2232,131,6,16,2,3,13,3,5,14,2,5,1,23957827,2735261,32898',kBL:'ZWEf'};google.sn='webhp';google.kHL='en';})();(function(){
google.lc=[];google.li=0;google.getEI=function(a){for(var b;a&&(!a.getAttribute||!(b=a.getAttribute("eid")));)a=a.parentNode;return b||google.kEI};google.getLEI=function(a){for(var b=null;a&&(!a.getAttribute
'''