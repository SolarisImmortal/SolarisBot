import re
import sys
import praw
import time
import string
import os.path
import webbrowser
import quick_values

def strip_list(var): # Strip any whitespace before and after each entry in a list
    i = 0
    while i < len(var):
        var[i] = var[i].rstrip().lstrip()
        i = i + 1
    return var

def is_separator(var): # See if each string in the list equals ':-:'
    i = 0
    while i < len(var):
        if not var[i] == ':-:':
            return False
        i = i + 1
    return True

def get_messages_from_table(table, message): # Creates messages based of a table of data and a message with locations for table data.
    table_raw = re.sub('\t+', ' ', table)           # Replace any tabs with spaces
    row_data = table_raw.split('\n')                # Break the table down into a list with the data of each row
    titles = strip_list(row_data[0].split(' | '))   # This is the first row of the table, the header with the titles for the columns 
    row1 = strip_list(row_data[1].split(' | '))     # This is the second row, its used to perform a check for removing the data
    rows = row_data[1:]
    if(is_separator(row1)):                         # if the second row is a separator row (only contains ":-:" for entries), only collect data from the third row on. 
        rows = row_data[2:]

    # Creates a list with the default message and the length equal to the number of messages to be sent
    messages = [message] * len(rows)
    
    r = 0
    while r < len(rows):
        t = 0
        row_values = strip_list(rows[r].split(' | '))
        while t < len(titles):
            # For each title, remove the <title value> from the message and replace it with the actual value from the table
            messages[r] = row_values[t].join(messages[r].split('<' + titles[t] + '>'))
            
            t = t + 1
        r = r + 1
    return messages # Return all the messages with the text replaced
