import sys
import praw
import time
import string
import os.path
import webbrowser
import account_info
import text_manipulation

# The ^^^ is reddit formatting to make the text smaller
ending = '^^^Beep ^^^Boop. ^^^I ^^^am ^^^a ^^^bot.'



#This section of code sets up the bot
print('\n\nConnecting to reddit...')

r = praw.Reddit(account_info.user_agent)
r.set_oauth_app_info(account_info.app_id, account_info.app_secret, account_info.app_uri)
r.refresh_access_information(account_info.app_refresh)

print('Done')



# This where the bulk of the bot is handled. It interprets messages and handles them accordingly if possible
while(True): # Run forever
    r.refresh_access_information(account_info.app_refresh) # I think this has to be called at least every hour for the bot to work

    try:
        unread_messages = r.get_unread()
        for message in unread_messages:
            if(''.join(str(message.subject).lower().split()) == 'tablehelp'): # If the subject is 'TableHelp' or 'table help' then send the messages in the post
                sections = text_manipulation.strip_list(message.body.split('***'))
                if(len(sections)==3):
                    post = r.get_submission(sections[0]) 
                    if(str(message.author) == str(post.author)):
                        message_replies = text_manipulation.get_messages_from_table(sections[2], sections[1])
                        print('\nAbout to send ' + str(len(message_replies)) + ' to ' + str(sections[0]))
                        for response in message_replies:
                            post.add_comment(response + '\n***\n' + ending)
                        message.reply('All messages have been sent as requested.\n***\n' + ending)
                    else:
                        message.reply('I will not perform this action since you did not create this post.\n***\n' + ending)
                else:
                    message.reply('Something doesn\'t seem to be working with your formatting.\n***\n' + ending)
                message.mark_as_read()
            else: 
                # Outputs information about messages that could not be handled
                if(str(message.subject) == 'comment reply' or str(message.subject) == 'username mention'):
                    message.mark_as_read()
                else:
                    print("\nThere is a message that I could not handle. It might be a request.\nSubject: " + str(message.subject) + " Author: /u/" + str(message.author) + "\nLink to request: " + str(message.id))
                    
        # Still in the while loop, sleep for a bit
        r.refresh_access_information(account_info.app_refresh) # I think this has to be called at least every hour for the bot to work
        sys.stdout.write('.') # This . is used to show that the bot is working, despite not performing any actions
        sys.stdout.flush()
        time.sleep(60) # Wait for one minute before continuing. Keeps the bot from hogging to many resources
    except (KeyboardInterrupt, SystemExit): # Allow the while true loop to end if the script is canceled
        print('Exiting');
        raise
    except: # Try to continue running, despite crashing
        r.refresh_access_information(account_info.app_refresh)
        print('\nSomething broke while recieving or sending messages, restarting in one minute')
        time.sleep(60)
        
    
