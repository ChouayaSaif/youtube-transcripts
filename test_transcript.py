import unittest
from youtube_transcript import get_youtube_transcript

class TestYouTubeTranscript(unittest.TestCase):
    def test_transcript_fetch(self):
        url = "https://www.youtube.com/watch?v=Wp7uLKCqqX8&t=6s"
        transcript = get_youtube_transcript(url)
        self.assertIsInstance(transcript, str)
        self.assertGreater(len(transcript), 0)
        # Optionally, check for expected content in the transcript
        self.assertIn("October 7th", transcript)

if __name__ == "__main__":
    unittest.main()
