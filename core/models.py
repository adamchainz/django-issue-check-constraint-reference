from django.db import models


class Book(models.Model):
    percent_read = models.PositiveIntegerField()
    percent_unread = models.PositiveIntegerField()
    percent_ignored = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.id} - {self.percent_read}% read"

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(
                    percent_read=(
                        100
                        - models.F("percent_unread")
                        - models.F("percent_ignored")
                    )
                ),
                name="percentages_sum_100",
            )
        ]
