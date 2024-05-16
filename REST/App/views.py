from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, APIView
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import *
from .models import *
from django.shortcuts import get_object_or_404
# Create your views here.


@api_view(http_method_names=["GET", "POST"])
def index(request:Request):
    if request.method =="POST":
        data=request.data
        response={"message":"POSt request","data":data}
        
        return Response(data=response, status=status.HTTP_201_CREATED)
    response = {"message": "Hello world"}  
    return Response(data=response, status=status.HTTP_200_OK)


# posts = [
#             {"user": "john_doe", "id": 123, "content": "This is the first dataset."},
#             {"user": "jane_smith", "id": 456, "content": "Here is the second dataset."},
#             {"user": "alice", "id": 789, "content": "This is the third dataset with different content."}
#         ]


# create and get the post 
# @api_view(http_method_names= ['GET', 'POST'])
# def post_list(request:Request):
#         posts=Post.objects.all()
        
#         if request.method =="POST":
#             data=request.data
#             serializer=PostSerializer(data=data)
            
#             if serializer.is_valid():
#                 serializer.save()
                
#                 response={
#                     "message":"data is posted",
#                     "data": serializer.data
#                 }
#                 return Response(data=response, status=status.HTTP_201_CREATED)
            
#             return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         serializer=PostSerializer(instance=posts, many=True)
        
#         response={
#             'message':'Posts',
#             'data':serializer.data
#         }
        # return Response(data=response, status=status.HTTP_201_CREATED)
    
    
    
# to show the posts..
@api_view(http_method_names=["GET"])
def post_details(requset:Request, post_id=int ):
    post=get_object_or_404(Post, pk=post_id)
 
    serializer= PostSerializer(instance=post)
    
    response={
        "message":"Getting data of ID",
        "data":serializer.data
    }
    return Response(data=response, status=status.HTTP_200_OK)
  
    
    
    
# # update the post 
# @api_view(http_method_names=["PUT"])
# def update_post(request:Request, post_id:int):
#     post=get_object_or_404(Post, pk=post_id)
#     if request.method == "PUT":
#         serializer=PostSerializer(instance=post, data=request.data)
    
#         if serializer.is_valid():
#             serializer.save()
            
#             response={
#                 "message":"post is about to update",
#                 "data":serializer.data
#             }
    
#             return Response(data=response, status=status.HTTP_200_OK)
#     return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# # delete the post 

# @api_view(http_method_names=["DELETE"])
# def delete_post(reques:Request, post_id=int):
#     post=get_object_or_404(Post, pk=post_id) 
    
#     post.delete()
    
#     return Response(status=status.HTTP_200_OK)





class ListPostView(APIView):
    serializer_class=PostSerializer
    
    def get(self,request:Request, *args, **kwargs):
        post=Post.objects.all()
        serializer=self.serializer_class(instance=post, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)    
            
    def post(self, request:Request, *args, **kwargs):
        data= request.data
        serializer= self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            
            response={
                "message":"Data hasbeen created",
                "data": serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    
class PostRetrieveUpdateDeleteView(APIView):
    serializer_class=PostSerializer
    
    def get(self, request:Request, post_id:int):
        post=get_object_or_404(Post, pk=post_id)
        serializer=self.serializer_class(instance=post)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request:Request, post_id:int):
        post=get_object_or_404(Post, pk=post_id)
        data=request.data
        
        serializer=self.serializer_class(instance=post, data=data)
        if serializer.is_valid():
            serializer.save()
            response={
                "message":"DATA is updated",
                "data":serializer.data
            }      
            return Response(data=response, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request:Request, post_id:int):
        post=get_object_or_404(Post, pk=post_id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)