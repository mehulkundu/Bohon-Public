from django.urls import path
from .views import rate_calculator_view, MySignUpView, user_home_view
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('product/rate_calculator/', rate_calculator_view, name="rate-calculator"),
    path('user/signup/', MySignUpView.as_view(), name="user-signup"),
    path('user/home/', user_home_view, name="user-home"),
    path('user/login/', LoginView.as_view(template_name="main_app/user_login_form.html"), name='user-login'),
    path('user/logout/', LogoutView.as_view(), name='user-logout'),
]

