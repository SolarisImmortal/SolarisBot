import sys
import string
import os.path
import text_manipulation

file = open('Input.txt', 'r')
file_text = file.read()
file.close()

sections = text_manipulation.strip_list(file_text.split('***'))

message_replies = text_manipulation.get_messages_from_table(sections[1], sections[0])

file = open('Output.txt','w')
file.write('\n\n'.join(message_replies))
file.close
