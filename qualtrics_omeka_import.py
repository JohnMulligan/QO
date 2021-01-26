import csv
import sys
import re
import os
import shutil
from import_vars import *
import omeka_interfacer as OI

fname=sys.argv[1]

media_dir=sys.argv[2]

if not os.path.exists(fname):
	print('error -- input csv does not exist:',fname)
	exit()
elif not fname.endswith('.csv'):
	print('error -- input file must be csv format:',fname)
	exit()
	
if not os.path.exists(media_dir):
	print('error -- media directory does not exist:',media_dir)
	exit()


print("IMPORTING FROM CSV:",fname)
print("ATTACHMENTS IN:",media_dir)

c=0


with open(fname) as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:

		if c>1:
			properties=[]
			for column in row:
				col_group=column.split('_')[0]
				if col_group in qualtrics_omeka_items_map:
					omeka_term,omeka_type=qualtrics_omeka_items_map[col_group]
				elif column in qualtrics_omeka_items_map:
					omeka_term,omeka_type=qualtrics_omeka_items_map[column]
				else:
					omeka_term=None
				
				val=row[column]
				
				if column=="ResponseId":
					ResponseId=row[column]
				
				if omeka_term!=None and val!='':
					properties.append({
					'term':omeka_term,
					'type':omeka_type,
					'value':row[column]
					})
			omeka_item_id=OI.create_item(properties)
			print(ResponseId,omeka_item_id)
			for col_group in qualtrics_omeka_media_map:
				
				cg=qualtrics_omeka_media_map[col_group]
				
				media_properties=[]
				for column in cg:
					if cg[column]=='FILENAME':
						clean_fname=row[column]
						upload_fname=ResponseId+'_'+clean_fname
					else:
						omeka_term=cg[column]['term']
						omeka_type=cg[column]['type']
						if 'HARDCODE' not in column:
							val=row[column]
						else:
							val=cg[column]['value']
						
						media_properties.append({
						'term':omeka_term,
						'type':omeka_type,
						'value':val
						})
				if clean_fname!='':
					shutil.copy(os.path.join(media_dir,col_group,upload_fname),clean_fname)
					OI.upload_attachment(omeka_item_id,media_properties,clean_fname)
					os.remove(clean_fname)
			
		c+=1
