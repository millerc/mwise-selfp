# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'AdBlock.display_ad'
        db.alter_column('selfpublish_adblock', 'display_ad_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['selfpublish.DisplayAd'], unique=True, null=True, on_delete=models.SET_NULL))
        # Adding field 'Lead.invitation_code'
        db.add_column('selfpublish_lead', 'invitation_code',
                      self.gf('django.db.models.fields.CharField')(default='c991ff1c-d35b-4c13-8eba-ab27b8646c0f', max_length=36),
                      keep_default=False)

    def backwards(self, orm):

        # Changing field 'AdBlock.display_ad'
        db.alter_column('selfpublish_adblock', 'display_ad_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['selfpublish.DisplayAd'], unique=True, null=True))
        # Deleting field 'Lead.invitation_code'
        db.delete_column('selfpublish_lead', 'invitation_code')

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
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'})
        },
        'selfpublish.ad': {
            'Meta': {'object_name': 'Ad'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lead': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['selfpublish.Lead']", 'null': 'True', 'blank': 'True'}),
            'publication': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['selfpublish.Publication']"}),
            'setup_done': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'setup_key': ('django.db.models.fields.CharField', [], {'default': "'b6682717-3587-4756-92a7-cc155a77bdee'", 'max_length': '36'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        'selfpublish.adblock': {
            'Meta': {'ordering': "['template_block__sequence']", 'object_name': 'AdBlock', '_ormbases': ['selfpublish.Block']},
            'ad_price_level': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['selfpublish.AdPriceLevel']"}),
            'block_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['selfpublish.Block']", 'unique': 'True', 'primary_key': 'True'}),
            'display_ad': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['selfpublish.DisplayAd']", 'unique': 'True', 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'price': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'template_ad_block': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['selfpublish.TemplateAdBlock']"})
        },
        'selfpublish.adline': {
            'Meta': {'ordering': "['sequence']", 'object_name': 'AdLine'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'line_ad': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['selfpublish.LineAd']"}),
            'sequence': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'selfpublish.adpricelevel': {
            'Meta': {'ordering': "['name']", 'object_name': 'AdPriceLevel'},
            'ad_size': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['selfpublish.AdSize']"}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'price': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        'selfpublish.adsize': {
            'Meta': {'ordering': "['name']", 'object_name': 'AdSize'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'height': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'width': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        'selfpublish.block': {
            'Meta': {'ordering': "['template_block__sequence']", 'object_name': 'Block'},
            'filled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'layout': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['selfpublish.Layout']"}),
            'template_block': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['selfpublish.TemplateBlock']", 'null': 'True', 'blank': 'True'})
        },
        'selfpublish.blocktype': {
            'Meta': {'ordering': "['label']", 'object_name': 'BlockType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'selfpublish.charblock': {
            'Meta': {'ordering': "['template_block__sequence']", 'object_name': 'CharBlock', '_ormbases': ['selfpublish.Block']},
            'block_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['selfpublish.Block']", 'unique': 'True', 'primary_key': 'True'}),
            'content': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'template_char_block': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['selfpublish.TemplateCharBlock']"})
        },
        'selfpublish.cover': {
            'Meta': {'object_name': 'Cover', '_ormbases': ['selfpublish.Layout']},
            'cover_template': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['selfpublish.CoverTemplate']"}),
            'layout_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['selfpublish.Layout']", 'unique': 'True', 'primary_key': 'True'}),
            'publication': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['selfpublish.Publication']", 'unique': 'True'})
        },
        'selfpublish.coverdesign': {
            'Meta': {'object_name': 'CoverDesign', '_ormbases': ['selfpublish.Design']},
            'design_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['selfpublish.Design']", 'unique': 'True', 'primary_key': 'True'}),
            'template': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['selfpublish.CoverTemplate']"}),
            'theme': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['selfpublish.Theme']", 'unique': 'True'})
        },
        'selfpublish.covertemplate': {
            'Meta': {'ordering': "['name']", 'object_name': 'CoverTemplate', '_ormbases': ['selfpublish.Template']},
            'template_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['selfpublish.Template']", 'unique': 'True', 'primary_key': 'True'})
        },
        'selfpublish.design': {
            'Meta': {'object_name': 'Design'},
            'annotated': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'preview': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        'selfpublish.displayad': {
            'Meta': {'object_name': 'DisplayAd', '_ormbases': ['selfpublish.Ad']},
            'ad_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['selfpublish.Ad']", 'unique': 'True', 'primary_key': 'True'}),
            'content': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        'selfpublish.file': {
            'Meta': {'object_name': 'File'},
            'byline': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        'selfpublish.fileblock': {
            'Meta': {'ordering': "['template_block__sequence']", 'object_name': 'FileBlock', '_ormbases': ['selfpublish.Block']},
            'block_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['selfpublish.Block']", 'unique': 'True', 'primary_key': 'True'}),
            'file': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['selfpublish.File']", 'null': 'True', 'blank': 'True'}),
            'template_file_block': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['selfpublish.TemplateFileBlock']"})
        },
        'selfpublish.image': {
            'Meta': {'object_name': 'Image'},
            'caption': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['selfpublish.ImageCategory']", 'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'credit': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        'selfpublish.imageblock': {
            'Meta': {'ordering': "['template_block__sequence']", 'object_name': 'ImageBlock', '_ormbases': ['selfpublish.Block']},
            'block_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['selfpublish.Block']", 'unique': 'True', 'primary_key': 'True'}),
            'caption': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['selfpublish.Image']", 'null': 'True', 'blank': 'True'}),
            'template_image_block': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['selfpublish.TemplateImageBlock']"})
        },
        'selfpublish.imagecategory': {
            'Meta': {'ordering': "['name']", 'object_name': 'ImageCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        'selfpublish.layout': {
            'Meta': {'object_name': 'Layout'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'preview': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'progress_bar': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'})
        },
        'selfpublish.lead': {
            'Meta': {'ordering': "['organization']", 'object_name': 'Lead'},
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invitation_code': ('django.db.models.fields.CharField', [], {'default': "'3abf0de9-5367-4bce-bd5f-1ffdf154931c'", 'max_length': '36'}),
            'note': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'organization': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'publication': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['selfpublish.Publication']"}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['selfpublish.LeadStatusType']", 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        'selfpublish.leadstatustype': {
            'Meta': {'object_name': 'LeadStatusType', '_ormbases': ['core.StatusType']},
            'statustype_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.StatusType']", 'unique': 'True', 'primary_key': 'True'})
        },
        'selfpublish.linead': {
            'Meta': {'object_name': 'LineAd', '_ormbases': ['selfpublish.Ad']},
            'ad_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['selfpublish.Ad']", 'unique': 'True', 'primary_key': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['selfpublish.LineAdCategory']", 'null': 'True', 'blank': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'selfpublish.lineadcategory': {
            'Meta': {'ordering': "['name']", 'object_name': 'LineAdCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35'})
        },
        'selfpublish.pagecount': {
            'Meta': {'ordering': "['page_count']", 'object_name': 'PageCount'},
            'advertisements': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'decrypted_key': ('django.db.models.fields.CharField', [], {'max_length': '13'}),
            'encrypted_key': ('django.db.models.fields.CharField', [], {'max_length': '44'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'listings': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'maximum_articles': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'maximum_membership': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'minimum_articles': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'minimum_membership': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'page_count': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'revenue': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'setup_fee': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        'selfpublish.publication': {
            'Meta': {'ordering': "['-updated']", 'object_name': 'Publication'},
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'deliverable': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'listing_price': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '299'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'page_count': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['selfpublish.PageCount']"}),
            'progress_bar': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'setup_done': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'setup_key': ('django.db.models.fields.CharField', [], {'default': "'53fb69a7-8d8e-4c29-87c3-00147852e88b'", 'max_length': '36'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['selfpublish.PublicationStatusType']", 'null': 'True', 'blank': 'True'}),
            'theme': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['selfpublish.Theme']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'selfpublish.publicationstatustype': {
            'Meta': {'object_name': 'PublicationStatusType', '_ormbases': ['core.StatusType']},
            'statustype_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.StatusType']", 'unique': 'True', 'primary_key': 'True'})
        },
        'selfpublish.spread': {
            'Meta': {'ordering': "['sequence']", 'object_name': 'Spread', '_ormbases': ['selfpublish.Layout']},
            'layout_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['selfpublish.Layout']", 'unique': 'True', 'primary_key': 'True'}),
            'publication': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['selfpublish.Publication']"}),
            'sequence': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'spread_template': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['selfpublish.SpreadTemplate']"})
        },
        'selfpublish.spreaddesign': {
            'Meta': {'object_name': 'SpreadDesign', '_ormbases': ['selfpublish.Design']},
            'design_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['selfpublish.Design']", 'unique': 'True', 'primary_key': 'True'}),
            'template': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['selfpublish.SpreadTemplate']"}),
            'theme': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['selfpublish.Theme']"})
        },
        'selfpublish.spreadtemplate': {
            'Meta': {'ordering': "['name']", 'object_name': 'SpreadTemplate', '_ormbases': ['selfpublish.Template']},
            'template_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['selfpublish.Template']", 'unique': 'True', 'primary_key': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['selfpublish.SpreadType']"})
        },
        'selfpublish.spreadtype': {
            'Meta': {'object_name': 'SpreadType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'selfpublish.spreadtypemap': {
            'Meta': {'ordering': "['page_count', 'sequence']", 'object_name': 'SpreadTypeMap'},
            'default_template': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['selfpublish.SpreadTemplate']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page_count': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['selfpublish.PageCount']"}),
            'sequence': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'spread_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['selfpublish.SpreadType']"})
        },
        'selfpublish.template': {
            'Meta': {'ordering': "['name']", 'object_name': 'Template'},
            'blocks_text': ('django.db.models.fields.TextField', [], {'default': "'No Blocks'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '7'})
        },
        'selfpublish.templateadblock': {
            'Meta': {'ordering': "['template', 'sequence']", 'object_name': 'TemplateAdBlock', '_ormbases': ['selfpublish.TemplateBlock']},
            'ad_size': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['selfpublish.AdSize']"}),
            'templateblock_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['selfpublish.TemplateBlock']", 'unique': 'True', 'primary_key': 'True'})
        },
        'selfpublish.templateblock': {
            'Meta': {'ordering': "['template', 'sequence']", 'object_name': 'TemplateBlock'},
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sequence': ('django.db.models.fields.IntegerField', [], {}),
            'template': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['selfpublish.Template']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['selfpublish.BlockType']"})
        },
        'selfpublish.templatecharblock': {
            'Meta': {'ordering': "['template', 'sequence']", 'object_name': 'TemplateCharBlock', '_ormbases': ['selfpublish.TemplateBlock']},
            'max_length': ('django.db.models.fields.IntegerField', [], {}),
            'templateblock_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['selfpublish.TemplateBlock']", 'unique': 'True', 'primary_key': 'True'})
        },
        'selfpublish.templatefileblock': {
            'Meta': {'ordering': "['template', 'sequence']", 'object_name': 'TemplateFileBlock', '_ormbases': ['selfpublish.TemplateBlock']},
            'target_word_count': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '500'}),
            'templateblock_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['selfpublish.TemplateBlock']", 'unique': 'True', 'primary_key': 'True'})
        },
        'selfpublish.templateimageblock': {
            'Meta': {'ordering': "['template', 'sequence']", 'object_name': 'TemplateImageBlock', '_ormbases': ['selfpublish.TemplateBlock']},
            'target_height': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'target_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'templateblock_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['selfpublish.TemplateBlock']", 'unique': 'True', 'primary_key': 'True'})
        },
        'selfpublish.theme': {
            'Meta': {'ordering': "['name']", 'object_name': 'Theme'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'rank': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '15'}),
            'swatch': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['selfpublish']