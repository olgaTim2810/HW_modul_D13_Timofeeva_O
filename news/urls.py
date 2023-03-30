from django.urls import path
# Импортируем созданное нами представление
from .views import PostList, PostDetail, PostSearch, PostCreate, PostUpdate, PostDelete, CategoryListView, subscribe
from .views import IndexView
#from django.views.decorators.cache import cache_page


urlpatterns = [

   path('', PostList.as_view(), name='post_list'),
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('<int:pk>/', PostDetail.as_view()),
   path('search/', PostList.as_view(), name='post_list'),

   path('<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
   path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),
   path('index/', IndexView.as_view()),  #D7
#D8
  # path('<int:pk>/', cache_page(15)(PostCreate.as_view()), name='post_create'), # добавим кэширование на создание новости. Раз в 10 минут новость будет записываться в кэш для экономии ресурсов.
]