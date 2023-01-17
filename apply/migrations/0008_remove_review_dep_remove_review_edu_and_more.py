# Generated by Django 4.0.3 on 2022-03-20 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("apply", "0007_remove_applicantform_reviewd_review_reviewd_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="review",
            name="dep",
        ),
        migrations.RemoveField(
            model_name="review",
            name="edu",
        ),
        migrations.RemoveField(
            model_name="review",
            name="exp",
        ),
        migrations.RemoveField(
            model_name="review",
            name="job",
        ),
        migrations.RemoveField(
            model_name="review",
            name="resume",
        ),
        migrations.AlterField(
            model_name="review",
            name="ratings",
            field=models.CharField(default=0, max_length=2),
        ),
    ]
