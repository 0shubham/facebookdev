import facebook

token='EAAFvwLcijh0BAIfKLkCZBhwsTMvK2Cnqtn71BAscU6YHFfmFumtoVCOioawiGH4PtKqLc0Ux984zU70JGXYVWEa4ifFNnNntSi6tuRe9oolVMQTXZBV9EFoMz4VX6MeO03RAXtl59dgr3hPVvrvAXkIoAwB0hQW6cslXgebHhsFE8RL342190fS5JxhQiU51yaniS2NgULZBnI6R5ZA77fFqDtyVa8EZD' # changes as per your access token.
fb = facebook.GraphAPI(access_token=token)

fb.put_object(parent_object='me', connection_name='feed', message='Hello... This is my test for fb page.') #parent_object= where you want ot put post here "me" means home page.
