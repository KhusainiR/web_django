from django import forms
from .models import BooksModel

class BooksForm(forms.ModelForm):

    class Meta:
        # specify model to be used
        model = BooksModel
 
        # specify fields to be used
        fields = [
            "judul",
            "deskripsi",
            "jenis_buku",
            "penulis",
            "penerbit",
            "tahun_terbit",
        ]