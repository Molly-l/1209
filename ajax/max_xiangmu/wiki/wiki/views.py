from django.http import JsonResponse

from ajax.max_xiangmu.wiki.user.models import UserProfile


def test(request):
    #对score字段进行+1操作
    u=UserProfile.objects.get()
    u.score+=1
    u.save()



    return JsonResponse({'code':200,'data':{}})