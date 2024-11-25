from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from user_auth.views import register, user_list, login_root_redirect
from . import views as root_view
from create_form import views as create_form_view
from answers import views as answer_view
from results import views as result_view

urlpatterns = [
    path('', root_view.index, name='home'),
    path('index', root_view.index, name='index'),
    path('admin/', admin.site.urls),
    path('results/', root_view.results, name='home'),
    path('', login_root_redirect, name='root_redirect'),
    path('login/', auth_views.LoginView.as_view(template_name='easy_survey/login.html'), name='login'),
    path('logout', root_view.logout_view, name="logout"),
    path('signup/', register, name='signup' ),
    path('userlist/', user_list, name='user_list'),
    path('create', create_form_view.create_form, name="create_form"),
    path('create/contact', create_form_view.contact_form_template, name="contact_form_template"),
    path('create/feedback', create_form_view.customer_feedback_template, name="customer_feedback_template"),
    path('create/event', create_form_view.event_registration_template, name="event_registration_template"),
    path('<str:code>/edit', create_form_view.edit_form, name="edit_form"),
    path('<str:code>/edit_title', create_form_view.edit_title, name="edit_title"),
    path('<str:code>/edit_description', create_form_view.edit_description, name="edit_description"),
    # path('<str:code>/edit_background_color', create_form_view.edit_bg_color, name="edit_background_color"),
    # path('<str:code>/edit_text_color', create_form_view.edit_text_color, name="edit_text_color"),
    path('<str:code>/add_cooperator', create_form_view.add_cooperator, name='add_cooperator'),
    path('<str:code>/edit_setting', create_form_view.edit_setting, name="edit_setting"),
    path('<str:code>/export_csv', create_form_view.exportcsv,name='export_csv'), 
    path('<str:code>/delete', create_form_view.delete_form, name="delete_form"),
    path('<str:code>/edit_question', create_form_view.edit_question, name="edit_question"),
    path('<str:code>/edit_choice', create_form_view.edit_choice, name="edit_choice"),
    path('<str:code>/add_choice', create_form_view.add_choice, name="add_choice"),
    path('<str:code>/remove_choice', create_form_view.remove_choice, name="remove_choice"),
    path('<str:code>/get_choice/<str:question>', create_form_view.get_choice, name="get_choice"),
    path('<str:code>/add_question', create_form_view.add_question, name="add_question"),
    path('<str:code>/delete_question/<str:question>', create_form_view.delete_question, name="delete_question"),
    path('<str:code>/score', create_form_view.score, name="score"),
    path('<str:code>/edit_score', create_form_view.edit_score, name="edit_score"),
    path('<str:code>/answer_key', answer_view.answer_key, name="answer_key"),
    path('<str:code>/feedback', create_form_view.feedback, name="feedback"),
    path('<str:code>/viewform', create_form_view.view_form, name="view_form"),
    path('<str:code>/submit', create_form_view.submit_form, name="submit_form"),
    path('<str:code>/responses', result_view.responses, name='responses'),
    path('<str:code>/response/<str:response_code>', answer_view.response, name="response"),
    path('<str:code>/response/<str:response_code>/edit', create_form_view.edit_response, name="edit_response"),
    path('<str:code>/responses/delete', create_form_view.delete_responses, name="delete_responses"),
    path('403', result_view.FourZeroThree, name="403"),
    path('404', result_view.FourZeroFour, name="404")
]
