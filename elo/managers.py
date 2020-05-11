from django.db import models

class modelManager(models.Manager):

    def update_record(self,score,likes,is_valid,exposure):
        try:
            self.update(score = score,likes=likes,is_valid=is_valid,exposure=exposure)
        except Exception as e:
            print('Exception in updating record',e)

