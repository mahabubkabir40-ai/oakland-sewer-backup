import glob
import os
import shutil

import generate_site


def build():
    generate_site.main()

    dest = "public"

    if os.path.exists(dest):
        shutil.rmtree(dest)
    os.makedirs(dest)

    dirs_to_copy = ["css", "images", "fonts"]
    for d in dirs_to_copy:
        if os.path.exists(d):
            shutil.copytree(d, os.path.join(dest, d))
            print(f"Copied directory: {d}")

    file_patterns = ["*.html", "*.png", "*.ico", "sitemap.xml", "robots.txt", "_headers"]
    for pattern in file_patterns:
        for filepath in glob.glob(pattern):
            if os.path.isfile(filepath):
                shutil.copy2(filepath, os.path.join(dest, os.path.basename(filepath)))
                print(f"Copied file: {filepath}")


if __name__ == "__main__":
    build()
    print("Build completed successfully!")
