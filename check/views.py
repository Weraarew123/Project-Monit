from django.shortcuts import redirect, render
from django.http import HttpResponse
from .tasks import add
from django_celery_beat.models import PeriodicTask, IntervalSchedule

def schedulePage(request):
    add.delay()
    return HttpResponse("TASK COMPLETE")


def schedule_task(request):
    interval, _ = IntervalSchedule.objects.get_or_create(
        every=60,
        period=IntervalSchedule.SECONDS,
    )
    
    PeriodicTask.objects.create(
        interval=interval,
        name="my-schedule",
        task="check.tasks.my_task",
    )
    
    return HttpResponse("Task Complete")

def homePage(request):
    return render(request, "check/home.html")
