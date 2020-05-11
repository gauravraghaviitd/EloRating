from django.apps import AppConfig
#from elo import views

class EloConfig(AppConfig):
    name = 'elo'
    def ready(self):
        from elo import views
        views.eloView.get_all_image()
    #    pass
    #    views.eloView.get_all_image()
