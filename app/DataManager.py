import json

from glob import glob
from app.Models.Room import Room


class DataManager:
    data_location = './data/'
    rooms = {}

    @staticmethod
    def load_data():
        print("INFO: loading all the data files.")
        DataManager.load_rooms()

    @staticmethod
    def save_data(self):
        print("INFO: saving all the data.")

    @staticmethod
    def load_rooms():
        room_files_location = DataManager.data_location + 'rooms/*'
        room_files = glob(room_files_location)
        print("INFO: found %d rooms to load in folder '%s'." % (len(room_files), room_files_location))

        for room_file in room_files:
            with open(room_file) as room_handler:
                room_json = json.load(room_handler)

                room_object = Room(**room_json)
                DataManager.rooms[room_json['id']] = room_object
        print()
