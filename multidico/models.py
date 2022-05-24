from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Language(models.Model):
	language_original_name=models.CharField(max_length=100)
	language_name=models.CharField(max_length=100)
	language_french_name=models.CharField(blank=True, null=True,max_length=100)
	I_want_to_learn_english=models.CharField(blank=True, null=True, max_length=400)
	I_want_to_learn_french=models.CharField(blank=True, null=True, max_length=400)
	def __str__(self):
		return str(self.language_name)

class CategoryManager(models.Manager):
	def that_has_word(self, lang):
		categories = self.all().order_by('order_index');
		cat_list = []
		for category in categories:
			if Word.objects.filter(language = lang, category__id=category.id):
				cat_list.append(category)
		return cat_list	

class Category(models.Model):
	category_name=models.CharField(max_length=200)
	category_french_name=models.CharField(blank=True, null=True,max_length=200)
	order_index=models.IntegerField(default=100)
	objects=CategoryManager()
	
	def __str__(self):
		return str(self.category_name)



class SubCategory(models.Model):
	subcategory_name=models.CharField(max_length=200)
	subcategory_french_name=models.CharField(blank=True, null=True,max_length=200)
	order_index=models.IntegerField(default=100)
	parent=models.ForeignKey(Category)
	def __str__(self):
		return self.subcategory_name
	
class Word(models.Model):
    def __str__(self):
        return u'%s, %s' % (self.english, self.language)
    language=models.ForeignKey(Language)
    category=models.ForeignKey(Category)
    subcategory=models.ForeignKey(SubCategory, null=True, blank=True)
    learning_progress=models.CharField(max_length=1,choices=(('B','Beginner'),('I','Intermediate'),('A','Advanced'),('F','Fluent'),('S','Slang')))
    english=models.CharField(max_length=300)
    english_local_prononciation=models.CharField(max_length=300)
    french=models.CharField(max_length=300)
    french_local_prononciation=models.CharField(max_length=300)
    local=models.CharField(max_length=300, blank=True, null=True)
    prononciation=models.CharField(null=True,blank=True,max_length=300)
    modified_by=models.ManyToManyField(User, blank=True, null=True)
    
class WordModified(models.Model):
	def __str__(self):
		return u'%s, %s' % (self.english, self.language)
	language=models.ForeignKey(Language)
	category=models.ForeignKey(Category)
	subcategory=models.ForeignKey(SubCategory, null=True, blank=True)
	learning_progress=models.CharField(max_length=1,choices=(('B','Beginner'),('I','Intermediate'),('A','Advanced'),('F','Fluent'),('S','Slang')))
	english=models.CharField(max_length=300)
	english_local_prononciation=models.CharField(max_length=300)
	french=models.CharField(max_length=300)
	french_local_prononciation=models.CharField(max_length=300)
	local=models.CharField(max_length=300,null=True,blank=True)
	prononciation=models.CharField(null=True,blank=True,max_length=300)
	modifier=models.ForeignKey(User)
	word_origin=models.ForeignKey(Word, null=True, blank=True)

class Number(models.Model):
	def __str__(self):
		return u'%s, %s' % (self.digit, self.local)
	language=models.ForeignKey(Language)
	digit=models.IntegerField()
	english=models.CharField(null=True, blank=True, max_length=50)
	english_local_prononciation=models.CharField(null=True, blank=True, max_length=50)
	french=models.CharField(null=True, blank=True, max_length=50)
	french_local_prononciation=models.CharField(null=True, blank=True, max_length=50)
	local=models.CharField(null=True, blank=True, max_length=50)
	prononciation=models.CharField(null=True,blank=True,max_length=50)



		
