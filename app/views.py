from django.shortcuts import render, redirect
from .models import Question, Answer, UserLike
from django.http import JsonResponse
import json


def index(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            question = request.POST['question']
            q_instance = Question()
            q_instance.question = question
            q_instance.user = request.user
            q_instance.save()
            redirect('home')
        questions = Question.objects.all()
        my_questions = questions.filter(user=request.user)
        questions_dict = {
            'questions': questions.order_by('-created_at'), 
            "my_questions": my_questions.order_by('-created_at')
        }
        return render(request, 'index.html', context=questions_dict)
    return render(request, 'index.html')


def answers_view(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            answer = request.POST['answer']
            ans = Answer()
            ans.answer = answer
            ans.user = request.user
            ans.question = question
            ans.save()
            redirect('answers', id=id)
        question = Question.objects.get(id=id)
        answers = Answer.objects.filter(question=question.id).order_by('-created_at')
        ans_dict = {}
        for ans in answers:
            ans_dict
        context_dict = {
            'question': question,
            'answers': answers
        }
        return render(request, 'answers.html', context=context_dict)
    redirect('home')


def like_view(request, id):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        ans_id = data.get('id')
        like_status = data.get('like')
        like_status = True if like_status == 'true' else False
        answer = Answer.objects.get(id=ans_id)
        like = UserLike.objects.filter(answer=answer, user=request.user)
        print(len(like), "##################")
        if like:
            like = like[0]
            if like_status and not like.is_liked:
                answer.likes += 1
            elif not like_status and like.is_liked:
                answer.likes -= 1
            
            like.is_liked = like_status
            like.save()
        else:
            like = UserLike()
            like.answer = answer
            like.user = request.user
            like.is_liked = like_status
            like.save()
            if like_status:
                answer.likes += 1
        answer.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})
