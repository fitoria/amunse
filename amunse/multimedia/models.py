 # -*- coding: UTF-8 -*-
from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from customfilefield import ContentTypeRestrictedFileField

#from south.modelsinspector import add_introspection_rules
#add_introspection_rules = ([], ["^multimedia\.customfilefield\.ContentTypeRestrictedFileField"]) 

class Adjunto(models.Model):
    '''Modelo Generico para subir archivos adjuntos a diferentes tipos de contenidos'''
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()
    nombre = models.CharField(max_length = 150)
#    adjunto = models.FileField(upload_to = 'attachments/documentos')
    adjunto = ContentTypeRestrictedFileField(upload_to = 'attachments/documentos', content_types=['application/pdf', 'application/zip', 'image/jpeg'], max_upload_size=5242880)

    def get_absolute_url(self):
        return '%s%s/%s' % (settings.MEDIA_URL, 
                         settings.ATTACHMENT_FOLDER, self.id)
    def get_download_url(self):
        return '%s%s' % (settings.MEDIA_URL, self.adjunto)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = "Adjunto"
        verbose_name_plural = "Adjuntos"
        

