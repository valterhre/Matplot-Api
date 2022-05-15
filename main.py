from Import import *

class Weather:

    def __init__(self):
        self.API=f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={KEY}"

    def api(self):
        weather=requests.get(self.API).json()
        #print(round((weather['current']['temp']-273.15), 1))
        #print(weather['current']['weather'][0]['main'])
        n=0
        temper=[]
        while n<47:
            n=n+1
            temper.append(round((weather['hourly'][n]['temp']-273.15), 1))
        return temper

    def graph(self):
        temper=self.api()
        y=[]
        for item in range(0, 47):
            y.append(item)
        plt.plot(y, temper)
        print(max(temper))
        plt.show()

if __name__ == "__main__":
    import requests
    import matplotlib.pyplot as plt
    d=Weather()
    d.api()
    d.graph()