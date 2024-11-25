from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from create_form.models import Form
from answers.models import Answer
from results.models import Responses

# Create your views here.
def responses(request, code):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    formInfo = Form.objects.filter(code = code)
    #Checking if form exists
    if formInfo.count() == 0:
        return HttpResponseRedirect(reverse('404'))
    else: formInfo = formInfo[0]

    responsesSummary = []
    choiceAnswered = {}
    filteredResponsesSummary = {}
    for question in formInfo.questions.all():
        answers = Answer.objects.filter(answer_to = question.id)
        if question.question_type == "multiple choice" or question.question_type == "checkbox":
            choiceAnswered[question.question] = choiceAnswered.get(question.question, {})
            for answer in answers:
                choice = answer.answer_to.choices.get(id = answer.answer).choice
                choiceAnswered[question.question][choice] = choiceAnswered.get(question.question, {}).get(choice, 0) + 1
        responsesSummary.append({"question": question, "answers":answers })
    for answr in choiceAnswered:
        filteredResponsesSummary[answr] = {}
        keys = choiceAnswered[answr].values()
        for choice in choiceAnswered[answr]:
            filteredResponsesSummary[answr][choice] = choiceAnswered[answr][choice]
    #Checking if form creator is user
    if formInfo.creator != request.user:
        return HttpResponseRedirect(reverse("403"))
    return render(request, "sub/responses.html", {
        "form": formInfo,
        "responses": Responses.objects.filter(response_to = formInfo),
        "responsesSummary": responsesSummary,
        "filteredResponsesSummary": filteredResponsesSummary
    })

# Error handler
def FourZeroThree(request):
    return render(request, "error/403.html")

def FourZeroFour(request):
    return render(request, "error/404.html")
