from tkinter import *
from PIL import ImageTk,Image
import webbrowser
import json
import requests
from datetime import datetime
from tkinter import messagebox
import webbrowser
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

win1=Tk()
win1.title("Weather Detection and Prediction")
win1.geometry("700x700")
win1.resizable(0,0)


p1=PhotoImage(file='icon.png')
win1.iconphoto(False,p1)
#-----------------------------------
#My API KEY
api_key = "2252e2375863d326aa4450fa11e4b888"

#--------------------------------------------------------------------------------------------------------------------------

def main_window():
    global win2
    win2=Toplevel(win1)
    win2.title("Weather Results")
    win2.geometry("1200x700")
    win2.resizable(0,0)
    win2.config(background="#383838")
    #--------------------------------------------------------------------------------------------------------------------------------------------
    # API FOR * HR FORECAST
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    
    #API for 8-hr forecast

    url_city=data["name"]
    url1 = "http://api.openweathermap.org/data/2.5/forecast?q=%s&appid=%s" %( url_city, api_key)
    response1 = requests.get(url1)
    data1 = json.loads(response1.text)
    # print(data1)

    url2 = "http://api.openweathermap.org/data/2.5/uvi?appid=%s&lat=%s&lon=%s" %(api_key,data['coord']['lat'],data['coord']['lon'])
    response2 = requests.get(url2)
    data2 = json.loads(response2.text)


    url3 = "http://api.openweathermap.org/data/2.5/forecast?q=%s&appid=%s" % (url_city,api_key)
    response3 = requests.get(url3)
    data3 = json.loads(response3.text)

    #-------------------------------------------------------------------------------------------------------------------------------------------------------

    #Icon Functions

    def iconfun(mn,dc):
        global filename1
        if(mn=="Clear"):
            filename1 = PhotoImage(file = "cleansky.png")
        elif(mn=="Clouds"):
            if(dc=="few clouds"):
                filename1 = PhotoImage(file = "fewclouds.png")
            elif(dc=="scattered clouds"):
                filename1 = PhotoImage(file = "scatteredclouds.png")
            elif(dc=="broken clouds"):
                filename1 = PhotoImage(file = "brokenclouds.png")
            else:
                filename1 = PhotoImage(file = "cleansky.png")
        elif(mn=="Snow"):
            if(dc=="light snow"):
                filename1 = PhotoImage(file = "lightsnow.png")
            elif(dc=="Heavy Snow"):
                passfilename1 = PhotoImage(file = "snow.png")
            else:
                filename1 = PhotoImage(file = "cleansky.png")
        elif(mn=="Thunderstorm"):
            if(dc=="thunderstorm with rain"):
                filename1 = PhotoImage(file = "thunderstorm.png")
            else:
                filename1 = PhotoImage(file = "thunderstorm.png")
        elif(mn=="Rain"):
            if(dc=="light rain"):
                filename1 = PhotoImage(file = "lightrain.png")
            elif(dc=="very heavy rain"):
                filename1 = PhotoImage(file = "heavytrain.png")
            else:
                filename1 = PhotoImage(file = "lightrain.png")
        elif(mn=="Drizzle"):
            filename1 = PhotoImage(file = "drizzle.png")
        elif(mn=="Mist"):
            filename1 = PhotoImage(file = "mist.png")
        elif(mn=="Smoke"):
            filename1 = PhotoImage(file = "smoke.png")
        elif(mn=="Haze"):
            filename1 = PhotoImage(file = "haze.png")
        elif(mn=="Dust"):
            filename1 = PhotoImage(file = "dust.png")
        elif(mn=="Fog"):
            filename1 = PhotoImage(file = "fog.png")
        elif(mn=="Tornado"):
            filename1 = PhotoImage(file = "tornado.png")
        else:
            filename1 = PhotoImage(file = "cleansky.png")




    def degToCompass(num):
        val=int((num/22.5)+.5)
        arr=["N","NNE","NE","ENE","E","ESE", "SE", "SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"]
        return arr[(val % 16)]

    def gotolink():
        webbrowser.open('https://www.google.com/maps/place/' + city_name.get()) 

    def download_json():
        with open("data_file.json", "w") as write_file:
            json.dump(data1, write_file)


    #------------------------------------------------------------------------------------------------------------------------------------------------------
    f_min=[]
    f_max=[]
    list_min=[]
    list_max=[]

    def the_list(a,b):
        for i in range(a,b):
            list_min.append(round(data3["list"][i]["main"]["temp_min"]-273.15,2))
            list_max.append(round(data3["list"][i]["main"]["temp_max"]-273.15,2))

        list_min.sort()
        list_max.sort()

        f_min.append(list_min[0])
        f_max.append(list_max[len(list_max)-1])

    the_list(0,8)
    the_list(8,16)
    the_list(16,24)
    the_list(24,32)
    the_list(32,40)

    # print(f_min)
    # print(f_max)

    x = ["Day1","Day2","Day3","Day4","Day5"]

    figure = Figure(figsize=(5, 4), dpi=100)
    plt = figure.add_subplot(1, 1, 1)
    figure.set_facecolor("#C2C2C2")


    plt.plot(x, f_min,label='Minimum Temperature', color='Blue', linestyle='dashed', linewidth = 2, 
            marker='o', markerfacecolor='Red', markersize=12)

    plt.plot(x, f_max,label='Maximum Temperature', color='Green', linestyle='dashed', linewidth = 2, 
            marker='o', markerfacecolor='Red', markersize=12)
    plt.grid(color='grey') 
    # plt.set_xlabel('DATES') 
    plt.set_ylabel('TEMPERATURE') 
    plt.set_title(url_city)
    # plt.set_background("#AEAEAE")
    plt.patch.set_facecolor('xkcd:light grey')
    # plt.title.set_color('red')

    canvas = FigureCanvasTkAgg(figure, win2)
    canvas.get_tk_widget().place(x=30,y=330,height=320,width=500)



    #-----------------------------------------------------------------------------------------------------------------------------------------
    #Variables
    win2_ans_city=StringVar()
    win2_ans_climate=StringVar()
    win2_ans_temp=StringVar()

    win2_tom_d=StringVar()
    win2_tom_m=StringVar()

    win2_day2_d=StringVar()
    win2_day2_m=StringVar()

    win2_day3_d=StringVar()
    win2_day3_m=StringVar()

    win2_day4_d=StringVar()
    win2_day4_m=StringVar()

    win2_day5_d=StringVar()
    win2_day5_m=StringVar()

    win2_tom_temp=StringVar()
    win2_day2_temp=StringVar()
    win2_day3_temp=StringVar()
    win2_day4_temp=StringVar()
    win2_day5_temp=StringVar()

    win2_tom_date=StringVar()
    win2_day2_date=StringVar()
    win2_day3_date=StringVar()
    win2_day4_date=StringVar()
    win2_day5_date=StringVar()

    win2_currentdate=StringVar()
    win2_currenttime=StringVar()

    win2_current_main=StringVar()
    win2_current_description=StringVar()
    win2_current_uv=StringVar()
    win2_current_visiblity=StringVar()
    win2_current_pressure=StringVar()
    win2_current_humidity=StringVar()
    win2_current_wind=StringVar()

    sunrise_time=StringVar()
    sunset_time=StringVar()

    rain_data=StringVar()

    #-----------------------------------------------------------------------------------------------------

    #----------------------------------------------------------------------------------------------------
    #LABELS

    l1=Label(win2,textvariable=win2_ans_city,relief="ridge",justify=CENTER,borderwidth="1",padx=5,background="#AEAEAE",font=("Ariel","24","bold"))
    l1.place(x=30,y=40,height=40,width=250)
    l16=Label(win2,textvariable=win2_currentdate,relief="ridge",justify=CENTER,borderwidth="1",padx=5,background="#AEAEAE",font=("Ariel","10","bold"))
    l16.place(x=30,y=80,height=20,width=250)
    l2=Label(win2,textvariable=win2_ans_temp,justify=RIGHT,anchor=E,borderwidth="1",padx=5,relief="ridge",background="#AEAEAE",font=("Ariel","26","bold"))
    l2.place(x=280,y=40,height=60,width=250)
    # l3=Label(win2,text="Map",relief="ridge",font=("Ariel","20","bold"))
    # l3.place(x=550,y=50,height=250,width=600)

    l6=Label(win2,text="5 Day Forecast",background="#AEAEAE",borderwidth=4,justify=CENTER,padx=5,font=("Open Sans","20","bold"))
    l6.place(x=550,y=330,height=50,width=600)

    l7=Label(win2,relief="ridge",anchor=NW,justify=LEFT,background="#C2C2C2",padx=5,font=("Ariel","10","bold"))
    l7.place(x=550,y=382,height=52,width=600)
    l71=Label(win2,textvariable=win2_tom_date,anchor=NW,background="#C2C2C2",justify=LEFT,padx=5,font=("Ariel","10","bold"))
    l71.place(x=550,y=382,height=52,width=150)
    l72=Label(win2,text="Tommorrow",anchor=NW,justify=LEFT,background="#C2C2C2",padx=5,font=("Ariel","10","bold"))
    l72.place(x=700,y=382,height=52,width=150)
    l73=Label(win2,textvariable=win2_tom_temp,anchor=NW,background="#C2C2C2",justify=LEFT,padx=5,font=("Ariel","10","bold"))
    l73.place(x=850,y=382,height=52,width=150)
    l74=Label(win2,textvariable=win2_tom_d,anchor=NW,background="#C2C2C2",justify=LEFT,padx=5,font=("Ariel","10","bold"))
    l74.place(x=1000,y=382,height=26,width=150)
    l75=Label(win2,textvariable=win2_tom_m,anchor=NW,background="#C2C2C2",justify=LEFT,padx=5,font=("Ariel","10","bold"))
    l75.place(x=1000,y=408,height=26,width=150)

    l8=Label(win2,relief="ridge",anchor=NW,justify=LEFT,background="#C2C2C2",padx=5,font=("Ariel","10","bold"))
    l8.place(x=550,y=436,height=52,width=600)
    l81=Label(win2,textvariable=win2_day2_date,anchor=NW,background="#C2C2C2",justify=LEFT,padx=5,font=("Ariel","10","bold"))
    l81.place(x=550,y=436,height=52,width=150)
    l82=Label(win2,text="Day 2",anchor=NW,justify=LEFT,background="#C2C2C2",padx=5,font=("Ariel","10","bold"))
    l82.place(x=700,y=436,height=52,width=150)
    l83=Label(win2,textvariable=win2_day2_temp,anchor=NW,background="#C2C2C2",justify=LEFT,padx=5,font=("Ariel","10","bold"))
    l83.place(x=850,y=436,height=52,width=150)
    l84=Label(win2,textvariable=win2_day2_d,anchor=NW,background="#C2C2C2",justify=LEFT,padx=5,font=("Ariel","10","bold"))
    l84.place(x=1000,y=436,height=26,width=150)
    l85=Label(win2,textvariable=win2_day2_m,anchor=NW,background="#C2C2C2",justify=LEFT,padx=5,font=("Ariel","10","bold"))
    l85.place(x=1000,y=462,height=26,width=150)

    l9=Label(win2,relief="ridge",anchor=NW,justify=LEFT,background="#C2C2C2",padx=5,font=("Ariel","10","bold"))
    l9.place(x=550,y=490,height=52,width=600)
    l91=Label(win2,textvariable=win2_day3_date,anchor=NW,background="#C2C2C2",justify=LEFT,padx=5,font=("Ariel","10","bold"))
    l91.place(x=550,y=490,height=52,width=150)
    l92=Label(win2,text="Day 3",anchor=NW,justify=LEFT,background="#C2C2C2",padx=5,font=("Ariel","10","bold"))
    l92.place(x=700,y=490,height=52,width=150)
    l93=Label(win2,textvariable=win2_day3_temp,anchor=NW,background="#C2C2C2",justify=LEFT,padx=5,font=("Ariel","10","bold"))
    l93.place(x=850,y=490,height=52,width=150)
    l94=Label(win2,textvariable=win2_day3_m,anchor=NW,background="#C2C2C2",justify=LEFT,padx=5,font=("Ariel","10","bold"))
    l94.place(x=1000,y=490,height=26,width=150)
    l95=Label(win2,textvariable=win2_day3_m,anchor=NW,background="#C2C2C2",justify=LEFT,padx=5,font=("Ariel","10","bold"))
    l95.place(x=1000,y=516,height=26,width=150)

    l10=Label(win2,relief="ridge",anchor=NW,justify=LEFT,background="#C2C2C2",padx=5,font=("Ariel","10","bold"))
    l10.place(x=550,y=544,height=52,width=600)
    l101=Label(win2,textvariable=win2_day4_date,anchor=NW,background="#C2C2C2",justify=LEFT,padx=5,font=("Ariel","10","bold"))
    l101.place(x=550,y=544,height=52,width=150)
    l102=Label(win2,text="Day 4",anchor=NW,justify=LEFT,background="#C2C2C2",padx=5,font=("Ariel","10","bold"))
    l102.place(x=700,y=544,height=52,width=150)
    l103=Label(win2,textvariable=win2_day4_temp,anchor=NW,background="#C2C2C2",justify=LEFT,padx=5,font=("Ariel","10","bold"))
    l103.place(x=850,y=544,height=52,width=150)
    l104=Label(win2,textvariable=win2_day4_m,anchor=NW,background="#C2C2C2",justify=LEFT,padx=5,font=("Ariel","10","bold"))
    l104.place(x=1000,y=544,height=26,width=150)
    l105=Label(win2,textvariable=win2_day4_m,anchor=NW,background="#C2C2C2",justify=LEFT,padx=5,font=("Ariel","10","bold"))
    l105.place(x=1000,y=570,height=26,width=150)

    l11=Label(win2,relief="ridge",anchor=NW,justify=LEFT,background="#C2C2C2",padx=5,font=("Ariel","10","bold"))
    l11.place(x=550,y=598,height=52,width=600)
    l111=Label(win2,textvariable=win2_day5_date,anchor=NW,background="#C2C2C2",justify=LEFT,padx=5,font=("Ariel","10","bold"))
    l111.place(x=550,y=598,height=52,width=150)
    l112=Label(win2,text="Day 5",anchor=NW,justify=LEFT,padx=5,background="#C2C2C2",font=("Ariel","10","bold"))
    l112.place(x=700,y=598,height=52,width=150)
    l113=Label(win2,textvariable=win2_day5_temp,anchor=NW,background="#C2C2C2",justify=LEFT,padx=5,font=("Ariel","10","bold"))
    l113.place(x=850,y=598,height=52,width=150)
    l114=Label(win2,textvariable=win2_day5_m,anchor=NW,background="#C2C2C2",justify=LEFT,padx=5,font=("Ariel","10","bold"))
    l114.place(x=1000,y=598,height=26,width=150)
    l115=Label(win2,textvariable=win2_day5_m,anchor=NW,background="#C2C2C2",justify=LEFT,padx=5,font=("Ariel","10","bold"))
    l115.place(x=1000,y=624,height=26,width=150)

    # ll4=Label(win2,text="5-Days graph",anchor=W,justify=LEFT,padx=5,border="0",relief="ridge",font=("Ariel","20","bold"))
    # ll4.place(x=52,y=332,height=50,width=400)


    sl1=Label(win2,textvariable=win2_current_main,justify=CENTER,borderwidth="1",background="#AEAEAE",padx=5,relief="ridge",font=("Ariel","14","bold"))
    sl1.place(x=30,y=120,height=50,width=250)
    ssl1=Label(win2,textvariable=win2_current_description,anchor=E,borderwidth="1",padx=5,background="#AEAEAE",relief="ridge",font=("Ariel","14","bold"))
    ssl1.place(x=280,y=120,height=50,width=250)





    sal2=Label(win2,textvariable=win2_current_wind,justify=CENTER,borderwidth="1",padx=5,background="#AEAEAE",relief="ridge",font=("Ariel","13","bold"))
    sal2.place(x=30,y=173,height=50,width=500)
    sbl2=Label(win2,textvariable=win2_current_pressure,anchor=E,borderwidth="1",padx=5,background="#AEAEAE",relief="ridge",font=("Ariel","13","bold"))
    sbl2.place(x=30,y=223,height=50,width=250)
    scl2=Label(win2,textvariable=win2_current_humidity,anchor=E,borderwidth="1",padx=5,background="#AEAEAE",relief="ridge",font=("Ariel","13","bold"))
    scl2.place(x=280,y=223,height=50,width=250)


    sal3=Label(win2,textvariable=win2_current_uv,anchor=E,borderwidth="1",padx=5,background="#AEAEAE",relief="ridge",font=("Ariel","13","bold"))
    sal3.place(x=30,y=273,height=40,width=250)
    sbl3=Label(win2,textvariable=win2_current_visiblity,anchor=E,borderwidth="1",background="#AEAEAE",padx=5,relief="ridge",font=("Ariel","13","bold"))
    sbl3.place(x=280,y=273,height=40,width=250)

    #---------------------------------------------------------------------------------------------------------------------------------------------
    #ICON LABELS
    
    ans_tom_m=data1["list"][0]["weather"][0]['main']
    ans_tom_d=data1["list"][0]["weather"][0]['description']
    ans_tom_d=ans_tom_d.capitalize()


    C1 = Canvas(win2, bg="blue", height=130, width=160)
    iconfun(ans_tom_m,ans_tom_d)
    icon1 = Label(win2, image=filename1,border=1)
    icon1.place(x=550, y=40)

    
    sun_rise_label=Label(win2,textvariable=sunrise_time,borderwidth="1",padx=5,anchor=E,background="#AEAEAE",relief="ridge",font=("Ariel","22","bold"))
    sun_rise_label.place(x=720,y=40,height=65,width=450)
    sun_set_label=Label(win2,textvariable=sunset_time,borderwidth="1",padx=5,anchor=E,background="#AEAEAE",relief="ridge",font=("Ariel","22","bold"))
    sun_set_label.place(x=720,y=105,height=65,width=450)


    rain_icon1=Label(win2,background="#383838").place(x=40,y=130,height=30,width=30)
    rain_icon2=Label(win2,background="#383838").place(x=290,y=130,height=30,width=30)

    
    sunrise_time.set("Sunrise on : "+"     "+(datetime.fromtimestamp(int(data["sys"]["sunrise"])).strftime('%H:%M:%S')))
    sunset_time.set("Sunset on : "+"     "+(datetime.fromtimestamp(int(data["sys"]["sunset"])).strftime('%H:%M:%S')))


    link_button=Button(win2,text="Find the Place \n on Map",background="#C2C2C2",borderwidth=2,command=gotolink,font=("Ariel","16","bold")).place(x=550,y=200,height=112,width=300)

    download_button=Button(win2,text="Download Detailed Data \n as JSON File",background="#C2C2C2",command=download_json,borderwidth=2,font=("Ariel","16","bold")).place(x=870,y=200,height=112,width=300)

    csunrise = Canvas(win2, bg="blue", height=61, width=78)
    filename3 = PhotoImage(file = "sunrise.png")
    iconsunrise = Label(win2, image=filename3,border=0)
    iconsunrise.place(x=720, y=42)

    csunset = Canvas(win2, bg="blue", height=63, width=78)
    filename4 = PhotoImage(file = "sunset.png")
    iconsunset = Label(win2, image=filename4,border=0)
    iconsunset.place(x=720, y=106)

    cpressure = Canvas(win2, bg="blue", height=50, width=50)
    filename5 = PhotoImage(file = "pressure.png")
    iconpre = Label(win2, image=filename5,border=0)
    iconpre.place(x=32, y=225)

    chumidity = Canvas(win2, bg="blue", height=43, width=52)
    filename6 = PhotoImage(file = "humidity.png")
    iconhum = Label(win2, image=filename6,border=0)
    iconhum.place(x=283, y=227)

    cvisiblity=Canvas(win2, bg="blue", height=38, width=42)
    filename7 = PhotoImage(file = "visiblity.png")
    iconvis = Label(win2, image=filename7,border=0)
    iconvis.place(x=285, y=274)

    cuv=Canvas(win2, bg="blue", height=38, width=42)
    filename8= PhotoImage(file = "uv.png")
    iconuv = Label(win2, image=filename8,border=0)
    iconuv.place(x=38, y=274)

    ctemp=Canvas(win2, bg="blue", height=60, width=32)
    filename9= PhotoImage(file = "temp.png")
    icontemp = Label(win2, image=filename9,border=0)
    icontemp.place(x=285, y=41)

    cwind=Canvas(win2, bg="blue", height=48, width=77)
    filename10= PhotoImage(file = "wind.png")
    iconwind = Label(win2, image=filename10,border=0)
    iconwind.place(x=31, y=174)

    cloc=Canvas(win2, bg="blue", height=28, width=24)
    filename11= PhotoImage(file = "location.png")
    iconloc = Label(win2, image=filename11,border=0)
    iconloc.place(x=35, y=45)



    #----------------------------------------------------------------------------------------------------------------------------------
    #SETTING THE VALUES

    win2_currentdate.set(dt_string)
    win2_current_uv.set("UV :"+str(data2['value']))
    win2_current_visiblity.set("Visibility : "+str(data['visibility'])+"km")

    win2_current_pressure.set("Pressure : "+str(data['main']['pressure'])+" hPa")
    win2_current_humidity.set("Humidity : "+str(data['main']['humidity'])+" %")
    win2_current_wind.set("    Wind Speed : "+str(data['wind']['speed'])+" m/s       Direction :   "+str(degToCompass(data['wind']['deg'])))
    #-------------------------------------------------------------------------------------
    
    var_min=0
    var_max=0
    win2_temperature_min=[]
    win2_temperature_max=[]
    for i in range(0,8):
        win2_temperature_min.append(data1["list"][i]["main"]["temp_min"])
        win2_temperature_max.append(data1["list"][i]["main"]["temp_max"])
        win2_temperature_min.sort()
        win2_temperature_max.sort()
        var_min=win2_temperature_min[0]
        var_max=win2_temperature_max[len(win2_temperature_max)-1]

    
    win2_tom_t=str(round(var_min-273.15,2))+" °C / "+str(round(var_max-273.15,2))+" °C"
    win2_tom_temp.set(win2_tom_t)
    

    var_min=0
    var_max=0
    win2_temperature_min=[]
    win2_temperature_max=[]
    for i in range(8,16): 
        win2_temperature_min.append(data1["list"][i]["main"]["temp_min"])
        win2_temperature_max.append(data1["list"][i]["main"]["temp_max"])
        win2_temperature_min.sort()
        win2_temperature_max.sort()
        var_min=win2_temperature_min[0]
        var_max=win2_temperature_max[len(win2_temperature_max)-1]

    
    win2_tom_t=str(round(var_min-273.15,2))+" °C / "+str(round(var_max-273.15,2))+" °C"
    win2_day2_temp.set(win2_tom_t)

    var_min=0
    var_max=0
    win2_temperature_min=[]
    win2_temperature_max=[]
    for i in range(16,24): 
        win2_temperature_min.append(data1["list"][i]["main"]["temp_min"])
        win2_temperature_max.append(data1["list"][i]["main"]["temp_max"])
        win2_temperature_min.sort()
        win2_temperature_max.sort()
        var_min=win2_temperature_min[0]
        var_max=win2_temperature_max[len(win2_temperature_max)-1]

    
    win2_tom_t=str(round(var_min-273.15,2))+" °C / "+str(round(var_max-273.15,2))+" °C"
    win2_day3_temp.set(win2_tom_t)

    var_min=0
    var_max=0
    win2_temperature_min=[]
    win2_temperature_max=[]
    for i in range(24,32): 
        win2_temperature_min.append(data1["list"][i]["main"]["temp_min"])
        win2_temperature_max.append(data1["list"][i]["main"]["temp_max"])
        win2_temperature_min.sort()
        win2_temperature_max.sort()
        var_min=win2_temperature_min[0]
        var_max=win2_temperature_max[len(win2_temperature_max)-1]

    
    win2_tom_t=str(round(var_min-273.15,2))+" °C / "+str(round(var_max-273.15,2))+" °C"
    win2_day4_temp.set(win2_tom_t)
    
    var_min=0
    var_max=0
    win2_temperature_min=[]
    win2_temperature_max=[]
    for i in range(32,40): 
        win2_temperature_min.append(data1["list"][i]["main"]["temp_min"])
        win2_temperature_max.append(data1["list"][i]["main"]["temp_max"])
        win2_temperature_min.sort()
        win2_temperature_max.sort()
        var_min=win2_temperature_min[0]
        var_max=win2_temperature_max[len(win2_temperature_max)-1]

    
    win2_tom_t=str(round(var_min-273.15,2))+" °C / "+str(round(var_max-273.15,2))+" °C"
    win2_day5_temp.set(win2_tom_t)
    





    alphabet=data1["list"][1]["dt_txt"]
    date_time = alphabet.split(" ",1)
    win2_tom_date.set(date_time[0])
    alphabet=data1["list"][11]["dt_txt"]
    date_time = alphabet.split(" ",1)
    win2_day2_date.set(date_time[0])
    alphabet=data1["list"][17]["dt_txt"]
    date_time = alphabet.split(" ",1)
    win2_day3_date.set(date_time[0])
    alphabet=data1["list"][26]["dt_txt"]
    date_time = alphabet.split(" ",1)
    win2_day4_date.set(date_time[0])
    alphabet=data1["list"][37]["dt_txt"]
    date_time = alphabet.split(" ",1)
    win2_day5_date.set(date_time[0])    





    
    #-----------------------------------------------------
    ans_city=data["name"]
    ans_climate=data["weather"][0]["description"]
    ans_temp=data["main"]["temp"]

    # ans_tom_m=
    

    win2_current_main.set(ans_tom_m)
    win2_current_description.set(ans_tom_d)
    # print(ans_tom_m,ans_tom_d)



    ans_day2_m=data1["list"][4]["weather"][0]['main']
    ans_day2_d=data1["list"][4]["weather"][0]['main']

    ans_day3_m=data1["list"][12]["weather"][0]['main']
    ans_day3_d=data1["list"][12]["weather"][0]['main']

    ans_day4_m=data1["list"][28]["weather"][0]['main']
    ans_day4_d=data1["list"][28]["weather"][0]['main']

    ans_day5_m=data1["list"][34]["weather"][0]['main']
    ans_day5_d=data1["list"][34]["weather"][0]['main']


    # print(ans_tom_d,ans_tom_m)
    #-----------------------------------------------------
    
    win2_ans_city.set(ans_city)
    # win2_ans_climate.set(ans_climate)
    win2_ans_temp.set(str(round(ans_temp-273.15,2))+ " °C")
    #-----------------------------------------------------

    win2_tom_m.set(ans_tom_m)
    win2_tom_d.set(ans_tom_d)

    win2_day2_m.set(ans_day2_m)
    win2_day2_d.set(ans_day2_d)

    win2_day3_m.set(ans_day3_m)
    win2_day3_d.set(ans_day3_d)

    win2_day4_m.set(ans_day4_m)
    win2_day4_d.set(ans_day4_d)

    win2_day5_m.set(ans_day5_m)
    win2_day5_d.set(ans_day5_d)





    #--------------------------------------------------------------------------------------------------------------------------------





    win2.mainloop()

























