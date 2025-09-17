"""
whisper_engine.py
-----------------
Handles transcription using OpenAI Whisper.
"""

import whisper
import numpy as np

class WhisperEngine:
    def __init__(self, model_size="small"):
        """
        Args:
            model_size: str - Whisper model size ('tiny', 'base', 'small', 'medium', 'large')
        """
        print(f"Loading Whisper model: {model_size}")
        self.model = whisper.load_model(model_size)

    def transcribe_chunk(self, audio_chunk: bytes, rate: int = 16000):
        """
        Transcribes a raw audio chunk.
        Args:
            audio_chunk: bytes of PCM16 audio
            rate: sampling rate
        Returns:
            dict: transcription result
        """
       
