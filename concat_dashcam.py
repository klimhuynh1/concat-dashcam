import os
import re
import subprocess


# TODO: Parameterise code to allow user to input directories and file names
def get_file_names(videos_dir_path):
    # list to store file names
    filenames = []

    for file_path in os.listdir(videos_dir_path):
        # check if current file_path is a file
        if os.path.isfile(os.path.join(videos_dir_path, file_path)):
            # add filename to list
            filenames.append(file_path)

    return filenames


def separate_filenames(filenames):
    # Separate filenames into front and rear
    front_files = [name for name in filenames if re.search(r"F\.MP4", name)]
    rear_files = [name for name in filenames if re.search(r"R\.MP4", name)]

    return front_files, rear_files


def create_input_text_file(front_files, rear_files):
    # Create a text file containing relative path of all front view dashcam footage
    with open("front_input.txt", "w") as file:
        for filename in front_files:
            file.write("file concat/" + filename + "\n")
        file.close()

    # Create a text file containing relative path of all rear view dashcam footage
    with open("rear_input.txt", "w") as file:
        for filename in rear_files:
            file.write("file concat/" + filename + "\n")
        file.close()


def concatenate_videos(input_file, output_file):
    # Build the ffmpeg command
    ffmpeg_cmd = ["ffmpeg", "-f", "concat", "-i", input_file, "-c", "copy", output_file]

    try:
        # Run the ffmpeg command using shell=True
        subprocess.run(" ".join(ffmpeg_cmd), check=True, shell=True)
        print(f"Concatenation complete. Output file: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error during concatenation: {e}")


def main():
    current_dir_path = os.getcwd()
    videos_dir_path = os.path.join(current_dir_path, "concat")
    filesnames = get_file_names(videos_dir_path)
    front_files, rear_files = separate_filenames(filesnames)
    create_input_text_file(front_files, rear_files)
    concatenate_videos("front_input.txt", "concat_front.mp4")
    concatenate_videos("rear_input.txt", "concat_rear.mp4")


if __name__ == "__main__":
    main()
