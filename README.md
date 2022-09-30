# Production API Payload

A to-go-to production API payload with an easy format for building APIs with Python.

## Quickstart

To get it running, follow the steps below:

1). Pip install the package in your project terminal:

```bash
pip install rest-api-payload
```

2). In the file (.py) that you wish to use it, import it:

```python
    from rest_api_payload import success_response, error_response
```

That's pretty much it - you can now call the function and pass the required arguments!

## Example

Suppose you have a function that returns a response to the client:

```python
...
    def list_of_posts(request):
        """Returns a list of posts"""
        post = Post.objects.all()
        post_serializer = PostSerializer(post, many=True)
        return Response(post_serializer.data)
```

The above response output would be:

```json
    [
        {
            "title": "First blog post", 
            "content": "Lorem ipsume content", 
            "author": 1
        },
        {
            "title": "Second blog post", 
            "content": "Lorem ipsume content", 
            "author": 2
        },
        {
            "title": "Third blog post", 
            "content": "Lorem ipsume content", 
            "author": 3
        }
    ]
```

This works too, but let's take the function to the next level by doing this:

```python
...
from rest_api_payload import success_response


    def list_of_posts(request):
        """Returns a list of post"""
        post = Post.objects.all()
        post_serializer = PostSerializer(post, many=True)

        payload = success_response(
            status=True,
            message="Post retrieved!",
            data=post_serializer.data
        )
        return Response(data=payload, status=status.HTTP_200_OK)
```

The above response output would be:

```json
    [   "status": true, 
        "message":"Posts retrieved!", 
        "data": {
            {
                "title": "First blog post", 
                "content": "Lorem ipsume content", 
                "author": 1
            },
            {
                "title": "Second blog post", 
                "content": "Lorem ipsume content", 
                "author": 2
            },
            {
                "title": "Third blog post", 
                "content": "Lorem ipsume content", 
                "author": 3
            }
        }
    ]
```

*I built this payload because of a project I took lead in building from scratch - and literally had to sympathize with the frontend (web and mobile) engineers. I hope you find this package useful, kindly leave a star if you did.*

## Contribute

All contributions are welcome:

- Read the issues, Fork the project and do a Pull Request.
- Request a new topic creating a `New issue` with the `enhancement` tag.
- Find any kind of errors in the `README` and create a `New issue` with the details or fork the project and do a Pull Request.
- Suggest a better or more pythonic way for existing examples.
