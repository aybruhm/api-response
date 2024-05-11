# Production API Response

[![Package Code Quality](https://github.com/aybruhm/api-response/actions/workflows/package-test.yml/badge.svg)](https://github.com/aybruhm/api-response/actions/workflows/package-test.yml) [![Package Published to PypI](https://github.com/aybruhm/api-response/actions/workflows/package-publish.yml/badge.svg)](https://github.com/aybruhm/api-response/actions/workflows/package-publish.yml)

A go-to production API response with an easy format for building APIs with Python.

## Quickstart

To get it running, follow the steps below:

1). Pip install the package in your project terminal:

```bash
pip install rest-api-response
```

2). In the file (.py) that you wish to use it, import it:

```python
from rest_api_response import success_response, error_response
```

That's pretty much it - you can now call the function and pass the required arguments!

## Example

Suppose you have an API class that returns a list of blog posts to a client:

```python
# imports goes here
...
class PostListAPIView(views.APIView):
    serializer_class = PostSerializer

    def get(self, request):
        """Returns a list of posts"""

        posts = Post.objects.all()
        serializer = self.serializer_class(posts, many=True)
        return Response(serializer.data)
```

The API response would be:

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

This works too, but let's take the response to the next level by doing this:

```python
# imports goes here
...
from rest_api_response import success_response


class PostListAPIView(views.APIView):
    serializer_class = PostSerializer

    def get(self, request):
        """Returns a list of posts"""

        posts = Post.objects.all()
        serializer = self.serializer_class(posts, many=True)
        _response = success_response(
            message="Post retrieved!",
            data=serializer.data
        )
        return Response(data=_response, status=status.HTTP_200_OK)
```

The API response would be:

```json
[   
    "status": true, 
    "message": "Posts retrieved!", 
    "data": [
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
]
```

And that's it. You have a nicely catchy response. :-)

## Contribute

All contributions are welcome:

- Read the issues, Fork the project and do a Pull Request.
- Request a new topic creating a `New issue` with the `enhancement` tag.
- Find any kind of errors in the `README` and create a `New issue` with the details or fork the project and do a Pull Request.
- Suggest a better or more pythonic way for existing examples.
