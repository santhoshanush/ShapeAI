import requests as r
cityname=str(input("enter city"))
APIkey="599090b6a96a9deb6a13f694b1744e78"
re=r.get("https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(cityname,APIkey))
res=re.json()
print(res)

temperature=res['main']['temp'] 
pressure=res['main']['pressure']
humidity=res['main']['humidity']
degree=res['wind']['deg']
sunrise=res['sys']['sunrise']
sunset=res['sys']['sunset']

print("""
                WEATHER FORCASTING

    CITY:{}


temperature={} 
pressure={}
humidity={}
degree={}
sunrise={}
sunset={}


""".format(cityname,temperature,pressure,humidity,degree,sunrise,sunset))
weathr=open("weathr.txt","w")
weathr.write("""
                WEATHER FORCASTING

    CITY:{}


temperature={} 
pressure={}
humidity={}
degree={}
sunrise={}
sunset={}


""".format(cityname,temperature,pressure,humidity,degree,sunrise,sunset))

