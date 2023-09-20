from forms import ModelForm
from models import BlogPost, Comment
    
class BlogPostForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = ("title", "text", "publication_date")

class AddCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ("text")

