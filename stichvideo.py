from moviepy.editor import VideoFileClip, concatenate_videoclips
import os

# Set the path to the folder containing the video files
video_folder = "file location"

# Get a list of all the video file names in the folder
video_files = sorted([f for f in os.listdir(videofolder) if f.endswith('.mp4')], key=lambda x: (int(x.split('')[0]) if x.split('_')[0].isdigit() else float('inf'), x))

# Create a list of video clips from the video files
video_clips = []
for file in video_files:
    file_path = os.path.join(video_folder, file)
    video_clip = VideoFileClip(file_path)
    video_clips.append(video_clip)

# Concatenate the video clips into a single video file
final_clip = concatenate_videoclips(video_clips, method='compose')

# Set the output file name and path
output_file = os.path.join(video_folder, "merged_video.mp4")

# Write the final video file to disk
final_clip.write_videofile(output_file)