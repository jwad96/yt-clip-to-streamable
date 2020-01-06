from json import loads
import requests
import base64
import os


#returns all files with a given prefix in current directory
def files_that_start_with(prefix):
    files = []
    for filename in os.listdir("."):
        if filename.startswith("converted"):
            files.append(filename)
    return files


# downloads YouTube video at given URL
# output file name is hardcoded as "converted"
def download_video(url):
    os.system(f"youtube-dl -o converted {url}")


# trims video to_trim starting at start_time, ending at end_time
# output file name is hardcoded as "converted2"
def trim_video_between(to_trim, start_time, end_time, extension):
    os.system(f"ffmpeg -i {to_trim} -ss {start_time} -to {end_time} converted2.{extension}")
    return f"converted2.{extension}"


# trims video to_trim starting at start_time until end of video
def trim_video_starting_at(to_trim, start_time, extension):
    os.system(f"ffmpeg -i {to_trim} -ss {start_time} converted2.{extension}")
    return f"converted2.{extension}"


# sends specified video to streamable, printing link to console
def upload(file_name, email, pw):
    file = open(f"{file_name}", "rb")
    url = "https://api.streamable.com/upload"
    credentials = f"{email}:{pw}"
    auth = base64.b64encode(credentials.encode()).decode("utf-8")

    headers = {"Authorization": f"Basic {auth}"}
    files = {"file": file}

    response = requests.post(url, files=files, headers=headers)
    
    print("https://streamable.com/" + loads(response.text)["shortcode"])

    file.close()

def print_message(msg):
    print(f"**********{msg}**********")


if __name__ == "__main__":
    url = input("YouTube URL: ")
    start_time = input("Start time: ")
    end_time = input("End time: ")

    download_video(url)
    print_message("Video downloaded!")
    current_video = files_that_start_with("converted")[0]
    extension = current_video.split('.')[-1]

    if start_time and end_time:
        current_video = trim_video_between(current_video, start_time, end_time, extension)
    elif end_time:
        current_video = trim_video_between(current_video, 0, end_time, extension)
    elif start_time:
        current_video = trim_video_starting_at(current_video, start_time, extension)
    print_message("Trimming complete. Uploading!")
    upload(current_video, "{your email}", "{your password}")
    print_message("All done, cleaning up!")
    for file in files_that_start_with("converted"):
        os.system(f"rm {file}")
