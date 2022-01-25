from django.db import models

# Create your models here.
class BooksModel(models.Model):
    # fields of the model
    judul = models.CharField(max_length = 200)
    deskripsi = models.TextField()
    jenis_buku = models.CharField(max_length = 200)
    penulis = models.CharField(max_length = 200)
    penerbit = models.CharField(max_length = 200)
    tahun_terbit = models.IntegerField()
    
    def __str__(self):
        return self.judul