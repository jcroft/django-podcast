from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('podcast.views',
  url(
    regex   = r'^$', 
    view    = 'podcast_show_list', 
    name    = 'podcast_shows',
  ),
  url(
    regex   = r'^(?P<slug>[-\w]+)/$', 
    view    = 'podcast_show_detail', 
    name    = 'podcast_show_detail',
  ),
  url(
    regex   = r'^(?P<slug>[-\w]+)/feed/$', 
    view    = 'podcast_show_feed', 
    name    = 'podcast_show_feed',
  ),
  url(
    regex   = r'^(?P<slug>[-\w]+)/atom/$', 
    view    = 'podcast_show_feed_atom', 
    name    = 'podcast_show_feed_atom',
  ),
  url(
    regex   = r'^(?P<slug>[-\w]+)/media-rss/$', 
    view    = 'podcast_show_feed_media_rss', 
    name    = 'podcast_show_feed_media_rss',
  ),
  url(
    regex   = r'^(?P<slug>[-\w]+)/sitemap.xml$', 
    view    = 'podcast_show_sitemap', 
    name    = 'podcast_show_sitemap',
  ),
  url(
    regex   = r'^(?P<show_slug>[-\w]+)/(?P<episode_slug>[-\w]+)/$', 
    view    = 'podcast_episode_detail', 
    name    = 'podcast_episode_detail',
  ),
)
