import re
from youtube_transcript_api import YouTubeTranscriptApi


def extract_video_id(youtube_url: str) -> str:
    """
    Extract the video ID from a given YouTube URL.
    Supports various URL formats.
    """
    # Common YouTube URL formats
    patterns = [
        r"(?:https?://)?(?:www\.)?youtube\.com/watch\?v=([\w-]{11})",
        r"(?:https?://)?(?:www\.)?youtu\.be/([\w-]{11})",
        r"(?:https?://)?(?:www\.)?youtube\.com/embed/([\w-]{11})"
    ]
    for pattern in patterns:
        match = re.match(pattern, youtube_url)
        if match:
            return match.group(1)
    # If not matched, try to find v= in query string
    match = re.search(r"v=([\w-]{11})", youtube_url)
    if match:
        return match.group(1)
    raise ValueError("Invalid YouTube URL or unable to extract video ID.")


def get_youtube_transcript(youtube_url: str, languages=None) -> str:
    """
    Given a YouTube URL, return the full transcript as a single text string.
    Optionally specify a list of languages to prefer.
    """
    video_id = extract_video_id(youtube_url)
    try:
        ytt_api = YouTubeTranscriptApi()
        fetched_transcript = ytt_api.fetch(video_id)
        transcript_data = fetched_transcript.to_raw_data()
    except Exception as e:
        raise RuntimeError(f"Failed to retrieve transcript: {e}")
    full_text = " ".join([entry['text'] for entry in transcript_data])
    return full_text


if __name__ == "__main__":
    # Example usage
    url = input("Enter YouTube video URL: ")
    try:
        transcript = get_youtube_transcript(url)
        print("\nTranscript:\n")
        print(transcript)
    except Exception as e:
        print(f"Error: {e}")
