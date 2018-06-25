from django.shortcuts import render
from student_profile.models import Student


# Create your views here.
def student_card(request):
    context = dict()
    context["students"] = Student.objects.all()
    # print("hello")
    return render(request, "cards.html", context)
