from django.conf.urls import url
from . import views

app_name = 'elections'
urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^areas/(?P<area>[가-힣].+)/$', views.areas),
    url(r'^areas/(?P<area>[가-힣]+)/results$', views.results),
    url(r'^polls/(?P<poll_id>\d+)/$', views.polls),
    url(r'^candidates/(?P<name>[가-힣]+)/$', views.candidates),
    # Django에서 url의 첫 번째 인자는 보통 r'^.../...$'과 같은 형태를 띄고 있습니다.
    # 따옴표 안에 들어가는 내용은 정규표현식으로 나타냅니다.

    # 정규표현식의 내용을 간략히 훑으면,

    # ^ : 문자열의 시작을 알립니다
    # areas : 문자 그대로 스트링 areas입니다.
    # $ : 문자열의 끝을 알립니다.
    # (?<name>...) : symbolic 그룹 이름 name으로 그룹과 매칭 되는 부분 문자열에 접근이 가능합니다. (?P<area>.+)의 경우
    # group 이름은 area(부등호<>로 감싸진 부분)이며, 이를 통해 views.areas에 문자열을 전달합니다.
    # .+는 개행 문자를 제외한 모든 문자를 의미합니다.
]
