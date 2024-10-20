import yt_dlp
import os

# Define the video URLs and save directory
video_urls = [
    "https://youtu.be/P1Ii87mgyJ0?si=vMSZDIzB9tUBrFAB"
]
save_dir = "C:\\Users\\Mdanm\\Downloads\\Python Practise\\Youtube_Videos"
ffmpeg_path = "C:\\Users\\Mdanm\\Documents\\ffmpeg-2024-10-17-git-e1d1ba4cbc-essentials_build\\ffmpeg-2024-10-17-git-e1d1ba4cbc-essentials_build\\bin"  # Path to FFmpeg folder

def download_video_or_audio(url, save_path, output_format):
    if output_format.lower() in ['mp3', 'wav']:
        # Download as audio
        ydl_opts_audio = {
            'format': 'bestaudio/best',
            'outtmpl': f'{save_path}/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': output_format.lower(),  # Convert to MP3 or WAV
            }],
            'ffmpeg_location': ffmpeg_path,  # Specify your FFmpeg path
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts_audio) as ydl:
                ydl.download([url])
                print(f"Downloaded audio as {output_format.upper()} with yt-dlp.")
        except Exception as e:
            print(f"An error occurred while downloading audio: {e}")

    elif output_format.lower() == 'video':
        # Download as video (MP4)
        ydl_opts_video = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
            'outtmpl': f'{save_path}/%(title)s.%(ext)s',
            'ffmpeg_location': ffmpeg_path,  # Specify your FFmpeg path
            'merge_output_format': 'mp4',
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts_video) as ydl:
                ydl.download([url])
                print(f"Downloaded video as MP4 with yt-dlp.")
        except Exception as e:
            print(f"An error occurred while downloading video: {e}")
    else:
        print(f"Invalid format specified: {output_format}. Please enter 'mp3', 'wav', or 'video'.")

# Get user input for the desired output format (mp3, wav, or video)
output_type = input("Would you like to download as audio or video? (Enter 'mp3', 'wav', or 'video'): ").lower()

# Example usage
for video in video_urls:
    print("Video URL: ", video)
    download_video_or_audio(video, save_dir, output_type)
