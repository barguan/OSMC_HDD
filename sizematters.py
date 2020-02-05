import os, shutil, re

root_path = "/media/bodie/adf509fe-a05b-4d45-8b63-6d38305c48af/completed"

movies = "/media/bodie/adf509fe-a05b-4d45-8b63-6d38305c48af/Movies"

series = "/media/bodie/adf509fe-a05b-4d45-8b63-6d38305c48af/Series"

seasonstr = ("S1", "S0",)

for dirpath, dnames, fnames in os.walk(root_path):
    for f in fnames:
        try:
            if os.path.getsize(os.path.join(dirpath, f)) > 100000000:
                movies_file_path   =  os.path.join(movies, f)
                source_file_path =  os.path.join(dirpath, f)
                shutil.move(source_file_path, movies_file_path)
        except:
            pass

for i in seasonstr:
    for dirpath, dnames, fnames in os.walk(movies):
        for f in fnames:
            try:
                if i in upper(f):
                    series_file_path   =  os.path.join(series, f)
                    source_file_path =  os.path.join(dirpath, f)
                    shutil.move(source_file_path, series_file_path)
            except:
                pass
            
shutil.rmtree(root_path, ignore_errors=True)
os.mkdir(root_path)

def movie_name():
	for filename in os.listdir(movies):   
		ext = filename[-4:]
		date_regex = re.search(r'[0-9]{4}', filename)
		head, sep, tail = filename.partition(date_regex.group(0))
		new_name = head + sep
		os.rename(os.path.join(movies ,filename), os.path.join(movies, new_name.replace('.', ' ') + ext))

def series_name():
		for filename in os.listdir(series):   
			ext = filename[-4:]
			season_regex = re.search(r'[sS][0-9]{2}[eE][0-9]{2}', filename)
			head, sep, tail = filename.partition(season_regex.group(0))
			new_name = head + sep
			print(new_name)
			os.rename(os.path.join(series ,filename), os.path.join(series, new_name.replace('.', ' ') + ext))	

movie_name()		

series_name()
		
quit()