#-----------------------------------
#MAIN FUNCTIONS

def city_name_search():
    global data
    url = "http://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s" % (city_name.get(), api_key)
    response = requests.get(url)
    data = json.loads(response.text)
    main_window()

def city_geographic_search():
    global data
    url = "http://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&appid=%s" % (coordinates[0],coordinates[1], api_key)
    response = requests.get(url)
    data = json.loads(response.text)
    main_window()

def city_id_search():
    global data
    url = "http://api.openweathermap.org/data/2.5/weather?id=%s&appid=%s" % (city_name.get(), api_key)
    response = requests.get(url)
    data = json.loads(response.text)
    main_window()


def city_zipcode_search():
    global data
    url = "http://api.openweathermap.org/data/2.5/weather?zip=%s,%s&appid=%s" % (zipcode_var[0],zipcode_var[1], api_key)
    response = requests.get(url)
    data = json.loads(response.text)
    main_window()
    
#-----------------------------------
#Clear Place Holder

def clear(event):
    entrycityname.delete(0,END)

def callback(url):
    webbrowser.open_new(url)
#------------------------------------------------------------------------------------------------------------------------------------------------------------
def search():
    if(number_verify==1):
        try:
            city_name_search()
        except(KeyError):
            win2.destroy()
            messagebox.showerror("Error !!","Please enter a Valid City Name")

    elif(number_verify==2):
        global coordinates
        try:
            coordinates=city_name.get().split(",")
            city_geographic_search()
        except(KeyError):
            win2.destroy()
            messagebox.showerror("Error !!","Please enter a Valid Latitude and Longitude Name")
    elif(number_verify==3):
        global zipcode_var
        try:
            zipcode_var=city_name.get().split(",")
            city_zipcode_search()
        except (KeyError):
            win2.destroy()
            messagebox.showerror("Error !!","Please enter a Valid Country Code and Zip Code")

    elif(number_verify==4):
        try:
            city_id_search()
        except(KeyError):
            win2.destroy()
            messagebox.showerror("Error !!","Please enter a Valid City ID")

