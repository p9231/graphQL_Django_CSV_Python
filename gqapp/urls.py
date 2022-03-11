# from xml.etree.ElementInclude import include
# from django.conf.urls import url, include
from django.urls import path, include
from graphene_django.views import GraphQLView


urlpatterns = [
    path('graphql/', GraphQLView.as_view(graphiql=True)),
]
