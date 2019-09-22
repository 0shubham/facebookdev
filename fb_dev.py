
import json
import facebook

def main():
    token={'EAAjJX1RAG3gBABvQfmUF6Vui4hUnAlZCNxBpdrZAUatyIH163KzvRjU3mpZBsXH2tr4NPZB71ZA8e9Vxyoy1yagqmZAy0KFepednlQGBkDahhuRyhgKqhoakfZBXAplfVqWtLFTkFrMLgteC6f5PXZBFHzkwKQ5d59sbNy5At3XepxYR5VKfESohZBUedCC7fZBS1NVUfyZAZCJp05afzDvcO2rf'}
    graph = facebook.GraphAPI(token)

    fields=['email','gender','birthday']

    profile = graph.get_objects('me', fields = fields)

    print(json.dumps(profile, indent=4))


if __name__ == "__main__":
    main()