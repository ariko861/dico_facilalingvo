from django.contrib import admin
from django.contrib.admin.helpers import ActionForm
from django import forms
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from multidico.models import Language, Category, Word, WordModified, SubCategory, Number
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin

# Register your models here.
def export_selected_objects(modeladmin, request, queryset):
    selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
    ct = ContentType.objects.get_for_model(queryset.model)
    return HttpResponseRedirect("/export/?ct=%s&ids=%s" % (ct.pk, ",".join(selected)))

def delete_selected(modeladmin, request, queryset):
	for wordmodif in queryset:
		if wordmodif.word_origin:
			wordmodif.word_origin.modified_by.clear()
		wordmodif.delete()
		
			


def confirm_modifications(modeladmin, request, queryset):
	for wordmodif in queryset:
		if not wordmodif.word_origin:
			
			new_word = Word(
						language=wordmodif.language,
						category=wordmodif.category,
						learning_progress=wordmodif.learning_progress,
						english=wordmodif.english,
						english_local_prononciation=wordmodif.english_local_prononciation,
						french=wordmodif.french,
						french_local_prononciation=wordmodif.french_local_prononciation,
						local=wordmodif.local,
						prononciation=wordmodif.prononciation,
			)
			new_word.save()
		else:	
			old_word=wordmodif.word_origin
			old_word.category = wordmodif.category
			old_word.learning_progress = wordmodif.learning_progress
			old_word.english = wordmodif.english
			old_word.english_local_prononciation = wordmodif.english_local_prononciation
			old_word.french = wordmodif.french
			old_word.french_local_prononciation = wordmodif.french_local_prononciation
			old_word.local = wordmodif.local
			old_word.prononciation = wordmodif.prononciation
			
			
			old_word.modified_by.clear()
			old_word.save()
		wordmodif.delete()

def special_copy_to_language(modeladmin, request, queryset):
	lang = request.POST['language_to_copy']
	for word in queryset:
		new_word = Word(
						language=Language.objects.get(id=lang),
						category=word.category,
						subcategory=word.subcategory,
						learning_progress=word.learning_progress,
						english=word.english,
						english_local_prononciation='-',
						french=word.french,
						french_local_prononciation='-',
		)
		new_word.save()
		
def special_copy_numbers_to_language(modeladmin, request, queryset):
	lang = request.POST['language_to_copy']
	for number in queryset:
		new_number = Number(
						language=Language.objects.get(id=lang),
						digit=number.digit,
						english=number.english,
						english_local_prononciation='-',
						french=number.french,
						french_local_prononciation='-',
		)
		new_number.save()
		

class CopyToNewLanguageForm(ActionForm):
	language_to_copy = forms.ModelChoiceField(queryset = Language.objects.all(),required=False)

class WordResource(resources.ModelResource):

	class Meta:
		model = Word


class WordAdmin(ImportExportActionModelAdmin):
#	fields=['english','local','category']
	list_display=['english','french','local','category','subcategory','learning_progress','language']
	search_fields=['english','french','local']
	list_filter=['language__language_name','category__category_name','learning_progress']
	ordering=['language__language_name','category','subcategory','english']
	list_max_show_all = 1000
	action_form = CopyToNewLanguageForm
	actions = [special_copy_to_language]
	resource_class = WordResource

class NumberAdmin(admin.ModelAdmin):
#	fields=['english','local','category']
	list_display=['digit','english','french','local','language']
	search_fields=['digit','english','french','local']
	list_filter=['language__language_name']
	ordering=['language__language_name','digit']
	list_max_show_all = 1000
	action_form = CopyToNewLanguageForm
	actions = [special_copy_numbers_to_language]


class WordModifAdmin(admin.ModelAdmin):
	list_display=['english','french','local','category','modifier','learning_progress','language']
	search_fields=['english','french','local']
	list_filter=['language__language_name','modifier__username','category','learning_progress']
	ordering=['language__language_name','category','english']
	list_max_show_all = 1000
	actions=[confirm_modifications, delete_selected]


class WordResourceAdmin(ImportExportActionModelAdmin):
	resource_class = WordResource


admin.site.register(Language)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Word, WordAdmin)
admin.site.register(WordModified, WordModifAdmin)
admin.site.register(Number, NumberAdmin)
