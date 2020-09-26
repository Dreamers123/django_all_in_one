from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets.views import(
SnippetList,
SnippetDetail,
)

app_name = 'account'

urlpatterns = [

	path('snippets', SnippetList.as_view(), name="test"),
	path('snippets/<int:pk>/',SnippetDetail.as_view(),name="snippet_details")
]
urlpatterns = format_suffix_patterns(urlpatterns)