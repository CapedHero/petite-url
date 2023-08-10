from django.db.models import CharField, DateTimeField, Model, URLField


class PetiteURL(Model):
    target_url = URLField(max_length=250)
    petite_code = CharField(max_length=10, unique=True)
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.petite_code} -> {self.target_url}"
