# ConfBooker
Simple application in Django to booking conference rooms.

![ConfBooker-logo](https://github.com/TheRizzy/ConfBooker/blob/main/ConfBooker/main/static/ConfBookLogo.png?raw=true)

After run server `python manage.py runserver` you can acces to this functions in view:
- home view - [http://127.0.0.1:8000/home/](http://127.0.0.1:8000/home/)
- add new room - [http://127.0.0.1:8000/room/new/](http://127.0.0.1:8000/room/new)
- show information about conference room - [http://127.0.0.1:8000/room/<int:id>/](http://127.0.0.1:8000/room/<int:id>/)
- delete conference room - [http://127.0.0.1:8000/room/delete/<int:id>/](http://127.0.0.1:8000/room/delete/<int:id>/)  
-  modify conference room - [http://127.0.0.1:8000/room/modify/<int:id>/](http://127.0.0.1:8000/room/modify/<int:id>/) 
-  reserve conference room - [http://127.0.0.1:8000/room/reserve/<int:id>/](http://127.0.0.1:8000/room/reserve/<int:id>/)  

Pleas note that `int:id` can be change to any id room in datebase - if it's not there return 404 page
***
In file `requirements.txt` you can check all packages use in the environment to run project.
