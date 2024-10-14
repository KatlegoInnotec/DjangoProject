from django import forms

from accounts.models import Topic, Article, Comment


class InputForm(forms.Form):
        name = forms.CharField()
        email = forms.EmailField()

class TopicForm(forms.ModelForm):
        class Meta():
                model = Topic
                fields = ('topic',)

class ArticleForm(forms.ModelForm):
        class Meta():
                model = Article
                fields = ("title", "author","article")

class CommentForm(forms.ModelForm):
        class Meta():
                model = Comment
                fields = ("comment",)