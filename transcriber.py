import whisper


def transcribe_audio(audio_path):
    print("Loading Whisper model...")

    model = whisper.load_model("base")

    print("Transcribing audio...")

    result = model.transcribe(
        audio_path,
        fp16=False
    )

    return result


if __name__ == "__main__":
    audio_path = "audio.wav"

    result = transcribe_audio(audio_path)

    print("\n--- TRANSCRIPTION ---\n")
    print(result["text"])

    print("\n--- SEGMENTS ---\n")

    for segment in result["segments"]:
        start = segment["start"]
        end = segment["end"]
        text = segment["text"].strip()

        print(f"{start:.2f} → {end:.2f} | {text}")