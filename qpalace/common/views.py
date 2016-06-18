import random
from django.shortcuts import render_to_response
from common.models import *
from PyQt4.QtCore import *

def randquestionid(database):
    exec('dataSum = len(%s.objects.all())' %database)
    return int(random.uniform(0, dataSum))

nowquestionid = 0 
nAnswerSum = 1
nRightSum = 0

# Create your views here.
def index(request, database):
    print 'database = ', database
    global nowquestionid
    global nAnswerSum
    global nRightSum
    exec('question = %s.objects.all()[nowquestionid].question' %database)
    exec('nQuestionSum = len(%s.objects.all())' %database)
    return render_to_response('index.html', {
	    'database': database,
        'question': question,
        'nQuestionSum': nQuestionSum,
        'nAnswerSum': nAnswerSum,
        'nRightSum': nRightSum,
        'fRightPercent':1.0*nRightSum/nAnswerSum})

def judge(request, database):
    global nowquestionid
    global nAnswerSum
    global nQuestionSum
    global nRightSum
    nAnswerSum += 1
    answer = QString(request.GET.get('answer', 'None'))
    answer = answer.replace(QRegExp('\s'), '')
    exec('solution = QString(%s.objects.all()[nowquestionid].solution)' % database)
    solution = solution.replace(QRegExp('\s'), '')
    if answer == solution:
        nowquestionid = randquestionid(database)
        nRightSum += 1
    return index(request, database)
