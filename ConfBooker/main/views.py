from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse
from main.models import ConferenceRoom, ReserveRoom
from django.db import IntegrityError
import datetime


# Create your views here.


class MainPage(View):
    @staticmethod
    def get(request):
        rooms = ConferenceRoom.objects.all()
        reserves = ReserveRoom.objects.all()
        today = datetime.date.today()
        return render(request, 'main-page.html', context={"rooms": rooms, "reserves": reserves, "today": today})


class NewRoomView(View):

    @staticmethod
    def get(request):
        return render(request, 'add-new-room.html')

    @staticmethod
    def post(request):
        new_name_room = request.POST.get('new_room_name')
        exist_room = ConferenceRoom.objects.filter(name_room=new_name_room).exists()
        capacity_room = int(request.POST.get('capacity_room'))
        projector_ability = request.POST.get('projector_ability') == 'on'

        if not exist_room and capacity_room > 0:
            ConferenceRoom.objects.create(name_room=new_name_room, capacity_room=capacity_room,
                                         projector_available=projector_ability)

        return render(request, 'add-new-room.html', context={'new_room_name': new_name_room,
                                                             'capacity_room': capacity_room,
                                                             'projector_ability': projector_ability,
                                                             'exist_room': exist_room}
                      )


class RoomView(View):

    @staticmethod
    def get(request, id):
        room = get_object_or_404(ConferenceRoom, id=id)
        reservation = ReserveRoom.objects.filter(id_room_id=id).order_by('date_reservation')
        return render(request, 'room-view.html', context={'room': room, 'reservation': reservation})


class DeleteRoomView(View):

    @staticmethod
    def get(request, id):
        room = get_object_or_404(ConferenceRoom, id=id)
        room.delete()
        return render(request, 'delete-room-view.html', context={'id': id})


class ModifyRoomView(View):

    @staticmethod
    def get(request, id):
        room = get_object_or_404(ConferenceRoom, id=id)
        return render(request, 'modify-room-view.html', context={'room': room})

    @staticmethod
    def post(request, id):
        room = get_object_or_404(ConferenceRoom, id=id)
        modify_room_name = request.POST.get('modify_room_name')
        exist_modify_room_name = ConferenceRoom.objects.filter(name_room=modify_room_name).exists()  # True or False
        modify_capacity_room = int(request.POST.get('modify_capacity_room'))
        projector_ability = request.POST.get('projector_ability') == 'on'  # True or False

        if not exist_modify_room_name and modify_capacity_room > 0 and modify_room_name != '':
            room.name_room = modify_room_name
            room.capacity_room = modify_capacity_room
            room.projector_available = projector_ability
            room.save()

        return render(request, 'modify-room-view.html', context={'modify_room_name': modify_room_name,
                                                                 'modify_capacity_room': modify_capacity_room,
                                                                 'projector_ability': projector_ability,
                                                                 'exist_modify_room_name': exist_modify_room_name,
                                                                 'room': room},
                      )


class ReserveView(View):

    @staticmethod
    def get(request, id):
        room = get_object_or_404(ConferenceRoom, id=id)
        return render(request, 'reserve-view.html', context={'room': room})

    @staticmethod
    def post(request, id):
        room = get_object_or_404(ConferenceRoom, id=id)
        comment = request.POST.get('comment_reservation')
        date = request.POST.get('date_reservation')

        # jeżeli istnieje rekord z rezerwacja to znaczy że sala jest zarezerwowana
        if ReserveRoom.objects.filter(date_reservation=date, id_room_id=room.id):
            return render(request, 'reserve-view.html', context={'room': room, 'error': "Room is booked on this day -"
                                                                                        " Chose another!"})

        if date < str(datetime.date.today()):
            return render(request, 'reserve-view.html', context={'room': room, 'error': "Date CAN NOT be from the past!"})

        ReserveRoom.objects.create(date_reservation=date, comment_reservation=comment, id_room_id=room.id)

        return render(request, 'reserve-view.html', context={'room': room, 'massage': "Reservation crate successful!"})
