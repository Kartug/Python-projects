from django.contrib.auth import views
from accounts import views as accounts_views
from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    #     path('password-reset/', views.PasswordResetView.as_view(), name='password_reset'),
    #     path('password-reset/done/', views.PasswordResetDoneView.as_view(),
    #          name='password_reset_done'),
    #     path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(),
    #          name='password_reset_confirm'),
    #     path('reset/done/', views.PasswordResetCompleteView.as_view(),
    #          name='password_reset_complete'),
    #     path('password-change/', views.PasswordChangeView.as_view(),
    #          name='password_change'),
    #     path('password-change/done/', views.PasswordChangeDoneView.as_view(),
    #          name='password_change_done'),
    url(r'^signup/$', accounts_views.signup, name='signup'),
    url(r'^reset/$',
        auth_views.PasswordResetView.as_view(
            template_name='registration/password_reset.html'
        ),
        name='password_reset'),
    url(r'^reset/done/$',
        auth_views.PasswordResetDoneView.as_view(
            template_name='registration/password_reset_done.html'),
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='registration/password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'^reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='registration/password_reset_complete.html'),
        name='password_reset_complete'),

    url(r'^settings/password/$', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
        name='registration/password_change'),
    url(r'^settings/password/done/$', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
        name='registration/password_change_done'),
]
