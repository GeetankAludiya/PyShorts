# PyShorts 🎬

**PyShorts** is an automated Python-based pipeline that converts long-form videos into engaging **YouTube Shorts**.

The project analyzes a video, transcribes its audio using **Whisper**, identifies potential short-form clips, generates vertical videos with subtitles, performs quality checks, creates AI-generated metadata, and can automatically upload the finished Shorts to YouTube.

---

## 🚀 What PyShorts Does

PyShorts is designed to automate the repetitive parts of creating YouTube Shorts from long videos.

### Pipeline

```text
HD Video
   │
   ▼
Audio Extraction / Transcription
   │
   ▼
Whisper Transcript + Timestamps
   │
   ▼
Candidate Clip Detection
   │
   ▼
Duplicate Protection
   │
   ▼
Vertical Video Generation
   │
   ▼
Subtitle Generation
   │
   ▼
Quality Assurance
   │
   ▼
AI Metadata Generation
   │
   ▼
YouTube Upload
```

The goal is to turn one long video into multiple ready-to-publish Shorts with minimal manual work.

---

# ✨ Features

* 🎥 Process locally downloaded HD videos
* 🎙️ Automatic speech-to-text transcription
* ⏱️ Sentence-level timestamps
* ✂️ Automatic candidate clip detection
* 🔁 Duplicate clip protection
* 📱 Automatic 9:16 vertical video generation
* 📝 Automatic subtitles/captions
* 🔍 Quality assurance before publishing
* 🤖 AI-generated titles and descriptions
* #️⃣ Automatic hashtag generation
* ▶️ YouTube upload automation
* 💾 Local intermediate files for debugging and verification

---

# 🏗️ How It Works

## 1. Input Video

The workflow starts with a high-quality video downloaded manually.

The project intentionally works with locally available video files instead of relying on automatic YouTube downloading.

Example:

```text
input/
└── video.mp4
```

This gives the user control over the source video's quality and avoids problems caused by changing YouTube download requirements.

---

# 2. Transcription

The video audio is transcribed using the **Whisper** speech-recognition model.

Whisper converts spoken audio into text while providing timestamps.

Example:

```json
{
    "start": 12.4,
    "end": 18.7,
    "text": "This is an example sentence from the video."
}
```

These timestamps are extremely important because the later stages use them to determine exactly where clips should begin and end.

The transcription stage produces a file similar to:

```text
output/transcript.json
```

---

# 3. Candidate Clip Detection

The transcript is analyzed to identify sections that could work as YouTube Shorts.

The system looks for meaningful sections of the conversation rather than simply cutting the video at fixed intervals.

A candidate clip contains information such as:

```json
{
    "start": 25.0,
    "end": 55.0,
    "transcript": "Example clip transcript..."
}
```

Candidate clips are stored in:

```text
output/candidate_clips.json
```

This creates a separation between **clip discovery** and **video generation**.

---

# 4. Duplicate Protection

PyShorts includes duplicate protection so that the same section of the source video is not repeatedly converted into Shorts.

Before generating a clip, the system checks existing candidate/final clip information.

This is important when the pipeline is executed multiple times on the same project.

Instead of producing:

```text
short_01.mp4
short_02.mp4
short_03.mp4
short_04.mp4
```

with several versions of the same section, the system attempts to keep each selected segment unique.

---

# 5. Vertical Video Generation

YouTube Shorts use a vertical format.

PyShorts converts the original landscape video into a **9:16 vertical composition** suitable for mobile viewing.

The processing stage handles:

* Video cropping
* Aspect-ratio conversion
* Clip trimming
* Audio preservation
* Vertical framing

Generated vertical videos are stored under:

```text
output/vertical/
```

---

# 6. Subtitle Generation

The transcript timestamps are used to create subtitles for the generated Shorts.

Instead of manually typing captions, the system automatically places the spoken words on the video.

This makes the Shorts easier to understand when viewers watch without sound and provides the fast-paced caption style commonly used in short-form content.

---

# 7. Quality Assurance

Before a Short reaches the publishing stage, PyShorts performs a QA check.

The purpose of QA is to prevent broken or incomplete videos from being uploaded automatically.

The pipeline verifies that generated videos meet the expected requirements before allowing them to continue.

Conceptually:

```text
Generated Short
      │
      ▼
    QA Check
      │
 ┌────┴────┐
 │         │
PASS      FAIL
 │         │
 ▼         ▼
Metadata   Stop
Generation
```

Only QA-approved videos continue to the metadata and upload stages.

---

# 8. AI Metadata Generation

Once a video passes QA, PyShorts generates publishing metadata.

The metadata can include:

* Title
* Description
* Hashtags
* Short-form keywords

For example:

```text
Title:
Are local lockdowns the new learning process?

Hashtags:
#shorts #publichealth #lockdown #statistics
```

The generated metadata is associated with the corresponding Short.

This eliminates the need to manually create a title and hashtags for every video.

---

# 9. YouTube Upload

The final stage is the YouTube uploader.

PyShorts identifies the completed videos and uploads them through the **YouTube Data API**.

The uploader can use the generated:

* Video file
* Title
* Description
* Hashtags
* Publishing settings

The final workflow therefore becomes:

