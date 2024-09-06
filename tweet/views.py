from django.shortcuts import render, redirect
from .models import Tweet
from .forms import TweetForm,UserRegistrationForm, searchForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request, 'tweet/index.html')

def list_tweets(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet/list_tweets.html', {'tweets': tweets})

@login_required
def create_tweet(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user= request.user
            tweet.save()
            return redirect('list_tweets')
    else:
        form = TweetForm()
    return render(request, 'tweet/tweet_form.html', {'form':form})

@login_required
def edit_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user= request.user
            tweet.save()
            return redirect('list_tweets')
    else:
        pass
    form = TweetForm(instance=tweet)
    return render(request, 'tweet/tweet_form.html', {'form':form}) 

@login_required
def delete_tweet(request, tweet_id):
    tweet=get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('list_tweets')
    return render(request, 'tweet/tweet_confirm_delete.html', {'tweet':tweet})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(user)
            return redirect('list_tweets')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form':form})

def search(request):
    pass
    