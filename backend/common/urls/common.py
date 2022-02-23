from django.urls import path

from common.views.modelsView import (ArticleView)


urlpatterns = [
    path(
        "get/articles/",
        ArticleView.as_view({"get":"get_articles"}),
        name="get_articles",
    ),
    
]
