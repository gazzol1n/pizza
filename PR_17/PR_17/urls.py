from django.urls import path
from PR_17_APP import views

urlpatterns = [
    path('', views.form_up_pdf, name='form_up_pdf'),
    path('form_up_pdf/delete_pdf/<int:id>/', views.delete_pdf, name='delete_pdf'),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

