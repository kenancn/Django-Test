from django.contrib import admin
from election.models import Survey
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from election.models import Question

class SurveyResource(resources.ModelResource):

    class Meta:
        model = Survey
        fields=('id','name','created_at','active')


class SurveyAdmin(ImportExportModelAdmin):
    resource_class = SurveyResource
    list_display = ('name','active','created_at','updated_at',)
    list_filter = ('active',)
    search_fields = ('name',)




class QuestionResource(resources.ModelResource):

    class Meta:
        model = Question
        fields=('id','survey_id','title','choice_one','choice_two','choice_three','choice_four',)

class QuestionAdmin(ImportExportModelAdmin):
    resource_class = QuestionResource
    list_display = ('id','survey','title','choice_one','choice_two','choice_three','choice_four',)

    search_fields = ('title',)

admin.site.register(Survey, SurveyAdmin)
admin.site.register(Question, QuestionAdmin)