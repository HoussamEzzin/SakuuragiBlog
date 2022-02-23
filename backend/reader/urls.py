from django.urls import path
from reader.views import PublisherNoAthenticatedView, PublisherView


urlpatterns = [
    path(
        "account/get/publishers/",
        PublisherView.as_view({"post": "get_publishers"}),
        name="get_publishers",
    ),
    path(
        "get/publishers/",
        PublisherNoAthenticatedView.as_view({"post":"get_publishers_no_authentication"}),
        name="get_publishers_no_authentication",
    )
]
