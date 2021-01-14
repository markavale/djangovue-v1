from typing import Text
from . serializers import PageVisitSerializer, TextMessageSerializer
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAdminUser
from rest_framework.generics import CreateAPIView
from . models import PageVisit, PageViewsAnalytics, TextMessage
from rest_framework import  viewsets #status
from rest_framework.response import Response

class addText(viewsets.ModelViewSet):
    serializer_class = TextMessageSerializer
    permission_classes = [AllowAny]
    queryset = TextMessage.objects.all().order_by('-timestamp')
    def create(self, request, *args, **kwargs):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

        if x_forwarded_for:
            ipaddress = x_forwarded_for.split(',')[-1].strip()
        else:
            ipaddress = request.META.get('REMOTE_ADDR')

        sender= TextMessage() #imported class from model
        sender.ip= ipaddress
        # sender.save()
        return super().create(request, *args, **kwargs)
    # def create(self, request, *args, **kwargs):
    #     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    #     if x_forwarded_for:
    #         ipaddress = x_forwarded_for.split(',')[-1].strip()
    #     else:
    #         ipaddress = request.META.get('REMOTE_ADDR')

    #     sender= TextMessage() #imported class from model
    #     sender.ip= ipaddress
    #     sender.save()
    #     return create().list(request, *args, **kwargs)

class PageViewSet(viewsets.ModelViewSet):
    queryset = PageVisit.objects.all()
    serializer_class = PageVisitSerializer
    lookup_field = 'id'

    def list(self, request):
        analytics = PageViewsAnalytics.objects.all()
        total_views = 0
        total_in_month = 0
        for viewer in analytics:
            total_views = viewer.get_total_views()
            total_in_month = viewer.get_avg_month()
        serializer = self.serializer_class(self.queryset, many=True)
        data = {
            "total_views":total_views,
            "total_in_month":total_in_month,
            "results": serializer.data
        }

        return Response(data)

    def create(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

        if x_forwarded_for:
            ipaddress = x_forwarded_for.split(',')[-1].strip()
        else:
            ipaddress = request.META.get('REMOTE_ADDR')

        viewer= PageVisit() #imported class from model
        viewer.ip= ipaddress
        viewer.count = 1
        viewer.save()
        obj, created = PageViewsAnalytics.objects.get_or_create()
        obj.viewers.add(viewer)
        serializer = self.serializer_class(viewer, many=False)
        data = {
            "Sucess": "Page view count successfully incremented!",
            "Data":serializer.data
        }
        return Response(data)

    def get_permissions(self):
    # """
    # Instantiates and returns the list of permissions that this view requires.
    # """
        if self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


