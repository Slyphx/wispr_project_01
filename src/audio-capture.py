"""
audio_capture.py
----------------
Captures live audio (microphone/system) in chunks and streams it to the pipeline.
"""

import pyaudio
import queue
import threading

class AudioCapture:
    def __init__(self, rate=16000, chunk_size=1024, channels=1):
        self.rate = rate
        self.chunk_size = chunk_size
        self.channels = channels
        self.audio_queue = queue.Queue()
        self._stop_event = threading.Event()

        self.p = pyaudio.PyAudio()
        self.stream = None

    def start_stream(self):
        """Start microphone stream."""
        self.stream = self.p.open(
            format=pyaudio.paInt16,
            channels=self.channels,
            rate=self.rate,
            input=True,
            frames_per_buffer=self.chunk_size,
            stream_callback=self._callback
        )
        self.stream.start_stream()

    def _callback(self, in_data, frame_count, time_info, status):
        """Callback that pushes audio chunks into queue."""
        self.audio_queue.put(in_data)
        return (in_data, pyaudio.paContinue)

    def read_chunk(self):
        """Get next audio chunk from queue (blocking)."""
        return self.audio_queue.get()

    def stop_stream(self):
        """Stop audio capture."""
        self._stop_event.set()
        if self.stream:
            self.stream.stop_stream()
            self.stream.close()
        self.p.terminate()


if __name__ == "__main__":
    cap = AudioCapture()
    cap.start_stream()
    print("🎤 Recording... Press Ctrl+C to stop")
    try:
