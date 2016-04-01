from django.shortcuts import render, redirect
from . models import Tweeter
from . forms import User_form, Login_form
from django.contrib.auth import login, authenticate, forms
from django.contrib import messages

# Create your views here.


def index(request):

	new_form = {'user_form' : User_form , 'login_form': Login_form}
	return render(request, 'login/index.html', new_form)

def reggy(request):
	name_ent = request.POST['name']
	username_ent = request.POST['username']
	password_ent = request.POST['password']
	password2_ent = request.POST['password2']
	existing_users = Tweeter.objects.all()
	print existing_users


	if len(name_ent) < 1 or len(username_ent) < 1 or len(password_ent) < 1 or len(password2_ent) < 1:
		messages.error(request, 'All fields must be filled out')
		return redirect('/')
	else:
		if password_ent != password2_ent:
			messages.error(request, 'Password and confirm password needs to be matching')
			return redirect('/')
		if len(existing_users) > 0:
			for i in existing_users:
				if username_ent in i.username:
					messages.error(request, 'User already exists')
					return redirect('/')
		newuser = Tweeter(name=request.POST['name'], username=request.POST['username'],password=request.POST['password'], password2=request.POST['password2'])
		newuser.save()
		try:
			request.session['this_user'] = request.POST['name']
		except:
			request.session['this_user'] = request.POST['name']
		context = {
			'this_user' :request.session['this_user'],
		}
		return render(request,'search/index.html', context)


def logging(request):
	uname = request.POST['username']
	passw = request.POST['password']
	# print uname
	# print passw
	existing_users = Tweeter.objects.all()
	# print existing_users
	if len(uname) < 1:
		messages.error(request, 'Username is blank')
		return redirect('/')
	if len(existing_users) < 1:
		messages.error(request, 'Username is not in our database')
		return redirect('/')
	else:
		for i in existing_users:
			if uname in i.username:
				if passw == i.password:
					try:
						request.session['this_user'] = i.name
					except:
						request.session['this_user'] = i.name
					context = {
						'this_user' :request.session['this_user'],
						}
					return render(request,'search/index.html', context)
				else:
					messages.error(request, 'Password is incorrect')
					return redirect('/')
		else:
			messages.error(request, 'Username not in our database')
			return redirect('/')




		# else: 
		# 	for i in existing_users:
		# 		print i
		# 		if uname in i.username:
		# 			if passw == i.password:

		# 				try:
		# 					request.session['this_user'] = i.name
		# 				except:
		# 					request.session['this_user'] = i.name
		# 				context = {
		# 					'this_user' :request.session['this_user'],
		# 					}
		# 				return render(request,'search/index.html', context)
		# 			else:
		# 				messages.error(request, 'Password is incorrect')
		# 				return redirect('/')
		# 		else:
		# 			messages.error(request, 'Username dfdsfsis not in our database')
		# 			return redirect('/')
	# return render(request, 'search/index.html')



