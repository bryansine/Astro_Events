import hashlib
from .models import Event
from django.template import loader
from profiles.models import Profile
from django.http import HttpResponse
from django.core.mail import send_mail
from .forms import EventCreationForm, EventEditForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def homeView(request):
    profile = Profile.objects.get(user=request.user)
    form    = EventCreationForm(request.POST or None, request.FILES or None)
    events  = Event.objects.all()
    if request.method == 'POST':
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = profile  
            event.ksh = float(event.price) * 133.50
            event.save()
            event.attendees.add(profile)  

            # Set a flag in the session to indicate a successful event creation
            request.session['eventCreated'] = True

    template = loader.get_template('events/home.html') # load template
    context  = {
        "profile": profile,
        'form'   : form,
        'events' : events,
    }
    return HttpResponse(template.render(context, request))


@login_required
def eventDetailView(request, id):
    profile = Profile.objects.get(user=request.user)
    event   = Event.objects.get(pk=id)

    profileEmail   = profile.email 
    profileName    = profile
    senderEmail    = "bryansine1738@gmail.com" #sender email
    eventName      = event.title
    eventLocation  = event.venue
    uuid           = generateUUID(profileEmail)
    profileSubject = f'Your tickets for : {eventName} {eventLocation}'

    if request.method == 'POST':
        if profile not in event.attendees.all():
            sendUUID(profileSubject, profileName, senderEmail, profileEmail, uuid, event)
            event.attendees.add(profile)
            request.session['eventBooked'] = True

    template = loader.get_template('events/eventDetail.html')
    context = {
        'event'  : event,
        'profile': profile,
        'uuid'   : uuid,  
    }
    return HttpResponse(template.render(context, request))

def generateUUID(email):
    hashObject = hashlib.sha1(email.encode())
    hexDigit = hashObject.hexdigest()
    uuid = '-'.join([hexDigit[:3], hexDigit[3:6], hexDigit[6:9]])
    return uuid

def sendUUID(eventName, profileName, senderEmail, receiverEmail, uuid, eventData):
    subject = f"🎉 {eventName} - Your Ticket Details Inside!"
    message = f"""
    Dear {profileName},

    We hope you're as excited as we are because you’re about to experience an unforgettable event! 🎟️✨

    Here are your exclusive ticket details:

    **Event Name:** {eventData.title}
    **Secret Code:** {uuid}
    **Date:** {eventData.date.strftime('%A, %B %d, %Y')}
    
    Make sure to keep this secret code safe. It's your golden ticket to an amazing time!

    We're thrilled to have you join us and can't wait to see you there!

    Best regards,
    The {eventName} Team
    """

    send_mail(subject, message, senderEmail, [receiverEmail], fail_silently=False)




@login_required
def eventEditView(request, id):
    profile = Profile.objects.get(user=request.user)
    event   = Event.objects.get(pk=id)

    if request.method == 'POST':
        form = EventEditForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('home:eventDetail', id=id)
    else:
        form = EventEditForm(instance=event)

    template = loader.get_template('events/eventEdit.html')
    context = {
        'event'  : event,
        'profile': profile,
        'form'   : form,
    }
    return HttpResponse(template.render(context, request))


@login_required
def eventDeleteView(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == 'POST':
        event.delete()
        return redirect('profiles:profile')  
    
    template = loader.get_template('events/eventEdit.html')
    context = {
        'event'  : event,
    }
    return HttpResponse(template.render(context, request))

