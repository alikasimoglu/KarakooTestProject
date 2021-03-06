from django.contrib import admin
from django.urls import path, include
from config import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    # MAIN URLS
    path('controlme/', admin.site.urls),
    path('', include('mainsite.urls')),
    path('accounts/', include('accounts.urls')),

    # Reset password urls
    path('accounts/password-reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html',
                                                                email_template_name='accounts/password_reset_email.html',
                                                                subject_template_name='accounts/password_reset_subject.txt'), name='password_reset'),
    path('accounts/password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('accounts/password-reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('accounts/password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),

    # ADDITIONAL URLS
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
