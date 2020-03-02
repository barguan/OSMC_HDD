#!/usr/bin/env python3

import os, shutil, re

completed = "/path/to/completed"

movies = "/path/to/Movies"

series = "/path/to/Series"

#Move all files over 100mb to Movies folder including subtitle files < 100mb.

def move_by_size():
    try:
        if os.path.getsize(os.path.join(dirpath, f)) > 100000000 or f.endswith(".sub"):
            movies_file_path   =  os.path.join(movies, f)
            source_file_path =  os.path.join(dirpath, f)
            shutil.move(source_file_path, movies_file_path)
            shutil.move(source_file_path, movies_file_path)
    except:
        pass
    
#Move all files from Movies that contain regex for series to Series 
#Rename all series files leaving uniform title, season and episode

def move_series():
    try:
        if re.search(r'[sS][0-9]{2}[eE][0-9]{2}', filename):
            ext = filename[-4:]
            season_regex = re.search(r'[sS][0-9]{2}[eE][0-9]{2}', filename)
            head, sep, tail = filename.partition(season_regex.group(0))
            new_name = str.title(head) + str.upper(sep)
            os.rename(os.path.join(movies ,filename), os.path.join(series, new_name.replace('.', ' ') + ext))
            
    except:
        pass
                 
#Rename all movies to leave title and year   
                        
def movie_name():
    try:
        ext = filename[-4:]
        date_regex = re.search(r'[0-9]{4}', filename)
        head, sep, tail = filename.partition(date_regex.group(0))
        new_name = str.upper(head) + sep
        os.rename(os.path.join(movies ,filename), os.path.join(movies, new_name.replace('.', ' ') + ext))
    except:
        pass
       
#Move all series into season directory if season directory doesnt exist create.

def series_dir():
    if os.path.isdir(os.path.join(series, filename)):
        pass
    else:
        season_regex = re.search(r'[sS][0-9]{2}', filename)
        head, sep, tail = filename.partition(season_regex.group(0))
        seas_dir = str.title(head) + str.upper(sep)
        seas_dir_path = os.path.join(series, seas_dir)
        if os.path.isdir(seas_dir_path):
            shutil.move(os.path.join(series, filename), os.path.join(seas_dir_path, filename))
        else:
            os.mkdir(seas_dir_path)
            shutil.move(os.path.join(series, filename), os.path.join(seas_dir_path, filename))
                
for dirpath, dnames, fnames in os.walk(completed):
    for f in fnames:
        move_by_size()

for filename in os.listdir(movies):
    move_series()
    movie_name()
   
for filename in os.listdir(series):   
    series_dir()
    
#Removes all remaining files in filetree completed. For removing samples/.txt/screenshots.
############WARNING WILL DELETE EVERYTHING IN COMPLETED DIRECTORY############
#Comment out next 2 lines to prevent
shutil.rmtree(completed, ignore_errors=True)
os.mkdir(completed)      

quit()


