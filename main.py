import os.path
import shutil

source_files = [
    "avcodec-lav-59.dll",
    "avfilter-lav-8.dll",
    "avformat-lav-59.dll",
    "avutil-lav-57.dll",
    "LAVAudio.ax",
    "LAVSplitter.ax",
    "LAVVideo.ax",
    "libbluray.dll",
    "swresample-lav-4.dll",
    "swscale-lav-6.dll",
    "IntelQuickSyncDecoder.dll",
]

source_dir = "bin_Win32"
dst_dir = "Artifacts"


def copy_artifacts():
    if not os.path.exists(source_dir):
        print("Source dir ", os.path.abspath(source_dir), " not exists")
        return

    for file_name in source_files:
        full_path = os.path.abspath(os.path.join(source_dir, file_name))
        if os.path.exists(full_path):
            dst_full_path = os.path.abspath(os.path.join(dst_dir, file_name))
            dst_dir_full_path = os.path.dirname(dst_full_path)
            if not os.path.exists(dst_dir_full_path):
                print("Make dir ", dst_dir_full_path, "\n")
                os.mkdir(dst_dir_full_path)

            print("Copy file from ", full_path, " to ", dst_full_path, "\n")
            shutil.copy2(full_path, dst_full_path)

        else:
            print("Source file ", full_path, " not exists")


if __name__ == '__main__':
    copy_artifacts()
    if os.name == "nt":
        os.system("pause")
