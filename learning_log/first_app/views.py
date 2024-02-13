from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from django.http import Http404
from .models import Topic,Entry
from .forms import TopicForm,EntryForm

def index(request):
    """Learning Log için ana sayfa"""
    return render(request,'first_app/index.html')

@login_required
def topics(request):
    """ Bütün konuları göster"""
    topics = Topic.objects.filter(owner = request.user).order_by('date_added')
    context = {'topics':topics}
    return render (request,'first_app/topics.html',context)

@login_required
def topic(request,topic_id):
    """ Tek bir konuyu ve bu konunun bütün girdilerini göster."""
    topic=Topic.objects.get(id=topic_id)
    #Konunun o anki kullanıcıya ait olduğundan emin olunuz.
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic,'entries':entries}
    return render(request,'first_app/topic.html',context)

@login_required
def new_topic(request):
    """ Yeni konu ekle"""
    if request.method != 'POST':
        # Hiçbir veri gönderilmemiştir;boş bir form oluştur.
        form = TopicForm()
        
    else:
        # POST verisi gönderildi; veriyi işle.
        form = TopicForm(data = request.POST)
        if form.is_valid():
            new_topic=form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('first_app:topics')
    # Boş veya geçersiz bir form görüntüle.
    context = {'form': form}
    return render(request,'first_app/new_topic.html',context)

@login_required
def new_entry(request,topic_id):
    """ Belirli bir konu için yeni bir girdi ekle."""
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404("Bu konuda yetkili değilsiniz")
    if request.method != 'POST':
        """ Hiçbir veri gönderilmemiş;boş bir form oluştur."""
        form = EntryForm()
    else: 
        """POST verisi gönderilmiş;veriyi işle"""
        form = EntryForm(data =request.POST)
        if form.is_valid:
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('first_app:topic',topic_id=topic_id)
    #Boş veya geçersiz bir form görüntüle.
    context = {'topic':topic,'form':form}
    return render(request,'first_app/new_entry.html',context) 

@login_required
def edit_entry(request,entry_id):
    """ Var olan bir girdiyi düzenle."""
    entry= Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST':
        #İlk istek;formu mevcut girdiyle önceden doldur.
        form = EntryForm(instance=entry)
    else:
        #POST verisi gönderildi,veriyi işle.
        form = EntryForm(instance=entry,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('first_app:topic',topic_id=topic.id)
    context={'entry':entry,'topic':topic,'form':form}
    return render(request,'first_app/edit_entry.html',context)

            
            
        