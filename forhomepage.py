import json
import facebook

def main():
    token = {'EAAjJX1RAG3gBAHQMTxrelWNGgcwZCwtQ0Dc8FAlIofFnZAvaVZCglyAMLQC4XYnlg2VB8dKAWXbE3LTmaKJ5Tax6xnUE6utTCQxWliBFFc2fXI420GV7ZAMjfujO7GSlfGOJxEhSh1SlnI8M4sFMDduiQa4qPFCWSnJvPwSwSXZAUZAZBct7QAkxoCctPYiD59MY9nDLpzmHgZDZD'} # changes as per your access token.
    graph = facebook.GraphAPI(token)
    # fields = {'post','message','comments'}
    profile = graph.get_object(id=111696833555937 , fields= 'posts{message,comments.summary(true){message}}') #id = page id , fields = the data you want from home page.
    print(json.dumps(profile, indent=4))


if __name__ == "__main__":
    main()
