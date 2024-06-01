from webscout import play_audio

def play_audio_message(message, voice="Brian"):
    audio_content = play_audio(message, voice=voice)

    # Save the audio to a file
    with open("output.mp3", "wb") as f:
        f.write(audio_content)

if __name__ == "__main__":
    message = "This is an example of text-to-speech."
    play_audio_message(message)
