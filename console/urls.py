from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r'^signin/', 'console.views_users.signin',  name='signin'),
    url(r'^signout/', 'console.views_users.signout',  name='signout'),
    url(r'^home/', 'console.views_users.home',  name='home'),

    # Job
    url(r'^jobs/list', 'console.views_jobs.job_list', name='job-list'),
    url(r'^jobs/trigger', 'console.views_jobs.job_trigger', name='job-trigger'),
    url(r'^jobs/end', 'console.views_jobs.job_force_end', name='job-list'),

    # New stock app
    url(r'^newstock/combine', 'console.views_newstock.combine', name='newstock-combine'),
    url(r'^newstock/list', 'console.views_newstock.list', name='newstock-list'),
)
