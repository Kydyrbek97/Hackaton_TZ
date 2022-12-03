from views import CreateMixin, ListingMixin, DetailMixin, UpdateMixin, DeleteMixin

class Cars(CreateMixin, ListingMixin, DetailMixin, UpdateMixin, DeleteMixin):

    def save(self):
       import json
       with open ('data.json', 'w') as file:
          json.dump(self.objects, file)
       return 'Saved!'


cars = Cars()
print('----------------------------------CREATE------------------------------------------------------')
print(cars.post(marka = 'BMW', model = 'X5', god_vypuska=2013, obyem_dvigatelya=2.3, 
svet = 'Black', tip_kuzova= 'Hatchbak', probeg='1000 km',  sena='22000$'))
# print()
# print('----------------------------------LIST--------------------------------------------------------')
# print(cars.list())
# print()
# print('----------------------------------DETAIL------------------------------------------------------')
# print(cars.detail(1))
# print()
# print('----------------------------------UPDATE------------------------------------------------------')
# print(cars.update(1, model = 'X7'))
# print()
# print('----------------------------------DELETE------------------------------------------------------')
# print(cars.delete(1))
# print()
# print('----------------------------------SAVE--------------------------------------------------------')
# print(cars.save())


