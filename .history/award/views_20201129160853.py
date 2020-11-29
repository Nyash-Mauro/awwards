from django.shortcuts import render,redirect
from . models import *
from .forms import ProjectUpload,UpdateProfileForm
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serializers import PostSerializer,ProfileSeralizer