from django.db import models

# Create your models here.



class Assets(models.Model):

    shortcut = models.CharField(max_length=350, null=False, blank=False, primary_key=True)
    name     = models.CharField(max_length=350, null=False, blank=False)
    url      = models.CharField(max_length=350, null=False, blank=False)
    type     = models.CharField(max_length=5, null=False, blank=False, default=1)
    high     = models.IntegerField(null=False, blank=True, default=0)
    mid      = models.IntegerField(null=False, blank=True, default=0)
    low      = models.IntegerField(null=False, blank=True, default=0)
    info     = models.IntegerField(null=False, blank=True, default=0)
    risk     = models.IntegerField(null=False, blank=True, default=1)

    class  Meta:
        db_table = '"assets"'

    
    
     

    
    def __str__(self):
        return "{} - {}".format(self.name, self.url)



class Scans(models.Model):

    reporthash = models.CharField(max_length=350, null=False, blank=False, primary_key=True)
    date       = models.DateTimeField(blank=False, auto_now=True)
    shortcut   = models.ForeignKey(Assets, on_delete=models.CASCADE, related_name='asset')
    success    = models.BooleanField(default=True)
    running    = models.BooleanField(default=True)
    
    class  Meta:
        db_table = '"scans"'

   


class Vulns(models.Model):

    id         = models.IntegerField(null=False, blank=False, primary_key=True)
    asset      = models.ForeignKey(Assets, on_delete=models.CASCADE)
    level      = models.IntegerField(null=False, blank=False, default=1)
    OWASP      = models.IntegerField(null=False, blank=False, default=5)
    status     = models.IntegerField(null=False, blank=False, default=0)
    title      = models.CharField(max_length=350, null=False, blank=False)
    
    
    class  Meta:
        db_table = '"vulns"'

    
    
