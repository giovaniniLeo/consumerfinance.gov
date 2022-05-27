# Generated by Django 3.2.13 on 2022-05-10 15:20

from django.db import migrations
import v1.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('form_explainer', '0001_2022_squash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formexplainerpage',
            name='content',
            field=wagtail.core.fields.StreamField([('explainer', wagtail.core.blocks.StructBlock([('pages', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(icon='image', required=True)), ('categories', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Optional. Leave blank if there is only one type of note for this image.', label='Category title', required=False)), ('notes', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('coordinates', wagtail.core.blocks.StructBlock([('left', wagtail.core.blocks.FloatBlock(max_value=100, min_value=0, required=True)), ('top', wagtail.core.blocks.FloatBlock(max_value=100, min_value=0, required=True)), ('width', wagtail.core.blocks.FloatBlock(max_value=100, min_value=0, required=True)), ('height', wagtail.core.blocks.FloatBlock(max_value=100, min_value=0, required=True))], form_classname='coordinates', help_text='Enter percentage values to define the area that will be highlighted on the image for this note.', label='Note image map coordinates')), ('heading', wagtail.core.blocks.CharBlock(label='Note heading', required=True)), ('body', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link', 'document-link'], label='Note text', required=True))], form_classname='explainer_notes', required=False), default=[]))], required=False)))], required=False)))])), ('well', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.RichTextBlock(label='Well', required=False))])), ('info_unit_group', wagtail.core.blocks.StructBlock([('format', wagtail.core.blocks.ChoiceBlock(choices=[('50-50', '50/50'), ('33-33-33', '33/33/33'), ('25-75', '25/75')], help_text='Choose the number and width of info unit columns.', label='Format')), ('heading', wagtail.core.blocks.StructBlock([('text', v1.blocks.HeadingTextBlock(required=False)), ('level', wagtail.core.blocks.ChoiceBlock(choices=[('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')])), ('icon', v1.blocks.HeadingIconBlock(help_text='Input the name of an icon to appear to the left of the heading. E.g., approved, help-round, etc. <a href="https://cfpb.github.io/design-system/foundation/iconography">See full list of icons</a>', required=False))], required=False)), ('intro', wagtail.core.blocks.RichTextBlock(required=False)), ('link_image_and_heading', wagtail.core.blocks.BooleanBlock(default=True, help_text="Check this to link all images and headings to the URL of the first link in their unit's list, if there is a link.", required=False)), ('has_top_rule_line', wagtail.core.blocks.BooleanBlock(default=False, help_text='Check this to add a horizontal rule line to top of info unit group.', required=False)), ('lines_between_items', wagtail.core.blocks.BooleanBlock(default=False, help_text='Check this to show horizontal rule lines between info units.', label='Show rule lines between items', required=False)), ('info_units', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.core.blocks.StructBlock([('upload', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt', wagtail.core.blocks.CharBlock(help_text="No character limit, but be as succinct as possible. If the image is decorative (i.e., a screenreader wouldn't have anything useful to say about it), leave this field blank.", required=False))])), ('heading', wagtail.core.blocks.StructBlock([('text', v1.blocks.HeadingTextBlock(required=False)), ('level', wagtail.core.blocks.ChoiceBlock(choices=[('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')])), ('icon', v1.blocks.HeadingIconBlock(help_text='Input the name of an icon to appear to the left of the heading. E.g., approved, help-round, etc. <a href="https://cfpb.github.io/design-system/foundation/iconography">See full list of icons</a>', required=False))], default={'level': 'h3'}, required=False)), ('body', wagtail.core.blocks.RichTextBlock(blank=True, required=False)), ('links', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(required=False)), ('aria_label', wagtail.core.blocks.CharBlock(help_text='Add an ARIA label if the link text does not describe the destination of the link (e.g. has ambiguous text like "Learn more" that is not descriptive on its own).', required=False)), ('url', wagtail.core.blocks.CharBlock(default='/', required=False))]), required=False))]), default=[])), ('sharing', wagtail.core.blocks.StructBlock([('shareable', wagtail.core.blocks.BooleanBlock(help_text='If checked, share links will be included below the items.', label='Include sharing links?', required=False)), ('share_blurb', wagtail.core.blocks.CharBlock(help_text='Sets the tweet text, email subject line, and LinkedIn post text.', required=False))]))]))]),
        ),
    ]
