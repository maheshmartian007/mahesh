from import_export import resources
from myapp.models import Posts
 
class PostResource(resources.ModelResource):
    class Meta:
        model = Post