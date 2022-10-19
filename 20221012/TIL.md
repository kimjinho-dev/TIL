# M:M

M:M관계에서 여러개의 외래키를 줄수없으므로 별도로 키 테이블을 만들어야한다.  

```python
class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.doctor.pk}번 의사의 {self.patient.pk}번 환자'
```
이러면 Doctor과 patient는 _set으로 역참조로 확인할 수 있다.  
하지만 굳이 테이블을 하나 더 만들지않고 manytomanyfield로 만들수있다.  

```python
class Patient(models.Model):
    doctors = models.ManyToManyField(Doctor)
    name = models.TextField()
    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'
```
이러면 위의 reservation처럼 M:M관계가 형성된다.  
다만 둘다 역참조가 아니라 patient에 대해선 참조, doctor에게는 역참조가 된다.  


이러한 M:M은 양쪽에서 자유롭게 서로를 참조하면서 조회, 수정 등 할수있다는 장점이 있다.
```python
## 추가
patient1.doctors.add(doctor2)     # 참조일때
doctor1.patient_set.add(patient2) # 역참조일때

## 조회
patient1.doctors.all()     # 참조일때
doctor1.patient_set.all()  # 역참조일때

## 삭제
patient1.doctors.remove(doctor2)      # 참조일때
doctor1.patient_set.remove(patient2)  # 역참조일때
```

현재 구조에서 조금 아쉬운것은 참조는 doctors로 적기좋으나, 역참조는 _set이 추가되면서 불편하다는것이다.  
따라서 이 명칭을 변경시켜준다.  
```python
class Patient(models.Model):
    doctors = models.ManyToManyField(Doctor, related_name='patients)
    name = models.TextField()
    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'
```
이렇게 변경됨에 따라서 
```python
## 추가
patient1.doctors.add(doctor2)     # 참조일때
doctor1.patients.add(patient2) # 역참조일때

## 조회
patient1.doctors.all()     # 참조일때
doctor1.patients.all()  # 역참조일때

## 삭제
patient1.doctors.remove(doctor2)      # 참조일때
doctor1.patients.remove(patient2)  # 역참조일때
```
형식으로 사용이 가능하다.

다만 이런경우에, 예약한 시간, 예약 특이사항등 별도의 테이블을 추가할 수 없다.  
따라서 기존에 사용하던 중계테이블을 다시 사용하는데, 이때 through 아규먼트를 사용하여서 이전과 사용방법은 유지하되  
원하는 대로 테이블을 추가할 수 있다.  

```python
class Patient(models.Model):
    doctors = models.ManyToManyField(Doctor, related_name='patients', through='Reservation')   # throough 아규먼트 추가
    name = models.TextField()
    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'

class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)      # 여전히 외래키는 필요. 여기선 manytomany필드에서 만들어질 외래키를
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)    # 대신한다는 생각으로 하면된다.
    symptom = models.TextField()                                      # 추가 테이블
    reserved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.doctor.pk}번 의사의 {self.patient.pk}번 환자'
```

추가 테이블에 데이터를 넣는 방법
```python
## 추가
patient1.doctors.add(doctor2, through_defaults={'symptom': 'flu'})     # 참조일때
doctor1.patients.add(patient2, through_defaults={'symptom': 'sol'}) # 역참조일때
```

이전에 쓰던 foreignkey, manytomonyfiled를 같이 사용하다보면 오류가 발생할 수 있다.
```python
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    list_users = models.ManyToManyField(settings.AUTH_USER_MODEL)
```

이는 역참조를 위해 user때 만든 article_set과 list_users때 만들어지는 article_set이 중복되어  
구분할 수 없어 발생하는 오류이다. 이를 해결하기 위해 relted_name을 적어도 하나는 설정해야한다.

```python
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    list_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
```

이제 이 모델에는 총 4개의 related manager가 존재한다
(1) article.user        : 참조
(2) user.article_set    : 역참조
(3) article.list_users  : 참조
(4) user.like_articles  : related_name 으로인해 변경된 역참조

