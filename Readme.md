# Qualtrics to Omeka importer

* Export your survey as csv with choice text and split columns
* Export your media attachments and unzip the folder
* In import_vars.py, map your Qualtrics questions:
   * from Column headers in export csv -- these can be grouped for multi-select questions as in the example provided
   * to Omeka terms and datatypes that exist in your site -- I used the custom ontology plugin in the example provided
   * AND -- define your media questions for importation in a separate dictionary -- again see the example file
* Define your Omeka API settings credentials in omeka_credentials.json -- template provided
* Run the import with qualtrics_omeka_import.py inputfile.csv attachmentsfolder.csv
   
   
I have only tested this on one dataset. I'm sure it has its limits and can be improved upon.  
   