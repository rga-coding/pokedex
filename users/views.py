from rest_framework.views import APIView
from rest_framework.response import Response
from users.serializer import UserRegisterSerializer
class UserCreateView(APIView):
    def post(self, request) -> object:
        user_data = {k: v.lower() for k, v in request.data.items()}
        serializer = UserRegisterSerializer(data=user_data)

        if serializer.is_valid():
            serializer.save()
        else:
            return Response(
                data={
                    "errors": f"{', '.join(serializer.errors.keys())}",
                },
                status=400,
            )
        return Response(serializer_data, status=201)
