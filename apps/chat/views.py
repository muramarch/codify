from requests import Response
from rest_framework import viewsets
from .models import Message
from .serializers import MessageSerializer
from openai_integration import generate_response


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exceptions=True)
        self.perform_create(serializer)

        input_message = serializer.validated_data['text']
        response_message = generate_response(input_message)
        
        self.save_messages(input_message, response_message)
        
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        
        
    def save_messages(self, input_message, response_message):
        input_msg = Message.objects.create(text=input_message)
        response_msg = Message.objects.create(text=response_message)
        return input_msg, response_msg