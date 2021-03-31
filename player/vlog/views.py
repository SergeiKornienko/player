from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Video


class VideosView(ListView):
    """List of videos."""
    model = Video
    queryset = Video.playlist.all()


class VideoDetailView(DetailView):
    """Video"""
    model = Video
    slug_field = 'pk'


