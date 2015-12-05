from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from .orders.order_schemas import OrderSchema


# Create your views here.


def home(request):
    """Just a basic View """
    # album = Album.objects.get(pk=1)
    # ser = AlbumSerializer(album)
    return render(request, "rest_api/home.html", {"greeting": "hello"})


@api_view(['GET', 'POST'])
def order(request):
    """View for handling GET and POST requests concerning orders"""
    if request.method == 'GET':
        data = {"not ": "implemented"}
        return Response(data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        json_order = Post_Order(request)
        schema = OrderSchema()
        response = schema.dump(json_order)
        # Remove parentItemId if it is empty
        for itemId in response.data['body']['itemList']:
            if itemId['parentItemId'] == 'empty':
                del itemId['parentItemId']
        # Return the serialized data back
        return Response(response.data, status=status.HTTP_200_OK)


###############TESTING ONLY###########################

@api_view(['GET', 'POST'])
# @permission_classes((permissions.AllowAny,))
def test(request):
    """This view is for testing purposes only"""
    if request.method == 'GET':
        data = {"not ": "implemented"}
        return Response(data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        simple = Post_Order(request)
        return Response(request.data, status=status.HTTP_200_OK)


def Post_Order(request):
    """
    Deserialize the Order to an Order object
    :param request: The json POST request
    :return: Object type of Order containing json data
    """
    schema = OrderSchema()
    result = schema.load(request.data)
    item = result.data
    # print item.body.itemList[1].parentItemId
    # if I want tot delete the parentItemId ---> del item.body.itemList[0].parentItemId
    # print item.body.itemList[0].parentItemId
    return item
