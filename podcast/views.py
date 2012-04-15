from django.views.generic.list_detail import object_detail, object_list

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, get_list_or_404, render_to_response, render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse

from models import Episode, Show, Enclosure




def podcast_show_list(request):

  # Get the show and episodes
  shows      = Show.objects.all()

  # Render the template
  template = 'podcast/show_list.html'
  context = {
    'shows': shows,
  }
  return render(request, template, context)




def podcast_show_detail(request, slug):

  # Get the show and episodes
  show      = get_object_or_404(Show, slug=slug)
  episodes  = Episode.objects.published().filter(show=show)

  # Render the template
  template = 'podcast/show_detail.html'
  context = {
    'show': show,
    'episodes': episodes,
  }
  return render(request, template, context)




def podcast_episode_detail(request, show_slug, episode_slug):

  # Get the show in question
  show = get_object_or_404(Show, slug=show_slug)
  
  # Get the episode in question
  try:
    episode = Episode.objects.published().get(show=show, slug=episode_slug) 
  except Episode.DoesNotExist:
    raise Http404

  # Render the template
  template = 'podcast/episode_detail.html'
  context = {
    'show': show,
    'episode': episode,
  }
  return render(request, template, context)








def podcast_show_sitemap(request, slug):
    """
    Episode sitemap

    Template:  ``podcast/episode_sitemap.html``
    Context:
        object_list
            List of episodes.
    """
    return object_list(
        request,
        mimetype='application/xml',
        queryset=Episode.objects.published().filter(show__slug__exact=slug).order_by('-date'),
        extra_context={
            'enclosure_list': Enclosure.objects.filter(episode__show__slug__exact=slug).order_by('-episode__date')},
        template_name='podcast/episode_sitemap.html')




def podcast_show_feed_atom(request, slug, template_name='podcast/show_feed_atom.html'):
    """
    Episode Atom feed for a given show

    Template:  ``podcast/show_feed_atom.html``
    Context:
        object
            Story detail
    """
    return object_detail(request,
        queryset=Show.objects.all(),
        mimetype='application/rss+xml',
        slug_field='slug',
        slug=slug,
        template_name=template_name,
        extra_context={
          'request': request,
        })


def podcast_show_feed(request, slug, template_name='podcast/show_feed.html'):
    """
    Episode RSS feed for a given show

    Template:  ``podcast/show_feed.html``
    Context:
        object
            Story detail
    """
    return object_detail(request,
        queryset=Show.objects.all(),
        mimetype='application/rss+xml',
        slug_field='slug',
        slug=slug,
        template_name=template_name,
        extra_context={
          'request': request,
        })





def podcast_show_feed_media_rss(request, slug, template_name='podcast/show_feed_media_rss.html'):
    """
    Episode Media feed for a given show

    Template:  ``podcast/show_feed_media.html``
    Context:
        object
            Story detail
    """
    return object_detail(request,
        queryset=Show.objects.all(),
        mimetype='application/rss+xml',
        slug_field='slug',
        slug=slug,
        template_name=template_name,
        extra_context={
          'request': request,
        })
