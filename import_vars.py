#here, you map column headers to omeka properties (later, I should allow for classes)
#you can map them one-to-one (e.g., StartDate or Q1_4 or Q3)
#or you can map multi-selects in groups simply by omitting the underscored sub-part (e.g., Q6_1,Q6_2,Q6_3 are all gathered up with Q6 by qualtrics_omeka_import.py)

##shoot -- I forgot to add data types. that's next.

qualtrics_omeka_items_map={
'StartDate':['ko:startDate','numeric:timestamp'],
'EndDate':['ko:endDate','numeric:timestamp'],
'IPAddress':['ko:ipAddress','literal'],
'Progress':['ko:progress','numeric:integer'],
'Duration (in seconds)':['ko:duration','numeric:integer'],
'Finished':['ko:finished','literal'],
'RecordedDate':['ko:recordedDate','numeric:timestamp'],
'ResponseId':['ko:responseID','literal'],
'LocationLatitude':['ko:locationLatitude','literal'],
'LocationLongitude':['ko:locationLongitude','literal'],
'UserLanguage':['ko:userLanguage','literal'],
'Q1_4':['ko:contactFirstName','literal'],
'Q1_5':['ko:contactLastName','literal'],
'Q1_6':['ko:contactEmail','literal'],
'Q3':['dcterms:title','literal'],
'Q4_4':['ko:institutionalLocation','literal'],
'Q4_5':['ko:geographicLocation','literal'],
'Q6':['ko:disciplinaryPerspectives','literal'],
'Q13':['ko:courseTopics','literal'],
'Q7':['ko:courseLevel','literal'],
'Q8':['ko:instructionalModality','literal'],
}

#this works sort of like the groups above
#except that because media properties need to be uploaded as their own quasi-items, we need to store the properties map for each in its own dictionary, in order to more efficiently bundle them up on the csv reader side
#FILENAME is reserved, for now, to be pulled by the upload_media function
qualtrics_omeka_media_map={
'Q10':{'Q10_Id':{'term':'ko:attachmentID','type':'literal'},
'Q10_Name':'FILENAME','HARDCODE1':{'term':'dcterms:type','type':'literal','value':'syllabus'}},
'Q14':{'Q14_Id':{'term':'ko:attachmentID','type':'literal'},
'Q14_Name':'FILENAME','HARDCODE1':{'term':'dcterms:type','type':'literal','value':'assignment'}},
'Q17':{'Q17_Id':{'term':'ko:attachmentID','type':'literal'},
'Q17_Name':'FILENAME','HARDCODE1':{'term':'dcterms:type','type':'literal','value':'assignment'}},
'Q19':{'Q19_Id':{'term':'ko:attachmentID','type':'literal'},
'Q19_Name':'FILENAME','HARDCODE1':{'term':'dcterms:type','type':'literal','value':'assignment'}},
'Q12':{'Q12_Id':{'term':'ko:attachmentID','type':'literal'},
'Q12_Name':'FILENAME','HARDCODE1':{'term':'dcterms:type','type':'literal','value':'cover image'}}
}