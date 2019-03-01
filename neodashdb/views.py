from django.shortcuts import render
import json

from rest_framework.response import Response
from rest_framework.views import status
from rest_framework import generics
from .models import Assets, Vulns, Scans
from .serializers import AssetsSerializer, ScansSerializer, VulnsSerializer
from django.db import IntegrityError
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework_jwt.settings import api_settings
from rest_framework import permissions

from rest_framework.permissions import IsAuthenticated

# Get the JWT settings, add these lines after the import/from lines
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

# ...

# Add this view to your views.py file

class LoginView(generics.CreateAPIView):
    """
    POST auth/login/
    """
    # This permission class will overide the global permission
    # class setting
    permission_classes = (permissions.AllowAny,)

    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # login saves the user’s ID in the session,
            # using Django’s session framework.
            login(request, user)
            serializer = TokenSerializer(data={
                # using drf jwt utility functions to generate a token
                "token": jwt_encode_handler(
                    jwt_payload_handler(user)
                )})
            serializer.is_valid()
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)






#Locals Class


# class ListAssetsView(generics.ListAPIView):
#     """
#     Provides a get method handler.
#     """
#     queryset = Assets.objects.all()
#     serializer_class = AssetsSerializer
#     permission_classes = (permissions.IsAuthenticated,)


class ListCreateAssetsView(generics.ListCreateAPIView):
    """
    GET Assets/
    POST Assets/
    """
    queryset = Assets.objects.all()
    serializer_class = AssetsSerializer
    permission_classes = (permissions.IsAuthenticated,)


    def post(self, request, *args, **kwargs):

        try:

            a_asset = Assets.objects.create(
                shortcut=request.data["shortcut"],
                name=request.data["name"],
                url=request.data["url"],
                type=request.data["type"],
                #high=request.data["high"],
                #mid=request.data["mid"],
                #low=request.data["low"],
                #info=request.data["info"],
                #risk=request.data["risk"],


            )
            return Response(
                data=AssetsSerializer(a_asset).data,
                status=status.HTTP_201_CREATED
            )
        except (IntegrityError) as e:
            return Response(
                data={"Ok: Created"},
                status=status.HTTP_201_CREATED
            )

        except (Exception) as e:
            return Response(
                data=json.dumps({'Error': str(e)}),
                status=status.HTTP_400_BAD_REQUEST
            )


class ListCreateScansView(generics.ListCreateAPIView):
    """
    GET Scans/
    POST Scans/
    """
    queryset = Scans.objects.all()
    serializer_class = ScansSerializer
    permission_classes = (permissions.IsAuthenticated,)


    def post(self, request, *args, **kwargs):

        try:

            a_asset = Scans.objects.create(
                reporthash=request.data["reporthash"],
                date=datetime.strptime(request.data["date"], "%Y.%m.%d %Hh%M"),
                shortcut=Assets.objects.get(pk=request.data["shortcut"]),

                success=request.data["success"],
                running=request.data["running"],


            )
            return Response(
                data=AssetsSerializer(a_asset).data,
                status=status.HTTP_201_CREATED
            )

        except (AttributeError) as e:
            return Response(
                data={"Ok: Created"},
                status=status.HTTP_201_CREATED
            )

        except (IntegrityError) as e:
            return Response(
                data={"Ok: Created"},
                status=status.HTTP_201_CREATED
            )
        except (Exception, KeyError) as e:
            return Response(
                data=json.dumps({'Error': str(e)}),
                status=status.HTTP_400_BAD_REQUEST
            )


class ListCreateVulnsView(generics.ListCreateAPIView):
    """
    GET Vulns/
    POST Vulns/
    """
    queryset = Vulns.objects.all()
    serializer_class = VulnsSerializer
    permission_classes = (permissions.IsAuthenticated,)


    def post(self, request, *args, **kwargs):

        try:

            a_asset = Vulns.objects.create(
                id=request.data["id"],

                asset=Assets.objects.get(pk=request.data["asset"]),

                level=request.data["level"],
                status=request.data["status"],
                title=request.data["title"],


            )
            return Response(
                data=VulnsSerializer(a_asset).data,
                status=status.HTTP_201_CREATED
            )
        except (AttributeError) as e:
            return Response(
                data={"Ok: Created att"},
                status=status.HTTP_201_CREATED
            )

        except (IntegrityError) as e:
            return Response(
                data={"Ok: Created integrity : {} " .format(e)},
                status=status.HTTP_201_CREATED
            )

        except (Exception, KeyError) as e:
            return Response(
                data=json.dumps({'Error': str(e)}),
                status=status.HTTP_400_BAD_REQUEST
            )



