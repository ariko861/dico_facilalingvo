# -*- coding: utf-8 -*-
from django import forms
from .models import Category
from django.contrib import auth
from django.utils.translation import ugettext_lazy as _

class WordForm(forms.Form):
	category = forms.ModelChoiceField(queryset = Category.objects.all(), widget=forms.Select, label = _("Category"))
	learning_progress = forms.ChoiceField(choices=(('B', _('Beginner')), ('I', _('Intermediate')),('A',_('Advanced')),('F',_('Fluent')),('S',_('Slang'))), widget=forms.Select, label = _("learning level"))
	english = forms.CharField(max_length=300, label=_("English"))
	english_local_prononciation=forms.CharField(max_length=300, label=_("Local pronunciation of English word"))
	french=forms.CharField(max_length=300, label=_("French"))
	french_local_prononciation=forms.CharField(max_length=300, label=_("Local pronunciation of French word"))
	local=forms.CharField(max_length=300, label=_("Local translation"))
	prononciation=forms.CharField(required=False, max_length=300, label=_("Local pronunciation"))