```text
Video
  ↓
Transcription
  ↓
Clip Detection
  ↓
Duplicate Protection
  ↓
Vertical Conversion
  ↓
Subtitles
  ↓
QA
  ↓
Metadata
  ↓
YouTube
```

---

# 📁 Project Structure

A simplified project structure looks like this:

```text
PyShorts/
│
├── main.py
├── clip_generator.py
├── generate_metadata.py
├── youtube_uploader.py
│
├── requirements.txt
├── README.md
├── .gitignore
│
├── input/
│
├── output/
│   ├── transcript.json
│   ├── candidate_clips.json
│   │
│   ├── vertical/
│   │
│   ├── clips/
│   │
│   ├── final/
│   │
│   └── metadata/
│
└── venv/
```

> The exact files and directories may change as the project evolves.

---

# 🧩 Main Components

## `main.py`

Acts as the main entry point for the video-processing workflow.

It coordinates the different stages of the pipeline.

---

## `clip_generator.py`

Responsible for generating the actual video clips from the selected timestamps.

It takes candidate clips and converts them into video files.

---

## `generate_metadata.py`

Handles metadata generation for QA-approved videos.

It generates information such as:

* Titles
* Hashtags
* Descriptions

---

## `youtube_uploader.py`

Handles the final YouTube publishing stage.

It finds the completed Shorts and uploads them using the YouTube API.

---

# 🛠️ Technologies Used

PyShorts is built primarily with Python.

### Core technologies

* **Python** — Main programming language
* **Whisper** — Speech-to-text transcription
* **FFmpeg** — Video/audio processing
* **MoviePy / video-processing libraries** — Video manipulation
* **YouTube Data API** — Automated YouTube uploads
* **JSON** — Intermediate pipeline data storage

Additional libraries may be added as the project develops.

---

# ⚙️ Installation

Clone the repository:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd PyShorts
```

Create a virtual environment:

### Windows

```powershell
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

Make sure **FFmpeg** is installed and available in your system PATH.

---

# 🔐 Configuration

Some parts of PyShorts require API credentials.

Sensitive information should **never be committed to GitHub**.

For example:

```text
.env
credentials.json
token.json
```

should be excluded using `.gitignore`.

Example:

```text
.env
credentials.json
token.json
venv/
__pycache__/
output/
*.mp4
*.wav
```

---

# ▶️ Running the Pipeline

Place your source video in the appropriate input location.

Then run the pipeline from the project directory.

For example:

```powershell
python main.py
```

After processing, review the generated files inside:

```text
output/
```

Once the videos pass QA, metadata can be generated:

```powershell
python generate_metadata.py
```

Finally, run the uploader:

```powershell
python youtube_uploader.py
```

---

# 🔄 Complete Workflow Example

Suppose you have a 60-minute interview.

PyShorts processes it like this:

```text
60-minute interview
        │
        ▼
    Whisper
        │
        ▼
  Full transcript
        │
        ▼
Interesting sections
        │
        ├── Clip 1
        ├── Clip 2
        ├── Clip 3
        └── Clip 4
        │
        ▼
   9:16 conversion
        │
        ▼
    Subtitles
        │
        ▼
       QA
        │
        ▼
AI-generated metadata
        │
        ▼
YouTube Shorts
```

One long-form video can therefore become multiple short-form pieces of content.

---

# 🎯 Project Goal

The main goal of PyShorts is to create a **repeatable, local-first content automation pipeline**.

Instead of manually performing:

1. Finding interesting moments
2. Checking timestamps
3. Cutting videos
4. Converting them to vertical format
5. Adding subtitles
6. Creating titles
7. Creating hashtags
8. Uploading each Short

PyShorts automates these steps into a single workflow.

---

# 🧠 Design Philosophy

PyShorts follows a modular architecture.

Each stage produces an output that can be inspected before the next stage begins.

For example:

```text
Transcript
    ↓
candidate_clips.json
    ↓
Video Clips
    ↓
QA
    ↓
Metadata
    ↓
YouTube
```

This approach makes the system easier to:

* Debug
* Modify
* Test
* Extend
* Recover from failures

If one stage fails, the entire pipeline does not necessarily need to start from the beginning.

---

# 🚧 Current Status

PyShorts is an actively developed project.

Current pipeline capabilities include:

* [x] Local HD video input
* [x] Speech transcription
* [x] Timestamp-based clip generation
* [x] Duplicate protection
* [x] Vertical video generation
* [x] Subtitle generation
* [x] QA validation
* [x] AI metadata generation
* [x] YouTube upload automation

Future improvements may include:

* Better clip-quality scoring
* More advanced AI highlight detection
* Face/person tracking for vertical cropping
* Automatic thumbnail generation
* Multi-platform publishing
* Analytics feedback loops
* Automatic retry and recovery
* Improved subtitle styling
* Content performance-based clip selection

---

# ⚠️ Important Notes

PyShorts is intended for videos that you have the right to process and publish.

You are responsible for ensuring that the source content complies with copyright, platform policies, and applicable laws.

API credentials and private configuration files should never be committed to the repository.

---

# 👨‍💻 Project

**PyShorts**
AI-powered long-form video → YouTube Shorts automation pipeline.

Built with Python 🐍

---

## ⭐ If You Find This Project Useful

Give the repository a ⭐ on GitHub and follow the project as it evolves.

```text
Long Video
     ↓
   PyShorts
     ↓
Multiple YouTube Shorts
```
