from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    """ Kullanıcıların öğrenmekte olduğu bir konu."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        """ Modelin dizgi gösterimini döndür."""
        return self.text

class Entry(models.Model):
    """Konu hakkında öğrenilen özel bir şey"""
    topic = models.ForeignKey(Topic,on_delete = models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):
        """Modelin dizgi gösterimini döndür"""
        return f"{self.text[:50]}{'...' if len(self.text) > 50 else ''}"
