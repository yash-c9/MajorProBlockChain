from django.conf.urls import patterns, include, url
from website import views

urlpatterns = patterns(
    '',
    url(r'^$', views.home, name='home'),
    url(r'^data$', views.store_data, name='data_storage'),
    url(r'^encryption_key_verify/$', views.encryption_key_verify, 
    	name='encryption_key_verify'),
    url(r'^generate_id/$', views.generate_id, name='generate_id'),
    url(r'^validate_data/$', views.validate_data, name='validate_data'),
    url(r'^profile/$', views.profile_data, name='profile_data'),
    url(r'^edit-profile/$', views.edit_profile, name='edit_profile'),
    url(r'^healthdata/$', views.healthdata, name='healthdata_input'),
    url(r'^healthcare-validate/$', views.healthdata_validate, name='healthcare-validate'),
    url(r'^healthcare-recieve/$', views.healthdata_recieve, name='healthcare-recieve'),
)
