from django.db import models
from django.contrib.auth.models import User




class Tag(models.Model):
    name = models.CharField(verbose_name=u'Nombre', max_length=20)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tag'


class Category (models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=50,
                            blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL,
                             null=True, verbose_name='Usuario')
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name='Fecha Creacion')
    mod = models.DateTimeField(auto_now=True,
                               verbose_name='Fecha Mod')

    def serialize(self):
        return {
            'name': self.name,
            'id': self.id
        }

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categoria'


class Post(models.Model):
    name = models.CharField(verbose_name='Titulo', max_length=50)
    tag = models.ManyToManyField(Tag, verbose_name='Datos',
                                 blank=True, null=True)
    user = models.ForeignKey(User, verbose_name='Usuario',
                             on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name='Fecha Creacion')
    mod = models.DateTimeField(auto_now=True,
                               verbose_name='Fecha Mod')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 verbose_name='Categoria', null=True)
    img = models.ImageField(verbose_name='Imagen')
    body_1 = models.TextField(verbose_name='Texto Superior')
    body_2 = models.TextField(verbose_name='Texto Superior Inf')
    body_3 = models.TextField(verbose_name='Texto Superior Cen')
    body_4 = models.TextField(verbose_name='Texto Baja')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Cuerpo'
        verbose_name_plural = 'Cuerpo'


class Comments(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=20)
    email = models.EmailField(verbose_name='Email', max_length=20)
    website = models.URLField(verbose_name=u'Website')
    message = models.TextField(verbose_name='Comentario')
    post = models.ForeignKey(Post, verbose_name=u'Publication',
                             on_delete=models.SET_NULL, null=True)

    def serialize(self):
        return {
            'name': self.name
        }

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentario'


class Footer(models.Model):
    name = models.CharField(verbose_name='Titulo', max_length=50)
    description = models.TextField(verbose_name='Descripción')
    #choice = models.CharField(verbose_name=u'c', max_length=50)
    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Model Footer'
        verbose_name_plural = 'Model Footer'


class FooterSocialNet(models.Model):
    category = models.ForeignKey(Footer, on_delete=models.SET_NULL,
                                 verbose_name='Footer', null=True)
    link = models.URLField(verbose_name='Link')

    def __str__(self):
        return str(self.link)

    class Meta:
        verbose_name = 'Redes Sociales'
        verbose_name_plural = 'Redes Sociales'


