from django.shortcuts import render, redirect
from .models import TodoList
from .forms import TodoListForm


def home(request):

    if request.method == "POST":
        form = TodoListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home-page")
    else:
        form = TodoListForm()
        todo_list = TodoList.objects.all()
        content = {
            "todo_list": todo_list,
            "form": form,
        }
        return render(request, "todo/index.html", content)


def deleteItem(request, pk):
    try:
        todo_item = TodoList.objects.get(pk=pk)
    except:
        print("not valid")
    todo_item.delete()
    return redirect("home-page")