# Generated by Django 4.0.7 on 2022-10-03 21:26

import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0005_blogindexpage_blogpage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="standardpage",
            name="story",
            field=wagtail.fields.StreamField(
                [
                    ("heading", wagtail.blocks.CharBlock(form_classname="full title")),
                    ("paragraph", wagtail.blocks.RichTextBlock()),
                    ("image", wagtail.images.blocks.ImageChooserBlock()),
                ],
                blank=True,
                null=True,
                use_json_field=True,
            ),
        ),
    ]