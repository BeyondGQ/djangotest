from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from form01.forms import TestForm, UserModelForm


def test(request):
    # if request.method == 'POST':
    #     test_form = TestForm(request.POST)
    #     if test_form.is_valid():
    #         test_form.clean_date['username']
    # else:
    #     test_form = TestForm()
    # print(test_form)
    # test_form = TestForm(inital={'choice':[(1,'女'),(2,'男')],'username':'xiaoming'})
    test_form = TestForm()
    # 表示通过所有的验证   True  False
    # 如果说返回 False那就表示数据不符合我们的业务规范，不应该去执行
    # if test_form.is_valid() and test_form.has_changed():
    #     # 获取用户传递的数据
    #     # uname = test_form.changed_data['username'] #{'username':'1213456'}
    #     # passwd = test_form.changed_data['password'] #{'password':'1213456'}
    #     # 保存数据
    #
    # return render(request, 'form01.html', {'form': test_form})

# 后台统一返回json restful flask
def register(request):
    if request.method == 'POST':
        user_form = UserModelForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return HttpResponse('验证成功')
    else:
        user_form = UserModelForm()
    return render(request, 'register.html', {'user_form': user_form})

'''
第一步定义 models
第二步 在 forms 模块中定义相关联的form

class XXXForm(forms.ModelForm):
    class Meat:
        model = models.XXX
        fields = '__all__'
        exclude = ['']
        

定义views

if request.method == 'POST':
# 表示是用户提交的数据
xxx_form = XXXForm(request.POST)
if xxx_form.is_valid():
    xxx_form.save()

else:
   # 表示初始化界面
   xxx_form = XXForm()
return render(request, '模板'，‘{'xxx_form':xxx_form}’) 

不给你生成表单
不给你提交按钮
<form>  
{{xxx_form}}
<input type="submit" value='提交'>

</form> 
'''

