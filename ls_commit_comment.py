#####################
#
# Creating python script to get all the 
# commit messages of a repository
# author : sanan
# email : sanan3946@gmail.com
#
#####################

import sys
import os
import requests

token = os.environ.get('TOKEN');

header_ = {
    "Authorization" : f"Bearer {token}",
    "Accept" : "application/json"
}

def url(owner_name, repo_name):
    url_f = f"https://api.github.com/repos/{owner_name}/{repo_name}/comments";
    return url_f;

def main():
    if len(sys.argv) < 3 : 
        print("""Wrong Command !!!
Command : python ls_commit_comment.py <OWNER_NAME> <REPO_NAME>""");
        return;
    
    response = requests.get(url(sys.argv[1], sys.argv[2]), headers = header_);
    
    if response.status_code == 200 : 
        data = response.json();
        for count,user in enumerate(data, start = 1) : 
            print(f"==========user : {count}=========");
            print(f"id : {str(user['id'])}");
            print(f"user : {str(user['user']['login'])}");
            print(f"commit id : {str(user['commit_id'])}");
            try : 
                print(f"message : {str(user['body'])}");
            except UnicodeEncodeError : 
                print("message : $ Not Readable $");
                
    else : 
        print(f"Error : {response.status_code}");
        print(response.text)
    

if __name__ == "__main__" :
    main(); 
    