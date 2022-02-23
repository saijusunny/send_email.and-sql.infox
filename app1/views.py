from django.conf import settings
from django.shortcuts import render, redirect
from app1.form import studentforms
from django.core.mail import send_mail



def stdform(request):
    form=studentforms()
    if request.method == 'POST': 
        form=studentforms(request.POST) #save table data to form from form.py
        if form.is_valid():  #used to mverify entered value is valid
            form.save()
            subject='Lerning softwere' #subject
            message='Dear Candidate,\n We are pleased to offer you an internsip' #messege
            recipient=form.cleaned_data.get('email')
            send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
            return redirect('/')
    return render(request, 'index.html', {'form':form})