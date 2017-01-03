
#from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.conf.urls import include, url
from firstsite.wec.ipic import image_setup, image_write
from firstsite.wec.views_test import modal_form, testing
from firstsite.wec.views import main, login_error, dashboard, pmain, mmain, test, fill, graph, done,test3
from firstsite.wec.views2 import thanks, login, register, members_db, membersdel, emailtest, services, about, contact
from firstsite.wec.views2 import registration, fade,pc,mobile, ssize, members_features,picture
from firstsite.wec.views_webpage import web, web_edit,page_delete,done_page_edit,web_page_reload,web_edit2,home,web_link
from firstsite.wec.views_webpage import web_template_initialize, home_link,home_initial
from firstsite.wec.views_website import image_update

# *******  Uploading pictures **************
from firstsite.wec.views_picture import image_upload
from firstsite.wec.views_admin import admin_add_users, display_users, display_webpages, admin_add_webpage, admin_debug
from firstsite.wec.views_admin import admin_delete_webpage,testlink
from firstsite.wec.views_test import create_table,poptest, pop_link,test2
from firstsite.wec.views_kodi import kodi_live, kodi_main, kodi_addons, kodi_install, create_koditable, kodi_remote

# *******  MODS ***********
from firstsite.wec.mod2 import create_directory, copy_directory, dir_test
from firstsite.wec.mod3 import repair_database, page_set, alter_database
from firstsite.wec.views_db_modifications import create_column, delete_column, change_column, change_column2


from firstsite.wec.we_scheduler import matrix, mainadd, maindel, matrice, imain, db, main_new
#from firstsite.wec.db1 import member
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
        url(r'^$', main),
		 
		url(r'^dir_test/',dir_test), 
		url(r'^testlink/',testlink),
		# ****************Web Page Design URL PATTERNS **** ***** * ************
		url(r'^web/(?P<addy>\w{0,50})',web),
		url(r'^home/(?P<addy>\w{0,50})',home_initial),
		url(r'^home_link/(?P<hook>\w{0,50})',home_link),
		
        
        		
        url(r'^web_template_initialize/',web_template_initialize),
        url(r'^web_edit/',web_edit),
        url(r'^web_page_reload/',web_page_reload),
        url(r'^web_edit2/',web_edit2),
        url(r'^page_delete/',page_delete),
        
        url(r'^web_link/',web_link),
		#url(r'^page_initialize/',page_initialize),
		
		# ************************************************************
		url(r'^test3/',test3),
        url(r'^login/',login),
        url(r'^emailtest/',emailtest),
        url(r'^register/',register),
        url(r'^fill/',login),
        url(r'^feature/',members_features),
        url(r'^pc/',pc),
        url(r'^pmain/',pmain),
        url(r'^ssize/get/(?P<wid>\d+)/(?P<hei>\d+)/$',ssize),
        url(r'^mmain/',mmain),
        url(r'^up/',image_upload),
        url(r'^update/',image_update),
        url(r'^mobile/',mobile),
        url(r'^about/',about),
        url(r'^contact/',contact),
        url(r'^services/',services),
        #url(r'^member/$', member),
        url(r'^fade/$', fade),
        url(r'^login_error/$', login_error),
        url(r'^dashboard/$', dashboard),
        url(r'^thanks/', thanks),
        url(r'^done/', done),
        url(r'^test2/$', test2),
		url(r'^done_page_edit/$', done_page_edit),
        url(r'^testing/$', testing),
        #url(r'^dm/$', dm),
        url(r'^imain/$', imain),
        url(r'^admin/', include(admin.site.urls)),
        url(r'^mainadd/$', mainadd),
        url(r'^matrix/$', matrix),
        url(r'^main_new/$', main_new),
        url(r'^db/$', db),
        url(r'^members_db/$', members_db),
        url(r'^picture/$', picture),
        #url(r'^registration/$', registration),
        url(r'^members_db/get/(?P<db_id>\d+)/$', membersdel),
        url(r'^db/get/(?P<db_id>\d+)/$', maindel),
        url(r'^registration/get/(?P<db_id>\d+)/$', registration),
        url(r'^matrice/get/(?P<index>\d+)/$', matrice),
        url(r'^image/',image_setup),
        url(r'^imagecheck/',image_write),
		url(r'^graph/',graph),
        url(r'^create/',create_table),
		
		url(r'^kodi_live/',kodi_live),
		url(r'^kodi_remote/',kodi_remote),
		url(r'^kodi_install/',kodi_install),
		url(r'^kodi_main/',kodi_main),
		url(r'^kodi_addons/',kodi_addons),
		url(r'^create_koditable/',create_koditable),
# ************ Admin Add Ons ******************************************
        url(r'^admin_add_users/',admin_add_users),
		url(r'^admin_add_webpage/',admin_add_webpage),
		url(r'^admin_delete_webpage/get/(?P<web>\w{0,50})/$', admin_delete_webpage),

		url(r'^admin_debug/',admin_debug),
		url(r'^display_webpages/',display_webpages),
        url(r'^display_users/',display_users),
        
        url(r'^cd/',create_directory),
        url(r'^cpd/',copy_directory),
# *********************************************************************   
# ************ WebPage Templates ******************************************   
        url(r'^poptest/',poptest),
		url(r'^pop_link/',pop_link),
        url(r'^modal_form/',modal_form),
# *********************************************************************  

# ************ Database Adjustments *************************************   
		url(r'^repair_database/',repair_database),
		url(r'^page_set/',page_set),
		url(r'^alter_database/',alter_database),
		url(r'^create_column/',create_column),
		url(r'^delete_column/',delete_column),
		url(r'^change_column/',change_column),
		url(r'^change_column2/',change_column2),

# *********************************************************************    
 
]


