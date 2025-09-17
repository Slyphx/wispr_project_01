from flask import Flask
from threading import Thread
import subprocess
import sounddevice as sd
import soundfile as sf
import os
import time
# import sounddevice as sd
print(sd.query_devices())
print("Default input:", sd.default.device)

model_path="D:\large dev\whisper.cpp\models\ggml-base.en.bin"
app = Flask(__name__)
recording = False
recording_thread = None

def record_audio():
    global recording
    fs = 16000
    filename = "temp.wav"
    with sf.SoundFile(filename, mode='w', samplerate=fs, channels=1) as file:
        def callback(indata, frames, time, status):
            if recording:
                file.write(indata)
            else:
                raise sd.CallbackAbort
        with sd.InputStream(samplerate=fs, channels=1, callback=callback, device=None):  # ensure VB-Cable is selected
            while recording:
                time.sleep(0.1)

@app.route('/start', methods=['POST'])
def start():
    global recording, recording_thread
    recording = True
    recording_thread = Thread(target=record_audio)
    recording_thread.start()
    return 'Recording started'

@app.route("/")
def home():
    return "helloworld!"

@app.route('/stop', methods=['POST'])
def stop():
    global recording, recording_thread
    recording = False

    if recording_thread is not None:
        recording_thread.join()
        recording_thread = None  # Reset after join

    # Run whisper.cpp on recorded file
    result = subprocess.run([
        "whisper-cli.exe", "-m", model_path, "-f", "temp.wav"
    ], capture_output=True, text=True)

    print(result.stdout)  # Optional: show transcription in terminal
    return 'Recording stopped and processed'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
