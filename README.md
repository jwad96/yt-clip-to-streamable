# yt-clip-to-streamable
Transfer YouTube video snippets to streamable

## Description
Takes YouTube video link + time range and generates streamable link for that clip.

## How to use
1) Substitute {your email} and {your password} for your streamable email and password
2) Run yt-clip-to-streamable.py
3) Enter YouTube URL when prompted
4) Enter start time (in seconds or HH:MM:SS). Default is start of video
5) Enter end time in similar format. Default is end of video
6) After running, streamable link will be printed

### Dependencies
* Python 3.6+
* requests
* streamable account
* ffmpeg
* youtube-dl
