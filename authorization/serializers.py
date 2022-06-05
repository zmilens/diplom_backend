from rest_framework import serializers
from .models import Account

# class Profile(serializers.ModelSerializer):

#     class Meta:
#         model = User
#         field = ['phone, data_of_birth, user']


class RegistrationSerializer(serializers.ModelSerializer):

	password_confirm = serializers.CharField(style={'input_type': 'password'}, write_only=True)

	class Meta:
		model = Account
		fields = ['email', 'phone', 'name', 'last_name', 'password', 'password_confirm']
		extra_kwargs = {
				'password': {'write_only': True},
		}	


	def	save(self):

		account = Account(
					email=self.validated_data['email'],
					phone=self.validated_data['phone'],
                    name=self.validated_data['name'],
                    last_name=self.validated_data['last_name'],
				)
		password = self.validated_data['password']
		password2 = self.validated_data['password_confirm']
		if password != password2:
			raise serializers.ValidationError({'password': 'Пароли должны совпадать'})
		account.set_password(password)
		account.save()
		return account
