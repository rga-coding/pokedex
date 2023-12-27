from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from users.serializer import UserRegisterSerializer
from rest_framework.authtoken.serializers import AuthTokenSerializer


class UserCreateView(APIView):
    def post(self, request) -> object:
        user_data = {k: v.lower() for k, v in request.data.items()}
        serializer = UserRegisterSerializer(data=user_data)

        if serializer.is_valid():
            # user = serializer.save()
            # token = Token.objects.get(user=user).key
            # serializer.save(token=token)
            # serializer.data['token'] = token
            user = serializer.save()
            token = Token.objects.get(user=user).key
            serializer_data = serializer.data.copy()
            serializer_data.update({'token': token})
        else:
            return Response(
                data={
                    "errors": f"{', '.join(serializer.errors.keys())}",
                },
                status=400,
            )
        return Response(serializer_data, status=201)


class UserLoginView(APIView):
    def post(self, request) -> object:
        user_data = {k: v.lower() for k, v in request.data.items()}
        serializer = AuthTokenSerializer(data=user_data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response(
                data={
                    "errors": f"{', '.join(serializer.errors.keys())}",
                },
                status=401,
            )
