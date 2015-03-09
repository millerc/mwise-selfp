# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'LayoutTemplateImageBlock'
        db.delete_table('selfpublish_layouttemplateimageblock')

        # Deleting model 'LayoutImageBlock'
        db.delete_table('selfpublish_layoutimageblock')

        # Deleting model 'LayoutTemplateUse'
        db.delete_table('selfpublish_layouttemplateuse')

        # Deleting model 'LayoutTemplateBlock'
        db.delete_table('selfpublish_layouttemplateblock')

        # Deleting model 'LayoutBlock'
        db.delete_table('selfpublish_layoutblock')

        # Deleting model 'PublicationTemplateStyle'
        db.delete_table('selfpublish_publicationtemplatestyle')

        # Removing M2M table for field suggested_templates on 'PublicationTemplateStyle'
        db.delete_table('selfpublish_publicationtemplatestyle_suggested_templates')

        # Deleting model 'LayoutFileBlock'
        db.delete_table('selfpublish_layoutfileblock')

        # Deleting model 'PublicationTemplate'
        db.delete_table('selfpublish_publicationtemplate')

        # Deleting model 'LayoutTemplateFileBlock'
        db.delete_table('selfpublish_layouttemplatefileblock')

        # Deleting model 'LayoutCharBlock'
        db.delete_table('selfpublish_layoutcharblock')

        # Deleting model 'LayoutTemplate'
        db.delete_table('selfpublish_layouttemplate')

        # Deleting model 'LayoutTemplateCharBlock'
        db.delete_table('selfpublish_layouttemplatecharblock')

        # Adding model 'Spread'
        db.create_table('selfpublish_spread', (
            ('layout_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['selfpublish.Layout'], unique=True, primary_key=True)),
            ('publication', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['selfpublish.Publication'])),
            ('spread_template', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['selfpublish.SpreadTemplate'])),
            ('sequence', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal('selfpublish', ['Spread'])

        # Adding model 'ImageBlock'
        db.create_table('selfpublish_imageblock', (
            ('block_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['selfpublish.Block'], unique=True, primary_key=True)),
            ('content', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('selfpublish', ['ImageBlock'])

        # Adding model 'Theme'
        db.create_table('selfpublish_theme', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('keywords', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('rank', self.gf('django.db.models.fields.FloatField')(default=0)),
        ))
        db.send_create_signal('selfpublish', ['Theme'])

        # Adding model 'TemplateFileBlock'
        db.create_table('selfpublish_templatefileblock', (
            ('templateblock_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['selfpublish.TemplateBlock'], unique=True, primary_key=True)),
            ('default_content', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('selfpublish', ['TemplateFileBlock'])

        # Adding model 'PageCountMemberMap'
        db.create_table('selfpublish_pagecountmembermap', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('page_count', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('minimum_membership', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('maximum_membership', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal('selfpublish', ['PageCountMemberMap'])

        # Adding model 'Template'
        db.create_table('selfpublish_template', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('selfpublish', ['Template'])

        # Adding model 'TemplateBlock'
        db.create_table('selfpublish_templateblock', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('template', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['selfpublish.Template'])),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('sequence', self.gf('django.db.models.fields.IntegerField')()),
            ('required', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('help_text', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('selfpublish', ['TemplateBlock'])

        # Adding model 'TemplateImageBlock'
        db.create_table('selfpublish_templateimageblock', (
            ('templateblock_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['selfpublish.TemplateBlock'], unique=True, primary_key=True)),
            ('default_content', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('selfpublish', ['TemplateImageBlock'])

        # Adding model 'TemplateCharBlock'
        db.create_table('selfpublish_templatecharblock', (
            ('templateblock_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['selfpublish.TemplateBlock'], unique=True, primary_key=True)),
            ('default_content', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('max_length', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('selfpublish', ['TemplateCharBlock'])

        # Adding model 'SpreadTemplate'
        db.create_table('selfpublish_spreadtemplate', (
            ('template_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['selfpublish.Template'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('selfpublish', ['SpreadTemplate'])

        # Adding model 'CharBlock'
        db.create_table('selfpublish_charblock', (
            ('block_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['selfpublish.Block'], unique=True, primary_key=True)),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('selfpublish', ['CharBlock'])

        # Adding model 'Cover'
        db.create_table('selfpublish_cover', (
            ('layout_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['selfpublish.Layout'], unique=True, primary_key=True)),
            ('cover_template', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['selfpublish.CoverTemplate'])),
        ))
        db.send_create_signal('selfpublish', ['Cover'])

        # Adding model 'FileBlock'
        db.create_table('selfpublish_fileblock', (
            ('block_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['selfpublish.Block'], unique=True, primary_key=True)),
            ('content', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('selfpublish', ['FileBlock'])

        # Adding model 'Block'
        db.create_table('selfpublish_block', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('layout', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['selfpublish.Layout'])),
            ('template_block', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['selfpublish.TemplateBlock'])),
        ))
        db.send_create_signal('selfpublish', ['Block'])

        # Adding model 'CoverTemplate'
        db.create_table('selfpublish_covertemplate', (
            ('template_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['selfpublish.Template'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('selfpublish', ['CoverTemplate'])

        # Adding model 'Design'
        db.create_table('selfpublish_design', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('template', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['selfpublish.Template'])),
            ('theme', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['selfpublish.Theme'])),
            ('preview', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('annotated', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('selfpublish', ['Design'])

        # Deleting field 'Publication.template'
        db.delete_column('selfpublish_publication', 'template_id')

        # Adding field 'Publication.subtitle'
        db.add_column('selfpublish_publication', 'subtitle', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Publication.cover'
        db.add_column('selfpublish_publication', 'cover', self.gf('django.db.models.fields.related.OneToOneField')(default=2, to=orm['selfpublish.Cover'], unique=True), keep_default=False)

        # Adding field 'Publication.page_count'
        db.add_column('selfpublish_publication', 'page_count', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=2), keep_default=False)

        # Deleting field 'Layout.layout_template_use'
        db.delete_column('selfpublish_layout', 'layout_template_use_id')

        # Deleting field 'Layout.publication'
        db.delete_column('selfpublish_layout', 'publication_id')


    def backwards(self, orm):
        
        # Adding model 'LayoutTemplateImageBlock'
        db.create_table('selfpublish_layouttemplateimageblock', (
            ('default_content', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('layouttemplateblock_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['selfpublish.LayoutTemplateBlock'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('selfpublish', ['LayoutTemplateImageBlock'])

        # Adding model 'LayoutImageBlock'
        db.create_table('selfpublish_layoutimageblock', (
            ('content', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('layoutblock_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['selfpublish.LayoutBlock'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('selfpublish', ['LayoutImageBlock'])

        # Adding model 'LayoutTemplateUse'
        db.create_table('selfpublish_layouttemplateuse', (
            ('publication_template', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['selfpublish.PublicationTemplate'])),
            ('layout_template', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['selfpublish.LayoutTemplate'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sequence', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal('selfpublish', ['LayoutTemplateUse'])

        # Adding model 'LayoutTemplateBlock'
        db.create_table('selfpublish_layouttemplateblock', (
            ('sequence', self.gf('django.db.models.fields.IntegerField')()),
            ('required', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('layout_template', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['selfpublish.LayoutTemplate'])),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('help_text', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('selfpublish', ['LayoutTemplateBlock'])

        # Adding model 'LayoutBlock'
        db.create_table('selfpublish_layoutblock', (
            ('layout', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['selfpublish.Layout'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('template_block', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['selfpublish.LayoutTemplateBlock'])),
        ))
        db.send_create_signal('selfpublish', ['LayoutBlock'])

        # Adding model 'PublicationTemplateStyle'
        db.create_table('selfpublish_publicationtemplatestyle', (
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255, db_index=True)),
            ('cover_preview', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('keywords', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rank', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('selfpublish', ['PublicationTemplateStyle'])

        # Adding M2M table for field suggested_templates on 'PublicationTemplateStyle'
        db.create_table('selfpublish_publicationtemplatestyle_suggested_templates', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_publicationtemplatestyle', models.ForeignKey(orm['selfpublish.publicationtemplatestyle'], null=False)),
            ('to_publicationtemplatestyle', models.ForeignKey(orm['selfpublish.publicationtemplatestyle'], null=False))
        ))
        db.create_unique('selfpublish_publicationtemplatestyle_suggested_templates', ['from_publicationtemplatestyle_id', 'to_publicationtemplatestyle_id'])

        # Adding model 'LayoutFileBlock'
        db.create_table('selfpublish_layoutfileblock', (
            ('content', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('layoutblock_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['selfpublish.LayoutBlock'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('selfpublish', ['LayoutFileBlock'])

        # Adding model 'PublicationTemplate'
        db.create_table('selfpublish_publicationtemplate', (
            ('style', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['selfpublish.PublicationTemplateStyle'])),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('minimum_suggested_membership', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('page_count', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('maximum_suggested_membership', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal('selfpublish', ['PublicationTemplate'])

        # Adding model 'LayoutTemplateFileBlock'
        db.create_table('selfpublish_layouttemplatefileblock', (
            ('default_content', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('layouttemplateblock_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['selfpublish.LayoutTemplateBlock'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('selfpublish', ['LayoutTemplateFileBlock'])

        # Adding model 'LayoutCharBlock'
        db.create_table('selfpublish_layoutcharblock', (
            ('content', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('layoutblock_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['selfpublish.LayoutBlock'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('selfpublish', ['LayoutCharBlock'])

        # Adding model 'LayoutTemplate'
        db.create_table('selfpublish_layouttemplate', (
            ('annotated_preview', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('preview', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('selfpublish', ['LayoutTemplate'])

        # Adding model 'LayoutTemplateCharBlock'
        db.create_table('selfpublish_layouttemplatecharblock', (
            ('max_length', self.gf('django.db.models.fields.IntegerField')()),
            ('default_content', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('layouttemplateblock_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['selfpublish.LayoutTemplateBlock'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('selfpublish', ['LayoutTemplateCharBlock'])

        # Deleting model 'Spread'
        db.delete_table('selfpublish_spread')

        # Deleting model 'ImageBlock'
        db.delete_table('selfpublish_imageblock')

        # Deleting model 'Theme'
        db.delete_table('selfpublish_theme')

        # Deleting model 'TemplateFileBlock'
        db.delete_table('selfpublish_templatefileblock')

        # Deleting model 'PageCountMemberMap'
        db.delete_table('selfpublish_pagecountmembermap')

        # Deleting model 'Template'
        db.delete_table('selfpublish_template')

        # Deleting model 'TemplateBlock'
        db.delete_table('selfpublish_templateblock')

        # Deleting model 'TemplateImageBlock'
        db.delete_table('selfpublish_templateimageblock')

        # Deleting model 'TemplateCharBlock'
        db.delete_table('selfpublish_templatecharblock')

        # Deleting model 'SpreadTemplate'
        db.delete_table('selfpublish_spreadtemplate')

        # Deleting model 'CharBlock'
        db.delete_table('selfpublish_charblock')

        # Deleting model 'Cover'
        db.delete_table('selfpublish_cover')

        # Deleting model 'FileBlock'
        db.delete_table('selfpublish_fileblock')

        # Deleting model 'Block'
        db.delete_table('selfpublish_block')

        # Deleting model 'CoverTemplate'
        db.delete_table('selfpublish_covertemplate')

        # Deleting model 'Design'
        db.delete_table('selfpublish_design')

        # Adding field 'Publication.template'
        db.add_column('selfpublish_publication', 'template', self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['selfpublish.PublicationTemplate']), keep_default=False)

        # Deleting field 'Publication.subtitle'
        db.delete_column('selfpublish_publication', 'subtitle')

        # Deleting field 'Publication.cover'
        db.delete_column('selfpublish_publication', 'cover_id')

        # Deleting field 'Publication.page_count'
        db.delete_column('selfpublish_publication', 'page_count')

        # Adding field 'Layout.layout_template_use'
        db.add_column('selfpublish_layout', 'layout_template_use', self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['selfpublish.LayoutTemplateUse']), keep_default=False)

        # Adding field 'Layout.publication'
        db.add_column('selfpublish_layout', 'publication', self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['selfpublish.Publication']), keep_default=False)


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.statustype': {
            'Meta': {'object_name': 'StatusType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'})
        },
        'selfpublish.block': {
            'Meta': {'object_name': 'Block'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'layout': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['selfpublish.Layout']"}),
            'template_block': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['selfpublish.TemplateBlock']"})
        },
        'selfpublish.charblock': {
            'Meta': {'object_name': 'CharBlock', '_ormbases': ['selfpublish.Block']},
            'block_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['selfpublish.Block']", 'unique': 'True', 'primary_key': 'True'}),
            'content': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'selfpublish.cover': {
            'Meta': {'object_name': 'Cover', '_ormbases': ['selfpublish.Layout']},
            'cover_template': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['selfpublish.CoverTemplate']"}),
            'layout_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['selfpublish.Layout']", 'unique': 'True', 'primary_key': 'True'})
        },
        'selfpublish.covertemplate': {
            'Meta': {'ordering': "['name']", 'object_name': 'CoverTemplate', '_ormbases': ['selfpublish.Template']},
            'template_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['selfpublish.Template']", 'unique': 'True', 'primary_key': 'True'})
        },
        'selfpublish.design': {
            'Meta': {'object_name': 'Design'},
            'annotated': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'preview': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'template': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['selfpublish.Template']"}),
            'theme': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['selfpublish.Theme']"})
        },
        'selfpublish.fileblock': {
            'Meta': {'object_name': 'FileBlock', '_ormbases': ['selfpublish.Block']},
            'block_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['selfpublish.Block']", 'unique': 'True', 'primary_key': 'True'}),
            'content': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'selfpublish.imageblock': {
            'Meta': {'object_name': 'ImageBlock', '_ormbases': ['selfpublish.Block']},
            'block_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['selfpublish.Block']", 'unique': 'True', 'primary_key': 'True'}),
            'content': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'selfpublish.layout': {
            'Meta': {'object_name': 'Layout'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'selfpublish.pagecountmembermap': {
            'Meta': {'ordering': "['page_count']", 'object_name': 'PageCountMemberMap'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maximum_membership': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'minimum_membership': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'page_count': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        'selfpublish.publication': {
            'Meta': {'ordering': "['-updated']", 'object_name': 'Publication'},
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'cover': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['selfpublish.Cover']", 'unique': 'True'}),
            'deliverable': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'page_count': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['selfpublish.PublicationStatusType']", 'null': 'True', 'blank': 'True'}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'selfpublish.publicationstatustype': {
            'Meta': {'object_name': 'PublicationStatusType', '_ormbases': ['core.StatusType']},
            'statustype_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.StatusType']", 'unique': 'True', 'primary_key': 'True'})
        },
        'selfpublish.spread': {
            'Meta': {'object_name': 'Spread', '_ormbases': ['selfpublish.Layout']},
            'layout_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['selfpublish.Layout']", 'unique': 'True', 'primary_key': 'True'}),
            'publication': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['selfpublish.Publication']"}),
            'sequence': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'spread_template': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['selfpublish.SpreadTemplate']"})
        },
        'selfpublish.spreadtemplate': {
            'Meta': {'ordering': "['name']", 'object_name': 'SpreadTemplate', '_ormbases': ['selfpublish.Template']},
            'template_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['selfpublish.Template']", 'unique': 'True', 'primary_key': 'True'})
        },
        'selfpublish.template': {
            'Meta': {'ordering': "['name']", 'object_name': 'Template'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'selfpublish.templateblock': {
            'Meta': {'ordering': "['sequence']", 'object_name': 'TemplateBlock'},
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sequence': ('django.db.models.fields.IntegerField', [], {}),
            'template': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['selfpublish.Template']"})
        },
        'selfpublish.templatecharblock': {
            'Meta': {'ordering': "['sequence']", 'object_name': 'TemplateCharBlock', '_ormbases': ['selfpublish.TemplateBlock']},
            'default_content': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'max_length': ('django.db.models.fields.IntegerField', [], {}),
            'templateblock_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['selfpublish.TemplateBlock']", 'unique': 'True', 'primary_key': 'True'})
        },
        'selfpublish.templatefileblock': {
            'Meta': {'ordering': "['sequence']", 'object_name': 'TemplateFileBlock', '_ormbases': ['selfpublish.TemplateBlock']},
            'default_content': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'templateblock_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['selfpublish.TemplateBlock']", 'unique': 'True', 'primary_key': 'True'})
        },
        'selfpublish.templateimageblock': {
            'Meta': {'ordering': "['sequence']", 'object_name': 'TemplateImageBlock', '_ormbases': ['selfpublish.TemplateBlock']},
            'default_content': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'templateblock_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['selfpublish.TemplateBlock']", 'unique': 'True', 'primary_key': 'True'})
        },
        'selfpublish.theme': {
            'Meta': {'ordering': "['name']", 'object_name': 'Theme'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'rank': ('django.db.models.fields.FloatField', [], {'default': '0'})
        }
    }

    complete_apps = ['selfpublish']
