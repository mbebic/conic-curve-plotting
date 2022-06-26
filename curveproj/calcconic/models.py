from django.db import models

# Create your models here.

# Adding a model-less permissions as explained in https://stackoverflow.com/a/37988537
class CalcRights(models.Model):
    class Meta:
        managed = False  # No database table creation or deletion \
                         # operations will be performed for this model. 
                
        default_permissions = () # providing an empty tuple disables "add", "change", \
                                 # "delete" and "view" default permissions

        permissions = (
            ('can_calc_conics', 'Allowed to calculate conics'),
        )
