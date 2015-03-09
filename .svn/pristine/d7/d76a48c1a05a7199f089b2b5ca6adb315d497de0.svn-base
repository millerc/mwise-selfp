# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'PublicationTemplateStyle'
        db.create_table('selfpublish_publicationtemplatestyle', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255, db_index=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('keywords', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('cover_preview', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('rank', self.gf('django.db.models.fields.FloatField')(default=0)),
        ))
        db.send_create_signal('selfpublish', ['PublicationTemplateStyle'])

        # Adding M2M table for field suggested_templates on 'PublicationTemplateStyle'
        db.create_table('selfpublish_publicationtemplatestyle_suggested_templates', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_publicationtemplatestyle', models.ForeignKey(orm['selfpublish.publicationtemplatestyle'], null=False)),
            ('to_publicationtemplatestyle', models.ForeignKey(orm['selfpublish.publicationtemplatestyle'], null=False))
        ))
        db.create_unique('selfpublish_publicationtemplatestyle_suggested_templates', ['from_publicationtemplatestyle_id', 'to_publicationtemplatestyle_id'])

        # Adding model 'LayoutTemplate'
        db.create_table('selfpublish_layouttemplate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('preview', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('annotated_preview', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('selfpublish', ['LayoutTemplate'])

        # Adding model 'PublicationTemplate'
        db.create_table('selfpublish_publicationtemplate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('style', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['selfpublish.PublicationTemplateStyle'])),
            ('page_count', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('minimum_suggested_membership', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('maximum_suggested_membership', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal('selfpublish', ['PublicationTemplate'])

        # Adding model 'LayoutTemplateUse'
        db.create_table('selfpublish_layouttemplateuse', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('publication_template', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['selfpublish.PublicationTemplate'])),
            ('layout_template', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['selfpublish.LayoutTemplate'])),
            ('sequence', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal('selfpublish', ['LayoutTemplateUse'])

        # Adding model 'LayoutTemplateBlock'
        db.create_table('selfpublish_layouttemplateblock', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('layout_template', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['selfpublish.LayoutTemplate'])),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('sequence', self.gf('django.db.models.fields.IntegerField')()),
            ('required', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('help_text', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('selfpublish', ['LayoutTemplateBlock'])

        # Adding model 'LayoutTemplateCharBlock'
        db.create_table('selfpublish_layouttemplatecharblock', (
            ('layouttemplateblock_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['selfpublish.LayoutTemplateBlock'], unique=True, primary_key=True)),
            ('default_content', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('max_length', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('selfpublish', ['LayoutTemplateCharBlock'])

        # Adding model 'LayoutTemplateFileBlock'
        db.create_table('selfpublish_layouttemplatefileblock', (
            ('layouttemplateblock_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['selfpublish.LayoutTemplateBlock'], unique=True, primary_key=True)),
            ('default_content', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('selfpublish', ['LayoutTemplateFileBlock'])

        # Adding model 'LayoutTemplateImageBlock'
        db.create_table('selfpublish_layouttemplateimageblock', (
            ('layouttemplateblock_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['selfpublish.LayoutTemplateBlock'], unique=True, primary_key=True)),
            ('default_content', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('selfpublish', ['LayoutTemplateImageBlock'])

        # Adding model 'PublicationStatusType'
        db.create_table('selfpublish_publicationstatustype', (
            ('statustype_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.StatusType'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('selfpublish', ['PublicationStatusType'])

        # Adding model 'Publication'
        db.create_table('selfpublish_publication', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('template', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['selfpublish.PublicationTemplate'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['selfpublish.PublicationStatusType'], null=True, blank=True)),
            ('deliverable', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('selfpublish', ['Publication'])

        # Adding model 'Layout'
        db.create_table('selfpublish_layout', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('publication', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['selfpublish.Publication'])),
            ('layout_template_use', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['selfpublish.LayoutTemplateUse'])),
        ))
        db.send_create_signal('selfpublish', ['Layout'])

        # Adding model 'LayoutBlock'
        db.create_table('selfpublish_layoutblock', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('layout', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['selfpublish.Layout'])),
            ('template_block', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['selfpublish.LayoutTemplateBlock'])),
        ))
        db.send_create_signal('selfpublish', ['LayoutBlock'])

        # Adding model 'LayoutCharBlock'
        db.create_table('selfpublish_layoutcharblock', (
            ('layoutblock_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['selfpublish.LayoutBlock'], unique=True, primary_key=True)),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('selfpublish', ['LayoutCharBlock'])

        # Adding model 'LayoutImageBlock'
        db.create_table('selfpublish_layoutimageblock', (
            ('layoutblock_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['selfpublish.LayoutBlock'], unique=True, primary_key=True)),
            ('content', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('selfpublish', ['LayoutImageBlock'])

        # Adding model 'LayoutFileBlock'
        db.create_table('selfpublish_layoutfileblock', (
            ('layoutblock_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['selfpublish.LayoutBlock'], unique=True, primary_key=True)),
            ('content', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('selfpublish', ['LayoutFileBlock'])


    def backwards(self, orm):
        
        # Deleting model 'PublicationTemplateStyle'
        db.delete_table('selfpublish_publicationtemplatestyle')

        # Removing M2M table for field suggested_templates on 'PublicationTemplateStyle'
        db.delete_table('selfpublish_publicationtemplatestyle_suggested_templates')

        # Deleting model 'LayoutTemplate'
        db.delete_table('selfpublish_layouttemplate')

        # Deleting model 'PublicationTemplate'
        db.delete_table('selfpublish_publicationtemplate')

        # Deleting model 'LayoutTemplateUse'
        db.delete_table('selfpublish_layouttemplateuse')

        # Deleting model 'LayoutTemplateBlock'
        db.delete_table('selfpublish_layouttemplateblock')

        # Deleting model 'LayoutTemplateCharBlock'
        db.delete_table('selfpublish_layouttemplatecharblock')

        # Deleting model 'LayoutTemplateFileBlock'
        db.delete_table('selfpublish_layouttemplatefileblock')

        # Deleting model 'LayoutTemplateImageBlock'
        db.delete_table('selfpublish_layouttemplateimageblock')

        # Deleting model 'PublicationStatusType'
        db.delete_table('selfpublish_publicationstatustype')

        # Deleting model 'Publication'
        db.delete_table('selfpublish_publication')

        # Deleting model 'Layout'
        db.delete_table('selfpublish_layout')

        # Deleting model 'LayoutBlock'
        db.delete_table('selfpublish_layoutblock')

        # Deleting model 'LayoutCharBlock'
        db.delete_table('selfpublish_layoutcharblock')

        # Deleting model 'LayoutImageBlock'
        db.delete_table('selfpublish_layoutimageblock')

        # Deleting model 'LayoutFileBlock'
        db.delete_table('selfpublish_layoutfileblock')


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
        'selfpublish.layout': {
            'Meta': {'object_name': 'Layout'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'layout_template_use': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['selfpublish.LayoutTemplateUse']"}),
            'publication': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['selfpublish.Publication']"})
        },
        'selfpublish.layoutblock': {
            'Meta': {'object_name': 'LayoutBlock'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'layout': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['selfpublish.Layout']"}),
            'template_block': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['selfpublish.LayoutTemplateBlock']"})
        },
        'selfpublish.layoutcharblock': {
            'Meta': {'object_name': 'LayoutCharBlock', '_ormbases': ['selfpublish.LayoutBlock']},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'layoutblock_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['selfpublish.LayoutBlock']", 'unique': 'True', 'primary_key': 'True'})
        },
        'selfpublish.layoutfileblock': {
            'Meta': {'object_name': 'LayoutFileBlock', '_ormbases': ['selfpublish.LayoutBlock']},
            'content': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'layoutblock_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['selfpublish.LayoutBlock']", 'unique': 'True', 'primary_key': 'True'})
        },
        'selfpublish.layoutimageblock': {
            'Meta': {'object_name': 'LayoutImageBlock', '_ormbases': ['selfpublish.LayoutBlock']},
            'content': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'layoutblock_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['selfpublish.LayoutBlock']", 'unique': 'True', 'primary_key': 'True'})
        },
        'selfpublish.layouttemplate': {
            'Meta': {'ordering': "['name']", 'object_name': 'LayoutTemplate'},
            'annotated_preview': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'preview': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        'selfpublish.layouttemplateblock': {
            'Meta': {'ordering': "['sequence']", 'object_name': 'LayoutTemplateBlock'},
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'layout_template': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['selfpublish.LayoutTemplate']"}),
            'required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sequence': ('django.db.models.fields.IntegerField', [], {})
        },
        'selfpublish.layouttemplatecharblock': {
            'Meta': {'ordering': "['sequence']", 'object_name': 'LayoutTemplateCharBlock', '_ormbases': ['selfpublish.LayoutTemplateBlock']},
            'default_content': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'layouttemplateblock_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['selfpublish.LayoutTemplateBlock']", 'unique': 'True', 'primary_key': 'True'}),
            'max_length': ('django.db.models.fields.IntegerField', [], {})
        },
        'selfpublish.layouttemplatefileblock': {
            'Meta': {'ordering': "['sequence']", 'object_name': 'LayoutTemplateFileBlock', '_ormbases': ['selfpublish.LayoutTemplateBlock']},
            'default_content': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'layouttemplateblock_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['selfpublish.LayoutTemplateBlock']", 'unique': 'True', 'primary_key': 'True'})
        },
        'selfpublish.layouttemplateimageblock': {
            'Meta': {'ordering': "['sequence']", 'object_name': 'LayoutTemplateImageBlock', '_ormbases': ['selfpublish.LayoutTemplateBlock']},
            'default_content': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'layouttemplateblock_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['selfpublish.LayoutTemplateBlock']", 'unique': 'True', 'primary_key': 'True'})
        },
        'selfpublish.layouttemplateuse': {
            'Meta': {'ordering': "['sequence']", 'object_name': 'LayoutTemplateUse'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'layout_template': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['selfpublish.LayoutTemplate']"}),
            'publication_template': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['selfpublish.PublicationTemplate']"}),
            'sequence': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        'selfpublish.publication': {
            'Meta': {'ordering': "['-updated']", 'object_name': 'Publication'},
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'deliverable': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['selfpublish.PublicationStatusType']", 'null': 'True', 'blank': 'True'}),
            'template': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['selfpublish.PublicationTemplate']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'selfpublish.publicationstatustype': {
            'Meta': {'object_name': 'PublicationStatusType', '_ormbases': ['core.StatusType']},
            'statustype_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.StatusType']", 'unique': 'True', 'primary_key': 'True'})
        },
        'selfpublish.publicationtemplate': {
            'Meta': {'ordering': "['page_count']", 'object_name': 'PublicationTemplate'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'layout_templates': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['selfpublish.LayoutTemplate']", 'through': "orm['selfpublish.LayoutTemplateUse']", 'symmetrical': 'False'}),
            'maximum_suggested_membership': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'minimum_suggested_membership': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'page_count': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'style': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['selfpublish.PublicationTemplateStyle']"})
        },
        'selfpublish.publicationtemplatestyle': {
            'Meta': {'ordering': "['name']", 'object_name': 'PublicationTemplateStyle'},
            'cover_preview': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'rank': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'}),
            'suggested_templates': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'suggested_templates_rel_+'", 'null': 'True', 'to': "orm['selfpublish.PublicationTemplateStyle']"})
        }
    }

    complete_apps = ['selfpublish']
