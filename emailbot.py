import time
import json
from fetch_story import fetch_story
from send_email import send_email

def load_email_map(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def main():
    # load the previously fetched data
    try:
        with open('story.json', 'r') as file:
            old_data = json.load(file)
    except FileNotFoundError:
        old_data = {}


    # fetch the current data
    current_data_dict = fetch_story()

    # save the current data to a file for future comparison
    with open('story.json', 'w') as file:
        json.dump(current_data_dict, file)

    # check for changes in status from "status_3" to "status_7"
    for story_id, story_data in current_data_dict.items():
        old_story_data = old_data.get(story_id)
        if old_story_data is None:
            continue

        print(f'Checking story {story_id}...')
        if old_story_data['status'] == 'status_3' and story_data['status'] == 'status_7':
            # send email
            # Load email mapping
            email_map = load_email_map('contact.json')  # replace with the correct path to your JSON file

            # Get the recipient emails from the mapping
            recipient_emails = [email_map.get(creator) for creator in story_data["creator"] if creator in email_map]

            # Ensure there are recipients to send the email to
            if recipient_emails:
                cc_emails = ['erdong.chen-ext@ldc.com'] # CC recipients
                send_email(recipient_emails, cc_emails, story_data)
            else:
                print(f"No recipients found for creators: {story_data['creator']}")
        else:
            print(f'Story {story_id} has not changed status.')

# run the main function every 60 seconds
while True:
    main()
    time.sleep(10)
