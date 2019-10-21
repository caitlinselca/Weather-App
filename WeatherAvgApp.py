#Caitlin Selca
#Python Personal Weather Project

# import all functions from the tkinter   
from Tkinter import *
  
# function to find weather details of any city using api key from openweathermap
def get_weather() : 
  
    # import required modules
    # requests module allows us to send http requests using python (returns response object with all the data)
    # json module allows us to store and exchange data
    import requests, json
  
    # enter your api key here; every individual can retain their own api key
    api_key = "API Key will be entered here"
  
    # base_url variable to store url 
    base_url = "https://api.openweathermap.org/data/2.5/weather?q="
  
  
    # take a city name from city_field entry box 
    city_name = city_field.get() 
  
    # complete_url variable to store complete url address 
    complete_url = base_url + city_name + "&appid=" + api_key
  
    # get method of requests module 
    # return response object
    # request to get the data from the url
    response = requests.get(complete_url) 
  
    # json method of response object convert 
    # json format data into python format data
    x = response.json() 
  
    # now x contains list of  nested dictionaries 
    # we know dictionary contains key value pair 
    # check the value of "cod" key is equal to "404" 
    # or not if not that means city is found 
    # otherwise city is not found 
    if x["cod"] != "404" : 
  
        # store the value of "main" key in variable y 
        y = x["main"]
  
        # store the value corresponding to the "temp" key of y 
        current_temperature = y["temp"] 
  
        # store the value corresponding to the "pressure" key of y 
        current_pressure = y["pressure"] 
  
        # store the value corresponding to the "humidity" key of y 
        current_humidiy = y["humidity"] 
  
        # store the value of "weather" key in variable z 
        z = x["weather"] 
  
        # store the value corresponding to the "description" key 
        # at the 0th index of z  
        weather_description = z[0]["description"] 
  
        # insert method inserting the  
        # value in the text entry box.  
        temp_field.insert(15, str(current_temperature) + " Kelvin") 
        atm_field.insert(10, str(current_pressure) + " hPa") 
        humid_field.insert(15, str(current_humidiy) + " %") 
        desc_field.insert(10, str(weather_description) ) 
  
    # if city is not found                    
    else : 
  
        # message dialog box appear which 
        # shows given Error meassgae 
        messagebox.showerror("Error", "City Not Found \n"
                             "Please enter valid city name") 
  
        # clear the content of city_field entry box 
        city_field.delete(0, END) 
  
  
# function that clears the contents of all text entry boxes   
def clear_all() :  
    city_field.delete(0, END)   
    temp_field.delete(0, END) 
    atm_field.delete(0, END) 
    humid_field.delete(0, END) 
    desc_field.delete(0, END) 
  
    # set focus on the city_field entry box  
    city_field.focus_set()  
  
  
# Driver code 
if __name__ == "__main__" : 
  
    # Create a GUI window 
    gui_window = Tk() 
  
    # set the name of tkinter GUI window 
    gui_window.title("Weather GUI Application") 
  
    # set the background color of GUI window  
    gui_window.configure(background = "pink") 
  
    # set the dimensions of GUI window  
    gui_window.geometry("550x300") 
  
    # creates a title label for the Weather App
    title_label = Label(gui_window, text = "Welcome to the Weather App!", 
                      fg = 'white', bg = 'purple') 
      
    # creates city name label
    city_label = Label(gui_window, text = "City name : ", 
                   fg = 'white', bg = 'green') 
      
    # creates temperature label
    temp_label = Label(gui_window, text = "Temperature :", 
                   fg = 'white', bg = 'green') 
  
    # creates pressure label
    pressure_label = Label(gui_window, text = "ATM Pressure :", 
                   fg = 'white', bg = 'green') 
  
    # creates humidity label 
    humidity_label = Label(gui_window, text = "Humidity :", 
                   fg = 'white', bg = 'green') 
  
    # creates description label 
    description_label = Label(gui_window, text = "Description  :", 
                   fg = 'white', bg = 'green') 
      
  
    # places widgets at specific positions in the GUI window  
    title_label.grid(row = 0, column = 1)  
    city_label.grid(row = 1, column = 0, sticky ="E")  
    temp_label.grid(row = 3, column = 0, sticky ="E")  
    pressure_label.grid(row = 4, column = 0, sticky ="E")  
    humidity_label.grid(row = 5, column = 0, sticky ="E")  
    description_label.grid(row = 6, column = 0, sticky ="E") 
  
  
    # Create a text entry box  
    # for filling or typing the information.  
    city_field = Entry(gui_window)  
    temp_field = Entry(gui_window)  
    atm_field = Entry(gui_window)  
    humid_field = Entry(gui_window)  
    desc_field = Entry(gui_window) 
  
    # places widgets at specific positions in the GUI window
    # ipadx keyword argument set width of entry space 
    city_field.grid(row = 1, column = 1, ipadx ="100")  
    temp_field.grid(row = 3, column = 1, ipadx ="100")  
    atm_field.grid(row = 4, column = 1, ipadx ="100")  
    humid_field.grid(row = 5, column = 1, ipadx ="100")  
    desc_field.grid(row = 6, column = 1, ipadx ="100") 
  
    # creates a submit button that has get_weather function attached to it  
    submit_button_ = Button(gui_window, text = "Submit", bg = 'pink',  
                     fg = 'pink', command = get_weather) 
  
    # creates a clear button that has clear_all function attached to it 
    clear_button_ = Button(gui_window, text = "Clear", bg = 'pink',  
                     fg = "white", command = clear_all) 
  
    # places widgets at specific positions in the GUI window
    submit_button_.grid(row = 2, column = 1) 
    clear_button_.grid(row = 7, column = 1) 
      
    # Start the GUI
    gui_window.mainloop() 
