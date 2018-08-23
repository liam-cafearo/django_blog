from django.conf.urls import url
import views

urlpatterns = [
    url(r'^blog/$', views.post_list),
    url(r'^blog/(?P<id>\d+)/$', views.post_detail),
    # Blog part 4 Challenge - Add URL Mapping - Taken
    # from solution as didn't understand the challenge
    # initially
    url(r'^blog/top', views.top_posts),
]
