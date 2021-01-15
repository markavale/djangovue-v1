from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from . serializers import MailSerailizer, RatingSerializer, SkipperSerializer
# from rest_framework.generics import CreateAPIView, ListAPIView
# from rest_framework.views import APIView
from . models import Mail, Rating, Skipper
from rest_framework import status, viewsets
from rest_framework.response import Response
import smtplib
from email.message import EmailMessage
from django.conf import settings

class MessagesViewSet(viewsets.ModelViewSet):
    queryset = Mail.objects.all()
    serializer_class = MailSerailizer
    lookup_field = 'id'

    # def list(self, request):
    #     pass

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Create EmailMessage Object
            email = EmailMessage()
            # Who is the email from
            email["from"] = settings.EMAIL_HOST_USER
            # To which email you want to send the email
            email["to"] = serializer.data['email']
            # Subject of the email
            email["subject"] = serializer.data['subject']
            message = f"Hello {serializer.data['name']}, thank you for reaching out. I will get in touch to you soon as possible."
            email.set_content(message)
            
            # Create smtp server
            with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
                smtp.ehlo()
                # Connect securely to server
                smtp.starttls()
                # Login using username and password to dummy email. Remember to set email to allow less secure apps if using Gmail
                smtp.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
                # Send email.
                smtp.send_message(email)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #return super().create(request, *args, **kwargs)

    # def retrieve(self, request, pk=None):
    #     pass

    # def update(self, request, pk=None):
    #     pass

    # def partial_update(self, request, pk=None):
    #     pass

    # def destroy(self, request, pk=None):
    #     pass

    def get_permissions(self):
    # """
    # Instantiates and returns the list of permissions that this view requires.
    # """
        if self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    lookup_field = 'id'

    def list(self, request):
        ratings = Rating.objects.all()
        serializer = RatingSerializer(ratings, many=True)
        if ratings:
            sum = 0.0
            for rating in ratings:
                sum += rating.rate
            computed_rating = round((sum / ratings.count()), 2)
        else:
            computed_rating = 0
        dict = {
            "ratings":serializer.data,
            "rating_computed":computed_rating
        }
        return Response(dict)

    # def create(self, request):
    #     pass

    # def retrieve(self, request, pk=None):
    #     pass

    # def update(self, request, pk=None):
    #     pass

    # def partial_update(self, request, pk=None):
    #     pass

    # def destroy(self, request, pk=None):
    #     pass

    def get_permissions(self):
    # """
    # Instantiates and returns the list of permissions that this view requires.
    # """
        if self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

class SkipperViewSet(viewsets.ModelViewSet):
    queryset = Skipper.objects.all().order_by('-timestamp')
    serializer_class = SkipperSerializer
    lookup_field = 'id'

    # def list(self, request):
    #     analytics = PageViewsAnalytics.objects.all()
    #     total_views = 0
    #     total_in_month = 0
    #     for viewer in analytics:
    #         total_views = viewer.get_total_views()
    #         total_in_month = viewer.get_avg_month()
    #     serializer = self.serializer_class(self.queryset, many=True)
    #     data = {
    #         "total_views":total_views,
    #         "total_in_month":total_in_month,
    #         "results": serializer.data
    #     }

    #     return Response(data)

    def create(self, request):
        # add a record
        if not request.session.session_key:
            request.session.create()
        session_id = request.session.session_key
        # PageVisit
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

        if x_forwarded_for:
            ipaddress = x_forwarded_for.split(',')[-1].strip()
        else:
            ipaddress = request.META.get('REMOTE_ADDR')
        
        skip= Skipper()#.objects.get_or_create(session_id=session_id) #imported class from model
        skip.session = session_id
        skip.ip= ipaddress
        skip.count = 1
        skip.save()
        serializer = self.serializer_class(skip, many=False)
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

# class AddRating(CreateAPIView):
#     serializer_class = RatingSerializer
#     permission_classes = [AllowAny]

# class RatingsList(ListAPIView):
#     serializer_class = RatingSerializer
#     permission_classes = [IsAdminUser]
#     queryset = Rating.objects.all()

# class MessagesList(ListAPIView):
#     serializer_class = MailSerailizer
#     permission_classes = [IsAdminUser]
#     queryset = Mail.objects.all()


