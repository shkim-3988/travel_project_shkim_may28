# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from .forms import CustomUserCreationForm, CustomAuthenticationForm, UserProfileForm
from .models import CustomUser

# 로그인 뷰
class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = CustomAuthenticationForm

# 로그아웃 뷰
class UserLogoutView(LogoutView):
    next_page = 'accounts:home'

# 회원가입 뷰
class UserRegisterView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        try:
            # 이메일 중복 체크
            email = form.cleaned_data.get('email')
            if CustomUser.objects.filter(email=email).exists():
                messages.error(self.request, f'이미 등록된 이메일 주소입니다: {email}')
                return self.form_invalid(form)
            
            # 비밀번호 확인
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            if password1 != password2:
                messages.error(self.request, '비밀번호가 일치하지 않습니다.')
                return self.form_invalid(form)
            
            # 회원가입 처리
            user = form.save()
            messages.success(self.request, '회원가입이 완료되었습니다. 로그인해주세요.')
            return redirect('accounts:login')
            
        except IntegrityError as e:
            messages.error(self.request, f'회원가입 중 오류가 발생했습니다: {str(e)}')
            return self.form_invalid(form)
        except ValidationError as e:
            messages.error(self.request, f'입력값이 올바르지 않습니다: {str(e)}')
            return self.form_invalid(form)
        except Exception as e:
            messages.error(self.request, f'예상치 못한 오류가 발생했습니다: {str(e)}')
            return self.form_invalid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f'{field}: {error}')
        return super().form_invalid(form)

# 홈 페이지 뷰
def home(request):
    return render(request, 'home.html')

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, '프로필이 업데이트되었습니다.')
            return redirect('accounts:profile')
    else:
        form = UserProfileForm(instance=request.user.profile)
    
    return render(request, 'accounts/profile.html', {'form': form})

# 문화 정보 페이지 뷰 추가
def culture(request):
    return render(request, 'accounts/culture.html')  # culture.html을 렌더링
