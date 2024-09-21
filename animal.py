class Animal:
    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound

    def make_sound(self):
        return f"{self.name} kêu {self.sound}"

# Tạo danh sách đối tượng Animal
animal_list = [
    Animal("Hổ mang", "Bò sát", "Rít"),
    Animal("Sư tử", "Có vú", "Gầm gừ"),
    Animal("Lợn rừng", "Có vú", "Rít"),
    Animal("Lạc đà", "Có vú", "Kêu"),
    Animal("Cá sấu", "Bò sát", "Gầm"),
]

#  thứ tự ngược lại của bảng chữ cái
def sort_zoo(animal_list):
    return sorted(animal_list, key=lambda x: x.name, reverse=True)

#  tên các con vật bắt đầu bằng chữ cái "L"
def filter_zoo(animal_list, begin):
    return [animal for animal in animal_list if animal.name.startswith(begin)]

# In ra  các con vật
print("Danh sách các con vật:")
for animal in animal_list:
    print(animal.name)

# Sắp xếp tên của các con vật theo thứ tự ngược lại của bảng chữ cái
sorted_animal_list = sort_zoo(animal_list)
print("\nDanh sách các con vật sắp xếp theo thứ tự ngược lại của bảng chữ cái:")
for animal in sorted_animal_list:
    print(animal.name)

# In ra màn hình tên các con vật bắt đầu bằng chữ cái "L"
filtered_animal_list = filter_zoo(animal_list, "L")
print("\nDanh sách các con vật bắt đầu bằng chữ cái 'L':")
for animal in filtered_animal_list:
    print(animal.name)