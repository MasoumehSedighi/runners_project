########################################################## Class Definition
class Runners:
    def __init__(self, id, name, distance, duration):
        self.id = id
        self.name = name
        self.distance = distance
        self.duration = duration
        self.get_category()

    ############################## Get Just Name
    def get_name(self):
        return self.name

    ############################## Get Just Distance
    def get_distance(self):
        return self.distance

    ############################## If Distance, Changed
    def set_distance(self, d):
        self.distance = d
        self.get_category()

    ############################## Calculate Speeds
    def calculate_speed(self):
        speed = self.distance / self.duration / 60
        return speed

    ############################## Calculated Paces
    def calculate_pace(self):
        pace = self.duration / self.distance
        return pace

    ############################## Classification:
    def get_category(self):
        x = self.distance
        self.category = (
            "not finisher"
            if x < 10
            else "10k"
            if 10 <= x <= 20
            else "half marathon"
            if 21 <= x <= 41
            else "marathon"
            if 42 <= x <= 60
            else "ultra"
        )
        return self.category


####################################################################################### Sample
samples = [{'id': 0, 'name': 'Kilian Jornet', 'distance': 46, 'duration': 283},
           {'id': 1, 'name': 'Akbar Naghdi', 'distance': 120, 'duration': 720},
           {'id': 2, 'name': 'Negar sammak Nejad', 'distance': 171, 'duration': 2760},
           {'id': 3, 'name': 'Mandana Nouri', 'distance': 21.0975, 'duration': 118},
           {'id': 4, 'name': 'Eliud Kipchoge ', 'distance': 42.195, 'duration': 119},
           {'id': 5, 'name': 'Julius PASKOV', 'distance': 86.3, 'duration': 870},
           {'id': 6, 'name': 'Anabela RENDA', 'distance': 25.7, 'duration': 195},
           {'id': 7, 'name': 'Alexis SEVENNEC', 'distance': 24.1, 'duration': 140},
           {'id': 8, 'name': 'Joyciline Jepkosgei', 'distance': 10, 'duration': 28},
           {'id': 9, 'name': 'Rhonex Kipruto', 'distance': 10, 'duration': 26},
           {'id': 10, 'name': 'Vincent Kibet', 'distance': 10, 'duration': 27},
           {'id': 11, 'name': 'Senbere Teferi', 'distance': 10, 'duration': 30.2},
           {'id': 12, 'name': 'Payam Dibaj', 'distance': 30, 'duration': 152},
           {'id': 13, 'name': 'Sepideh Nouri', 'distance': 27, 'duration': 142},
           {'id': 14, 'name': 'Mohammad Jafar Moradi', 'distance': 42.195, 'duration': 137}]

################################################################################ Main:
runners_list = []
runners_name = []
ultra = []
non_finisher = []
ten_ka = []
marathon = []
half_marathon = []

######################################## Object Definition And Classifications:
for sample in samples:
    name = sample['name']
    id = sample['id']
    distance = sample['distance']
    duration = sample['duration']
    r = Runners(id, name, distance, duration)
    runners_list.append(r)
    runners_name.append(r.name)
    if r.get_category() == 'ultra':
        ultra.append(r)
    elif r.get_category() == "not finisher":
        non_finisher.append(r)
    elif r.get_category() == "10k":
        ten_ka.append(r)
    elif r.get_category() == "marathon":
        marathon.append(r)
    else:
        half_marathon.append(r)

######################################## 1.1.1: List All Runners
print(runners_name)
sorted_runners_name = sorted(runners_name)
######################################## 1.1.2: List All Runner Sorted By Alphabet
print(sorted_runners_name)

# Sorting based on runners speed
sorted_runners_speed = sorted(runners_list, key=lambda x: x.calculate_speed(), reverse=True)
# Sorting based on runners distance
sorted_runners_distance = sorted(runners_list, key=lambda x: x.get_distance(), reverse=True)
first_three_in_speed = sorted_runners_speed[:3]

######################################## 1.1.3: List Of Top Three Runners Based On Speed:
rank = 0
for r in first_three_in_speed:
    rank = rank + 1
    print(f'rank {rank} : {r.get_name()} with speed {r.calculate_speed():3.4f} in category {r.get_category()}')
    #################################### 1.1.6: The Fastest Runner:
    if rank == 1:
        print(f'fastest runner in the whole race is {r.get_name()}')

######################################## 1.1.5: The Best Runner in Each Category Based On Speed:
if len(non_finisher) > 0:
    sorted_runners_speed1 = sorted(non_finisher, key=lambda x: x.calculate_speed(), reverse=True)
    fastest_not_finisher = sorted_runners_speed1[0]
    print(f'fastest runner in not finisher category is {fastest_not_finisher.get_name()}')

sorted_runners_speed2 = sorted(ten_ka, key=lambda x: x.calculate_speed(), reverse=True)
fastest_10k = sorted_runners_speed2[0]
print(f'fastest runner in 10K category is {fastest_10k.get_name()}')

sorted_runners_speed3 = sorted(half_marathon, key=lambda x: x.calculate_speed(), reverse=True)
fastest_half_marathon = sorted_runners_speed3[0]
print(f'fastest runner in half marathon category is {fastest_half_marathon.get_name()}')

sorted_runners_speed4 = sorted(marathon, key=lambda x: x.calculate_speed(), reverse=True)
fastest_marathon = sorted_runners_speed4[0]
print(f'fastest runner in marathon category is {fastest_marathon.get_name()}')

sorted_runners_speed5 = sorted(ultra, key=lambda x: x.calculate_speed(), reverse=True)
fastest_ultra = sorted_runners_speed5[0]
print(f'fastest runner in ultra category is {fastest_ultra.get_name()}')

######################################## 1.1.7: The Runner Who has traveled the most distance:
high_distance = sorted_runners_distance[0]
print(f'runners with highest distance is : {high_distance.get_name()}')
