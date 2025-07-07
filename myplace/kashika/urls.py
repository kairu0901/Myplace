from django.urls import path
from .views import CsvUploadAndResultView
app_name = 'kashika'
urlpatterns = [
    path('kashika/upload/', CsvUploadAndResultView.as_view(), name='upload'),
]
