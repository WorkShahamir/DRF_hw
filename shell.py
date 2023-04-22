from app.models import *

c1 = Category.objects.create(name='Food')
c2 = Category.objects.create(name='Washer')

Product.objects.create(name='Bread', price=20, category=c1)
Product.objects.create(name='Water', price=45, category=c1)
Product.objects.create(name='Mylomoyka', price=150, category=c2)
Product.objects.create(name='Poroshok', price=320, category=c2)
Product.objects.create(name='Shampun', price=500, category=c2)