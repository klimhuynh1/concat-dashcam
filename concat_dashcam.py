import os
import re
import subprocess

def get_file_names(dir_path):
    # list to store file names
    filenames = []

    for file_path in os.listdir(dir_path):
        # check if current file_path is a file
        if os.path.isfile(os.path.join(dir_path, file_path)):
            # add filename to list
            filenames.append(file_path)
    return filenames
    

def separate_filenames(filenames):
    # Separate filenames into F and R
    front_files = [name for name in filenames if re.search(r'F\.MP4', name)]
    rear_files = [name for name in filenames if re.search(r'R\.MP4', name)]
    print(front_files)
    print(rear_files)
    return front_files, rear_files

def create_input_text_file(front_files, rear_files):
    with open("front_input.txt", 'w') as file:
        for filename in front_files:
            file.write("file concat/" + filename + "\n")
        file.close()

    with open("rear_input.txt", 'w') as file:
        for filename in rear_files:
            file.write("file concat/" + filename + "\n")
        file.close()


def concatenate_front_videos():
    # Build the ffmpeg command
    ffmpeg_cmd = [
        'ffmpeg',
        '-f', 'concat',
        '-i', 'front_input.txt',
        '-c', 'copy',
        'concat_front.mp4'
    ]

    try:
        # Run the ffmpeg command using shell=True
        subprocess.run(' '.join(ffmpeg_cmd), check=True, shell=True)
        print(f"Concatenation complete. Output file: concat_front.mp4")
    except subprocess.CalledProcessError as e:
        print(f"Error during concatenation: {e}")

def concatenate_rear_videos():
    # Build the ffmpeg command
    ffmpeg_cmd = [
        'ffmpeg',
        '-f', 'concat',
        '-i', 'rear_input.txt',
        '-c', 'copy',
        'concat_rear.mp4'
    ]

    try:
        # Run the ffmpeg command using shell=True
        subprocess.run(' '.join(ffmpeg_cmd), check=True, shell=True)
        print(f"Concatenation complete. Output file: concat_rear.mp4")
    except subprocess.CalledProcessError as e:
        print(f"Error during concatenation: {e}")


def main():
    current_dir_path = os.getcwd()
    dir_path =  os.path.join(current_dir_path,"concat")
    concatenate_front_videos()
    concatenate_rear_videos()

if __name__ == "__main__":
    main()