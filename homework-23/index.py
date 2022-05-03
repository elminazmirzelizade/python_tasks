#1. `ferma = ['at', 'qoyun', 'inek', 'at', 'inek', 'qoyun', 'at', 'at', 'keci']` şəklində fermaya sahib bir fermer bizdən bəzi köməkliklər istəyir. Fermerə kömək etmək üçün aşağıdakı tapşırıqları yerinə yetirin.
ferma = ['at', 'qoyun', 'inek', 'at', 'inek', 'qoyun', 'at', 'at', 'keci']
# a. Fermada keçinin sırasını tapın
print(ferma.index('keci'))
# b. Fermadakı heyvanları ad sırasına görə sıralayın
ferma.sort()
print(ferma)
# c. Fermadan bir at çıxarıb, ən sağdan bir toyuq əlavə edin
ferma.remove('at')
ferma.append('toyuq')
print(ferma)
# d. Ən soldan bir keci əlavə edin
ferma.insert(0,'keci')
print(ferma)
# e. Fermanın yarısını dinamik bir şəkildə silin
ferma[0:int(len(ferma)) // 2] = []
print(ferma)
# f. Yeni gələn ['at', 'qoyun', 'inek', 'inek', 'qoyun'] heyvanları fermaya əlavə edin
ferma.extend(['at', 'qoyun', 'inek', 'inek', 'qoyun'])
print(ferma)
# g. Fermadakı heyvanları 3 qatına çıxarın
print(ferma*3)
# h. Fermadakı heyvanları tərsinə sıralayın
ferma[::-1]
print(ferma)
# i. Fermadakı ineklerin sayının ümumi fermanın neçə faizi olduğunu tapın
print(int((ferma.count('inek')/len(ferma))*100))
# j. Oxşar fermadan istəyən basqa bir fermerə fermamızın kopyasını verini
fermaCopy=ferma.copy()
print(fermaCopy)
# k. Fermada təmir işi getməlidi, heyvanları çölə çıxarmaq üçün fermanı təmizləyin 
ferma.clear()
print(ferma)

#2.  Aşağıdakı `result` listinin 0-cı indexinə `numbers` listi daxilindəki müsbət ədədlərin cəmini, 1-ci indexə isə mənfi ədədlərin cəmini yerləşdirin.
# Alacağınız cavab `[154.2, -71.84]` olmalıdır
# result = [0, 0]
# numbers = [10.2, -32, -5.45, 32, 7, 43, -24.06, -4, -6.33, 62]

numbers = [10.2, -32, -5.45, 32, 7, 43, -24.06, -4, -6.33, 62]
result=[]
positive=sum([p for p in numbers if p > 0],0)
negative=sum([n for n in numbers if n < 0],0)
result.insert(0,positive)
result.insert(1,negative)
print(result)

#3 İstifadəçinin girdiyi ədədi tək ədədlərdən ibarət tərsinə çevirilmiş list şəklinə salın. Listin bütün elementlərinin integer olmasına diqqət edin. Örnək:
# input: 834255
# output: [5, 5, 2, 4, 3, 8]
eded=input('eded:')
result=[]
for x in reversed(eded):
    result.append(int(x))
print(result)

#4 numbers = [10.2, -32, -5.45, 32, 7, 43, -24.06, -4, -6.33, 62] list içərisindəki ən böyük və ən kiçik ədədi dinamik şəkildə tapın.
numbers = [10.2, -32, -5.45, 32, 7, 43, -24.06, -4, -6.33, 62] 
numbers.sort()
print(numbers[0],",",numbers[len(numbers)-1])


#5 Aşağıda tələbələrin semestr nəticələri qeyd edilmişdir. Buna əsasən qeyd olunmuş statistik məlumatları eyni anda print edin.
    # a. Tələbə sayı
    # b. Ümumi ortalama.
    # c. Kəsilən tələbələrin ümumi faizi (51- qiymət alanlar)
    # d. Yüksək nəticə göstərən tələbələrin ümumu faizi (80+ qiytət alanlar)

r=[31, 38, 69, 83, 83, 56, 38, 41, 96, 48, 43, 60, 49, 47, 73, 60, 69, 96, 50, 74]
print(len(r), (sum(r,0)/len(r)), int(len([k for k in r if k<51])/len(r)*100), int(len([k for k in r if k>80])/len(r)*100))