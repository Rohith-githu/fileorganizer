import shutil
import os
    
source_dir = 'unk'
target_dir = 'unkmover'
    
file_names = os.listdir(source_dir)
for file_name in file_names:
	   shutil.move(os.path.join(source_dir, file_name), target_dir)