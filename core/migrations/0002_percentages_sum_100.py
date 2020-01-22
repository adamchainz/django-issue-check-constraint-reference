from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="book",
            constraint=models.CheckConstraint(
                check=models.Q(
                    percent_read=django.db.models.expressions.CombinedExpression(
                        django.db.models.expressions.CombinedExpression(
                            django.db.models.expressions.Value(100),
                            "-",
                            django.db.models.expressions.F("percent_unread"),
                        ),
                        "-",
                        django.db.models.expressions.F("percent_ignored"),
                    )
                ),
                name="percentages_sum_100",
            ),
        ),
    ]
