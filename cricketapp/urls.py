from .views import get_player_count,get_player_name,get_player_right,get_player_capcon,get_players_age,get_emp_range,get_emp_up,get_emp_op
# from .views import get_emp_range,get_emp_female,get_emp_dept,get_age, get_exp,get_desig

from django.urls import path 
urlpatterns = [
       path('cricket/',get_player_count),

       path('name/',get_player_name),
       path('side/',get_player_right),
       path('cc/',get_player_capcon),
       path('age/',get_players_age),
       path('range/',get_emp_range),
       path('up/',get_emp_up),
       path('desig/',get_emp_op),


 ]