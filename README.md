
# 🎙️ Real-Time Subtitle Generation using Whisper

This project enables **real-time subtitle generation** from audio using [OpenAI Whisper](https://github.com/openai/whisper).  
It extends Whisper’s raw transcription capabilities with **LLM-powered context-aware enhancements**, making subtitles more accurate, readable, and user-friendly.

---

## 🚀 Features

- **Real-Time Transcription**  
  - Capture live audio streams (system audio or microphone).  
  - Generate subtitles on the fly using Whisper.  

- **Context-Aware Subtitle Enhancement (via LLM)**  
  - Fix grammar & punctuation in real time.  
  - Expand shorthand or acronyms (e.g., `FYI` → `For your information`).  
  - Insert speaker tags (if diarization is added in the pipeline).  

- **Streaming Support**  
  - Chunk-based processing for **low latency transcription**.  
  - Smooth subtitle rendering for videos or conferencing apps.  

- **Future Extensions**  
  - **Translation:** Real-time subtitle translation into other languages.  
  - **Summarization:** Generate concise meeting notes alongside subtitles.  
  - **Searchable Transcripts:** Store transcripts in a vector DB for retrieval.  

---

## 🧠 How It Works

The pipeline can be summarized as:

1. **Audio Capture** → Microphone/System audio recorded in small chunks.  
2. **Preprocessing** → Convert audio to **log-Mel spectrogram**.  
   <img src="https://github.com/user-attachments/assets/244b7491-9c10-4b4e-a4f5-c2200b985c66" alt="log-mel spectrogram" width="500"/>
3. **Whisper Model** → Transcribes spectrogram into raw text (tokens).  
   <img src="https://github.com/user-attachments/assets/e5e91d14-309c-44c0-914e-7e3c98dfffb6" alt="whisper model" width="500"/>
4. **LLM Enhancement** → Fix grammar, add punctuation, expand acronyms, tag speakers.  
   - [[insert diagram here: LLM diagram for punctuation correction]]  
5. **Subtitle Renderer** → Output subtitles in `.srt`, `.vtt`, or overlay in real time.  

<img width="768" height="120" alt="llm_punctuation_correction_diagram" src="https://github.com/user-attachments/assets/86c47b55-9bfb-43b0-9719-8fcd4d26adb4" />

---

## 🛠️ Tech Stack

- **Core Model**: [Whisper](https://github.com/openai/whisper)  
- **Enhancement Layer**: LLMs (OpenAI GPT, LLaMA, Mistral, etc.)  
- **Audio Handling**: PyAudio / FFmpeg 
- **UI/Output**:  
  - CLI for live subtitles  
  - Web dashboard for streaming subtitles  
  - Export as `.srt` / `.vtt` files  

---

## 📂 Project Structure

```
real-time-subtitles/
├── README.md
├── src/
│   ├── audio_capture.py       # Capture audio in real time
│   ├── whisper_engine.py      # Whisper transcription logic
│   ├── llm_enhancer.py        # Context-aware subtitle enhancement
│   ├── subtitle_renderer.py   # Real-time subtitle display/export
│   └── utils/                 # Helper functions
├── requirements.txt
└── examples/
    └── demo.mp4
```

---

## ⚡ Quick Start

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/real-time-subtitles.git
   cd real-time-subtitles
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run real-time transcription**
   ```bash
   python src/main.py --source mic
   ```

---

## 📊 Example Output

**Raw Whisper Output:**  
```
hey guys welcome back this is part 2 fyi we are covering transformers today
```

**LLM-Enhanced Subtitle:**  
```
[Speaker 1]: Hey guys, welcome back!  
This is part two. For your information, today we are covering Transformers.
```

---


## 📖 References

- [Whisper Paper](https://arxiv.org/abs/2212.04356)  
- [OpenAI Whisper GitHub](https://github.com/openai/whisper)  
- [WebRTC for Audio Streaming](https://webrtc.org/)  

---