#------------------------------------------------------------------------------------------------------------------------------------------------------------
#Main Screen Jugad

number_verify=1

def reset1():
    b2['background']='#000000'
    b2['borderwidth']=0
    b2['fg']="#E7E6E6"

def reset2():
    b3['background']='#000000'
    b3['borderwidth']=0
    b3['fg']="#E7E6E6"
    link1.destroy()

def reset3():
    b4['background']='#000000'
    b4['borderwidth']=0
    b4['fg']="#E7E6E6"

def reset4():
    b5['background']='#000000'
    b5['borderwidth']=0
    b5['fg']="#E7E6E6"
#------------------------------------------------------------------------------------------------------------------------------------------------------------

def togglecolor1():
    global number_verify
    if(b2['background']=='#000000'):
        b2['background']='#A0BCC6'
        b2['borderwidth']=1
        b2['fg']="black"
        entrycityname.delete(0,END)
        entrycityname.insert(0,"Enter City name")
        reset2()
        reset3()
        reset4()
        number_verify=1
        # print(number_verify)
    elif(b2['background']=='#A0BCC6'):
        reset1()
        number_verify=0
def togglecolor2():
    if(b3['background']=='#000000'):
        global number_verify
        b3['background']='#A0BCC6'
        b3['borderwidth']=1
        b3['fg']="black"
        entrycityname.delete(0,END)
        entrycityname.insert(0,"Enter Latitude, Longitude")
        #--------------
        #HyperLink
        global link1
        link1 = Label(win1, text="Find Your Coordinates", background="#000000",fg="blue", cursor="hand2")
        link1.place(x=175,y=610,height=20,width=175)
        link1.bind("<Button-1>", lambda e: callback("https://www.latlong.net/"))

        #--------------

        reset1()
        reset3()
        reset4()
        number_verify=2
        # print(number_verify)
    elif(b3['background']=='#A0BCC6'):
        reset2()
        number_verify=0
