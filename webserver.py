from flask import Flask, render_template, Response
from camera import Camera
from picamera2 import Picamera2
from picamera2.encoders import JpegEncoder
from picamera2.outputs import FileOutput
import io
import time

buffer = io.BytesIO()
output = FileOutput(buffer)

def capture():
	with Picamera2() as cam:
		time.sleep(2)
		cam.configure(cam.create_video_configuration())
		time.sleep(2)
		cam.start_recording(JpegEncoder(), output)
		time.sleep(2)
		while True:
			buffer.seek(0)
			yield buffer.read()
			buffer.seek(0)
			buffer.truncate()

app = Flask(__name__)

def gen():
	while True:
		frame = next(capture())
		yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
	return render_template('PortalPage.html')


@app.route('/live')
def live():
	return render_template('live.html')


@app.route('/live_feed')
def live_feed():
	return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')



if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=8000, threaded=True)

