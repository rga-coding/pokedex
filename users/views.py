from rest_framework.views import APIView
from rest_framework.response import Response
from users.serializer import UserRegisterSerializer
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
