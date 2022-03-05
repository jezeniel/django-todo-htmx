from django.urls import path
from .views import TodoDoneView, TodoListView, TodoItemView, TodoUndoneView, index


app_name = "todo"
urlpatterns = [
    path("", index),
    path("htmx/todo/items/<int:pk>/", TodoItemView.as_view(), name="items"),
    path(
        "htmx/todo/items/<int:pk>/done/",
        TodoDoneView.as_view(),
        name="done",
    ),
    path(
        "htmx/todo/items/<int:pk>/undone/",
        TodoUndoneView.as_view(),
        name="undone",
    ),
    path("htmx/todo/items/", TodoListView.as_view(), name="items-list"),
]
