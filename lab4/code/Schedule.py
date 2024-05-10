from typing import List
from Train import Train
from Station import Station


class Schedule:
    def __init__(self):
        self.stations: List[Station] = []
        self.trains: List[Train] = []

    def add_station(self, station: Station) -> None:
        self.stations.append(station)

    def remove_station(self, station: Station) -> None:
        self.stations.remove(station)

    def add_train(self, train: Train):
        self.trains.append(train)

    def remove_train(self, train: Train):
        self.trains.remove(train)

    def move_train(self) -> None:
        print("Available trains:")
        for i, train in enumerate(self.trains, 1):
            print(f"{i}. Train {train.number} --> {train.station.station_name}")

        train_choice = input("Choose a train by entering its number: ")
        try:
            train_index = int(train_choice) - 1
            chosen_train = self.trains[train_index]
        except (ValueError, IndexError):
            print("Invalid choice. Please enter a valid train number.")
            return

        print(f"You have chosen train: {chosen_train.number}")
        current_station_index: int = -1
        for index, station in enumerate(self.stations):
            if station == chosen_train.station:
                current_station_index = index
                break

        if current_station_index == -1:
            print("Train is not scheduled to stop at any station.")
            return
        chosen_train.load_passenger(chosen_train.station.platform.persons)
        next_station_index: int = (current_station_index + 1) % len(self.stations)
        next_station: Station = self.stations[next_station_index]
        chosen_train.station = next_station
        chosen_train.unload_passenger()
        print(f"Train {chosen_train.number} moved to {next_station.station_name}.")

        if chosen_train.station.station_name == Station.StationName.STATION_SERVICE.value:
            chosen_train.transportation_services()
