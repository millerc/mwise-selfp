# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'TemplateFileBlock.default_content'
        db.delete_column('selfpublish_templatefileblock', 'default_content')

        # Deleting field 'TemplateBlock.required'
        db.delete_column('selfpublish_templateblock', 'required')

        # Deleting field 'TemplateImageBlock.default_content'
        db.delete_column('selfpublish_templateimageblock', 'default_content')

        # Deleting field 'TemplateCharBlock.default_content'
        db.delete_column('selfpublish_templatecharblock', 'default_content')


    def backwards(self, orm):
        
        # Adding field 'TemplateFileBlock.default_content'
        db.add_column('selfpublish_templatefileblock', 'default_content', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'TemplateBlock.required'
        db.add_column('selfpublish_templateblock', 'required', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'TemplateImageBlock.default_content'
        db.add_column('selfpublish_templateimageblock', 'default_content', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'TemplateCharBlock.default_content'
        db.add_column('selfpublish_templatecharblock', 'default_content', self.gf('django.db.models.fields.CharField')(default='changeme', max_length=255), keep_default=False)


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
        'selfpublish.blocktype': {
            'Meta': {'ordering': "['label']", 'object_name': 'BlockType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '255'})
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
            'byline': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'selfpublish.imageblock': {
            'Meta': {'object_name': 'ImageBlock', '_ormbases': ['selfpublish.Block']},
            'block_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['selfpublish.Block']", 'unique': 'True', 'primary_key': 'True'}),
            'caption': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'credit': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
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
            'sequence': ('django.db.models.fields.IntegerField', [], {}),
            'template': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['selfpublish.Template']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['selfpublish.BlockType']"})
        },
        'selfpublish.templatecharblock': {
            'Meta': {'ordering': "['sequence']", 'object_name': 'TemplateCharBlock', '_ormbases': ['selfpublish.TemplateBlock']},
            'max_length': ('django.db.models.fields.IntegerField', [], {}),
            'templateblock_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['selfpublish.TemplateBlock']", 'unique': 'True', 'primary_key': 'True'})
        },
        'selfpublish.templatefileblock': {
            'Meta': {'ordering': "['sequence']", 'object_name': 'TemplateFileBlock', '_ormbases': ['selfpublish.TemplateBlock']},
            'target_word_count': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '500'}),
            'templateblock_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['selfpublish.TemplateBlock']", 'unique': 'True', 'primary_key': 'True'})
        },
        'selfpublish.templateimageblock': {
            'Meta': {'ordering': "['sequence']", 'object_name': 'TemplateImageBlock', '_ormbases': ['selfpublish.TemplateBlock']},
            'target_height': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'target_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
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
