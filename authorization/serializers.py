from rest_framework import serializers
from .models import Account
from django.contrib.auth.models import Group
from shop.models import Shop

class RegistrationSerializer(serializers.ModelSerializer):

	password_confirm = serializers.CharField(style={'input_type': 'password'}, write_only=True)

	class Meta:
		model = Account
		fields = ['email', 'phone', 'name', 'last_name', 'password', 'password_confirm', 'group']
		extra_kwargs = {
				'password': {'write_only': True},
		}	


	def	save(self):
		
		account = Account(
					email=self.validated_data['email'],
					phone=self.validated_data['phone'],
                    name=self.validated_data['name'],
                    last_name=self.validated_data['last_name'],
					group = self.validated_data['group'],
				)
		
		password = self.validated_data['password']
		password2 = self.validated_data['password_confirm']
		if password != password2:
			raise serializers.ValidationError({'password': 'Пароли должны совпадать'})
		account.set_password(password)
		group = self.validated_data['group']

		
		account.save()
		if group == ('customer'):
			account.groups.add(Group.objects.get(name='customer'))
		elif group == ('operator'):
			account.groups.add(Group.objects.get(name='operator'))
		elif group == ('shop owner'):
			account.groups.add(Group.objects.get(name='shop owner'))
		# 	shop = Shop(
		# 		title='ggg',
		# 		city='mkk',
        #         address='jjnjk',
        #         owner_id=account.id,
		# 	)
		# print(shop.owner_id)
		return account

class AccountSerializer(serializers.ModelSerializer):
	
		
	class Meta:
		model = Account
		fields = ['id', 'email', 'phone', 'name', 'last_name', 'profile_image', 'date_of_birth', 'group']
	
	

		

# class RegistrationShopSerializer(serializers.ModelSerializer):

# 	class Meta:
# 		model = Shop
# 		fields = ['title', 'city', 'address', 'owner_id']
# 	def	save(self, account):
		
# 		shop = Shop(
# 					title=self.validated_data['title'],
# 					city=self.validated_data['city'],
#                     address=self.validated_data['address'],
#                     owner_id=account.id
# 				)
# 		return shop

			