from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Choice, Question

# no fieldsets
# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']
#
# admin.site.register(Question, QuestionAdmin)

# This line makes the form a long list
# class ChoiceInline(admin.StackedInline):

#This line makes the talbe inline and easier to read
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)

# removing this line to give the option to add choices while makeing a quesiton
# admin.site.register(Choice)


