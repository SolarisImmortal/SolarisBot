import gspread
from oauth2client.service_account import ServiceAccountCredentials

# SOLARR is just a filler name until a better one is created.

# This file provides NEARR and FARR with some baseline features
# as well as features specific to FARR or NEARR.
# The management of these features is performed in another file.

class Application(object):

    def __init__(self, pagekey):
        self.url = url
        
        credentials = ServiceAccountCredentials.from_json_keyfile_name('login/google_access.json', scope)
        gc = gspread.authorize(credentials)

        wks = gc.open_by_key(pagekey).sheet1

        # Record the titles for each colomn, except the timestamp
        c = 2 # Start a two to skip the timestamp
        self.titles = []
        flag = True

        while flag:
            if(wks.cell(1,c)==''):
                flag = False
            elif:
                self.titles.append(wks.cell(1,c))
                c = c + 1

        # Count the number of entries
        row_count = 0
        r = 2 # Start a two to skip titles
        flag = True
        while flag:
            if(wks.cell(r,1)==''):
                flag = False
            elif:
                row_count = row_count + 1
                r = r + 1

        # Now to record the user data, this will be long
        self.applicants = []
        r = 2
        while r < row_count + 2:
            c = 2
            data = []
            while c < len(titles) + 2:
                data.append([].extend(wks.cell(r,c).split(', '))) # This records the data to a list of lists.
                c = c + 1
            self.applicants.append(Applicant(data))
            r = r + 1
        
class Applicant(object):

    def __init__(self, data):
        self.name = data[0]
        self.data = data[1:] # Store uncatagorized data to self.data
