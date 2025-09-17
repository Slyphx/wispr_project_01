"""
subtitle_renderer.py
--------------------
Renders subtitles in real-time (console, file, or overlay).
"""

import time

class SubtitleRenderer:
    def __init__(self, mode="console", output_file="subtitles.srt"):
        self.mode = mode
        self.output_file = output_file
        self.counter = 1

    def render(self, text, start_time=None, end_time=None):
        """
        Render subtitles.
        Args:
            text: str - Subtitle text
            start_time: float - Start timestamp
            end_time: float - End timestamp
        """
        if self.mode == "console":
            print(f"📝 {text}")
        elif self.mode == "srt":
            self._write_srt(text, start_time, end_time)

    def _write_srt(self, text, start_time, end_time):
        """Append a subtitle line to .srt file."""
        with open(self.output_file, "a", encoding="utf-8") as f:
            f.write(f"{self.counter}\n")
            f.write(f"{self._format_time(start_time)} --> {self._format_time(end_time)}\n")
            f.write(f"{text}\n\n")
        self.counter += 1

    @staticmethod
    def _format_time(seconds):
        """Convert seconds → SRT time format."""
        t = time.gmtime(seconds)
        ms = int((seconds - int(seconds)) * 1000)
        return time.strftime(f"%H:%M:%S,{ms:03d}", t)


if __name__ == "__main__":
    renderer = SubtitleRenderer(mode="srt")
    renderer.render("Hello world!", start_time=0.0, end_time=2.5)
    print("Subtitle written to file.")
