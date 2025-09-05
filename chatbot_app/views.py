from rest_framework import viewsets
from .models import Chat
from .serializers import ChatSerializer

from rest_framework import status
from rest_framework.response import Response
from .chat_service import ChatService


class ChatViewSet(viewsets.ModelViewSet):
    

    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    # permission_classes = [IsAccountAdminOrReadOnly]


    def create(self,request):
        serializer = ChatSerializer(data=request.data)
        if serializer.is_valid():
            
            # instance of chat service
            chat_service = ChatService()
            ai_response = chat_service.ai_response(request.data['prompt'] )
            serializer.validated_data['ai_response'] = ai_response.choices[0].message.content
            serializer.validated_data['chat_id'] = ai_response.id
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    