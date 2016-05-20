from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
	username = forms.CharField(label="Nombre de usuario",widget=forms.TextInput())
	email    = forms.EmailField(label="Correo Electronico",widget=forms.TextInput())
	password_one = forms.CharField(label="Password",widget=forms.PasswordInput(render_value=False))
	password_two = forms.CharField(label="Confirmar Password",widget=forms.PasswordInput(render_value=False))

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			u = user.objects.get(username=username)
		except user.DoesNotExit:
			return username
		raise forms.ValidationError('Nombre de usuario ya existe')

	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			u = user.objects.get(email= email)
		except user.DoesNotExit:
			return email
		raise forms.ValidationError('Email ya registrado ')

	def clean_password_two(self):
		password_one = self.cleaned_data['password_one']
		password_two = self.cleaned_data['password_two']
		if password_one == password_two:
			pass
		else:
			raise forms.ValidationError('Password no coinciden')
		
		

class contact_form(forms.Form):
	correo = forms.EmailField(widget = forms.TextInput())
	titulo = forms.CharField(widget = forms.TextInput())
	texto  = forms.CharField(widget = forms.Textarea())

class Login_form(forms.Form):	
	usuario= forms.CharField(widget = forms.TextInput())
	clave  = forms.CharField(widget = forms.PasswordInput(render_value = False))
	