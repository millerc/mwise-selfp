from django.contrib import admin

from bugs.models import *

class AttachmentInline(admin.TabularInline):
    model = Attachment
    extra = 1

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'priority', 'assigned_to', 'submitter', 'submitted_date', 'modified_date')
    list_filter = ('priority', 'status', 'assigned_to', 'submitted_date')
    search_fields = ('title', 'description',)
    inlines = [AttachmentInline,CommentInline]

admin.site.register(Ticket, TicketAdmin)