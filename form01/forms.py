# 专门用来存放 form 对象
'''
1.第一步定义对象
'''
from django import forms

from form01 import models

'''
field  属性

label
required  默认必须是要填
error_message
widget 标签

如果修改默认的 widget添加一下额外的属性

常用的API

'''

class TestForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=15, min_length=6,
                               widget=(forms.TextInput(attrs={'placeholder': '请输入用户名'})),
                               error_messages={'max_length': u'你输入的太长了','min_length':'最小是6位'})
    # username = forms
    password = forms.CharField(label='密码', widget=(forms.PasswordInput(attrs={'placeholder': '请输入密码'})))
    is_accept = forms.BooleanField(label='同意', error_messages={'required': '必须接受'})
    file = forms.FileField(label='请选择上传的文件', required=False)
    img = forms.ImageField(label='请选择图片', required=False)
    test_date = forms.DateField(label='请输入日期', input_formats=['%Y-%m-%d'])
    test_datetime = forms.DateTimeField(label='请输入日期', input_formats=['%Y-%m-%d %H%M%S'])
    sex = forms.ChoiceField(label='性别', choices=[(1, '女'), (2, '男')])
    email = forms.EmailField(label='邮箱', max_length=20)

    def __init__(self):
        super().__init__()
        self.fields['sex'].inital = {[(1, '女'), (2, '男')]}


    # 重写验证
    # 全局  局部
    def clean_username(self):
        # 表示用户名必须包含字母
        if self.cleaned_data['username'].isalpha():
            return self.cleaned_data['username']
        else:
            raise EnvironmentError('用户名必须包含字母')

class UserModelForm(forms.ModelForm):
    class Meta:
        model = models.User

        # 素有的属性都生成form
        fields = '__all__'
        #指定特定的属性生成form
        fields = ['username', 'password']
        # 不包含
        exclude = ['is_del']

# class UserModelForm(forms.ModelForm):
#     class Meta:
#         model = models.User
#         fields = '__all__'
#         exclude = ['username']


