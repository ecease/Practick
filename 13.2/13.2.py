#Кондратюк Егор 3ИСд-1.22
#Практическая 13 вариант 8
#8 Дан файл, содержащий сведения о безработных: специальность, опыт работы, образование, пол, возраст. Требуется:
#а) подобрать кандидатов на должность врача с опытом работы не менее пяти лет;
#б) найти работников с высшим экономическим образованием не старше 35 лет;
#в) найти работников, имеющих опыт профессиональной деятельности в сфере торговли;
#г) получить полную информацию обо всех женщинах в возрасте от 20 до 40 лет;
#д) определить средний возраст всех мужчин, ищущих в данныймомент работу;
#е) выяснить, кого в базе данных больше с высшим образованием: женщин или мужчин;
#ж) найти л самых молодых работников.





def read_data(filename):
    records = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            specialty, experience, education, gender, age = line.split(',')
            record = {
                'specialty': specialty.strip(),
                'experience': int(experience.strip()),
                'education': education.strip(),
                'gender': gender.strip(),
                'age': int(age.strip())
            }
            records.append(record)
    return records

def main():
    data = read_data('data.txt')
    
    
    doctors_with_experience = [
        person for person in data
        if person['specialty'].lower() == 'врач'
        and person['experience'] >= 5
    ]
    
    
    econ_younger_35 = [
        person for person in data
        if person['education'].lower() == 'экономическое'
        and person['age'] <= 35
    ]
    
    
    trade_workers = [
        person for person in data
        if 'торгов' in person['specialty'].lower() or 'торгов' in person['education'].lower()
    ]
    
    
    women_20_40 = [
        person for person in data
        if person['gender'].lower() == 'женщина'
        and 20 <= person['age'] <= 40
    ]
    
   
    men = [person for person in data if person['gender'].lower() == 'мужчина']
    if len(men) > 0:
        avg_age_men = sum(p['age'] for p in men) / len(men)
    else:
        avg_age_men = 0
    
    
    possible_higher_educations = ['экономическое', 'медицинское']
    
    women_with_higher = [
        p for p in data
        if p['gender'].lower() == 'женщина'
        and p['education'].lower() in possible_higher_educations
    ]
    men_with_higher = [
        p for p in data
        if p['gender'].lower() == 'мужчина'
        and p['education'].lower() in possible_higher_educations
    ]
    
    more_higher_education = 'женщины'
    if len(men_with_higher) > len(women_with_higher):
        more_higher_education = 'мужчины'
    
    
    if len(data) > 0:
        min_age = min(p['age'] for p in data)
        youngest = [p for p in data if p['age'] == min_age]
    else:
        youngest = []
    
   
    
    print("a) Врачи с опытом >= 5 лет:")
    for person in doctors_with_experience:
        print(f"{person['specialty']}, {person['experience']} лет опыта, {person['education']}, {person['gender']}, {person['age']} лет")
    print()
    
    
    print("b) Экономическое образование, не старше 35:")
    for person in econ_younger_35:
        print(f"{person['specialty']}, {person['experience']} лет опыта, {person['education']}, {person['gender']}, {person['age']} лет")
    print()
    
    
    print("c) Работники в сфере торговли:")
    for person in trade_workers:
        print(f"{person['specialty']}, {person['experience']} лет опыта, {person['education']}, {person['gender']}, {person['age']} лет")
    print()
    
   
    print("d) Все женщины 20-40 лет:")
    for person in women_20_40:
        print(f"{person['specialty']}, {person['experience']} лет опыта, {person['education']}, {person['gender']}, {person['age']} лет")
    print()
    
    
    print(f"e) Средний возраст мужчин: {avg_age_men:.2f}")
    print()
    
    
    print(f"f) Больше всего людей с высшим (по нашему определению) образованием у: {more_higher_education}")
    print()
    
    
    print("g) Самые молодые работники:")
    for person in youngest:
        print(f"{person['specialty']}, {person['experience']} лет опыта, {person['education']}, {person['gender']}, {person['age']} лет")


main()
