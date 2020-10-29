from flask import Flask,render_template,request
import pickle
import numpy as np

#Load pickel file
filename = 'bike_rental.pickle'
rfc = pickle.load(open(filename, 'rb'))



app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/predict',methods=['POST'])
def predict():

    if request.method == 'POST':

        # season = int(request.form['season'])

        season=request.form['season']

        if (season== 'springe'):
            season = 1
        elif (season== 'summer'):
            season = 2
        elif (season == 'fall'):
            season = 3
        else:
            season = 4

        # weather = int(request.form['weather'])

        weather=request.form['weather']

        if (weather== 'clear'):
            weather = 1
        elif (weather== 'Cloudy'):
            weather = 2
        elif (weather == 'Light_rain'):
            weather = 3
        else:
            weather = 4


        temp = float(request.form['temp'])

        humidity = int(request.form['humidity'])
        windspeed = float(request.form['windspeed'])

        casual = int(request.form['casual'])
        registered = int(request.form['registered'])

        hour = int(request.form['hour'])
        if hour < 0 or hour >23:
            return render_template('index.html', prediction_test='Enter Hour In Between 0-23')

        data = np.array([[season,weather,temp,humidity,windspeed,casual,registered,hour]])


        my_prediction = rfc.predict(data)[0].astype(int)

        return render_template('index.html',prediction = my_prediction)

if __name__ == '__main__':
	app.run(debug=True)