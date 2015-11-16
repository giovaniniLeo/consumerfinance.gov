# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0007_auto_20151113_1337'),
    ]

    operations = [
        migrations.CreateModel(
            name='LandingPage',
            fields=[
                ('cfgovpage_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='v1.CFGOVPage')),
                ('hero', wagtail.wagtailcore.fields.StreamField([(b'hero', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=True)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), (b'image_path', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'image_alt', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'background_color', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'link_url', wagtail.wagtailcore.blocks.URLBlock(required=False)), (b'link_text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'is_button', wagtail.wagtailcore.blocks.BooleanBlock(required=False))]))], blank=True)),
                ('introduction', wagtail.wagtailcore.fields.StreamField([(b'text_introduction', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=True)), (b'intro', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=True)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'link_url', wagtail.wagtailcore.blocks.URLBlock(required=False)), (b'link_text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'has_rule', wagtail.wagtailcore.blocks.BooleanBlock(required=False))]))], blank=True)),
                ('content', wagtail.wagtailcore.fields.StreamField([(b'half_width_link_blob', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=True)), (b'content', wagtail.wagtailcore.blocks.RichTextBlock(blank=True)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.URLBlock(required=False))], required=False, icon=b'user')))])), (b'image_text_25_75', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=True)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), (b'image_path', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'image_alt', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'link_url', wagtail.wagtailcore.blocks.URLBlock(required=False)), (b'link_text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'has_rule', wagtail.wagtailcore.blocks.BooleanBlock(required=False))])), (b'image_text_50_50', wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=True)), (b'description', wagtail.wagtailcore.blocks.RichTextBlock(blank=True)), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), (b'image_path', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'image_alt', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'is_widescreen', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'is_button', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'link_url', wagtail.wagtailcore.blocks.URLBlock(required=False)), (b'link_text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False))])), (b'well', wagtail.wagtailcore.blocks.StructBlock([(b'template_path', wagtail.wagtailcore.blocks.CharBlock(required=True))]))], blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('v1.cfgovpage',),
        ),
    ]
