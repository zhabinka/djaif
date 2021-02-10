from django.urls import path

from djaif.book import views

urlpatterns = [
    path('', views.view_books),
    path('book/<int:book_id>', views.view_book, name='book'),
    path('book/<int:book_id>/go/<int:pagelink_id>', views.go_to, name='go_to'),
    path('book/<int:book_id>/take/<int:item_id>', views.take, name='take'),
    path('book/<int:book_id>/saves', views.view_saves, name='saves'),
    path(
        'book/<int:book_id>/saves/new',
        views.save_to,
        name='save_new',
    ),
    path(
        'book/<int:book_id>/saves/save_to/<int:save_id>',
        views.save_to,
        name='save_to',
    ),
    path(
        'book/<int:book_id>/saves/load_from/<int:save_id>',
        views.load_from,
        name='load_from',
    ),
    path(
        'book/<int:book_id>/saves/delete/<int:save_id>',
        views.delete_save,
        name='delete_save',
    ),
    path('book/<int:book_id>/map.svg', views.view_book_map),
]
