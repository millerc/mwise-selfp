# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Template'
        db.create_table('marketwise_template', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255, db_index=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('keywords', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('swatch', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('preview', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('annotated_preview', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('rank', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('credits_required', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('marketwise', ['Template'])

        # Adding M2M table for field color_variations on 'Template'
        db.create_table('marketwise_template_color_variations', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_template', models.ForeignKey(orm['marketwise.template'], null=False)),
            ('to_template', models.ForeignKey(orm['marketwise.template'], null=False))
        ))
        db.create_unique('marketwise_template_color_variations', ['from_template_id', 'to_template_id'])

        # Adding M2M table for field related_templates on 'Template'
        db.create_table('marketwise_template_related_templates', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_template', models.ForeignKey(orm['marketwise.template'], null=False)),
            ('to_template', models.ForeignKey(orm['marketwise.template'], null=False))
        ))
        db.create_unique('marketwise_template_related_templates', ['from_template_id', 'to_template_id'])

        # Adding M2M table for field suggested_templates on 'Template'
        db.create_table('marketwise_template_suggested_templates', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_template', models.ForeignKey(orm['marketwise.template'], null=False)),
            ('to_template', models.ForeignKey(orm['marketwise.template'], null=False))
        ))
        db.create_unique('marketwise_template_suggested_templates', ['from_template_id', 'to_template_id'])

        # Adding model 'TemplateType'
        db.create_table('marketwise_templatetype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255, db_index=True)),
            ('parent_type', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='children', null=True, to=orm['marketwise.TemplateType'])),
        ))
        db.send_create_signal('marketwise', ['TemplateType'])

        # Adding model 'TemplateTypeIndustry'
        db.create_table('marketwise_templatetypeindustry', (
            ('templatetype_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['marketwise.TemplateType'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('marketwise', ['TemplateTypeIndustry'])

        # Adding model 'TemplateTypePurpose'
        db.create_table('marketwise_templatetypepurpose', (
            ('templatetype_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['marketwise.TemplateType'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('marketwise', ['TemplateTypePurpose'])

        # Adding M2M table for field industries on 'TemplateTypePurpose'
        db.create_table('marketwise_templatetypepurpose_industries', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('templatetypepurpose', models.ForeignKey(orm['marketwise.templatetypepurpose'], null=False)),
            ('templatetypeindustry', models.ForeignKey(orm['marketwise.templatetypeindustry'], null=False))
        ))
        db.create_unique('marketwise_templatetypepurpose_industries', ['templatetypepurpose_id', 'templatetypeindustry_id'])

        # Adding model 'TemplateTypeFormat'
        db.create_table('marketwise_templatetypeformat', (
            ('templatetype_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['marketwise.TemplateType'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('marketwise', ['TemplateTypeFormat'])

        # Adding model 'TemplateTypeColor'
        db.create_table('marketwise_templatetypecolor', (
            ('templatetype_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['marketwise.TemplateType'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('marketwise', ['TemplateTypeColor'])

        # Adding model 'TemplateClassification'
        db.create_table('marketwise_templateclassification', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('template', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['marketwise.Template'])),
        ))
        db.send_create_signal('marketwise', ['TemplateClassification'])

        # Adding model 'TemplateClassificationIndustry'
        db.create_table('marketwise_templateclassificationindustry', (
            ('templateclassification_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['marketwise.TemplateClassification'], unique=True, primary_key=True)),
            ('industry', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['marketwise.TemplateTypeIndustry'])),
        ))
        db.send_create_signal('marketwise', ['TemplateClassificationIndustry'])

        # Adding model 'TemplateClassificationPurpose'
        db.create_table('marketwise_templateclassificationpurpose', (
            ('templateclassification_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['marketwise.TemplateClassification'], unique=True, primary_key=True)),
            ('purpose', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['marketwise.TemplateTypePurpose'])),
        ))
        db.send_create_signal('marketwise', ['TemplateClassificationPurpose'])

        # Adding model 'TemplateClassificationFormat'
        db.create_table('marketwise_templateclassificationformat', (
            ('templateclassification_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['marketwise.TemplateClassification'], unique=True, primary_key=True)),
            ('format', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['marketwise.TemplateTypeFormat'])),
        ))
        db.send_create_signal('marketwise', ['TemplateClassificationFormat'])

        # Adding model 'TemplateClassificationColor'
        db.create_table('marketwise_templateclassificationcolor', (
            ('templateclassification_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['marketwise.TemplateClassification'], unique=True, primary_key=True)),
            ('color', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['marketwise.TemplateTypeColor'])),
        ))
        db.send_create_signal('marketwise', ['TemplateClassificationColor'])

        # Adding model 'TemplateBlock'
        db.create_table('marketwise_templateblock', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('template', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['marketwise.Template'])),
            ('required', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('sequence', self.gf('django.db.models.fields.IntegerField')()),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('help_text', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('profile_field', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal('marketwise', ['TemplateBlock'])

        # Adding model 'TemplateCharBlock'
        db.create_table('marketwise_templatecharblock', (
            ('templateblock_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['marketwise.TemplateBlock'], unique=True, primary_key=True)),
            ('default_content', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('max_length', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('marketwise', ['TemplateCharBlock'])

        # Adding model 'TemplateTextBlock'
        db.create_table('marketwise_templatetextblock', (
            ('templateblock_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['marketwise.TemplateBlock'], unique=True, primary_key=True)),
            ('default_content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('marketwise', ['TemplateTextBlock'])

        # Adding model 'TemplateImageBlock'
        db.create_table('marketwise_templateimageblock', (
            ('templateblock_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['marketwise.TemplateBlock'], unique=True, primary_key=True)),
            ('default_content', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('marketwise', ['TemplateImageBlock'])

        # Adding model 'CustomizationStatusType'
        db.create_table('marketwise_customizationstatustype', (
            ('statustype_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.StatusType'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('marketwise', ['CustomizationStatusType'])

        # Adding model 'Customization'
        db.create_table('marketwise_customization', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('template', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['marketwise.Template'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['marketwise.CustomizationStatusType'], null=True, blank=True)),
            ('deliverable', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('marketwise', ['Customization'])

        # Adding model 'Block'
        db.create_table('marketwise_block', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('customization', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['marketwise.Customization'])),
            ('template_block', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['marketwise.TemplateBlock'])),
        ))
        db.send_create_signal('marketwise', ['Block'])

        # Adding model 'ImageBlock'
        db.create_table('marketwise_imageblock', (
            ('block_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['marketwise.Block'], unique=True, primary_key=True)),
            ('content', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('marketwise', ['ImageBlock'])

        # Adding model 'CharBlock'
        db.create_table('marketwise_charblock', (
            ('block_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['marketwise.Block'], unique=True, primary_key=True)),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('marketwise', ['CharBlock'])

        # Adding model 'TextBlock'
        db.create_table('marketwise_textblock', (
            ('block_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['marketwise.Block'], unique=True, primary_key=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('marketwise', ['TextBlock'])


    def backwards(self, orm):
        
        # Deleting model 'Template'
        db.delete_table('marketwise_template')

        # Removing M2M table for field color_variations on 'Template'
        db.delete_table('marketwise_template_color_variations')

        # Removing M2M table for field related_templates on 'Template'
        db.delete_table('marketwise_template_related_templates')

        # Removing M2M table for field suggested_templates on 'Template'
        db.delete_table('marketwise_template_suggested_templates')

        # Deleting model 'TemplateType'
        db.delete_table('marketwise_templatetype')

        # Deleting model 'TemplateTypeIndustry'
        db.delete_table('marketwise_templatetypeindustry')

        # Deleting model 'TemplateTypePurpose'
        db.delete_table('marketwise_templatetypepurpose')

        # Removing M2M table for field industries on 'TemplateTypePurpose'
        db.delete_table('marketwise_templatetypepurpose_industries')

        # Deleting model 'TemplateTypeFormat'
        db.delete_table('marketwise_templatetypeformat')

        # Deleting model 'TemplateTypeColor'
        db.delete_table('marketwise_templatetypecolor')

        # Deleting model 'TemplateClassification'
        db.delete_table('marketwise_templateclassification')

        # Deleting model 'TemplateClassificationIndustry'
        db.delete_table('marketwise_templateclassificationindustry')

        # Deleting model 'TemplateClassificationPurpose'
        db.delete_table('marketwise_templateclassificationpurpose')

        # Deleting model 'TemplateClassificationFormat'
        db.delete_table('marketwise_templateclassificationformat')

        # Deleting model 'TemplateClassificationColor'
        db.delete_table('marketwise_templateclassificationcolor')

        # Deleting model 'TemplateBlock'
        db.delete_table('marketwise_templateblock')

        # Deleting model 'TemplateCharBlock'
        db.delete_table('marketwise_templatecharblock')

        # Deleting model 'TemplateTextBlock'
        db.delete_table('marketwise_templatetextblock')

        # Deleting model 'TemplateImageBlock'
        db.delete_table('marketwise_templateimageblock')

        # Deleting model 'CustomizationStatusType'
        db.delete_table('marketwise_customizationstatustype')

        # Deleting model 'Customization'
        db.delete_table('marketwise_customization')

        # Deleting model 'Block'
        db.delete_table('marketwise_block')

        # Deleting model 'ImageBlock'
        db.delete_table('marketwise_imageblock')

        # Deleting model 'CharBlock'
        db.delete_table('marketwise_charblock')

        # Deleting model 'TextBlock'
        db.delete_table('marketwise_textblock')


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
        'marketwise.block': {
            'Meta': {'object_name': 'Block'},
            'customization': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['marketwise.Customization']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'template_block': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['marketwise.TemplateBlock']"})
        },
        'marketwise.charblock': {
            'Meta': {'object_name': 'CharBlock', '_ormbases': ['marketwise.Block']},
            'block_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['marketwise.Block']", 'unique': 'True', 'primary_key': 'True'}),
            'content': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'marketwise.customization': {
            'Meta': {'ordering': "['-updated']", 'object_name': 'Customization'},
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'deliverable': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['marketwise.CustomizationStatusType']", 'null': 'True', 'blank': 'True'}),
            'template': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['marketwise.Template']"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'marketwise.customizationstatustype': {
            'Meta': {'object_name': 'CustomizationStatusType', '_ormbases': ['core.StatusType']},
            'statustype_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.StatusType']", 'unique': 'True', 'primary_key': 'True'})
        },
        'marketwise.imageblock': {
            'Meta': {'object_name': 'ImageBlock', '_ormbases': ['marketwise.Block']},
            'block_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['marketwise.Block']", 'unique': 'True', 'primary_key': 'True'}),
            'content': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        'marketwise.template': {
            'Meta': {'ordering': "['-rank']", 'object_name': 'Template'},
            'annotated_preview': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'color_variations': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'color_variations_rel_+'", 'null': 'True', 'to': "orm['marketwise.Template']"}),
            'credits_required': ('django.db.models.fields.IntegerField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'preview': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'rank': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'related_templates': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'related_templates_rel_+'", 'null': 'True', 'to': "orm['marketwise.Template']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'}),
            'suggested_templates': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'suggested_templates_rel_+'", 'null': 'True', 'to': "orm['marketwise.Template']"}),
            'swatch': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'marketwise.templateblock': {
            'Meta': {'ordering': "['sequence']", 'object_name': 'TemplateBlock'},
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'profile_field': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sequence': ('django.db.models.fields.IntegerField', [], {}),
            'template': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['marketwise.Template']"})
        },
        'marketwise.templatecharblock': {
            'Meta': {'ordering': "['sequence']", 'object_name': 'TemplateCharBlock', '_ormbases': ['marketwise.TemplateBlock']},
            'default_content': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'max_length': ('django.db.models.fields.IntegerField', [], {}),
            'templateblock_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['marketwise.TemplateBlock']", 'unique': 'True', 'primary_key': 'True'})
        },
        'marketwise.templateclassification': {
            'Meta': {'object_name': 'TemplateClassification'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'template': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['marketwise.Template']"})
        },
        'marketwise.templateclassificationcolor': {
            'Meta': {'object_name': 'TemplateClassificationColor', '_ormbases': ['marketwise.TemplateClassification']},
            'color': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['marketwise.TemplateTypeColor']"}),
            'templateclassification_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['marketwise.TemplateClassification']", 'unique': 'True', 'primary_key': 'True'})
        },
        'marketwise.templateclassificationformat': {
            'Meta': {'object_name': 'TemplateClassificationFormat', '_ormbases': ['marketwise.TemplateClassification']},
            'format': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['marketwise.TemplateTypeFormat']"}),
            'templateclassification_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['marketwise.TemplateClassification']", 'unique': 'True', 'primary_key': 'True'})
        },
        'marketwise.templateclassificationindustry': {
            'Meta': {'object_name': 'TemplateClassificationIndustry', '_ormbases': ['marketwise.TemplateClassification']},
            'industry': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['marketwise.TemplateTypeIndustry']"}),
            'templateclassification_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['marketwise.TemplateClassification']", 'unique': 'True', 'primary_key': 'True'})
        },
        'marketwise.templateclassificationpurpose': {
            'Meta': {'object_name': 'TemplateClassificationPurpose', '_ormbases': ['marketwise.TemplateClassification']},
            'purpose': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['marketwise.TemplateTypePurpose']"}),
            'templateclassification_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['marketwise.TemplateClassification']", 'unique': 'True', 'primary_key': 'True'})
        },
        'marketwise.templateimageblock': {
            'Meta': {'ordering': "['sequence']", 'object_name': 'TemplateImageBlock', '_ormbases': ['marketwise.TemplateBlock']},
            'default_content': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'templateblock_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['marketwise.TemplateBlock']", 'unique': 'True', 'primary_key': 'True'})
        },
        'marketwise.templatetextblock': {
            'Meta': {'ordering': "['sequence']", 'object_name': 'TemplateTextBlock', '_ormbases': ['marketwise.TemplateBlock']},
            'default_content': ('django.db.models.fields.TextField', [], {}),
            'templateblock_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['marketwise.TemplateBlock']", 'unique': 'True', 'primary_key': 'True'})
        },
        'marketwise.templatetype': {
            'Meta': {'ordering': "['parent_type__description', 'description']", 'object_name': 'TemplateType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['marketwise.TemplateType']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'})
        },
        'marketwise.templatetypecolor': {
            'Meta': {'ordering': "['parent_type__description', 'description']", 'object_name': 'TemplateTypeColor', '_ormbases': ['marketwise.TemplateType']},
            'templatetype_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['marketwise.TemplateType']", 'unique': 'True', 'primary_key': 'True'})
        },
        'marketwise.templatetypeformat': {
            'Meta': {'ordering': "['parent_type__description', 'description']", 'object_name': 'TemplateTypeFormat', '_ormbases': ['marketwise.TemplateType']},
            'templatetype_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['marketwise.TemplateType']", 'unique': 'True', 'primary_key': 'True'})
        },
        'marketwise.templatetypeindustry': {
            'Meta': {'ordering': "['parent_type__description', 'description']", 'object_name': 'TemplateTypeIndustry', '_ormbases': ['marketwise.TemplateType']},
            'templatetype_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['marketwise.TemplateType']", 'unique': 'True', 'primary_key': 'True'})
        },
        'marketwise.templatetypepurpose': {
            'Meta': {'ordering': "['parent_type__description', 'description']", 'object_name': 'TemplateTypePurpose', '_ormbases': ['marketwise.TemplateType']},
            'industries': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['marketwise.TemplateTypeIndustry']", 'symmetrical': 'False'}),
            'templatetype_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['marketwise.TemplateType']", 'unique': 'True', 'primary_key': 'True'})
        },
        'marketwise.textblock': {
            'Meta': {'object_name': 'TextBlock', '_ormbases': ['marketwise.Block']},
            'block_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['marketwise.Block']", 'unique': 'True', 'primary_key': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['marketwise']
