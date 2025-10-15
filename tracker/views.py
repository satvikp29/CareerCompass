from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Application

@login_required
def applications_list(request):
    apps = Application.objects.filter(owner=request.user).order_by("-created_at")
    return render(request, "tracker/applications_list.html", {"apps": apps})
from django.shortcuts import redirect
from .forms import ApplicationForm

@login_required
def add_application(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            app = form.save(commit=False)
            app.owner = request.user
            app.save()
            return redirect("applications_list")
    else:
        form = ApplicationForm()
    return render(request, "tracker/add_application.html", {"form": form})
from django.shortcuts import redirect
from .forms import ApplicationForm

@login_required
def add_application(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            app = form.save(commit=False)
            app.owner = request.user
            app.save()
            return redirect("applications_list")
    else:
        form = ApplicationForm()
    return render(request, "tracker/add_application.html", {"form": form})
from django.shortcuts import get_object_or_404

@login_required
def edit_application(request, pk):
    app = get_object_or_404(Application, pk=pk, owner=request.user)
    if request.method == "POST":
        form = ApplicationForm(request.POST, instance=app)
        if form.is_valid():
            form.save()
            return redirect("applications_list")
    else:
        form = ApplicationForm(instance=app)
    return render(request, "tracker/edit_application.html", {"form": form, "app": app})

@login_required
def delete_application(request, pk):
    app = get_object_or_404(Application, pk=pk, owner=request.user)
    if request.method == "POST":
        app.delete()
        return redirect("applications_list")
    return render(request, "tracker/delete_application.html", {"app": app})
from django.db.models import Count
from django.utils.timezone import now, timedelta

@login_required
def dashboard(request):
    apps = Application.objects.filter(owner=request.user)

    total = apps.count()
    offers = apps.filter(status="offer").count()
    rejected = apps.filter(status="rejected").count()
    interviews = apps.filter(status="interview").count()

    # Apps per status for chart
    by_status = (
        apps.values("status")
        .annotate(count=Count("status"))
        .order_by()
    )

    status_labels = [s["status"].capitalize() for s in by_status]
    status_counts = [s["count"] for s in by_status]

    return render(
        request,
        "tracker/dashboard.html",
        {
            "total": total,
            "offers": offers,
            "rejected": rejected,
            "interviews": interviews,
            "status_labels": status_labels,
            "status_counts": status_counts,
        },
    )



