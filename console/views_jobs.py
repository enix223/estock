# -*- coding: utf-8 -*-

# Sys modules
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

# User define modules
from console.models import Job
from helper import render_to_json_response


# List the job in the system
@login_required
def job_list(request):
    jobs = Job.objects.all
    return render_to_json_response(jobs)


# Trigger the job with specified job_id
@login_required
def job_trigger(request, job_id):
    job = get_object_or_404(job_id)
    # Runner.run(job.name)
    return render_to_json_response(1)


@login_required
def job_force_end(request, job_id):
    job = get_object_or_404(job_id)
    # Runner.end(job.pid)
    return render_to_json_response(1)

