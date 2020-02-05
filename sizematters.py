import os, shutil, re

root_path = "/media/bodie/adf509fe-a05b-4d45-8b63-6d38305c48af/completed"

movies = "/media/bodie/adf509fe-a05b-4d45-8b63-6d38305c48af/Movies"

series = "/media/bodie/adf509fe-a05b-4d45-8b63-6d38305c48af/Series"

seasonstr = ("S1", "S0",)




for dirpath, dnames, fnames in os.walk(root_path):
    for f in fnames:
        try:
            if os.path.getsize(os.path.join(dirpath, f)) > 100000000 or f.endswith(".sub"):
                movies_file_path   =  os.path.join(movies, f)
                source_file_path =  os.path.join(dirpath, f)
                shutil.move(source_file_path, movies_file_path)
        except:
            pass

for i in seasonstr:
    for dirpath, dnames, fnames in os.walk(movies):
        for f in fnames:
            try:
                if i in str.upper(f):
                    series_file_path   =  os.path.join(series, f)
                    source_file_path =  os.path.join(dirpath, f)
                    shutil.move(source_file_path, series_file_path)
            except:
                pass 
            
shutil.rmtree(root_path, ignore_errors=True)
os.mkdir(root_path)

def movie_name():
    for filename in os.listdir(movies):
        try:
            ext = filename[-4:]
            date_regex = re.search(r'[0-9]{4}', filename)
            head, sep, tail = filename.partition(date_regex.group(0))
            new_name = head + sep
            os.rename(os.path.join(movies ,filename), os.path.join(movies, new_name.replace('.', ' ') + ext))
        except:
            pass
            
def series_name():
    for filename in os.listdir(series):
        if os.path.isdir(os.path.join(series, filename)):
            pass
        else:
            ext = filename[-4:]
            season_regex = re.search(r'[sS][0-9]{2}[eE][0-9]{2}', filename)
            head, sep, tail = filename.partition(season_regex.group(0))
            new_name = head + str.upper(sep)
            os.rename(os.path.join(series ,filename), os.path.join(series, new_name.replace('.', ' ') + ext))   


def series_dir():
    for filename in os.listdir(series):
        if os.path.isdir(os.path.join(series, filename)):
            pass
        else:
            season_regex = re.search(r'[sS][0-9]{2}', filename)
            head, sep, tail = filename.partition(season_regex.group(0))
            seas_dir = head + str.upper(sep)
            seas_dir_path = os.path.join(series, seas_dir)
            if os.path.isdir(seas_dir_path) != True:
                os.mkdir(seas_dir_path)
                shutil.move(os.path.join(series, filename), os.path.join(seas_dir_path, filename))
            else:
                shutil.move(os.path.join(series, filename), os.path.join(seas_dir_path, filename))
                

movie_name()        

series_name()

series_dir()
        
quit()
