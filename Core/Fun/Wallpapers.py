# Import modules

from ctypes import windll


# Sets a photo on the desktop wallpaper

def SetWallpapers(Photo, Directory):
 windll.user32.SystemParametersInfoW(20, 0, Directory + Photo.file_path, 0)