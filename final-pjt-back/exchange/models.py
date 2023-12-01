from django.db import models

# Create your models here.
class Exchange(models.Model):
   result = models.IntegerField()
   cur_unit = models.TextField()
   ttb = models.TextField() 
   tts = models.TextField() 
   deal_bas_r = models.TextField()
   bkpr = models.TextField()
   yy_efee_r = models.TextField()
   ten_dd_efee_r = models.TextField()
   kftc_bkpr = models.TextField()
   kftc_deal_bas_r = models.TextField()
   cur_nm = models.TextField()
   date_field = models.TextField()