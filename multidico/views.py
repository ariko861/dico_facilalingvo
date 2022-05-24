from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Language, Category, Word, WordModified, SubCategory, Number
from django.utils import translation
from django import http
from django.conf import settings
from django import forms
from .forms import WordForm
from django.db.models import Q

# Create your views here.

def language_choice(request):
	language_list=Language.objects.all().order_by('language_name')
	return render(request, 'language_choice.html', {'language_list': language_list})


def category_choice(request, language):

	lang=Language.objects.get(language_name=language)
	category_list = Category.objects.that_has_word(lang)	
	listoflist=[]
	langcss = 'css/'+language+'.css'

	if request.method == 'POST':
		order = request.POST['orderchoice']
		numberlist={}
		if 'numbers' in request.POST:
			for n in Number.objects.filter(language = lang):
				
				numberlist[n.digit]=n
			
		for categorie in category_list:
			listo=[]
			prout = 1
			if categorie.category_name in request.POST:
				listo.append(categorie)
				subcategories = SubCategory.objects.filter(parent = categorie).order_by('order_index')
				for word in Word.objects.filter(category=categorie,language=lang).order_by(order):
					if not word.subcategory:
						if request.user in word.modified_by.all():
							userword = WordModified.objects.get(word_origin=word)
						else:
							userword = word
						if userword.learning_progress in request.POST:
							listo.append(userword)
				if request.user.is_authenticated():
					for wordmodif in WordModified.objects.filter(category=categorie, language=lang, modifier=request.user).order_by(order):
						if not wordmodif.subcategory:
							if wordmodif.learning_progress in request.POST and not wordmodif.word_origin:
								listo.append(wordmodif)
				
				if subcategories:
					for subcategorie in subcategories:
						listo.append(subcategorie)
						for word in Word.objects.filter(category=categorie,subcategory=subcategorie,language=lang).order_by(order):
							if request.user in word.modified_by.all():
								userword = WordModified.objects.get(word_origin=word)
							else:
								userword = word
							if userword.learning_progress in request.POST:
								listo.append(userword)
						if request.user.is_authenticated():
							for wordmodif in WordModified.objects.filter(category=categorie,subcategory=subcategorie, language=lang, modifier=request.user).order_by(order):
								if wordmodif.learning_progress in request.POST and not wordmodif.word_origin:
									listo.append(wordmodif)
			
				
				listoflist.append(listo)
				
		if 'local_learn' in request.POST:
			local_learning = True
		else:
			local_learning = False
		if 'french_noob' in request.POST:
			french_noob = True
		else:
			french_noob = False
		return render(request, 'word_list.html', {'numberlist':numberlist,'listoflist':listoflist, 'language':language, 'local_learning':local_learning, 'french_noob':french_noob, 'langcss':langcss})
	    
	else:
		return render(request, 'category_choice.html', {'category_list': category_list, 'language':lang, 'langcss':langcss})

def change_word(request, changement, wordid):
	
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
	
	if changement == "change":
		w=Word
	elif changement  == "changeagain":
		w=WordModified
	else:
		return HttpResponseRedirect('/')
	
	word = w.objects.get(id=wordid)
	
	
	if request.method == 'POST':
		
		form = WordForm(request.POST)
		if form.is_valid():
			cleaned_form = form.cleaned_data
			
			if w == Word:
				new_word_modified = WordModified(
					language=word.language,
					category=cleaned_form['category'],
					learning_progress=cleaned_form['learning_progress'],
					english=cleaned_form['english'],
					english_local_prononciation=cleaned_form['english_local_prononciation'],
					french=cleaned_form['french'],
					french_local_prononciation=cleaned_form['french_local_prononciation'],
					local=cleaned_form['local'],
					prononciation=cleaned_form['prononciation'],
					modifier = request.user,
					word_origin = word,
					
				)
				
				new_word_modified.save()
				
				word.modified_by.add(request.user)
				word.save()
				
			elif w == WordModified:
				word.category=cleaned_form['category']
				word.learning_progress=cleaned_form['learning_progress']
				word.english=cleaned_form['english']
				word.english_local_prononciation=cleaned_form['english_local_prononciation']
				word.french=cleaned_form['french']
				word.french_local_prononciation=cleaned_form['french_local_prononciation']
				word.local=cleaned_form['local']
				word.prononciation=cleaned_form['prononciation']
				

				word.save()
							
			
			return HttpResponseRedirect('/'+ word.language.language_name + '/')
		
		
	else:
		form = WordForm(initial = {'category':word.category, 'learning_progress':word.learning_progress, 'english':word.english, 'english_local_prononciation':word.english_local_prononciation, 'french':word.french, 'french_local_prononciation':word.french_local_prononciation, 'local':word.local, 'prononciation':word.prononciation })
		
		return render(request, 'word_form.html', { 'action':'change','form':form })


def add_word(request, language, category):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
		
	if request.method == 'POST':
		
		form = WordForm(request.POST)
		if form.is_valid():
			cleaned_form = form.cleaned_data
			
			new_word_modified = WordModified(
					language=Language.objects.get(language_name=language),
					category=cleaned_form['category'],
					learning_progress=cleaned_form['learning_progress'],
					english=cleaned_form['english'],
					english_local_prononciation=cleaned_form['english_local_prononciation'],
					french=cleaned_form['french'],
					french_local_prononciation=cleaned_form['french_local_prononciation'],
					local=cleaned_form['local'],
					prononciation=cleaned_form['prononciation'],
					modifier = request.user,
										
				)
				
			new_word_modified.save()							
			
			return HttpResponseRedirect('/'+ language + '/')
		
		
	else:
		cat = Category.objects.get(category_name=category)
		form = WordForm(initial = {'category':cat})
		
		return render(request, 'word_form.html', { 'action':'add','form':form })
