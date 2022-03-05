from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django_htmx.http import trigger_client_event

from .forms import AddTodoForm
from .models import Todo


def index(request):
    items = Todo.objects.all().order_by("-created_at")
    form = AddTodoForm()
    return render(request, "todo/index.html", context={"items": items, "form": form})


class TodoListView(View):
    def post(self, request):
        form = AddTodoForm(request.POST)
        if not form.is_valid():
            return render(request, "todo/add_item_form.html", context={"form": form})

        item = Todo.objects.create(description=form.cleaned_data["description"])
        response = render(
            request, "todo/add_item_form.html", context={"form": form, "item": item}
        )
        # trigger_client_event(response, "todo_item_created", {})
        return response


class TodoItemView(View):
    def delete(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        todo.delete()
        return HttpResponse("ok")


class TodoDoneView(View):
    def post(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        todo.is_done = True
        todo.save()
        return render(request, "todo/item.html", context={"item": todo})


class TodoUndoneView(View):
    def post(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        todo.is_done = False
        todo.save()
        return render(request, "todo/item.html", context={"item": todo})
