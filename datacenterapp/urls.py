from django.urls import path
from .views import index, video_feed_html,start_scanning, Red_Green, start_swapping, fire, faical_recog, video_feed_depth, armController, amrController,faical_recog_cancel

urlpatterns = [
    path('', index, name='index.html'),
    # path('webcam_feed/', webcam_feed, name='webcam_feed'),
    path('video_feed_html/', video_feed_html, name='video_feed_html'),
    path('start_scanning/', start_scanning, name='start_scanning'),
    path('start_swapping/', start_swapping, name='start_swapping'),
    path('Red_Green/', Red_Green, name='Red_Green'),
    path('fire/', fire, name='fire'),
    path('faical_recog/', faical_recog, name='faical_recog'),
    path('video_feed_depth/', video_feed_depth, name='video_feed_depth'),
    path('armController/', armController, name='armController'),
    path('amrController/', amrController, name='amrController'),
    path('faical_recog_cancel/', faical_recog_cancel, name='faical_recog_cancel'),  
]
