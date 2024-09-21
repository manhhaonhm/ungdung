# Code mẫu
class AnimeItem:
  def __init__(self, anime_id, title, release_date, image=None, rating=None, link=None):
    self.id = anime_id
    self.title = title
    self.release_date = release_date
    self.image = image
    self.rating = float(rating) if rating else 0
    self.link = link

  def update(self, new_data:dict):
  # Thuộc tính nào trống sẽ không cập nhật
    for attribute, value in new_data.items():
      if value:
        setattr(self, attribute, value)


anime1 = AnimeItem(1, "Jujutsu no Kaisen", "01/01/2022")
anime2 = AnimeItem(2, "Kimetsu no Yaiba", "01/05/2022")
anime3 = AnimeItem(3, "Attack on Titan", "05/05/2019")
new_data={"title":"Attack on Titan part 2", "release_date":"01/05/2024"}
anime3.update(new_data)
animes = [anime1, anime2, anime3]

for k in animes:
  print(k.id)
  print(k.title)
  print(k.release_date)
  print("\n")

#k=['doraemon', 'conan','thon tinh vệ thông', 'thanh gươm diệt quỷ']
#print(k[0:])