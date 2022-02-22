from django.urls import path

from common.views.modelsView import (ArticleView)


urlpatterns = [
    path(
        "get/articles/",
        ArticleView.as_view({"get":"get_articles"}),
        name="get_articles",
    ),
    path(
        "add/article/",
        ArticleView.as_view({"post":"add_article"}),
        name="add_article",
    ),
    path(
        "delete/article/<slug:pk>/",
        ArticleView.as_view({"delete":"destroy_article"}),
        name="destroy_article"
    )
]
