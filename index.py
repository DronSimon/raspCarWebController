from flask import Flask, render_template
#import RPi.GPIO as GPIO

#GPIO.setmode(GPIO.BCM)

#GPIO.setup(20, GPIO.OUT)
#GPIO.setup(21, GPIO.OUT)
#GPIO.setup(23, GPIO.OUT)
#GPIO.setup(24, GPIO.OUT)

app = Flask(__name__, template_folder='', static_folder='', static_url_path='')

@app.route('/')
def index():
	return render_template('index.html')

#@app.route('/fw')
#def fw():
#	GPIO.output(23, True)
#	GPIO.output(24, False)
#        GPIO.output(20, True)
"""        GPIO.output(21, False)
	return ''

@app.route('/bw')
def bw():
        GPIO.output(23, False)
        GPIO.output(24, True)
        GPIO.output(20, False)
        GPIO.output(21, True)
	return '' 

@app.route('/le')
def le():
        GPIO.output(23, False)
        GPIO.output(24, True)
        GPIO.output(20, True)
        GPIO.output(21, False)
        return '' 

@app.route('/ri')
def ri():
        GPIO.output(20, False)
        GPIO.output(21, True)
        GPIO.output(23, True)
        GPIO.output(24, False)
        return '' 
"""
if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
