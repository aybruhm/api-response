Industry ready custom API payload with an easy format for building Python APIs (Django/Django Rest Framework)

Yosh! If you are a django backend developer and have used the amazing utility toolkit for creating amazing APIs. You probably have come across the way django rest framework lets you return data by default. Not industry standard, if I may add. 

So you serialize what object you want, and it serialized and you return it like so:

    class GetPostsAPiView(APIView):

        def get(self, request):
            posts = Post.objects.all()
            post_serializer = PostSerializer(posts,  many=True)

            if post_serializer.is_valid():
                post_serializer.save()
                return Response(serializer.data)
            
            else:
                return Response(serializer.errors)


    # OUTPUT
    -----------
    - success response
    {
        'title': 'First blog post', 
        'content': 'Lorem ipsume content', 
        'author': 1
    }

    - error response
    {
        ['title']: 'field is required'
    }


Does the above ouput makes sense to you? I mean, it clearly doesn't help the frontend devs, trying putting yourself in their shoes. Imagine the dev is trying to check for the status code in the data been outputted, and the above is what the developer got. Dang! Extra work, right? I happen to work with a mobile developer, and he changed the way I build APIs. So instead of the above way, what do you think of this:

    from rest_api_payload import success_response, error_response


    class GetPostsAPiView(APIView):

        def get(self, request):
            posts = Post.objects.all()
            post_serializer = PostSerializer(posts,  many=True)

            if post_serializer.is_valid():
                post_serializer.save()

                payload = success_response(
                    status="200 ok",
                    message="All the posts don come, chief!"
                    data=serializer.data
                )
                return Response(data=payload)
            
            else:
                payload = error_response(
                    status="400 bad request",
                    message="Something went wrong, chief! Try again sometime"
                )
                return Response(data=payload)


    # OUTPUT
    -----------
    - success response
    {
        'status': '200 ok', 
        'message':'All the posts don come, chief!', 
        'data': {'title': 'First blog post', 'content': 'Lorem ipsume content', 'author': 1}'
    }

    - error response
    {
        'status': '400 bad request',
        'message': 'Ahh, chief, nothing dey here oooo!',
        'data': {['title']: 'field is required'}
    }



What do you think about the above? Pretty neat and industry standard, right? Installing the package is pretty is easy, fam. Here's how to:

    pip install rest-api-payload

In the file (.py) that you wish to use it, import it. <br>

    from rest_api_payload import success_response, error_response

And that's all, you can begin calling the function and passing arguments!

<br>

## Contribute

All contributions are welcome:

- Read the issues, Fork the project and do a Pull Request.
- Request a new topic creating a `New issue` with the `enhancement` tag.
- Find any kind of errors in the `README` and create a `New issue` with the details or fork the project and do a Pull Request.
- Suggest a better or more pythonic way for existing examples.