def togglecolor3():
    if(b4['background']=='#000000'):
        global number_verify
        b4['background']='#A0BCC6'
        b4['borderwidth']=1
        b4['fg']="black"
        entrycityname.delete(0,END)
        entrycityname.insert(0,"Enter Country Code, Zipcode")
        reset1()
        reset2()
        reset4()
        number_verify=3
    elif(b4['background']=='#A0BCC6'):
        reset3()
        number_verify=0
def togglecolor4():
    if(b5['background']=='#000000'):
        global number_verify
        b5['background']='#A0BCC6'
        b5['borderwidth']=1
        b5['fg']="black"
        entrycityname.delete(0,END)
        entrycityname.insert(0,"Enter City ID")
        reset1()
        reset2()
        reset3()
        number_verify=4
    elif(b5['background']=='#A0BCC6'):
        reset4()
        number_verify=0
#------------------------------------------------------------------------------------------------------------------------------------------------------------
city_name=StringVar()


C = Canvas(win1, bg="blue", height=250, width=300)
filename = PhotoImage(file = "mont.png")
background_label = Label(win1, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

entrycityname=Entry(win1,textvariable=city_name,background="#314952",fg="#A0BCC6",justify="center",font=("Ariel","18","bold"))
entrycityname.insert(0,"Enter City name")
entrycityname.place(x=180,y=350,height=50,width=320)
entrycityname.bind("<Button-1>",clear)
b1=Button(win1,text="Search",background="#A0BCC6",borderwidth=2,command=search,activebackground="#314952",font=("Ariel","16","bold"))
b1.place(x=300,y=410,height=40,width=100)


b2=Button(win1,text="By City Name",background="#A0BCC6",fg="black",borderwidth=1,activebackground="#A0BCC6",command=togglecolor1,font=("Ariel","13","bold"))
b2.place(x=0,y=630,height=70,width=175)
b3=Button(win1,text="By Geographic \n Co-ordinates",background="#000000",fg="#E7E6E6",borderwidth=0,command=togglecolor2,activebackground="#A0BCC6",font=("Ariel","13","bold"))
b3.place(x=175,y=630,height=70,width=175)
b4=Button(win1,text="By Zip Code",background="#000000",borderwidth=0,fg="#E7E6E6",activebackground="#A0BCC6",command=togglecolor3,font=("Ariel","13","bold"))
b4.place(x=350,y=630,height=70,width=175)
b5=Button(win1,text="By City ID",background="#000000",borderwidth=0,fg="#E7E6E6",activebackground="#A0BCC6",command=togglecolor4,font=("Ariel","13","bold"))
b5.place(x=525,y=630,height=70,width=175)

win1.mainloop()