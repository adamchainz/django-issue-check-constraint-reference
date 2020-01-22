from django import forms

from core.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["percent_read", "percent_unread", "percent_ignored"]

    def clean(self):
        cleaned_data = super().clean()

        try:
            percentages_sum = (
                cleaned_data["percent_read"]
                + cleaned_data["percent_unread"]
                + cleaned_data["percent_ignored"]
            )
        except KeyError:
            pass
        else:
            if percentages_sum != 100:
                self.add_error(
                    None,
                    (
                        f"Percentages must add up to 100%, they currently add"
                        + f" up to {percentages_sum}%"
                    )
                )

        return cleaned_data
