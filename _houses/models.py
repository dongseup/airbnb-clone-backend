from django.db import models


class House(models.Model):

    """Model Definition for Houses"""

    name = models.CharField(max_length=140)
    price_per_night = models.PositiveIntegerField(
        verbose_name="Price", help_text="Positive Numbers Only"
    )  # 양수의 숫자
    description = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(
        default=True,
        verbose_name="Pets Allowed?",
        help_text="Does this house allow pets?",
    )
    owner = models.ForeignKey(
        "users.User", on_delete=models.CASCADE
    )  # models.CASCADE, models.SET_NULL

    def __str__(self):
        return self.name
