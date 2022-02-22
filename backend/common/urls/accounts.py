from django.urls import include, path
from common.models.models import Reader

from common.views.accounts import(
    ReaderView,
    PublisherView,
    PasswordReset,
    RequestPasswordReset
)

from common.views.auth import (
    LogoutView,
    PublisherUpdateView,
    UserLognView,
    UserUpdateView
)

from common.views.modelsView import (
    ArticleView,
    CategoryView
)


urls_reader = [
    path(
        "reader/register",
        ReaderView.as_view[{"post": "create"}],
        name="reader-register",
    ),
    path(
        "reader/update/<slug:pk>/",
        ReaderView.as_view({"put": "update"}),
        name = "reader-update",
    ),
    path(
        "reader/me/retrieve/<slug:username>/",
        ReaderView.as_view({"get":"retrieve", "delete":"destroy"}),
        name="reader-detail",
    ),
    path(
        "reader/activated/",
        ReaderView.as_view({"get": "activated"}),
        name="reader-activated",
    ),
    path(
        "reader/password_change/<slug:username>/",
        ReaderView.as_view({"get":"retrieve", "put":"set_password"}),
        name="reader-set-password",
    ),
    path(
        "reader/email_change/<slug:username>/",
        ReaderView.as_view({"get":"retrieve", "put":"set_email"}),
        name="reader-set-email"
    )
]

urls_publisher = [
    path(
        "publisher/update-partial/<slug:pk>/",
        PublisherUpdateView.as_view({"put": "publisher_update"}),
        name="partial_update",
    ),
    path(
        "publisher/register/",
        PublisherView.as_view({"post": "create"}),
        name="publisher-register",
    ),
    path(
        "publisher/me/retrieve/<slug:username>/",
        PublisherView.as_view({"get":"retrieve","delete":"destroy"}),
        name="publisher-detail"
    ),
    path(
        "publisher/activated/",
        PublisherView.as_view({"get": "activated"}),
        name="publisher-activated",
    ),
    path(
        "publisher/password_change/<slug:username>/",
        PublisherView.as_view({"get":"retrieve", "put":"set_password"}),
        name="set-password-publisher",
    ),
    path(
        "publisher/email_change/<slug:username>/",
        PublisherView.as_view({"get":"retrieve","put":"set_email"}),
        name="set_email",
    )

]

urlpatterns = [
    path("accounts/", include(urls_reader)),
    path("accounts/", include(urls_publisher)),
    path(
        "accounts/update-partial/<slug:pk>/",
        UserUpdateView.as_view({"put":"user_update"}),
        name="partial_update",
    ),
    path(
        "accounts/login/",
        UserLognView.as_view({"post":"login"}),
        name="login",
    ),
    path(
        "accounts/logout",
        LogoutView.as_view({"post":"logout"}),
        name="logout"
    ),
    path(
        "reset_password/",
        RequestPasswordReset.as_view({"post":"request_password_reset"}),
        name="request_password_reset",
    ),
    path(
        "reset_password/edit/",
        PasswordReset.as_view({"post": "password_reset"}),
        name="password_reset"
    ),
    path(
        "accounts/publihser/articles/<slug:pk>/",
        ArticleView.as_view({"get":"get_publisher_articles"}),
        name="get_publisher_articles"
    ),
    path(
        "accounts/add_article_picture/<slug:id>/",
        ArticleView.as_view({"put":"add_article_picture"}),
        name="add_article_picture"
    ),
    path(
        "accounts/add_category/",
        CategoryView.as_view({"post":"add_category"}),
        name="add_category",
    ),
    path(
        "accounts/get_categories/",
        CategoryView.as_view({"get":"get_categories"}),
        name="get_categories"
    ),
    path(
        "accounts/get_article_by_category",
        CategoryView.as_view({"post":"get_article_by_category"}),
        name="get_article_by_category"
    ),
    path(
        "accounts/articles/delete_article/<slug:pk>/",
        ArticleView.as_view({"delete":"destroy_article"}),
        name="destroy_article"
        )
]
