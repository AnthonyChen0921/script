import requests
import json

# Load the cookies from the file
with open('cookies.json', 'r') as f:
    cookie_list = json.load(f)

def fetch_story_unclassified(workspace_id, cookie_list):
    # Convert the list of cookie dictionaries to a string format
    cookies = "; ".join([f"{c['name']}={c['value']}" for c in cookie_list])

    url = "https://www.tapd.cn/api/aggregation/story_aggregation/get_story_fields_userviews_roles_workflowsteps_category_and_list"
    params = {
        "workspace_id": "55989309",
        "data[type]": "story",
        "location": "/prong/stories/stories_list",
        "data[query_token]": "f7404cf77c01fb0ca5a2d44f21f28fa8",
        "from": "stories_list"
    }
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Cookie": cookies,
        "Host": "www.tapd.cn",
        "Origin": "https://www.tapd.cn",
        "Referer": "https://www.tapd.cn/tapd_fe/55989309/story/list?queryToken=f7404cf77c01fb0ca5a2d44f21f28fa8&categoryId=1155989309001000006&sort_name=&order=&useScene=storyList&conf_id=1155989309001004492&page=1",
        "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"115\", \"Chromium\";v=\"115\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    }

    data = {"workspace_id":"55989309","conf_id":"1155989309001004492","sort_name":"","confIdType":"URL","order":"","perpage":"100","page":1,"query_token":"f7404cf77c01fb0ca5a2d44f21f28fa8","category_id":"-1","location":"/prong/stories/stories_list","target":"55989309/story/list","entity_types":["story"],"use_scene":"storyList","list_type":"flat","need_category_counts":1,"menu_workitem_type_id":"","dsc_token":"1OaxKPDD0LFFc93M"}

    response = requests.post(url, headers=headers, params=params, data=json.dumps(data), verify=False)

    # Parse the response JSON into a dictionary
    story_data = response.json()
    
    # Navigate to the list of stories
    stories = story_data['data']['stories_list']['data']['stories_list']

    # Form the dictionary using the list of stories
    story_data_dict = {story['Story']['id']: story['Story'] for story in stories}

    # Save the dictionary to a file
    with open('story_unclassified.json', 'w') as file:
        json.dump(story_data_dict, file)

    print(f'Status Code: {response.status_code}')
    print('Unclassified Story data has been fetched and saved to story.json')

    return story_data_dict


def main():
    """
    Main function to fetch the story data and store it in a JSON file.
    """
    try:
        # Fetch and save the story data
        story_data_dict = fetch_story_unclassified("55989309", cookie_list)

        # Optionally, print or process the returned story data as needed
        print("Number of stories fetched:", len(story_data_dict))

    except Exception as e:
        # Handle any exceptions that might occur
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()