class Profile :
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def __str__(self):
        return "{}은(는) {}세이고, {}입니다.".format(self.name, self.age, self.gender)

짱구 = Profile("짱구", 5, "남자")
도라에몽 = Profile("도라에몽", 14, "남자")
코난 = Profile("코난", 8, "남자")
쇼콜라 = Profile("쇼콜라", 15, "여자")
아무 = Profile("아무", 12, "여자")
가영 = Profile("가영", 16, "여자")

print(짱구)
print(도라에몽)
print(코난)
print(쇼콜라)
print(아무)
print(가영)
